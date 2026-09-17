# ENMA

La ENMA es una iniciativa de producción de datos primarios que releva las condiciones de vida en las
que se encuentran las personas migrantes, solicitantes de asilo y refugiadas que viven en la
República Argentina, sus trayectorias y su nivel de acceso efectivo a derechos en todos los órdenes
sociales. Se desarrolla desde la Red de Investigaciones en Derechos Humanos del CONICET en conjunto
con organizaciones de migrantes, con un enfoque práctico de derechos humanos, y se realiza cada tres
años desde 2020.

Este repositorio reúne las bases de datos de la encuesta en la versión que se publica para su uso
abierto, con la documentación de cada edición, y el procesamiento en R que sirvió de base a los ocho
capítulos del Anuario Migratorio Argentino 2024
(https://www.encuestamigrante.ar/wp-content/uploads/documentos/anuario_enma_2023_vf.pdf).

## Descargar las bases

**ENMA 2023 — https://github.com/natdebandi/ENMA/releases/tag/datos-v1**

**ENMA 2020 — https://github.com/natdebandi/ENMA/releases/tag/datos-2020-v1**

La descarga no requiere credenciales. Cada release ofrece el archivo separado por comas de la
edición, el paquete comprimido que reúne los datos con su documentación y la licencia, y el listado
de verificación de integridad `SHA256SUMS.txt`.

| | ENMA 2020 | ENMA 2023 |
|---|---:|---:|
| Casos | 3.114 | 4.679 |
| Variables | 202 | 228 |
| Preguntas del cuestionario | 62 | 73 |
| Regiones de residencia | 6 más una categoría residual | 6 |
| Ponderador de estimaciones totales | `pesos_para_estimaciones_totales` | `weightvec` |
| Ponderador por nacionalidad | `pesos_para_estimaciones_por_nacionalidad` | `weightvec_0` |
| Documentación de la base | [`documentacion/BASE_enma2020.md`](documentacion/BASE_enma2020.md) | [`documentacion/BASE_enma2023.md`](documentacion/BASE_enma2023.md) |

**Antes de trabajar con los datos conviene leer el documento de base de la edición.** Documenta la
composición de la muestra, la organización de las variables, el despliegue de las preguntas de
selección múltiple, las formas de valor ausente y, en particular, la diferencia entre los dos
ponderadores, que no son intercambiables.

## Contenido del repositorio

- `documentacion/`, la documentación de las dos ediciones publicadas. Para cada una reúne el
  documento de base y las advertencias que condicionan su uso, el informe técnico del tratamiento
  aplicado y la medición del riesgo residual, el documento metodológico y el cuestionario de la
  fuente, y el listado de verificación de integridad.
- `Cap1_v2.Rmd` a `Cap8_v2.Rmd`, los capítulos del Anuario Migratorio Argentino 2024 sobre la edición
  2023, en R Markdown con su versión html. El orden es perfil sociodemográfico, situación
  documentaria, educación, salud, trabajo, vivienda, discriminación y participación. Sirven de punto
  de partida para otras explotaciones de la base.
- `LICENSE-datos.txt`, la licencia de los datos.

Los capítulos leen el archivo desde `data/`, ruta que el control de versiones no incluye. Su
ejecución requiere descargar la base y ubicarla allí.

## Advertencia sobre la comparación entre ediciones

Las bases de 2020 y de 2023 **no son integrables de manera automática**, porque los cuestionarios
difieren en secciones, preguntas y opciones. La edición 2020 publica una variable de región con las
mismas categorías que la de 2023, de modo que el cruce territorial es posible entre ambas, pero eso
no vuelve comparables las preguntas. El equipo estadístico de la ENMA trabaja en la integración de
las dos ediciones.

## Marco de uso

La encuesta se diseñó desde una perspectiva de derechos humanos, promoviendo la igualdad y el respeto
de las personas migrantes. Todo uso opuesto a ese objetivo, así como la tergiversación de los datos y
cualquier intento de reidentificación de las personas encuestadas, resulta contrario al propósito con
que fue producida.

Las versiones que se publican aquí no incluyen identificadores directos, geografía por debajo de la
región ni campos de texto libre. Quien requiera los microdatos completos puede solicitarlos a la
fuente mediante el formulario disponible en https://www.encuestamigrante.ar/

El uso de los datos se enmarca en los Lineamientos para el Comportamiento Ético en las Ciencias
Sociales y Humanidades del Comité de Ética de CONICET (Res. 2857/2006), en la Guía para
Investigaciones con Seres Humanos (Res. Ministerio de Salud 1480/2011) y en la Ley de Protección de
Datos Personales (N.º 25.326).

Los datos se distribuyen bajo licencia Creative Commons Atribución 4.0 Internacional, cuyo texto
consta en `LICENSE-datos.txt`.

## Autoría

Natalia Debandi. Centro de Inteligencia Artificial Interdisciplinario (CIAI), Universidad Nacional
de San Martín y CONICET, Argentina. ORCID https://orcid.org/0000-0002-2619-6270

La autoría corresponde a la preparación de las bases publicadas y al procesamiento que contiene el
repositorio. La encuesta es obra colectiva de la ENMA, así como los documentos metodológicos y los
cuestionarios que se reproducen en `documentacion/`.

## Cómo citar

Cita de la fuente, en el formato que sugieren los documentos metodológicos:

> ENMA 2020. Encuesta Nacional Migrante de Argentina 2020 [Base de datos]. Recuperado de
> https://encuestamigrante.ar/

> ENMA 2023 (06/2024). Encuesta Nacional Migrante de Argentina 2023 [Base de datos]. Recuperado de
> https://encuestamigrante.ar/

Cita de la versión publicada de cada base:

> Debandi, Natalia (2026). ENMA 2020. Base de datos, versión 1. Centro de Inteligencia Artificial
> Interdisciplinario, Universidad Nacional de San Martín y CONICET.
> https://github.com/natdebandi/ENMA/releases/tag/datos-2020-v1

> Debandi, Natalia (2026). ENMA 2023. Base de datos, versión 1. Centro de Inteligencia Artificial
> Interdisciplinario, Universidad Nacional de San Martín y CONICET.
> https://github.com/natdebandi/ENMA/releases/tag/datos-v1

La cita de cada versión no reemplaza la de la encuesta como fuente primaria.
