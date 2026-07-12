# Crear VMs con virt-install

> Ajusta rutas ISO, CPU, RAM y disco según tu PC.

## Variables sugeridas

```bash
export ISO_UBUNTU="$HOME/ISO/ubuntu-24.04-live-server-amd64.iso"
export ISO_WINDOWS="$HOME/ISO/windows.iso"
export VM_DIR="$HOME/VMs/SOC-Lab"
mkdir -p "$VM_DIR"
```

## VM-SERVER-SOC

```bash
virt-install \
  --name VM-SERVER-SOC \
  --memory 8192 \
  --vcpus 4 \
  --disk path="$VM_DIR/vm-server-soc.qcow2",size=100,bus=virtio,format=qcow2 \
  --cdrom "$ISO_UBUNTU" \
  --os-variant ubuntu24.04 \
  --network network=soc-lab-net,model=virtio \
  --graphics spice \
  --boot useserial=on
```

## VM-CLIENT-01 Linux opcional

```bash
virt-install \
  --name VM-CLIENT-01-LINUX \
  --memory 4096 \
  --vcpus 2 \
  --disk path="$VM_DIR/vm-client-01-linux.qcow2",size=60,bus=virtio,format=qcow2 \
  --cdrom "$ISO_UBUNTU" \
  --os-variant ubuntu24.04 \
  --network network=soc-lab-net,model=virtio \
  --graphics spice
```

## VM-CLIENT-01 Windows

Para Windows, normalmente necesitarás ISO de VirtIO drivers si quieres disco/red VirtIO.

```bash
virt-install \
  --name VM-CLIENT-01-WIN \
  --memory 4096 \
  --vcpus 2 \
  --disk path="$VM_DIR/vm-client-01-win.qcow2",size=60,bus=sata,format=qcow2 \
  --cdrom "$ISO_WINDOWS" \
  --os-variant win10 \
  --network network=soc-lab-net,model=e1000e \
  --graphics spice
```

## Validación

```bash
virsh list --all
virsh domifaddr VM-SERVER-SOC
virsh domifaddr VM-CLIENT-01-LINUX
```
