# 14. Operación y mantenimiento

## Objetivo

Mantener el laboratorio estable y documentado.

## Arranque diario

En el host Linux:

```bash
virsh list --all
virsh start VM-SERVER-SOC
virsh start VM-CLIENT-01
```

En el servidor:

```bash
sudo systemctl status wazuh-manager --no-pager
sudo systemctl status wazuh-indexer --no-pager
sudo systemctl status wazuh-dashboard --no-pager
```

Para servicios Docker:

```bash
cd ~/soc-lab/services/<servicio>
docker compose ps
```

## Apagado ordenado

En cada VM:

```bash
sudo shutdown now
```

O desde host:

```bash
virsh shutdown VM-CLIENT-01
virsh shutdown VM-SERVER-SOC
```

## Backups mínimos

Guardar:

- Documentación del repositorio.
- Configuraciones sanitizadas.
- Capturas/evidencias públicas.
- Informes finales.

No guardar en GitHub:

- `.env` reales.
- Contraseñas.
- Certificados privados.
- Tokens API.

## Revisión semanal

Checklist:

- [ ] Las VMs arrancan.
- [ ] Wazuh Dashboard carga.
- [ ] Agente aparece activo.
- [ ] TheHive carga.
- [ ] Shuffle carga.
- [ ] No hay contenedores reiniciando.
- [ ] Las evidencias nuevas están documentadas.
- [ ] El README refleja el estado actual.

## Troubleshooting rápido

### Wazuh no muestra agente

```bash
sudo systemctl status wazuh-agent --no-pager
sudo tail -n 100 /var/ossec/logs/ossec.log
```

### Wazuh Dashboard no carga

```bash
sudo systemctl status wazuh-dashboard --no-pager
sudo journalctl -u wazuh-dashboard -n 100 --no-pager
```

### Docker consume demasiada RAM

```bash
docker stats
free -h
```

Solución temporal:

- Apagar servicios que no estés usando.
- Ejecutar TheHive y Shuffle por fases.
- Aumentar swap solo como apoyo, no como solución principal.

## Evolución del proyecto

Ideas de mejora:

- Añadir un cliente Linux adicional.
- Añadir Sysmon con configuración afinada.
- Añadir reglas personalizadas de Wazuh.
- Añadir dashboards por caso de uso.
- Añadir Ansible para automatizar instalación.
- Añadir integración con notificaciones.
- Añadir más documentación de investigación.
