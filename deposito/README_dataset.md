# ENMA 2023 — Base anonimizada

## Qué es

La Encuesta Nacional Migrante de Argentina releva las condiciones de vida, las trayectorias y el
acceso a derechos de las personas migrantes, solicitantes de asilo y refugiadas residentes en el
país. Su propósito es producir información representativa para el diseño y la incidencia de
políticas públicas.

Esta base reúne los **4.679 casos** de la edición 2023, con **228 variables**. El archivo
`ENMA2023_anonima_v2.csv` está en codificación UTF-8, con una fila por persona encuestada y
encabezados en la primera línea, de modo que puede abrirse con cualquier lector de datos. No
contiene identificadores directos ni datos que permitan identificar a las personas encuestadas, de
acuerdo con el carácter anónimo con que se levantó la encuesta.

## Qué contiene

De las 228 variables, 216 corresponden a las preguntas del cuestionario y 12 son variables
elaboradas para el análisis.

El cuestionario se organiza en once secciones:

- **Información general.** Edad, país de nacimiento, género, descendencia, lengua materna y nivel de
  comprensión del castellano.
- **Trayectorias y proyecto migratorio.** Año de llegada, modo de ingreso, residencia previa en el
  país y motivos de la migración.
- **Situación documentaria.** Tenencia y situación del DNI, situación documentaria, dificultades de
  trámite, solicitud de asilo y naturalización.
- **Situación familiar y hogar.** Composición del hogar, convivencia en pareja, discapacidad y
  cantidad de hijos.
- **Hijes y educación.** Hijos nacidos en Argentina y en el exterior, asistencia escolar,
  inconvenientes de acceso y discriminación en el ámbito educativo.
- **Derecho a la salud.** Cobertura, problemas de salud, circuito de resolución, acceso al sistema y
  dificultades encontradas.
- **Vivienda.** Tipo, tenencia, problemas habitacionales y servicios con que cuenta.
- **Su trayectoria educativa.** Máximo nivel alcanzado, estudios en curso, inconvenientes de
  inscripción y problemas durante la cursada.
- **Situación socioeconómica.** Situación ocupacional, experiencia laboral, dificultades de acceso
  al trabajo, envío de remesas, estrategias de gastos y percepción de subsidios.
- **Discriminación y violencia.** Experiencias de discriminación por ámbito y situaciones de
  violencia.
- **Participación social y política.** Participación en organizaciones, elecciones locales y
  elecciones en el exterior.

Las preguntas de selección múltiple se presentan expandidas. Cada opción de respuesta es una columna
indicadora, de manera que las categorías originales se reconstruyen sumando las opciones que
correspondan.

Las doce variables elaboradas son las agrupaciones de género, edad, nacionalidad, región, nivel
educativo, tiempo de residencia y migración reciente, una tipología de circuitos laborales, y los
dos ponderadores `weightvec` y `weightvec_0`. Los ponderadores permiten calcular estimaciones
representativas y conviene usarlos en cualquier tabulación.

## Cómo usar la base y el código

El CSV se lee directamente desde el entorno que se prefiera. En R, por ejemplo:

```r
enma <- read.csv("ENMA2023_anonima_v2.csv", encoding = "UTF-8")

library(dplyr)
enma %>%
  group_by(nacionalidad_agrup, genero_agrup) %>%
  summarise(casos = sum(weightvec), .groups = "drop")
```

El repositorio de código está en https://github.com/natdebandi/ENMA_2023 y acompaña a esta base. Sus
ocho capítulos en R Markdown reproducen los cruces y las tabulaciones del Anuario Migratorio
Argentino 2024 y sirven como punto de partida para otras explotaciones: cada capítulo carga la base,
la procesa y presenta los cuadros, de modo que pueden adaptarse cambiando las variables de
agrupamiento. Los capítulos leen el archivo desde la ruta `data/`, que no se distribuye, así que
para reutilizarlos hay que guardar el CSV descargado en esa carpeta con el nombre
`ENMA2023_anonima_v2.csv`.

El repositorio incluye además `scripts/medir_reidentificacion.py`, que mide el riesgo de
reidentificación por combinación de variables, y `scripts/anonimizar_enma.py`, que documenta cómo se
generó esta versión desde el archivo de origen.

## Marco de uso

La base no constituye una liberación oficial de la ENMA. Su uso se enmarca en los lineamientos del
Comité de Ética de CONICET y en la Ley de Protección de Datos Personales (N.º 25.326), que son el
marco declarado por la encuesta para la circulación de sus datos.

## Fuente y cómo citar

**Fuente:** Encuesta Nacional Migrante de Argentina (ENMA), edición 2023. La encuesta es una
iniciativa de la Red de Investigaciones en Derechos Humanos del CONICET y de organizaciones de
migrantes e investigadoras e investigadores de todo el país. Sitio de la encuesta y documentación:
https://www.encuestamigrante.ar/

Base anonimizada, versión 1:
https://github.com/natdebandi/ENMA_2023/releases/tag/datos-v1

Licencia: Creative Commons Atribución 4.0 Internacional.
