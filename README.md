# ENMA 2023

La ENMA es una iniciativa de producción de datos primarios que busca relevar las condiciones de vida en las que se encuentran las personas migrantes, solicitantes de asilo y refugiadas que viven en la República Argentina, así como su nivel de acceso a derechos en todos los órdenes sociales.

La ENMA releva las condiciones de vida, las trayectorias y el acceso efectivo a derechos de las
personas migrantes, solicitantes de asilo y refugiadas residentes en el país. Se desarrolla desde la
Red de Investigaciones en Derechos Humanos del CONICET en conjunto con más de 55 organizaciones de
migrantes, con un enfoque práctico de derechos humanos, y se realiza cada tres años desde 2020.

Este repositorio reúne dos cosas. La base de datos de la edición 2023, en la versión que se publica
para su uso abierto, y el procesamiento en R que sirvió de base a los ocho capítulos del Anuario
Migratorio Argentino 2024
(https://www.encuestamigrante.ar/wp-content/uploads/documentos/anuario_enma_2023_vf.pdf).

## Descargar la base

**https://github.com/natdebandi/ENMA_2023/releases/tag/datos-v1**

La descarga no requiere credenciales. El release ofrece el archivo `ENMA2023_anonima_v2.csv`, el
paquete comprimido que reúne los datos con su documentación y la licencia, y el listado de
verificación de integridad `SHA256SUMS.txt`.

La base contiene 4.679 casos y 228 variables, con una fila por persona encuestada. Cubre información
general, trayectoria y proyecto migratorio, situación documentaria, hogar y familia, educación de
hijos e hijas, salud, vivienda, trayectoria educativa, situación socioeconómica, discriminación y
violencia, y participación social y política.

**Antes de trabajar con los datos conviene leer [`documentacion/BASE_enma2023.md`](documentacion/BASE_enma2023.md).**
Documenta la composición de la muestra, la organización de las variables, el despliegue de las
preguntas de selección múltiple, las dos formas de valor ausente y, en particular, la diferencia
entre los dos ponderadores, que no son intercambiables.

## Contenido del repositorio

- `Cap1_v2.Rmd` a `Cap8_v2.Rmd`, los capítulos del Anuario en R Markdown con su versión html. El
  orden es perfil sociodemográfico, situación documentaria, educación, salud, trabajo, vivienda,
  discriminación y participación. Sirven de punto de partida para otras explotaciones de la base.
- `documentacion/BASE_enma2023.md`, la descripción de la base publicada y las advertencias que
  condicionan su uso.
- `documentacion/Documento_metodologico_ENMA_2023.pdf`, el diseño muestral, el trabajo de campo y la
  construcción de los ponderadores, en el documento de la fuente.
- `documentacion/Cuestionario_ENMA_2023.pdf`, el instrumento completo, con la redacción y el orden
  de las preguntas que dan origen a cada variable.
- `documentacion/INFORME_tratamiento_base.md`, el tratamiento aplicado a la base, la medición del
  riesgo de reidentificación y las decisiones de publicación.
- `documentacion/SHA256SUMS.txt`, la verificación de integridad de los archivos del release.
- `LICENSE-datos.txt`, la licencia de los datos.

Los capítulos leen el archivo desde `data/`, ruta que el control de versiones no incluye. Su
ejecución requiere descargar la base y ubicarla allí.

## Marco de uso

La encuesta se diseñó desde una perspectiva de derechos humanos, promoviendo la igualdad y el respeto
de las personas migrantes. Todo uso opuesto a ese objetivo, así como la tergiversación de los datos y
cualquier intento de reidentificación de las personas encuestadas, resulta contrario al propósito con
que fue producida.

La versión que se publica aquí no incluye identificadores directos, geografía por debajo de la región
ni campos de texto libre. Quien requiera los microdatos completos puede solicitarlos a la fuente
mediante el formulario disponible en https://www.encuestamigrante.ar/

El uso de los datos se enmarca en los Lineamientos para el Comportamiento Ético en las Ciencias
Sociales y Humanidades del Comité de Ética de CONICET (Res. 2857/2006), en la Guía para
Investigaciones con Seres Humanos (Res. Ministerio de Salud 1480/2011) y en la Ley de Protección de
Datos Personales (N.º 25.326).

Los datos se distribuyen bajo licencia Creative Commons Atribución 4.0 Internacional, cuyo texto
consta en `LICENSE-datos.txt`.

## Autoría

Natalia Debandi. Centro de Inteligencia Artificial Interdisciplinario (CIAI), Universidad Nacional
de San Martín y CONICET, Argentina. ORCID https://orcid.org/0000-0002-2619-6270

La autoría corresponde a la preparación de la base publicada y al procesamiento que contiene el
repositorio. La encuesta es obra colectiva de la ENMA, así como el documento metodológico y el
cuestionario que se reproducen en `documentacion/`.

## Cómo citar

Cita de la fuente, en el formato que sugiere su documento metodológico:

> ENMA 2023 (06/2024). Encuesta Nacional Migrante de Argentina 2023 [Base de datos]. Recuperado de
> https://encuestamigrante.ar/

Cita de esta versión de la base:

> Debandi, Natalia (2026). ENMA 2023. Base de datos, versión 1. Centro de Inteligencia Artificial
> Interdisciplinario, Universidad Nacional de San Martín y CONICET.
> https://github.com/natdebandi/ENMA_2023/releases/tag/datos-v1

La cita de esta versión no reemplaza la de la encuesta como fuente primaria.
