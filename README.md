# ENMA 2023

Base de datos y procesamiento de la segunda edición de la Encuesta Nacional Migrante de Argentina,
levantada en 2023.

El repositorio reúne dos cosas. La base de datos de la edición 2023, en una versión preparada para
su uso público, y el procesamiento en R que sirvió de base a los ocho capítulos del Anuario
Migratorio Argentino 2024
(https://www.encuestamigrante.ar/wp-content/uploads/documentos/anuario_enma_2023_vf.pdf).

## La base de datos

La base reúne 4.679 casos y 228 variables, donde cada fila corresponde a una persona migrante,
solicitante de asilo o refugiada mayor de 18 años residente en la Argentina. Cubre perfil
sociodemográfico, trayectoria migratoria, situación documentaria, hogar, educación, salud, vivienda,
trabajo, ingresos, discriminación y participación, con seis regiones de residencia y dos vectores de
ponderación.

Se descarga desde la versión `datos-v1` del repositorio, en
https://github.com/natdebandi/ENMA_2023/releases/tag/datos-v1

La descripción de la base, su composición, la organización de las variables, el tratamiento de las
preguntas de respuesta múltiple, las convenciones de valores ausentes y el uso de los ponderadores
constan en `deposito/README_dataset.md`. Conviene leer ese archivo antes de trabajar con los datos.

## Contenido del repositorio

- `Cap1_v2.Rmd` a `Cap8_v2.Rmd`, con los capítulos del Anuario y su versión html. El orden es perfil
  sociodemográfico, situación documentaria, educación, salud, trabajo, vivienda, discriminación y
  participación.
- `deposito/`, con la documentación que acompaña a la base publicada, la licencia de los datos y el
  listado de verificación de integridad.
- `informe/INFORME_enma2023.md`, con el tratamiento aplicado a la base, la medición del riesgo de
  reidentificación y las decisiones de publicación.

Los capítulos leen el archivo desde `data/`, ruta que el control de versiones no incluye. Su
ejecución requiere descargar la base y ubicarla allí.

## Marco de uso

La ENMA es una iniciativa de la Red de Investigaciones en Derechos Humanos del CONICET y de
organizaciones de migrantes e investigadoras e investigadores de todo el país. Se realiza cada tres
años desde 2020 con un enfoque práctico de derechos humanos.

La versión que se publica aquí no constituye una liberación oficial de la encuesta. Los microdatos de
la ENMA se solicitan a la fuente mediante el formulario disponible en
https://www.encuestamigrante.ar/ . El uso de los datos se enmarca en los lineamientos del Comité de
Ética de CONICET y en la Ley de Protección de Datos Personales (N.º 25.326), y excluye todo intento
de reidentificación de las personas que respondieron.

Los datos se distribuyen bajo licencia Creative Commons Atribución 4.0 Internacional, cuyo texto
consta en `deposito/LICENSE_datos_CC-BY-4.0.txt`.

## Autoría

Natalia Debandi. Centro de Inteligencia Artificial Interdisciplinario (CIAI), Universidad Nacional
de San Martín y CONICET, Argentina. ORCID https://orcid.org/0000-0002-2619-6270

La autoría corresponde a la preparación de la base publicada y al procesamiento que contiene el
repositorio. La encuesta es obra colectiva de la ENMA.

## Cómo citar

Debandi, Natalia (2026). ENMA 2023. Base de datos anonimizada, versión 1. Centro de Inteligencia
Artificial Interdisciplinario, Universidad Nacional de San Martín y CONICET.
https://github.com/natdebandi/ENMA_2023/releases/tag/datos-v1

Corresponde que los trabajos que utilicen la base referencien también a la Encuesta Nacional
Migrante de Argentina como fuente primaria, en https://www.encuestamigrante.ar/
