# Informe final - SOC-Lab

> Este informe se completa solo con evidencias reales del laboratorio. Las gráficas deben generarse desde exportaciones reales, no con datos inventados.

## 1. Resumen ejecutivo

```text
Pendiente
```

## 2. Objetivo del proyecto

Crear un entorno simulado de SOC con SIEM/XDR, agente endpoint, ticketing y automatización para practicar detección, triage, gestión de casos y documentación de incidentes controlados.

## 3. Arquitectura implementada

Incluir diagrama final y capturas sanitizadas.

| Componente | Implementado | Evidencia |
|---|---|---|
| VM servidor | Pendiente | Pendiente |
| VM cliente | Pendiente | Pendiente |
| Wazuh | Pendiente | Pendiente |
| Wazuh Agent | Pendiente | Pendiente |
| TheHive | Pendiente | Pendiente |
| Shuffle | Pendiente | Pendiente |
| Sysmon opcional | Pendiente | Pendiente |

## 4. Casos de uso implementados

| ID | Caso de uso | Herramientas | Estado |
|---|---|---|---|
| CU-001 | Autenticación fallida | Wazuh, TheHive, Shuffle | Pendiente |
| CU-002 | Cambio de archivo monitorizado | Wazuh FIM, TheHive, Shuffle | Pendiente |
| CU-003 | Evento Windows/Sysmon | Wazuh, Sysmon, TheHive | Pendiente |

## 5. Resultados técnicos

### 5.1 Alertas Wazuh

```text
Pendiente
```

### 5.2 Casos TheHive

```text
Pendiente
```

### 5.3 Ejecuciones Shuffle

```text
Pendiente
```

## 6. Métricas

| Métrica | Valor | Fuente |
|---|---:|---|
| Total de alertas analizadas | Pendiente | Wazuh export |
| Total de casos creados | Pendiente | TheHive |
| Playbooks ejecutados | Pendiente | Shuffle |
| Tiempo medio de triage | Pendiente | Medición manual |
| Eventos descartados como prueba | Pendiente | Informe |

## 7. Gráficas

Insertar gráficas generadas desde `analysis/generate_graphs.py` cuando existan datos reales en `data/`.

Gráficas sugeridas:

- Alertas por nivel de regla.
- Alertas por agente.
- Alertas por técnica MITRE, si existe el campo.
- Casos por severidad.
- Tiempo de triage por caso.

## 8. Hallazgos

| ID | Hallazgo | Evidencia | Severidad | Acción tomada | Estado |
|---|---|---|---|---|---|
| H-001 | Pendiente | Pendiente | Pendiente | Pendiente | Pendiente |

## 9. Limitaciones

Ejemplos de limitaciones reales que podrían aparecer:

- RAM insuficiente para ejecutar todo a la vez.
- Alertas con mucho ruido.
- Integración Wazuh → Shuffle pendiente.
- TheHive requiere ajuste de recursos.
- Sysmon genera demasiados eventos si no se filtra.

No marques una limitación como resuelta si no lo probaste.

## 10. Conclusiones

```text
Pendiente
```

## 11. Próximas mejoras

- Añadir más endpoints.
- Crear dashboards específicos.
- Mejorar reglas y decodificadores.
- Añadir Cortex u otro sistema de enriquecimiento.
- Añadir notificaciones por correo/Telegram/Slack.
- Automatizar despliegue con Ansible.
