# 10. Pruebas controladas Fase 2

## Objetivo

Ejecutar pruebas más completas usando SIEM, ticketing y playbooks.

Fase 2 no significa usar ataques reales. Significa conectar más piezas del SOC:

```text
Evento controlado → Wazuh → Shuffle → TheHive → informe → gráfica
```

## Escenario 1: autenticación fallida con caso automático

### Hipótesis

Si se producen varios intentos fallidos de autenticación en el endpoint, Wazuh debe generar un evento relevante y Shuffle debe crear un caso en TheHive.

### Pasos

1. Verificar agente activo.
2. Ejecutar 3 intentos fallidos controlados.
3. Buscar alerta en Wazuh.
4. Enviar alerta a Shuffle o disparar flujo equivalente con payload basado en la alerta real.
5. Confirmar caso en TheHive.
6. Guardar evidencias.

### Métricas

| Métrica | Valor |
|---|---|
| Tiempo de generación del evento | Pendiente |
| Tiempo hasta visualización en Wazuh | Pendiente |
| Tiempo hasta creación de caso | Pendiente |
| Falsos positivos observados | Pendiente |

## Escenario 2: cambio de archivo monitorizado

### Hipótesis

Si un archivo monitorizado cambia, Wazuh debe generar alerta FIM y el playbook debe crear una tarea de validación.

### Pasos

1. Confirmar ruta monitorizada.
2. Modificar archivo de prueba.
3. Validar alerta FIM.
4. Ejecutar playbook PB-002.
5. Confirmar tarea en TheHive.
6. Clasificar como cambio autorizado o no autorizado.

## Escenario 3: evento Windows/Sysmon

### Hipótesis

Si se ejecuta un proceso controlado en Windows, el endpoint debe generar telemetría que pueda verse en Wazuh y usarse para triage.

### Pasos

1. Confirmar agente Windows activo.
2. Confirmar Sysmon, si está instalado.
3. Ejecutar proceso benigno.
4. Buscar evento en Wazuh.
5. Ejecutar playbook PB-003.
6. Documentar si la señal fue útil o demasiado ruidosa.

## Criterios de finalización

Fase 2 termina cuando existan:

- 3 escenarios ejecutados.
- 3 evidencias principales en Wazuh.
- 1 o más casos en TheHive.
- 1 o más ejecuciones de Shuffle.
- CSV/exportaciones reales para generar gráficas.
- Informe final completado.
