# 13. Evidencias y gráficas

## Objetivo

Definir cómo guardar evidencias y cómo generar gráficas sin inventar datos.

## Estructura recomendada

```text
evidence/
├── fase-1/
│   ├── auth-fail/
│   ├── fim/
│   └── windows-sysmon/
├── fase-2/
│   ├── auth-fail-playbook/
│   ├── fim-playbook/
│   └── windows-playbook/

data/
├── wazuh_alerts_export.csv
├── thehive_cases_export.csv

reports/
├── figures/
│   ├── alerts_by_rule_level.png
│   ├── alerts_by_agent.png
│   └── alerts_by_mitre.png
```

## Nombres de archivos

Formato recomendado:

```text
YYYY-MM-DD_fase_prueba_descripcion.ext
```

Ejemplos:

```text
2026-07-11_fase1_authfail_wazuh-alert.png
2026-07-11_fase1_fim_alert-export.json
2026-07-11_fase2_shuffle_execution.png
```

## Qué debe tener una evidencia válida

| Elemento | Obligatorio |
|---|---|
| Fecha/hora | Sí |
| Herramienta | Sí |
| Máquina afectada | Sí |
| Evento o alerta | Sí |
| Contexto de la prueba | Sí |
| Captura/exportación | Sí |
| Datos sensibles ocultos | Sí |

## Exportar datos para gráficas

Desde Wazuh Dashboard, exporta alertas a CSV si la interfaz lo permite. Guarda el archivo como:

```text
data/wazuh_alerts_export.csv
```

El script `analysis/generate_graphs.py` intentará detectar columnas comunes como:

```text
rule.level
agent.name
rule.mitre.technique
```

Si tus columnas tienen otros nombres, modifica el script o renombra columnas en el CSV.

## Generar gráficas

Instala dependencias:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install pandas matplotlib
```

Ejecuta:

```bash
python analysis/generate_graphs.py data/wazuh_alerts_export.csv reports/figures
```

El script no genera datos simulados. Si no hay CSV real, termina con error.

## Reglas para publicar evidencias

Antes de subir a GitHub:

- Oculta tokens.
- Oculta contraseñas.
- Oculta IP pública si aparece.
- Evita nombres reales de usuarios.
- Evita datos personales.
- Mantén IPs privadas del laboratorio solo si no te preocupa mostrarlas.
