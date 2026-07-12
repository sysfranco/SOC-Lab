# 02. Requisitos

## Requisitos del host

| Recurso | Recomendado |
|---|---:|
| CPU | 6 cores / 12 threads o superior |
| RAM | 16 GB mínimo práctico |
| Disco libre | 180 GB o más |
| Sistema | Linux con KVM/libvirt |
| Virtualización BIOS/UEFI | Activada |

## VMs sugeridas

### Perfil recomendado si el host tiene 16 GB RAM

| VM | CPU | RAM | Disco | Sistema |
|---|---:|---:|---:|---|
| VM-SERVER-SOC | 4 vCPU | 8 GB | 100 GB | Ubuntu Server 24.04 LTS |
| VM-CLIENT-01 | 2 vCPU | 4 GB | 60 GB | Windows 10/11 o Ubuntu |

### Perfil más cómodo

| VM | CPU | RAM | Disco | Sistema |
|---|---:|---:|---:|---|
| VM-SERVER-SOC | 4-6 vCPU | 10-12 GB | 120 GB | Ubuntu Server 24.04 LTS |
| VM-CLIENT-01 | 2 vCPU | 4 GB | 60 GB | Windows 10/11 |

## Paquetes necesarios en el host Linux

En distribuciones basadas en Ubuntu/Debian:

```bash
sudo apt update
sudo apt install -y qemu-kvm libvirt-daemon-system libvirt-clients virt-manager virtinst bridge-utils
sudo usermod -aG libvirt,kvm "$USER"
```

Cierra sesión y vuelve a entrar para aplicar los grupos.

Validación:

```bash
virsh list --all
virt-host-validate
```

## Imágenes ISO

- Ubuntu Server 24.04 LTS para VM-SERVER-SOC.
- Windows 10/11 o Ubuntu Desktop/Server para VM-CLIENT-01.

## Cuentas y contraseñas

No publiques credenciales reales. Usa un archivo local `.env` o un gestor de contraseñas. El `.gitignore` ya excluye `.env`, certificados y archivos sensibles.

## Requisitos de documentación

Cada fase debe dejar evidencia en:

```text
evidence/
reports/
data/
```

No subas datos privados. Si una captura contiene IPs, nombres reales o tokens, redáctala antes de publicarla.
