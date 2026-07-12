# 06. Instalación de Shuffle

## Objetivo

Instalar Shuffle en `VM-SERVER-SOC` para crear playbooks de automatización de seguridad.

## Enfoque recomendado

Shuffle se despliega normalmente con Docker Compose y usa un archivo `.env` para configuración. En el laboratorio se usará como SOAR local.

## Preparación

Asegúrate de tener Docker y Docker Compose funcionando:

```bash
docker version
docker compose version
docker run hello-world
```

## Clonar Shuffle

```bash
mkdir -p ~/soc-lab/services
cd ~/soc-lab/services
git clone https://github.com/Shuffle/Shuffle.git shuffle
cd shuffle
```

Revisa los archivos:

```bash
ls -la
ls -la docker-compose.yml .env
```

## Configuración local

Revisa `.env` antes de arrancar. No subas `.env` a GitHub.

Puntos a revisar:

- Puerto de frontend.
- URL pública/local.
- Persistencia de base de datos.
- Credenciales iniciales.
- Opciones de conexión externa.

## Puesta en marcha

```bash
docker compose pull
docker compose up -d
```

Validación:

```bash
docker compose ps
docker compose logs --tail=100
```

Accede desde navegador usando el puerto definido por Shuffle.

## Primer workflow de prueba

Crea un workflow llamado:

```text
SOC-Lab - Webhook Test
```

Entrada:

```json
{
  "source": "manual-test",
  "event_type": "connectivity-check",
  "severity": "low",
  "host": "vm-client-01"
}
```

Salida esperada:

- Ejecución registrada en Shuffle.
- Registro de entrada recibido.
- Sin acciones destructivas.

## Evidencia mínima de esta fase

Guardar en:

```text
evidence/fase-1/shuffle-install/
```

Evidencias recomendadas:

- `docker compose ps`.
- Pantalla inicial de Shuffle.
- Workflow de prueba creado.
- Ejecución de webhook de prueba.

## Reglas de seguridad

- No configures acciones destructivas al inicio.
- No uses tokens reales en capturas públicas.
- No automatices bloqueo de usuarios o aislamiento de endpoints hasta validar manualmente.
- Toda acción de respuesta debe tener modo `manual approval` en las primeras fases.
