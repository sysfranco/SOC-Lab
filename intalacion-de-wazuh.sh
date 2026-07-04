#!/bin/bash

# Sistema operativo: Ubuntu Server 24.04.3

sudo apt update && sudo apt upgrade -y

# Herramientas esenciales
sudo apt install curl apt-transport-https unzip lsb-releas gnupg -y

# IMPORTANTE: Antes de instalar debes tener +20GB disponible en disco para la instalacion

# Script de instalacion de Wazuh
curl -sO https://packages.wazuh.com/4.14/wazuh-install.sh
sudo bash wazuh-install.sh -a # -a: All-In-One
