# ENMA_2023

Encuesta Nacional Migrante de Argentina, edición 2023.

El repositorio contiene el procesamiento en R de los datos de la ENMA 2023 que sirvió de base al
Anuario Migratorio Argentino 2024
(https://www.encuestamigrante.ar/wp-content/uploads/documentos/anuario_enma_2023_vf.pdf)

## Contenido

- `Cap1_v2.Rmd` a `Cap8_v2.Rmd`: los capítulos del Anuario, cada uno con su versión html.
- `scripts/anonimizar_enma.py`: genera la versión anonimizada de la base.
- `scripts/medir_reidentificacion.py`: mide el riesgo de reidentificación por combinación de variables.
- `informe/INFORME_enma2023.md`: documenta el tratamiento aplicado y las decisiones adoptadas.
- `deposito/`: documentación que acompaña a la base publicada.

## Los datos

Los microdatos de la ENMA se solicitan a la fuente mediante formulario, en
https://www.encuestamigrante.ar/ . El archivo original no forma parte de este repositorio; su
reproducción requiere disponer de él en `data/`, ruta que el `.gitignore` mantiene fuera del control
de versiones.

La base que se publica es una versión anonimizada, de 4.679 registros y 228 variables, generada
desde el original con `scripts/anonimizar_enma.py`. Está disponible como adjunto de la versión
`datos-v1` en https://github.com/natdebandi/ENMA_2023/releases y el detalle del tratamiento consta
en `informe/INFORME_enma2023.md`.

La encuesta es una iniciativa del CONICET y de organizaciones de migrantes y de derechos humanos.
El uso de los datos se enmarca en la Ley de Protección de Datos Personales (N.º 25.326) y en los
lineamientos del Comité de Ética de CONICET.

## Cómo citar

Base anonimizada, versión 1:
https://github.com/natdebandi/ENMA_2023/releases/tag/datos-v1

Sitio de la encuesta: https://www.encuestamigrante.ar/
