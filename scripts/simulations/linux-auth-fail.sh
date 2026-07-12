#!/usr/bin/env bash
set -euo pipefail

# SOC-Lab controlled signal: authentication failure helper
# Uso: ./linux-auth-fail.sh <IP_CLIENTE>
# Este script NO hace fuerza bruta. Solo inicia pocos intentos manuales controlados.

TARGET_IP="${1:-}"
if [[ -z "$TARGET_IP" ]]; then
  echo "Uso: $0 <IP_CLIENTE>"
  exit 1
fi

echo "[SOC-Lab] Prueba controlada de autenticación fallida contra $TARGET_IP"
echo "Se harán 3 intentos con usuario inexistente. Introduce una contraseña incorrecta si SSH la pide."

for i in 1 2 3; do
  echo "Intento $i/3"
  ssh -o PreferredAuthentications=password -o PubkeyAuthentication=no -o ConnectTimeout=5 "soclab_noexiste@$TARGET_IP" true || true
  sleep 2
done

echo "Prueba terminada. Busca eventos relacionados con sshd/authentication failed en Wazuh."
