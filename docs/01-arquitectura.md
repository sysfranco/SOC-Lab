# 01. Arquitectura del laboratorio

## Diagrama lógico

```text
                      ┌──────────────────────────────┐
                      │ Host Linux                    │
                      │ KVM/libvirt + virt-manager    │
                      └──────────────┬───────────────┘
                                     │
                         Red virtual SOC-Lab
                         NAT o red aislada
                                     │
        ┌────────────────────────────┼────────────────────────────┐
        │                            │                            │
┌───────▼────────┐          ┌────────▼────────┐           ┌───────▼────────┐
│ VM-SERVER-SOC  │          │ VM-CLIENT-01    │           │ Host físico    │
│ Ubuntu Server  │          │ Windows/Linux   │           │ navegador/admin│
│                │          │                 │           │                │
│ Wazuh Manager  │◄────────►│ Wazuh Agent     │           │ Acceso web     │
│ Wazuh Indexer  │ eventos  │ Sysmon opcional │           │ SSH/HTTPS      │
│ Wazuh Dashboard│          │                 │           │                │
│ TheHive        │◄─────────┤                 │           │                │
│ Shuffle        │◄─────────┤                 │           │                │
└────────────────┘          └─────────────────┘           └────────────────┘
```

## Componentes

### VM-SERVER-SOC

Servidor central del laboratorio. Aloja los servicios de seguridad:

- Wazuh Manager.
- Wazuh Indexer.
- Wazuh Dashboard.
- TheHive.
- Shuffle.
- Docker Engine y Docker Compose para servicios en contenedores.

### VM-CLIENT-01

Endpoint monitorizado. Puede ser:

- Windows 10/11 para telemetría de endpoint, eventos de seguridad y Sysmon.
- Ubuntu/Debian si se quiere una prueba más ligera.

En este cliente se instala Wazuh Agent. Sysmon es opcional, pero recomendable si el cliente es Windows.

## Red recomendada

Para empezar, usa una red NAT de libvirt. Es más simple y permite que las VMs tengan salida a Internet para instalar paquetes.

Nombre sugerido:

```text
soc-lab-net
```

Rango sugerido:

```text
192.168.100.0/24
```

Asignación sugerida:

| Equipo | IP sugerida | Función |
|---|---:|---|
| VM-SERVER-SOC | 192.168.100.10 | Wazuh, TheHive, Shuffle |
| VM-CLIENT-01 | DHCP o 192.168.100.20 | Endpoint monitorizado |

## Puertos orientativos

| Servicio | Puerto común | Uso |
|---|---:|---|
| SSH | 22 | Administración del servidor Linux |
| Wazuh Dashboard | 443 | Interfaz web de Wazuh |
| Wazuh Agent | 1514/1515 | Comunicación y enrolamiento del agente |
| TheHive | según despliegue | Case management |
| Shuffle | según despliegue | SOAR / workflows |

> Ajusta los puertos según la instalación oficial y evita exponerlos fuera de tu red local.

## Decisión de diseño

Se usa una arquitectura mínima de 1 servidor y 1 cliente para que el proyecto sea viable en un PC personal. Si el host tiene 16 GB de RAM, conviene iniciar primero Wazuh y el cliente; después añadir TheHive y Shuffle cuando la base esté validada.
