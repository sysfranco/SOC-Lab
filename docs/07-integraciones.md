# 07. Integraciones

## Objetivo

Definir cómo se conectan Wazuh, TheHive y Shuffle dentro del laboratorio.

## Flujo objetivo

```text
Endpoint
  │
  │ Wazuh Agent / Sysmon opcional
  ▼
Wazuh
  │
  │ alerta o evento relevante
  ▼
Shuffle
  │
  │ playbook: normalizar, enriquecer, decidir
  ▼
TheHive
  │
  │ caso, tareas, observables
  ▼
Informe
```

## Fase inicial: integración manual

Antes de automatizar, hazlo manual:

1. Genera una alerta controlada.
2. Localízala en Wazuh.
3. Copia sus campos principales.
4. Crea un caso manual en TheHive.
5. Adjunta captura o exportación.
6. Documenta el razonamiento del analista.

Ventaja: entiendes el flujo sin depender todavía de automatizaciones.

## Fase intermedia: Shuffle recibe webhooks

Crea un webhook en Shuffle para recibir payloads de prueba.

Campos mínimos esperados:

```json
{
  "source": "wazuh",
  "rule_id": "<id>",
  "rule_level": "<level>",
  "description": "<description>",
  "agent_name": "<agent>",
  "timestamp": "<timestamp>"
}
```

Acciones iniciales del playbook:

1. Recibir evento.
2. Validar campos obligatorios.
3. Asignar severidad.
4. Crear alerta/caso en TheHive.
5. Registrar resultado.

## Fase avanzada: alerta real hacia Shuffle

Cuando Wazuh esté validado, configura una integración que envíe alertas relevantes a Shuffle. No actives todas las alertas desde el inicio; filtra por caso de uso.

Filtros recomendados:

| Caso | Filtro |
|---|---|
| Autenticación fallida | Regla o grupo relacionado con auth/failed login |
| FIM | Reglas de integridad de archivos |
| Windows/Sysmon | Evento de proceso o conexión relevante |

## TheHive: modelo de caso

Campos mínimos al crear caso:

| Campo | Fuente |
|---|---|
| Título | Wazuh rule description + agente |
| Severidad | Mapeo de nivel Wazuh |
| Descripción | Resumen normalizado |
| Observables | IP, hostname, usuario, hash, proceso |
| Tareas | Triage, validación, respuesta, cierre |

## Mapeo de severidad sugerido

| Nivel Wazuh | Severidad SOC-Lab |
|---:|---|
| 0-3 | Informativo |
| 4-6 | Baja |
| 7-9 | Media |
| 10-12 | Alta |
| 13-15 | Crítica |

> Ajusta este mapeo tras observar tus alertas reales.

## Criterio de éxito

La integración se considera funcional cuando puedes demostrar:

- Una alerta real en Wazuh.
- Un workflow ejecutado en Shuffle.
- Un caso/alerta creado en TheHive.
- Evidencia guardada en `evidence/`.
- Registro claro en el informe.
