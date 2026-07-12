# 09. Playbooks de automatización

## Objetivo

Diseñar playbooks claros, seguros y ejecutables con Shuffle. En la primera versión, los playbooks no deben realizar acciones destructivas automáticamente.

## Principios

- Primero observar.
- Después clasificar.
- Luego crear caso.
- Finalmente responder con aprobación manual.

## Playbook 1: autenticación fallida

### Nombre

```text
PB-001 - Failed Authentication Triage
```

### Entrada esperada

```json
{
  "source": "wazuh",
  "event_type": "auth_failed",
  "agent_name": "vm-client-01",
  "src_ip": "<ip>",
  "user": "<user>",
  "rule_level": "<level>",
  "timestamp": "<timestamp>"
}
```

### Flujo

1. Recibir alerta.
2. Validar campos obligatorios.
3. Clasificar severidad.
4. Crear alerta/caso en TheHive.
5. Añadir tarea: validar si fue prueba controlada.
6. Añadir observable: IP origen.
7. Registrar ejecución.

### Salida esperada

- Caso creado en TheHive.
- Tarea de triage asignada.
- Evidencia de ejecución en Shuffle.

### Respuesta automática permitida

Solo documentación y creación de caso. No bloquear IP automáticamente en Fase 1.

## Playbook 2: File Integrity Monitoring

### Nombre

```text
PB-002 - FIM Change Triage
```

### Entrada esperada

```json
{
  "source": "wazuh",
  "event_type": "fim_change",
  "agent_name": "vm-client-01",
  "file_path": "/opt/soc-lab/watch/important-file.txt",
  "action": "modified",
  "rule_level": "<level>",
  "timestamp": "<timestamp>"
}
```

### Flujo

1. Recibir alerta FIM.
2. Comprobar ruta afectada.
3. Clasificar si pertenece a ruta del laboratorio.
4. Crear caso en TheHive.
5. Añadir tarea: verificar contenido del cambio.
6. Añadir tarea: confirmar si fue cambio autorizado.
7. Cerrar como `Test controlado` si coincide con la prueba.

## Playbook 3: evento Windows/Sysmon

### Nombre

```text
PB-003 - Windows Process Event Triage
```

### Entrada esperada

```json
{
  "source": "wazuh",
  "event_type": "windows_process",
  "agent_name": "vm-client-win",
  "process_name": "notepad.exe",
  "user": "<user>",
  "timestamp": "<timestamp>"
}
```

### Flujo

1. Recibir evento.
2. Normalizar nombre de proceso.
3. Crear alerta en TheHive si cumple condición definida.
4. Añadir observable: proceso.
5. Añadir tarea: revisar si hay comando sospechoso.

## Tabla de madurez de playbooks

| Nivel | Descripción | Permitido en este lab |
|---|---|---|
| 1 | Notificar y registrar | Sí |
| 2 | Crear caso y tareas | Sí |
| 3 | Enriquecer con datos internos | Sí |
| 4 | Ejecutar respuesta con aprobación | Sí, más adelante |
| 5 | Respuesta automática sin aprobación | No recomendado |

## Evidencia requerida por playbook

Cada playbook necesita:

- Captura del workflow.
- Payload de entrada sanitizado.
- Resultado de ejecución.
- Caso creado en TheHive, si aplica.
- Conclusión: funcionó / falló / mejora pendiente.
