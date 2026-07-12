# 04. Instalación de Wazuh

## Objetivo

Instalar Wazuh en `VM-SERVER-SOC` y validar que el dashboard funciona.

## Nota de recursos

La instalación rápida de Wazuh instala los componentes centrales en el mismo host: Wazuh Server, Wazuh Indexer y Wazuh Dashboard. Para un laboratorio pequeño, esto simplifica el despliegue.

## Preparación del servidor

En `VM-SERVER-SOC`:

```bash
sudo apt update
sudo apt upgrade -y
sudo apt install -y curl wget vim net-tools ca-certificates gnupg lsb-release
hostnamectl
ip a
```

Asigna hostname:

```bash
sudo hostnamectl set-hostname vm-server-soc
```

Reinicia si es necesario:

```bash
sudo reboot
```

## Instalación rápida

> Verifica antes la documentación oficial de Wazuh por si la versión cambió.

Comando base:

```bash
curl -sO https://packages.wazuh.com/4.14/wazuh-install.sh
sudo bash ./wazuh-install.sh -a
```

Cuando termine, guarda las credenciales en un sitio privado. No las subas a GitHub.

Para leer contraseñas generadas:

```bash
sudo tar -O -xvf wazuh-install-files.tar wazuh-install-files/wazuh-passwords.txt
```

## Acceso al dashboard

Desde el navegador del host físico:

```text
https://<IP_VM_SERVER_SOC>
```

Usuario inicial esperado:

```text
admin
```

La advertencia del certificado en el navegador es normal en laboratorio si se usa certificado autofirmado.

## Validaciones

En el servidor:

```bash
sudo systemctl status wazuh-manager --no-pager
sudo systemctl status wazuh-indexer --no-pager
sudo systemctl status wazuh-dashboard --no-pager
```

Comprobación de puertos:

```bash
sudo ss -tulpn | grep -E '443|1514|1515|55000'
```

## Instalación del agente Wazuh en cliente Linux

En la interfaz web de Wazuh:

```text
Agents management > Deploy new agent
```

Selecciona el sistema operativo y copia el comando generado por Wazuh.

Validación en cliente Linux:

```bash
sudo systemctl status wazuh-agent --no-pager
sudo tail -f /var/ossec/logs/ossec.log
```

## Instalación del agente Wazuh en cliente Windows

En Wazuh Dashboard:

```text
Agents management > Deploy new agent > Windows
```

Copia el comando PowerShell generado por Wazuh y ejecútalo como Administrador en Windows.

Validación:

```powershell
Get-Service WazuhSvc
```

## Sysmon opcional en Windows

Sysmon no sustituye a Wazuh Agent. Su función es generar telemetría detallada de procesos, conexiones de red y otros eventos que luego puede recoger el agente/SIEM.

Instalación orientativa:

```powershell
# Ejecutar como Administrador en una carpeta donde esté Sysmon64.exe
.\Sysmon64.exe -accepteula -i sysmonconfig.xml
```

Validación:

```powershell
Get-WinEvent -LogName "Microsoft-Windows-Sysmon/Operational" -MaxEvents 5
```

## Evidencia mínima de esta fase

Guarda capturas en:

```text
evidence/fase-1/wazuh-install/
```

Evidencias recomendadas:

- Dashboard de Wazuh accesible.
- Servicios Wazuh activos.
- Agente conectado en Wazuh.
- Log de agente sin errores críticos.

## Problemas comunes

### No carga el dashboard

Revisa:

```bash
sudo systemctl status wazuh-dashboard
sudo journalctl -u wazuh-dashboard -n 100 --no-pager
```

### Agente no conecta

Revisa:

```bash
sudo ss -tulpn | grep -E '1514|1515'
sudo tail -f /var/ossec/logs/ossec.log
```

Causas comunes:

- IP incorrecta del manager.
- Firewall bloqueando puertos.
- Servicio del agente detenido.
- Diferencia de red entre VMs.
