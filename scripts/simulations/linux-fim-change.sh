#!/usr/bin/env bash
set -euo pipefail

# SOC-Lab controlled signal: File Integrity Monitoring change
# Debe ejecutarse en el cliente Linux donde Wazuh Agent monitoriza /opt/soc-lab/watch

WATCH_DIR="/opt/soc-lab/watch"
WATCH_FILE="$WATCH_DIR/important-file.txt"

sudo mkdir -p "$WATCH_DIR"
if [[ ! -f "$WATCH_FILE" ]]; then
  echo "baseline" | sudo tee "$WATCH_FILE" >/dev/null
fi

echo "controlled change $(date -Is)" | sudo tee -a "$WATCH_FILE" >/dev/null

echo "Cambio controlado realizado en $WATCH_FILE"
echo "Busca evento FIM en Wazuh."
