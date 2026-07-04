## Para el servidor de Wazuh

Comprobar que el puerto 443 (SSL) esta ecuchando:
```bash
sudo ss -tulnp | grep :443
```

Comprobar el estado de los servicios del servidor Wazuh:
```bash
# Comprobar el estado del dashboard
sudo systemctl status wazuh-dashboard

# Comprobar el estado del idexador
sudo systemctl status wazuh-indexer

# Comprobar el estado del manager
sudo systemctl status wazuh-manager
```