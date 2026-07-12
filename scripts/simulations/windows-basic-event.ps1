# SOC-Lab controlled signal: Windows basic process event
# Ejecutar en PowerShell. No realiza acciones destructivas.

Write-Host "[SOC-Lab] Señal controlada Windows"
Write-Host "Usuario: $(whoami)"
Write-Host "Equipo: $env:COMPUTERNAME"
Write-Host "Fecha: $(Get-Date -Format o)"

Start-Process notepad.exe
Start-Sleep -Seconds 3
Stop-Process -Name notepad -ErrorAction SilentlyContinue

Write-Host "Prueba terminada. Busca eventos del endpoint en Wazuh y, si aplica, eventos Sysmon."
