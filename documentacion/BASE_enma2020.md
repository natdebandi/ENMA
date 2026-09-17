# ENMA 2020 — Base de datos

## Qué es

La Encuesta Nacional Migrante de Argentina releva las condiciones de vida, las trayectorias y el
acceso efectivo a derechos de las personas migrantes, solicitantes de asilo y refugiadas residentes
en el país. Es una fuente de datos primarios específica y de aplicación periódica sobre esta
población, se realiza cada tres años desde 2020 y su propósito es producir información para el
análisis, la incidencia pública y el diseño de políticas.

Esta base reúne los **3.114 casos** de la primera edición, de 2020, con **202 variables**. El archivo
`ENMA2020_anonima_v1.csv` está en codificación UTF-8, con una fila por persona encuestada y
encabezados en la primera línea, de modo que puede abrirse con cualquier lector de datos. No
contiene identificadores directos ni datos que permitan identificar a las personas encuestadas, de
acuerdo con el carácter anónimo con que se levantó la encuesta.

El universo son las personas nacidas en un país distinto de la Argentina, mayores de 18 años y
residentes en el país. El diseño muestral emplea un enfoque de cuotas y la muestra se calibró por
género, edad, nacionalidad y región de residencia. El detalle del diseño, del trabajo de campo y de
la construcción de los ponderadores consta en el documento metodológico de la edición, que acompaña
a esta documentación en `Documento_metodologico_ENMA_2020.pdf`. El instrumento completo consta en
`Cuestionario_ENMA_2020.doc`. Ambos son documentos de la ENMA y se reproducen aquí para que la base
pueda leerse sin salir del repositorio.

La encuesta de 2020 se aplicó de manera virtual y autoadministrada, con la herramienta Survey
Monkey, entre el 15 de octubre y el 30 de noviembre de ese año. El documento metodológico informa
que se recibieron 3.777 respuestas, de las cuales se excluyeron las de población argentina, las
respuestas duplicadas de una misma persona, las encuestas con abandono temprano y las
inconsistencias, hasta alcanzar los 3.114 casos válidos.

## Qué contiene

De las 202 variables, 192 corresponden a las preguntas del cuestionario y 10 son variables
elaboradas para el análisis. El cuestionario tuvo 62 preguntas dispuestas en bloques temáticos, y se
expresa en más variables porque las preguntas de selección múltiple se despliegan en una columna
indicadora por opción.

| Bloque | Preguntas | Variables | Contenido |
|---|---|---:|---|
| Características de la persona | q1 a q6 | 8 | Género, edad, país de nacimiento, ascendencia, lengua materna y nivel de comprensión del castellano |
| Proyecto y trayectoria migratoria | q10 a q12 | 12 | Tiempo de residencia, motivos de la migración y planes de mudanza |
| Situación documentaria | q13 a q16 | 5 | Situación del DNI, dificultades de trámite, solicitud de asilo y naturalización |
| Situación familiar | q17 a q19 | 3 | Convivencia en pareja, discapacidad en el hogar y tenencia de hijos e hijas |
| Hijes y acceso a la educación | q20 a q24 | 33 | Asistencia escolar, tipo de institución, inconvenientes de inscripción y continuidad durante la pandemia |
| Acceso a la salud | q25 a q30 | 26 | Cobertura, circuito de resolución, dificultades de acceso, enfermedades y COVID-19 |
| Hábitat y acceso a servicios básicos | q31 a q36 | 27 | Tipo y tenencia de la vivienda, dificultades habitacionales, servicios y problemas durante el aislamiento |
| Trayectoria educativa y situación laboral | q37 a q49 | 30 | Nivel educativo, estudios en curso, situación laboral previa y durante la pandemia, remesas y deudas |
| Acceso a ayudas o programas sociales | q50 a q52 | 21 | Ingreso Familiar de Emergencia, ayudas recibidas y programas sociales |
| Discriminación y violencias | q53 a q56 | 11 | Frecuencia y ámbitos de discriminación, violencia institucional y violencia de género |
| Participación política y comunitaria | q57 a q60 | 15 | Participación en organizaciones, elecciones locales y elecciones del país de origen |
| Módulo final | q61 | 1 | Percepción del cambio en la propia situación en el último año |

Las diez variables elaboradas son `Genero_i`, `estudios_i`, `tiempo_i`, `documentos_i`, `edad_i`,
`nacionalidad_c`, `region_amba_agrup` y los dos ponderadores. La base de la fuente no traía la
variable de región, que se construyó para esta versión y se documenta más abajo. El detalle de la
construcción de cada agrupación consta en el informe técnico del repositorio.

## Composición de la muestra

| Dimensión | Distribución de casos |
|---|---|
| Región de residencia | AMBA 2.081 (66,8 %), Región Pampeana 545 (17,5 %), Patagonia 169 (5,4 %), NOA 143 (4,6 %), NEA 62 (2,0 %), Cuyo 57 (1,8 %), sin clasificar 57 (1,8 %) |
| Género | Mujer 1.816 (58,3 %), Varón 1.201 (38,6 %), LGBTTIQ+ 84 (2,7 %), sin dato 13 (0,4 %) |
| Edad | 18 a 34 años 1.337 (42,9 %), 35 a 54 años 1.352 (43,4 %), 55 y más 425 (13,6 %). Rango de 18 a 95 años, mediana de 36 |
| Nacionalidad | Venezuela 989 (31,8 %), Paraguay 402 (12,9 %), Bolivia 263 (8,4 %), Perú 209 (6,7 %), Colombia 198 (6,4 %), Senegal 190 (6,1 %), Chile 163 (5,2 %), Haití 120 (3,9 %), Brasil 98 (3,1 %), y 53 categorías más con 482 casos |
| Tiempo de residencia | Hasta 5 años 1.582 (50,8 %), más de 10 años 1.082 (34,7 %), entre 5 y 9 años 450 (14,5 %) |
| Nivel educativo | Alto 1.267 (40,7 %), medio 893 (28,7 %), bajo 391 (12,6 %), sin dato 563 (18,1 %) |
| Tenencia de DNI | Tiene DNI 2.240 (71,9 %), no tiene 760 (24,4 %), sin dato 114 (3,7 %) |

El país de nacimiento registra veintiocho categorías cerradas más un campo abierto, encabezadas por
Venezuela, Paraguay, Bolivia, Perú, Colombia y Senegal. La pregunta de ascendencia admite más de una
respuesta y la categoría más frecuente es la de quienes no se reconocen en ninguno de los grupos
enunciados. La lengua materna más declarada después del castellano es el guaraní, seguida del wolof,
el portugués y el creole haitiano. El wolof y el francés remiten al colectivo senegalés, que en esta
edición reúne 190 casos y es, después de los cinco colectivos más numerosos, el mejor representado
entre los grupos sin referencia estadística propia.

## La variable de región

La edición 2020 no incluye en la base una variable de región de residencia, y el documento
metodológico consigna que el diseño buscó representatividad regional y no provincial. Sin esa
variable no hay análisis territorial posible ni comparación con la edición 2023, de modo que esta
versión la incorpora como `region_amba_agrup`, con las mismas categorías que publica 2023: AMBA,
Región Pampeana, Cuyo, NEA, NOA y Patagonia.

La asignación se resolvió en dos pasos. Las veintitrés provincias distintas de la Provincia de
Buenos Aires se asignaron por su pertenencia regional directa. La Provincia de Buenos Aires, que
reúne 902 casos, se desdobló entre AMBA y Región Pampeana según la localidad declarada, que es la
información que el documento metodológico usa para ese corte y que el formulario recogía en una
pregunta abierta. Para esa clasificación se recuperó la que la propia fuente aplicó en la edición
2023, disponible en la base de ese año, en lugar de construir una lista propia.

Cincuenta y siete casos de la Provincia de Buenos Aires quedan en la categoría sin clasificar. En su
mayoría son registros sin localidad declarada o con nombres ilegibles, ambiguos o con errores de
carga que no admiten asignación sin forzar el dato. La categoría es residual y se declara como tal
en lugar de distribuir esos casos por criterio.

## Los ponderadores

Los dos ponderadores cumplen funciones distintas y **no son intercambiables**. Ambos suman 3.114, es
decir el tamaño de la muestra, de modo que las sumas ponderadas se expresan en casos y no en
población proyectada.

**`pesos_para_estimaciones_totales`** es el ponderador principal, de pesos para estimaciones
totales. Equilibra el peso proporcional según nacionalidad, género y edad. Corresponde usarlo
siempre que se analicen los datos a nivel del total de la base, y es el que va en prácticamente
cualquier tabulación.

**`pesos_para_estimaciones_por_nacionalidad`** es el ponderador de pesos para estimaciones por
nacionalidad. Calibra por género y edad agrupada dentro de cada nacionalidad, y solo para las
nacionalidades que el documento metodológico señala como cuantitativamente representativas. Ese
documento advierte además que para China, Ecuador, Haití y Senegal, que no tienen datos de
referencia para el ajuste intra-nacional, el ponderador mantiene los datos tal como se obtuvieron en
la muestra en lugar de corregirlos. Corresponde usarlo únicamente cuando se analiza el comportamiento
de una variable al interior de alguno de los colectivos alcanzados, y para cualquier otro conviene
trabajar en valores absolutos.

## Cómo leer el archivo

Las variables conservan la numeración del cuestionario, con el prefijo `q` seguido del número de
pregunta y una etiqueta descriptiva, de modo que `q13_sit_docu` corresponde a la pregunta 13. La
numeración presenta saltos, que se explican más abajo.

Las preguntas de selección simple ocupan una sola variable. Las que admitían además un campo abierto
se desdoblan en dos, como `q3_pais` y `q3_otro`.

Las preguntas de selección múltiple aparecen desplegadas en una columna indicadora por opción. Cada
una de esas columnas toma el valor de la opción elegida cuando esa opción fue seleccionada y queda
vacía cuando no lo fue, de modo que no usan codificación 0/1. La base contiene 151 variables de este
tipo. Las preguntas de selección simple, en cambio, ocupan una sola columna con la categoría cerrada
en cada fila, como `q42_trabajo_preCOVID`, con diez categorías, y `q44_ocupacion`, con catorce.

El archivo maneja dos formas de ausencia que conviene distinguir. La celda vacía indica en general
que la pregunta no correspondía por el filtro del cuestionario, de modo que las preguntas filtradas
concentran bloques amplios de celdas vacías. La cadena `Missing` aparece en tres variables
elaboradas, `Genero_i`, `estudios_i` y `documentos_i`, y señala que la información de origen no
alcanzó para construir la agrupación. Al importar el archivo corresponde declarar las dos formas
como ausentes.

Los dos ponderadores vienen con punto decimal, de modo que se leen como números sin intervención.
El archivo usa la coma como separador de campos y está codificado en UTF-8 sin marca de orden de
bytes.

En R:

```r
enma <- read.csv("ENMA2020_anonima_v1.csv",
                 encoding = "UTF-8",
                 na.strings = c("Missing", ""))

library(dplyr)
enma %>%
  group_by(region_amba_agrup, Genero_i) %>%
  summarise(casos = sum(pesos_para_estimaciones_totales, na.rm = TRUE), .groups = "drop")
```

En Python:

```python
import pandas as pd

enma = pd.read_csv("ENMA2020_anonima_v1.csv",
                   na_values=["Missing", ""],
                   keep_default_na=False)

(enma.groupby(["region_amba_agrup", "Genero_i"])["pesos_para_estimaciones_totales"]
     .sum()
     .reset_index(name="casos"))
```

## Advertencias de uso

**Representatividad territorial.** La muestra es representativa a nivel de las regiones de
residencia y no de cada provincia. La categoría sin clasificar de `region_amba_agrup` reúne 57 casos
y conviene excluirla de los cruces territoriales en lugar de tratarla como una región.

**Edad.** La variable `edad_i` de la base agrupa en tres tramos, de 18 a 34, 35 a 54 y 55 y más
años. El documento metodológico describe para esta edición seis tramos de calibración, de 18 a 29,
30 a 40, 41 a 50, 51 a 60, 61 a 70 y 71 a 110 años, de modo que la agrupación disponible no coincide
con los grupos de calibración. Quien necesite esos tramos puede construirlos desde `q2_edad`, que
conserva la edad en años simples.

**Género.** La calibración se realizó en términos binarios. La variable `Genero_i` conserva la
categoría LGBTTIQ+ con 84 casos, que conviene analizar en valores absolutos, y reúne bajo la marca
de dato ausente las respuestas de quienes prefirieron no informar y de quienes declararon otro
género.

**Contexto de la edición.** El trabajo de campo transcurrió entre octubre y noviembre de 2020, con
la encuesta aplicada de manera virtual durante las restricciones sanitarias por COVID-19. Varios
bloques del cuestionario preguntan de manera explícita por la situación durante la pandemia y por
las estrategias de continuidad, de modo que esas variables describen un momento acotado y no la
situación actual.

**Comparación con 2023.** Las bases de la ENMA 2020 y de la ENMA 2023 no son integrables de manera
automática, porque los cuestionarios difieren en secciones, preguntas y opciones. La variable de
región de esta versión usa las mismas categorías que la de 2023 para que el cruce territorial sea
posible, pero eso no vuelve comparables las preguntas, que en su mayoría cambiaron de redacción,
opciones o lugar en el instrumento.

## Qué no incluye esta versión

La numeración de las variables presenta un salto de tres números consecutivos, que corresponde a las
preguntas 7, 8 y 9. Son las variables que esta versión retira por el tratamiento de anonimización.

Esta versión retira las variables que permitían reidentificar a una persona, sea por combinación con
otras o por el contenido mismo de la respuesta. Son el identificador del registro, la fecha exacta
de la encuesta, la provincia y la localidad de residencia, la residencia previa en otra provincia y
las respuestas de redacción libre de los campos de especificación. El detalle del tratamiento y la
medición del riesgo residual constan en el informe técnico del repositorio.

Las preguntas 7, 8 y 9, sobre provincia, localidad y residencia previa, son las que se retiran por
ese tratamiento. La pregunta final abierta del cuestionario, que invitaba a comentar cualquier
aspecto no incluido, no integra la base de la fuente.
El documento metodológico explica ese criterio al señalar que los campos libres frecuentemente
contienen información sensible que puede permitir identificar a las personas, por lo que el texto
original se sustituyó por la opción de relleno y esos campos no están disponibles. Los campos
cualitativos, agrega, quedan reservados al equipo de la RIOSP bajo controles de resguardo de la
privacidad.

Quien requiera los microdatos completos, con geografía fina o con los campos de texto, puede
solicitarlos a la fuente mediante el formulario disponible en https://www.encuestamigrante.ar/

## Marco de uso

La encuesta se diseñó desde una perspectiva de derechos humanos, promoviendo la igualdad y el respeto
de las personas migrantes. Todo uso opuesto a ese objetivo, así como la tergiversación de los datos y
cualquier intento de reidentificación de las personas encuestadas, resulta contrario al propósito con
que fue producida.

El uso de los datos se enmarca en los Lineamientos para el Comportamiento Ético en las Ciencias
Sociales y Humanidades del Comité de Ética de CONICET (Res. 2857/2006), en la Guía para
Investigaciones con Seres Humanos (Res. Ministerio de Salud 1480/2011) y en la Ley de Protección de
Datos Personales (N.º 25.326).

Para interpretar los datos correctamente conviene leer el documento metodológico de la edición, que
detalla el contexto de producción, el objetivo con que fueron recolectados y las limitaciones que el
propio equipo señala.

## Fuente y cómo citar

La ENMA se desarrolla desde la Red de Investigaciones en Derechos Humanos del CONICET, en conjunto
con más de 30 investigadores del Eje Migración y Asilo de la RIOSP-CONICET y organizaciones de
migrantes y de derechos humanos de todo el país. Sitio de la encuesta y documentación:
https://www.encuestamigrante.ar/

Cita de la fuente:

> ENMA 2020. Encuesta Nacional Migrante de Argentina 2020 [Base de datos]. Recuperado de
> https://encuestamigrante.ar/

Cita de esta versión de la base:

> Debandi, Natalia (2026). ENMA 2020. Base de datos, versión 1. Centro de Inteligencia Artificial
> Interdisciplinario, Universidad Nacional de San Martín y CONICET.
> https://github.com/natdebandi/ENMA/releases/tag/datos-2020-v1

La cita de esta versión no reemplaza la de la encuesta como fuente primaria.

Licencia: Creative Commons Atribución 4.0 Internacional, cuyo texto consta en `LICENSE-datos.txt`,
en la raíz del repositorio. La integridad de la descarga se verifica contra
`documentacion/SHA256SUMS_ENMA2020.txt`.
