"""Testes para o script docker_manage.sh.

Estes testes exercitam a lógica de ciclo de vida do script (up/status/down)
sem subir Docker de verdade. Para isso, colocamos stubs executáveis de
``docker``, ``curl`` e ``sleep`` no início do PATH:

* ``docker`` — registra cada invocação num arquivo de log e sai com 0;
* ``curl``   — simula a resposta do endpoint ``/health`` conforme ``CURL_MODE``
  (``up`` devolve JSON saudável, qualquer outro valor simula API fora do ar);
* ``sleep``  — vira no-op, para o laço de retry do health check rodar instantâneo.

Com isso conseguimos validar os três cenários que importam:
"Docker subiu e a API ficou saudável", "Docker subiu mas a API não respondeu"
e "Docker desceu/limpou corretamente".
"""

import os
import stat
import subprocess
import tempfile
import unittest


REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT = os.path.join(REPO_DIR, "docker_manage.sh")

DOCKER_STUB = """#!/usr/bin/env bash
echo "docker $*" >> "$DOCKER_LOG"
exit 0
"""

# Simula o /health. Em modo "up" devolve JSON saudável (curl -sf -> exit 0);
# em qualquer outro modo simula conexão recusada (curl -sf -> exit != 0).
CURL_STUB = """#!/usr/bin/env bash
case "${CURL_MODE:-down}" in
  up) echo '{"status":"ok","ollama":true}'; exit 0 ;;
  *)  exit 7 ;;
esac
"""

# sleep vira no-op para o retry do health check não levar minutos no teste.
SLEEP_STUB = """#!/usr/bin/env bash
exit 0
"""


class DockerManageScriptTests(unittest.TestCase):
    def setUp(self):
        self.assertTrue(
            os.path.exists(SCRIPT), f"Script não encontrado: {SCRIPT}"
        )
        self._tmp = tempfile.TemporaryDirectory()
        self.bindir = self._tmp.name
        self.docker_log = os.path.join(self.bindir, "docker_calls.log")
        self._write_stub("docker", DOCKER_STUB)
        self._write_stub("curl", CURL_STUB)
        self._write_stub("sleep", SLEEP_STUB)

    def tearDown(self):
        self._tmp.cleanup()

    def _write_stub(self, name, body):
        path = os.path.join(self.bindir, name)
        with open(path, "w", encoding="utf-8") as f:
            f.write(body)
        os.chmod(path, os.stat(path).st_mode | stat.S_IEXEC | stat.S_IXGRP | stat.S_IXOTH)

    def _run(self, command, curl_mode="down"):
        env = dict(os.environ)
        env["PATH"] = self.bindir + os.pathsep + env.get("PATH", "")
        env["DOCKER_LOG"] = self.docker_log
        env["CURL_MODE"] = curl_mode
        return subprocess.run(
            ["C:\\Git\\usr\\bin\\bash.exe", SCRIPT, command],
            cwd=REPO_DIR,
            env=env,
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=60,
        )

    def _docker_calls(self):
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

        self.assertEqual(result.returncode, 0, msg=result.stderr)
        self.assertIn("compose up -d", self._docker_calls())
        # Health check confirmou a API e leu o JSON corretamente.
        self.assertIn("API UP", result.stdout)
        self.assertIn("status=ok", result.stdout)
        self.assertIn("ollama=true", result.stdout)

    def test_up_falha_quando_api_nao_responde(self):
        """Docker subiu mas a API nunca respondeu: o script aborta com erro."""
        result = self._run("up", curl_mode="down")

        self.assertNotEqual(result.returncode, 0)
        # Ainda assim tentou subir os containers...
        self.assertIn("compose up -d", self._docker_calls())
        # ...e reportou a falha do health check via die().
        self.assertIn("API não respondeu", result.stderr)

    # ------------------------------------------------------------------ #
    # DOWN / CLEAN                                                        #
    # ------------------------------------------------------------------ #

    def test_down_para_containers(self):
        """Docker desceu corretamente: chama compose down e termina com sucesso."""
        result = self._run("down")

        self.assertEqual(result.returncode, 0, msg=result.stderr)
        self.assertIn("compose down", self._docker_calls())
        self.assertIn("Serviços parados", result.stdout)

    def test_clean_remove_imagens_e_volumes(self):
        """clean derruba e remove imagens locais, volumes e orphans."""
        result = self._run("clean")

        self.assertEqual(result.returncode, 0, msg=result.stderr)
        calls = self._docker_calls()
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
        self.assertIn("Uso:", result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
