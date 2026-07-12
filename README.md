# SOC-Lab
Laboratorio SOC virtualizado para practicar detección, análisis, gestión de casos y automatización usando **Wazuh**, **TheHive** y **Shuffle**.

> Estado del proyecto: documentación base para implementación. Los informes y gráficas no contienen datos inventados; se completan cuando existan evidencias reales del laboratorio.

## Objetivo

Crear un entorno simulado de SOC que permita:

=======
- Instalar y validar un SIEM/XDR con Wazuh.
- Conectar endpoints mediante Wazuh Agent.
- Gestionar alertas e investigaciones con TheHive.
- Automatizar playbooks con Shuffle.
- Ejecutar pruebas controladas y seguras.
- Documentar hallazgos reales con evidencias reproducibles.

## Arquitectura mínima

```text
┌──────────────────────────────┐
│ Host Linux + KVM/libvirt     │
│ virt-manager / virsh         │
└──────────────┬───────────────┘
               │ red NAT o red aislada SOC-Lab
               │
   ┌───────────▼───────────┐        ┌────────────────────┐
   │ VM-SERVER-SOC         │        │ VM-CLIENT-ENDPOINT │
   │ Ubuntu Server         │◄──────►│ Windows o Linux    │
   │ Wazuh Manager         │ agent  │ Wazuh Agent        │
   │ Wazuh Dashboard       │ logs   │ Sysmon opcional    │
   │ TheHive               │        │                    │
   │ Shuffle               │        │                    │
   └───────────────────────┘        └────────────────────┘
```

## Fases

| Fase | Resultado esperado |
|---|---|
| 0. Preparación | Repositorio, red, VMs y checklist listos. |
| 1. Base instalada | Wazuh, TheHive, Shuffle y agente funcionando. |
| 2. Señales controladas | Alertas reales generadas por acciones seguras. |
| 3. Informe Fase 1 | Informe con evidencias, no simulado. |
| 4. Playbooks | Automatizaciones documentadas y probadas. |
| 5. Pruebas Fase 2 | Casos más completos usando playbooks. |
| 6. Informe final | Hallazgos, métricas y gráficas desde datos exportados. |

## Documentación principal

1. [`docs/00-alcance-y-reglas.md`](docs/00-alcance-y-reglas.md)
2. [`docs/01-arquitectura.md`](docs/01-arquitectura.md)
3. [`docs/02-requisitos.md`](docs/02-requisitos.md)
4. [`docs/03-roadmap-ejecutable.md`](docs/03-roadmap-ejecutable.md)
5. [`docs/04-instalacion-wazuh.md`](docs/04-instalacion-wazuh.md)
6. [`docs/05-instalacion-thehive.md`](docs/05-instalacion-thehive.md)
7. [`docs/06-instalacion-shuffle.md`](docs/06-instalacion-shuffle.md)
8. [`docs/07-integraciones.md`](docs/07-integraciones.md)
9. [`docs/08-pruebas-fase-1.md`](docs/08-pruebas-fase-1.md)
10. [`docs/09-playbooks.md`](docs/09-playbooks.md)
11. [`docs/10-pruebas-fase-2.md`](docs/10-pruebas-fase-2.md)
12. [`docs/11-informe-fase-1-template.md`](docs/11-informe-fase-1-template.md)
13. [`docs/12-informe-final-template.md`](docs/12-informe-final-template.md)
14. [`docs/13-evidencias-y-graficas.md`](docs/13-evidencias-y-graficas.md)
15. [`docs/14-operacion-y-mantenimiento.md`](docs/14-operacion-y-mantenimiento.md)

## Regla importante sobre informes

Este repositorio no debe publicar informes inventados. Cada hallazgo debe tener:

- Fecha y hora.
- Máquina afectada.
- Acción controlada realizada.
- Captura o exportación de alerta.
- Interpretación técnica.
- Decisión del analista.
- Resultado del playbook, si aplica.

Las gráficas del informe final deben generarse desde datos exportados de Wazuh o TheHive. Usa [`analysis/generate_graphs.py`](analysis/generate_graphs.py) cuando tengas un CSV real.

## Fuentes oficiales recomendadas

- Wazuh documentation: https://documentation.wazuh.com/current/
- TheHive documentation: https://docs.strangebee.com/thehive/
- Shuffle documentation: https://shuffler.io/docs
- Microsoft Sysmon: https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon

Fuentes consultadas y enlaces de referencia: [`docs/99-fuentes-oficiales.md`](docs/99-fuentes-oficiales.md)

