# 05. Instalación de TheHive

## Objetivo

Instalar TheHive en `VM-SERVER-SOC` para usarlo como sistema de ticketing y gestión de casos del laboratorio.

## Enfoque recomendado

Para el laboratorio se recomienda usar Docker Compose y apoyarse en los templates oficiales del proyecto/StrangeBee. TheHive no debe tratarse como una app aislada: normalmente necesita servicios auxiliares como base de datos, motor de indexación y proxy.

## Preparación de Docker

En `VM-SERVER-SOC`:

```bash
sudo apt update
sudo apt install -y ca-certificates curl gnupg jq
```

Instala Docker siguiendo la documentación oficial de Docker para Ubuntu. Después valida:

```bash
docker version
docker compose version
docker run hello-world
```

## Clonar despliegue oficial

```bash
mkdir -p ~/soc-lab/services
cd ~/soc-lab/services
git clone https://github.com/StrangeBeeCorp/docker.git thehive-docker
cd thehive-docker
```

Revisa los perfiles disponibles en el repositorio clonado y lee su README antes de levantar servicios.

## Variables y secretos

Nunca publiques el `.env` real. Si el template incluye `dot.env.template`, copia a `.env` y modifica contraseñas localmente:

```bash
cp dot.env.template .env
nano .env
```

Sube al repositorio solo un ejemplo sanitizado si hace falta:

```text
.env.example
```

## Puesta en marcha

Desde el perfil que elijas según el README oficial:

```bash
docker compose pull
docker compose up -d
```

Validación:

```bash
docker compose ps
docker compose logs --tail=100
```

## Primer acceso

Accede desde el navegador del host físico al puerto definido por el perfil Docker Compose.

Documenta:

- URL local usada.
- Usuario inicial creado.
- Organización del laboratorio.
- Plantilla de caso creada.

No publiques la contraseña.

## Modelo mínimo de casos

Crea una plantilla llamada:

```text
SOC-Lab Endpoint Alert
```

Campos mínimos:

| Campo | Contenido |
|---|---|
| Título | Tipo de alerta + endpoint |
| Severidad | Baja / Media / Alta |
| TLP | CLEAR o AMBER, según práctica |
| Descripción | Resumen de la alerta Wazuh |
| Tareas | Triage, validación, contención, cierre |
| Observables | IP, hostname, usuario, hash si existe |

## Evidencia mínima de esta fase

Guardar en:

```text
evidence/fase-1/thehive-install/
```

Evidencias recomendadas:

- `docker compose ps` sin errores.
- Pantalla de login de TheHive.
- Organización creada.
- Plantilla de caso creada.

## Problemas comunes

### Contenedores reiniciando

```bash
docker compose ps
docker compose logs --tail=200 <servicio>
```

Causas comunes:

- RAM insuficiente.
- Variables `.env` incompletas.
- Puertos ocupados.
- Volúmenes con permisos incorrectos.

### Consumo alto de RAM

En un host de 16 GB, puede ser necesario trabajar por fases:

1. Validar Wazuh + agente.
2. Apagar cliente si no se usa.
3. Levantar TheHive.
4. Levantar Shuffle después.
