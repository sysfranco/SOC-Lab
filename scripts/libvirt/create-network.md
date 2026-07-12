# Crear red virtual SOC-Lab en libvirt

> Este documento usa una red NAT simple para empezar. Ajusta el rango si ya usas `192.168.100.0/24`.

## 1. Crear XML de red

```bash
cat > /tmp/soc-lab-net.xml <<'XML'
<network>
  <name>soc-lab-net</name>
  <forward mode='nat'/>
  <bridge name='virbr100' stp='on' delay='0'/>
  <ip address='192.168.100.1' netmask='255.255.255.0'>
    <dhcp>
      <range start='192.168.100.100' end='192.168.100.200'/>
    </dhcp>
  </ip>
</network>
XML
```

## 2. Definir y arrancar red

```bash
virsh net-define /tmp/soc-lab-net.xml
virsh net-start soc-lab-net
virsh net-autostart soc-lab-net
```

## 3. Validar

```bash
virsh net-list --all
virsh net-dumpxml soc-lab-net
```
