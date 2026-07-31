"""Testes para o script docker_manage.sh.

Contém dois níveis de teste:

**Testes de unidade com stubs** (``DockerManageScriptTests``)
  Exercitam a lógica de ciclo de vida do script (up/status/down) sem subir
  Docker de verdade. Stubs de ``docker``, ``curl`` e ``sleep`` são colocados
  na frente do PATH para interceptar as chamadas do script.

**Testes de integração com Docker real** (``DockerIntegrationTests``)
  Sobem os containers de verdade via ``docker compose`` e validam o
  comportamento real da API. Requerem Docker instalado e rodando.
  Ativados pela variável de ambiente ``INTEGRATION=1``.

  Execução::

      INTEGRATION=1 python -m pytest tests/test_docker_manage.py -v

  Atenção: o Ollama pode levar vários minutos para ficar healthy na primeira
  vez (pull de imagem + carregamento do modelo). O timeout padrão é 10 min.
"""

import json
import os
import stat
import subprocess
import tempfile
import time
import unittest
import urllib.error
import urllib.request


# Diretório raiz do projeto (um nível acima de /tests).
REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Caminho absoluto para o script que será testado.
SCRIPT = os.path.join(REPO_DIR, "docker_manage.sh")

# Stub do comando `docker`: registra cada chamada no arquivo $DOCKER_LOG e
# retorna 0 (sucesso) para não bloquear o fluxo do script.
DOCKER_STUB = """#!/usr/bin/env bash
echo "docker $*" >> "$DOCKER_LOG"
exit 0
"""

# Stub do comando `curl`: simula o endpoint /health.
# Em modo "up" devolve JSON saudável (exit 0); em qualquer outro modo
# simula conexão recusada saindo com código 7 (equivalente ao curl real).
CURL_STUB = """#!/usr/bin/env bash
case "${CURL_MODE:-down}" in
  up) echo '{"status":"ok","ollama":true}'; exit 0 ;;
  *)  exit 7 ;;
esac
"""

# Stub do comando `sleep`: vira no-op para o laço de retry do health check
# não levar minutos durante os testes.
SLEEP_STUB = """#!/usr/bin/env bash
exit 0
"""


class DockerManageScriptTests(unittest.TestCase):

    def setUp(self):
        # Garante que o script existe antes de qualquer teste.
        self.assertTrue(
            os.path.exists(SCRIPT), f"Script não encontrado: {SCRIPT}"
        )
        # Cria um diretório temporário exclusivo para os stubs desta execução.
        self._tmp = tempfile.TemporaryDirectory()
        self.bindir = self._tmp.name

        # Arquivo onde o stub do docker acumula todas as chamadas recebidas.
        self.docker_log = os.path.join(self.bindir, "docker_calls.log")

        # Grava os três stubs no diretório temporário.
        self._write_stub("docker", DOCKER_STUB)
        self._write_stub("curl", CURL_STUB)
        self._write_stub("sleep", SLEEP_STUB)

    def tearDown(self):
        # Remove o diretório temporário e todos os stubs ao final de cada teste.
        self._tmp.cleanup()

    def _write_stub(self, name, body):
        """Grava um script stub em bindir e torna-o executável."""
        path = os.path.join(self.bindir, name)
        with open(path, "w", encoding="utf-8") as f:
            f.write(body)
        # Adiciona bit de execução para owner, group e others.
        os.chmod(path, os.stat(path).st_mode | stat.S_IEXEC | stat.S_IXGRP | stat.S_IXOTH)

    def _run(self, command, curl_mode="down"):
        """Executa docker_manage.sh com o comando dado, usando os stubs no PATH.

        curl_mode controla o comportamento do stub de curl:
          "up"   → simula API saudável (exit 0 + JSON);
          outros → simula API fora do ar (exit 7).
        """
        env = dict(os.environ)
        # Coloca bindir na frente do PATH para que os stubs sejam encontrados
        # antes dos binários reais do sistema.
        env["PATH"] = self.bindir + os.pathsep + env.get("PATH", "")
        # Informa ao stub do docker onde gravar o log de chamadas.
        env["DOCKER_LOG"] = self.docker_log
        # Informa ao stub do curl qual modo de simulação usar.
        env["CURL_MODE"] = curl_mode
        return subprocess.run(
            ["bash", SCRIPT, command],
            cwd=REPO_DIR,
            env=env,
            capture_output=True,
            text=True,
            timeout=60,
        )

    def _docker_calls(self):
        """Retorna o conteúdo acumulado do log de chamadas ao stub do docker."""
        if not os.path.exists(self.docker_log):
            return ""
        with open(self.docker_log, "r", encoding="utf-8") as f:
            return f.read()

    # ------------------------------------------------------------------ #
    # UP                                                                  #
    # ------------------------------------------------------------------ #

    def test_up_sucesso_quando_api_fica_saudavel(self):
        """Docker subiu e o /health respondeu: o script termina com sucesso."""
        result = self._run("up", curl_mode="up")

        # Script deve terminar com código 0 (sucesso).
        self.assertEqual(result.returncode, 0, msg=result.stderr)
        # Deve ter invocado `docker compose up -d`.
        self.assertIn("compose up -d", self._docker_calls())
        # Health check confirmou a API e leu o JSON corretamente.
        self.assertIn("API UP", result.stdout)
        self.assertIn("status=ok", result.stdout)
        self.assertIn("ollama=true", result.stdout)

    def test_up_falha_quando_api_nao_responde(self):
        """Docker subiu mas a API nunca respondeu: o script aborta com erro."""
        result = self._run("up", curl_mode="down")

        # Script deve terminar com código diferente de 0 (falha).
        self.assertNotEqual(result.returncode, 0)
        # Ainda assim tentou subir os containers antes de desistir.
        self.assertIn("compose up -d", self._docker_calls())
        # A mensagem de erro do die() deve aparecer no stderr.
        self.assertIn("API não respondeu", result.stderr)

    # ------------------------------------------------------------------ #
    # DOWN / CLEAN                                                        #
    # ------------------------------------------------------------------ #

    def test_down_para_containers(self):
        """Docker desceu corretamente: chama compose down e termina com sucesso."""
        result = self._run("down")

        self.assertEqual(result.returncode, 0, msg=result.stderr)
        # Verifica que o comando correto foi passado ao docker.
        self.assertIn("compose down", self._docker_calls())
        self.assertIn("Serviços parados", result.stdout)

    def test_clean_remove_imagens_e_volumes(self):
        """clean derruba e remove imagens locais, volumes e orphans."""
        result = self._run("clean")

        self.assertEqual(result.returncode, 0, msg=result.stderr)
        calls = self._docker_calls()
        # Confirma que as três flags de limpeza profunda foram passadas.
        self.assertIn("--rmi local", calls)
        self.assertIn("--volumes", calls)
        self.assertIn("--remove-orphans", calls)

    # ------------------------------------------------------------------ #
    # Misc                                                                #
    # ------------------------------------------------------------------ #

    def test_comando_desconhecido_mostra_usage(self):
        """Comando inválido sai com erro e imprime a ajuda."""
        result = self._run("inexistente")

        self.assertNotEqual(result.returncode, 0)
        # A mensagem de uso deve aparecer em stdout ou stderr.
        self.assertIn("Uso:", result.stdout + result.stderr)


@unittest.skipUnless(os.environ.get("INTEGRATION"), "set INTEGRATION=1 to run")
class DockerIntegrationTests(unittest.TestCase):
    """Testes de integração que sobem Docker de verdade.

    ``setUpClass`` faz build + up uma única vez para todos os testes da classe.
    ``tearDownClass`` derruba tudo ao final.
    O teste ``test_z_script_down`` (último alfabeticamente) valida o comando
    ``down`` e encerra os containers; ``tearDownClass`` repete o down de forma
    idempotente para garantir limpeza mesmo se o teste falhar.
    """

    API_URL = "http://localhost:8000/health"
    STARTUP_TIMEOUT = 600   # segundos — ollama pode demorar na primeira vez
    POLL_INTERVAL = 10

    # ------------------------------------------------------------------ #
    # Ciclo de vida da suite                                               #
    # ------------------------------------------------------------------ #

    OLLAMA_MODEL = "gemma3:4b"
    OLLAMA_CONTAINER = "revisaotecnica-ollama-1"

    @classmethod
    def setUpClass(cls):
        # Garante estado limpo antes de subir (preserva volumes para cache do modelo).
        subprocess.run(
            ["docker", "compose", "down", "--remove-orphans"],
            cwd=REPO_DIR, check=False, capture_output=True, timeout=60,
        )
        # Reconstrói as imagens locais.
        subprocess.run(
            ["docker", "compose", "build"],
            cwd=REPO_DIR, check=True, timeout=600,
        )
        # Sobe todos os serviços em background.
        subprocess.run(
            ["docker", "compose", "up", "-d"],
            cwd=REPO_DIR, check=True, timeout=60,
        )
        # Garante que o modelo está disponível no Ollama (faz pull se necessário).
        subprocess.run(
            ["docker", "exec", cls.OLLAMA_CONTAINER, "ollama", "pull", cls.OLLAMA_MODEL],
            check=True, timeout=600,
        )
        # Bloqueia até a API responder (ou esgotar o timeout).
        cls._aguarda_api()

    @classmethod
    def tearDownClass(cls):
        # Não passa --volumes para preservar o cache do modelo Ollama entre execuções.
        subprocess.run(
            ["docker", "compose", "down", "--remove-orphans"],
            cwd=REPO_DIR, check=False, capture_output=True, timeout=60,
        )

    @classmethod
    def _aguarda_api(cls):
        deadline = time.time() + cls.STARTUP_TIMEOUT
        while time.time() < deadline:
            try:
                with urllib.request.urlopen(cls.API_URL, timeout=5) as resp:
                    if resp.status == 200:
                        return
            except Exception:
                pass
            time.sleep(cls.POLL_INTERVAL)
        raise RuntimeError(
            f"API não respondeu em {cls.STARTUP_TIMEOUT}s. "
            "Verifique: docker compose logs app"
        )

    # ------------------------------------------------------------------ #
    # Testes                                                               #
    # ------------------------------------------------------------------ #

    def test_health_retorna_status_ok(self):
        """Endpoint /health retorna JSON com status=ok e ollama=true."""
        with urllib.request.urlopen(self.API_URL, timeout=10) as resp:
            data = json.loads(resp.read())
        self.assertEqual(data.get("status"), "ok")
        self.assertTrue(data.get("ollama"), "ollama deve estar true no /health")

    def test_containers_estao_rodando(self):
        """docker compose ps lista app e ollama como serviços ativos."""
        result = subprocess.run(
            ["docker", "compose", "ps"],
            cwd=REPO_DIR, capture_output=True, text=True, timeout=30,
        )
        self.assertEqual(result.returncode, 0, msg=result.stderr)
        self.assertIn("app", result.stdout)
        self.assertIn("ollama", result.stdout)

    def test_script_status_contra_containers_reais(self):
        """docker_manage.sh status termina com sucesso e exibe o JSON do /health."""
        result = subprocess.run(
            ["bash", SCRIPT, "status"],
            cwd=REPO_DIR, capture_output=True, text=True, timeout=30,
        )
        self.assertEqual(result.returncode, 0, msg=result.stderr)
        # step_status imprime a resposta formatada pelo python3 -m json.tool
        self.assertIn('"status"', result.stdout)
        self.assertIn('"ollama"', result.stdout)

    def test_z_script_down_para_containers(self):
        """docker_manage.sh down encerra os containers; API para de responder."""
        result = subprocess.run(
            ["bash", SCRIPT, "down"],
            cwd=REPO_DIR, capture_output=True, text=True, timeout=60,
        )
        self.assertEqual(result.returncode, 0, msg=result.stderr)
        self.assertIn("Serviços parados", result.stdout)

        # Após o down, a API não deve mais aceitar conexões.
        with self.assertRaises((urllib.error.URLError, OSError)):
            urllib.request.urlopen(self.API_URL, timeout=5)


if __name__ == "__main__":
    unittest.main()
