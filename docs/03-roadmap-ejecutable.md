# 03. Roadmap ejecutable

## Vista general

Este roadmap convierte el plan de implementación en tareas verificables.

## Fase 0: Preparación del repositorio

Objetivo: dejar listo el repositorio GitHub y la estructura documental.

Tareas:

- [ ] Crear repositorio `SOC-Lab` en GitHub.
- [ ] Subir esta estructura inicial.
- [ ] Revisar `.gitignore`.
- [ ] Crear carpeta `evidence/` para capturas y exportaciones.
- [ ] Crear carpeta `reports/` para informes.
- [ ] Crear carpeta `data/` para CSV reales exportados.

Criterio de finalización:

- Repositorio visible con README, roadmap y documentos técnicos.

## Fase 1: Base del entorno

Objetivo: tener servidor y cliente funcionando.

Tareas:

- [ ] Crear red virtual `soc-lab-net`.
- [ ] Crear VM-SERVER-SOC.
- [ ] Crear VM-CLIENT-01.
- [ ] Confirmar conectividad entre VMs.
- [ ] Instalar Wazuh en VM-SERVER-SOC.
- [ ] Instalar Wazuh Agent en VM-CLIENT-01.
- [ ] Confirmar que el agente aparece como activo en Wazuh.
- [ ] Instalar TheHive.
- [ ] Instalar Shuffle.

Criterio de finalización:

- Dashboard de Wazuh accesible.
- Agente conectado.
- TheHive accesible.
- Shuffle accesible.

## Fase 2: Señales controladas iniciales

Objetivo: generar eventos reales y seguros para validar el SIEM.

Tareas:

- [ ] Prueba de autenticación fallida.
- [ ] Prueba de File Integrity Monitoring.
- [ ] Prueba de evento Windows/Sysmon, si el cliente es Windows.
- [ ] Capturar alertas o eventos en Wazuh.
- [ ] Guardar evidencias en `evidence/fase-1/`.

Criterio de finalización:

- Al menos 3 evidencias reales guardadas.
- Informe Fase 1 completado sin datos inventados.

## Fase 3: TheHive como ticketing

Objetivo: convertir hallazgos en casos.

Tareas:

- [ ] Crear organización/lab en TheHive.
- [ ] Crear taxonomía simple de severidad.
- [ ] Crear plantilla de caso para alerta de endpoint.
- [ ] Crear manualmente un caso a partir de una alerta real.
- [ ] Documentar el flujo alerta → caso → tarea → cierre.

Criterio de finalización:

- Al menos 1 caso real basado en una alerta real del laboratorio.

## Fase 4: Playbooks con Shuffle

Objetivo: automatizar acciones repetibles.

Tareas:

- [ ] Crear webhook de entrada en Shuffle.
- [ ] Crear playbook para alerta de autenticación fallida.
- [ ] Crear playbook para alerta FIM.
- [ ] Crear playbook para alerta Windows/Sysmon.
- [ ] Probar playbooks con eventos controlados.
- [ ] Documentar entradas, acciones y salidas.

Criterio de finalización:

- Al menos 1 playbook funcional con evidencia de ejecución.

## Fase 5: Pruebas Fase 2

Objetivo: ejecutar escenarios más completos.

Tareas:

- [ ] Repetir señales controladas con mayor trazabilidad.
- [ ] Usar TheHive para gestión de casos.
- [ ] Usar Shuffle para automatización.
- [ ] Medir tiempos: detección, triage, respuesta.
- [ ] Exportar datos para gráficas.

Criterio de finalización:

- Informe final con evidencias, métricas y gráficas generadas desde datos reales.
