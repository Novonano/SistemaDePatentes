#!/usr/bin/env bash
# Gerencia o ciclo de vida dos containers Docker do projeto RevisaoTecnica.
# Uso: ./docker_manage.sh [build|up|status|down|clean|all]
set -euo pipefail

# Endpoint da API FastAPI usado para verificar se o serviço está saudável.
API_URL="http://localhost:8000/health"

# Número máximo de tentativas antes de desistir do health check.
HEALTH_RETRIES=30

# Intervalo em segundos entre cada tentativa de health check.
HEALTH_INTERVAL=5

# Modelo Ollama que será baixado automaticamente no step_up.
OLLAMA_MODEL="${OLLAMA_MODEL:-gemma3:4b}"

# --------------------------------------------------------------------------- #
# Helpers                                                                       #
# --------------------------------------------------------------------------- #

# Imprime uma mensagem prefixada com o horário atual.
log() { echo "[$(date '+%H:%M:%S')] $*"; }

# Imprime uma mensagem de erro no stderr e encerra o script com falha.
die() { echo "[ERRO] $*" >&2; exit 1; }

# Aguarda a API responder no endpoint /health, fazendo polling até HEALTH_RETRIES
# tentativas com intervalo de HEALTH_INTERVAL segundos entre elas.
# Retorna 0 se a API ficar disponível, 1 se esgotar as tentativas.
health_check() {
    local i
    for i in $(seq 1 "$HEALTH_RETRIES"); do
        local response
        # -s silencia o progresso; -f falha silenciosamente em erros HTTP.
        response=$(curl -sf "$API_URL" 2>/dev/null) && {
            local status ollama
            # Extrai os campos "status" e "ollama" do JSON retornado.
            status=$(echo "$response" | grep -o '"status":"[^"]*"' | cut -d'"' -f4)
            ollama=$(echo "$response" | grep -o '"ollama":[a-z]*' | cut -d':' -f2)
            log "API UP — status=$status ollama=$ollama"
            return 0
        }
        log "Aguardando API... ($i/$HEALTH_RETRIES)"
        sleep "$HEALTH_INTERVAL"
    done
    return 1
}

# --------------------------------------------------------------------------- #
# Etapas                                                                        #
# --------------------------------------------------------------------------- #

# Constrói (ou reconstrói) as imagens Docker definidas no docker-compose.yml.
step_build() {
    log "=== BUILD ==="
    docker compose build
    log "Build concluído."
}

# Sobe os containers em modo detached e aguarda a API ficar disponível.
# Aborta com erro se o health check esgotar todas as tentativas.
step_up() {
    log "=== UP ==="
    docker compose up -d
    log "Serviços iniciados. Aguardando API ficar disponível..."
    log "Baixando modelo Ollama: $OLLAMA_MODEL (pode demorar na primeira vez)..."
    docker compose exec ollama ollama pull "$OLLAMA_MODEL" \
        || die "Falha ao baixar o modelo $OLLAMA_MODEL. Verifique: docker compose logs ollama"
    log "Modelo $OLLAMA_MODEL disponível."
    health_check || die "API não respondeu após $((HEALTH_RETRIES * HEALTH_INTERVAL))s. Verifique: docker compose logs app"
}

# Exibe o estado atual dos containers e a resposta bruta do endpoint /health.
step_status() {
    log "=== STATUS ==="
    docker compose ps
    echo ""
    log "Resposta do /health:"
    curl -sf "$API_URL" | python3 -m json.tool || log "API não acessível."
}

# Para e remove todos os containers e a rede criada pelo compose.
step_down() {
    log "=== DOWN ==="
    docker compose down
    log "Serviços parados e containers removidos."
}

# Para os containers e remove também imagens locais, volumes anônimos e orphans.
# Útil para liberar espaço em disco ou forçar um build do zero.
step_clean() {
    log "=== CLEAN ==="
    docker compose down --rmi local --volumes --remove-orphans
    log "Imagens locais, volumes anônimos e orphans removidos."
}

# --------------------------------------------------------------------------- #
# Execução                                                                      #
# --------------------------------------------------------------------------- #

# Imprime as instruções de uso e encerra com erro.
usage() {
    echo "Uso: $0 [build|up|status|down|clean|all]"
    echo ""
    echo "  build   — constrói as imagens Docker"
    echo "  up      — sobe os containers e verifica saúde da API"
    echo "  status  — exibe containers ativos e resposta do /health"
    echo "  down    — para e remove os containers"
    echo "  clean   — down + remove imagens locais e volumes anônimos"
    echo "  all     — build → up → status → down → clean"
    exit 1
}

# Lê o primeiro argumento; se omitido, executa o fluxo completo (all).
CMD="${1:-all}"

case "$CMD" in
    build)  step_build ;;
    up)     step_up ;;
    status) step_status ;;
    down)   step_down ;;
    clean)  step_clean ;;
    all)
        # Fluxo completo: constrói, sobe, valida, derruba e limpa.
        step_build
        step_up
        step_status
        step_down
        step_clean
        log "=== CONCLUÍDO ==="
        ;;
    *) usage ;;
esac
