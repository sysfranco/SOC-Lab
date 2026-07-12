# 00. Alcance y reglas del SOC-Lab

## Propósito

Este proyecto genera la base documental y operativa para construir un laboratorio SOC en un entorno virtualizado con libvirt/KVM. El objetivo no es demostrar resultados falsos, sino crear un camino ejecutable para instalar herramientas, generar señales controladas, analizar alertas y documentar evidencias reales.

## Herramientas principales

| Función | Herramienta |
|---|---|
| SIEM/XDR | Wazuh |
| Endpoint/EDR básico | Wazuh Agent |
| Telemetría Windows opcional | Sysmon |
| Ticketing / case management | TheHive |
| Playbooks / SOAR | Shuffle |
| Virtualización | KVM/libvirt, virt-manager o virsh |

## Qué entra en el alcance

- Creación de una VM servidor y una VM cliente.
- Instalación de Wazuh en el servidor SOC.
- Instalación del agente Wazuh en el cliente.
- Instalación de TheHive para gestión de casos.
- Instalación de Shuffle para automatización.
- Pruebas controladas y seguras para producir alertas.
- Informes basados en evidencias del laboratorio.
- Gráficas generadas desde CSV/exportaciones reales.

## Qué queda fuera del alcance

- Ataques reales contra terceros.
- Explotación de sistemas públicos.
- Uso de malware real.
- Publicar credenciales, IPs públicas, tokens o datos personales.
- Simular informes como si fueran resultados reales.

## Regla de evidencia

Un hallazgo solo puede aparecer como resultado si existe evidencia mínima:

1. Captura de Wazuh, TheHive o Shuffle.
2. Fecha/hora del evento.
3. Máquina origen/destino.
4. Acción controlada que generó la señal.
5. Interpretación del evento.
6. Conclusión del analista.

## Forma correcta de presentar el proyecto en GitHub

Este repositorio debe verse como un proyecto profesional de implementación. No hace falta tener un SOC perfecto desde el primer día. Lo importante es que cada fase muestre:

- Qué se quería conseguir.
- Cómo se instaló o configuró.
- Cómo se validó.
- Qué evidencia se obtuvo.
- Qué limitación quedó pendiente.
- Qué mejora viene después.
