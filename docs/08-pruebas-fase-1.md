# 08. Pruebas controladas Fase 1

## Objetivo

Generar señales reales, seguras y controladas para validar que Wazuh recibe eventos del cliente.

## Regla principal

No se usa malware real. No se atacan terceros. No se inventan alertas. Cada prueba debe ejecutarse dentro del laboratorio.

## Estructura de evidencia

Crear carpetas:

```bash
mkdir -p evidence/fase-1/{auth-fail,fim,windows-sysmon,manual-notes}
```

Cada prueba debe tener:

```text
evidence/fase-1/<prueba>/README.md
evidence/fase-1/<prueba>/captura-wazuh.png
evidence/fase-1/<prueba>/export-alert.json o export-alert.csv
```

## Prueba 1: autenticación fallida Linux

### Objetivo

Validar que Wazuh detecta eventos de autenticación fallida.

### Preparación

En el cliente Linux, confirma que el agente está activo:

```bash
sudo systemctl status wazuh-agent --no-pager
```

### Ejecución segura

Desde otra VM o desde el servidor, intenta iniciar sesión con un usuario inexistente o contraseña incorrecta contra el cliente Linux:

```bash
ssh usuario_inexistente@<IP_CLIENTE>
```

Repite pocas veces, por ejemplo 3 intentos. No hagas fuerza bruta real.

### Validación

En Wazuh Dashboard busca:

```text
failed login
authentication failed
sshd
```

### Evidencia

Guardar:

- Captura del evento en Wazuh.
- Hora exacta de la prueba.
- IP origen y destino.
- Número de intentos.

## Prueba 2: File Integrity Monitoring

### Objetivo

Validar detección de cambios en archivos monitorizados.

### Preparación

En el cliente Linux:

```bash
sudo mkdir -p /opt/soc-lab/watch
sudo bash -c 'echo "baseline" > /opt/soc-lab/watch/important-file.txt'
```

Configura Wazuh para monitorizar esa ruta según la documentación del agente. Tras cambiar configuración, reinicia el agente:

```bash
sudo systemctl restart wazuh-agent
```

### Ejecución segura

```bash
echo "controlled change $(date -Is)" | sudo tee -a /opt/soc-lab/watch/important-file.txt
```

### Validación

En Wazuh busca eventos de integridad de archivos relacionados con:

```text
/opt/soc-lab/watch/important-file.txt
```

### Evidencia

Guardar:

- Configuración aplicada.
- Captura del evento FIM.
- Comando ejecutado.
- Interpretación del evento.

## Prueba 3: evento Windows básico

### Objetivo

Validar recepción de eventos de Windows mediante Wazuh Agent.

### Ejecución segura

En Windows PowerShell como usuario normal:

```powershell
whoami
hostname
Get-Date
```

Si Sysmon está instalado, ejecuta una acción simple que genere evento de proceso:

```powershell
Start-Process notepad.exe
Start-Sleep -Seconds 3
Stop-Process -Name notepad -ErrorAction SilentlyContinue
```

### Validación

En Wazuh busca eventos del agente Windows por nombre del endpoint.

Si usas Sysmon, busca el log:

```text
Microsoft-Windows-Sysmon/Operational
```

### Evidencia

Guardar:

- Captura del agente Windows conectado.
- Captura del evento recibido.
- Hora de ejecución.

## Resultado esperado de Fase 1

Al finalizar, debes tener al menos:

| Prueba | Evidencia | Estado |
|---|---|---|
| Auth fail | Captura/export Wazuh | Pendiente/OK |
| FIM | Captura/export Wazuh | Pendiente/OK |
| Windows/Sysmon | Captura/export Wazuh | Pendiente/OK |

El informe Fase 1 se completa en:

```text
docs/11-informe-fase-1-template.md
```
