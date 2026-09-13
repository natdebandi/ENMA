# ENMA 2023 — Base de datos

## Qué es

La Encuesta Nacional Migrante de Argentina releva las condiciones de vida, las trayectorias y el
acceso efectivo a derechos de las personas migrantes, solicitantes de asilo y refugiadas residentes
en el país. Es la única fuente de datos primarios específica y de aplicación periódica sobre esta
población en la Argentina, se realiza cada tres años desde 2020 y su propósito es producir
información para el análisis, la incidencia pública y el diseño de políticas.

Esta base reúne los **4.679 casos** de la edición 2023, con **228 variables**. El archivo
`ENMA2023_anonima_v2.csv` está en codificación UTF-8, con una fila por persona encuestada y
encabezados en la primera línea, de modo que puede abrirse con cualquier lector de datos. No
contiene identificadores directos ni datos que permitan identificar a las personas encuestadas, de
acuerdo con el carácter anónimo con que se levantó la encuesta.

El universo son las personas nacidas en un país distinto de la Argentina, mayores de 18 años y
residentes en el país. El diseño muestral emplea un enfoque de cuotas y la muestra fue calibrada por
nacionalidad, género, edad, región de residencia y nivel educativo. El detalle del diseño, del
trabajo de campo y de la construcción de los ponderadores consta en el documento metodológico de la
edición, disponible en https://www.encuestamigrante.ar/

## Qué contiene

De las 228 variables, 216 corresponden a las preguntas del cuestionario y 12 son variables
elaboradas para el análisis. El cuestionario tuvo 73 preguntas organizadas en once secciones, y se
expresa en 216 variables porque las preguntas de selección múltiple se despliegan en una columna
indicadora por opción.

| Sección | Preguntas | Variables | Contenido |
|---|---|---:|---|
| Información general | q2 a q7 | 15 | Edad, país de nacimiento, género, descendencia, lengua materna y nivel de comprensión del castellano |
| Trayectorias y proyecto migratorio | q12 a q16 | 17 | Modo de ingreso, año de llegada, motivos de la migración y mudanzas dentro del país |
| Situación documentaria | q17 a q25 | 18 | Tenencia y situación del DNI, dificultades de trámite, solicitud de asilo y naturalización |
| Situación familiar y hogar | q26 a q31 | 7 | Composición del hogar, convivencia, discapacidad e hijos en el país y en el exterior |
| Hijes y educación | q32 a q35 | 11 | Asistencia escolar, inconvenientes de acceso y discriminación en el ámbito educativo |
| Derecho a la salud | q36 a q40 | 26 | Cobertura, problemas de salud, circuito de resolución, acceso al sistema y dificultades |
| Vivienda | q41 a q45 | 24 | Lugar, tipo, tenencia, problemas habitacionales y servicios disponibles |
| Trayectoria educativa | q46 a q50 | 18 | Máximo nivel alcanzado, estudios en curso e inconvenientes de inscripción y cursada |
| Situación socioeconómica | q51 a q61 | 44 | Situación ocupacional, experiencia, dificultades de acceso al trabajo, remesas, estrategias de gasto, endeudamiento y transferencias estatales |
| Discriminación y violencia | q62 a q65 | 14 | Frecuencia y ámbitos de discriminación, violencia institucional y violencia de género |
| Participación social y política | q66 a q71 | 21 | Participación en organizaciones, en elecciones locales y en elecciones del país de origen |
| Conclusiones | q72 | 1 | Percepción del cambio en la propia situación en los últimos dos años |

Las doce variables elaboradas son `genero_agrup`, `edad_agrup`, `nacionalidad_var`,
`nacionalidad_agrup`, `region_amba_agrup`, `niveled_agrup`, `sec_completo_agrup`,
`tiempo_residencia_agrup`, `migracion_reciente` y `circuitos_laborales`, más los dos ponderadores
`weightvec` y `weightvec_0`. Son las que utilizan los capítulos del Anuario.

## Composición de la muestra

| Dimensión | Distribución de casos |
|---|---|
| Región de residencia | AMBA 3.211 (68,6 %), Región Pampeana 483 (10,3 %), Cuyo 399 (8,5 %), Patagonia 276 (5,9 %), NEA 173 (3,7 %), NOA 137 (2,9 %) |
| Género | Mujer 3.103 (66,3 %), Varón 1.501 (32,1 %), otros géneros 60 (1,3 %), prefiere no responder 15 (0,3 %) |
| Edad | 18 a 34 años 1.609 (34,4 %), 35 a 54 años 2.285 (48,8 %), 55 y más 785 (16,8 %). Rango de 18 a 100 años, mediana de 39 |
| Nacionalidad agrupada | MERCOSUR 4.103 (87,7 %), extra MERCOSUR no europeas 425 (9,1 %), extra MERCOSUR europeas 150 (3,2 %), apátrida 1 |
| Tiempo de residencia | Hasta 5 años 1.312 (28,0 %), entre 5 y 9 años 753 (16,1 %), más de 10 años 2.584 (55,2 %), sin dato 30 |
| Nivel educativo | Superior completo y más 1.843 (39,4 %), secundario completo 1.708 (36,5 %), hasta secundario incompleto 1.083 (23,1 %), sin dato 45 |

El país de nacimiento registra veinticuatro países declarados más una categoría de resto, encabezados
por Venezuela (1.001 casos), Paraguay (956), Bolivia (636), Perú (398), Colombia (357), Brasil (304)
y Chile (249). El diseño buscó además un sobremuestreo de Haití, Senegal, China, República
Dominicana y Cuba, del cual solo Haití alcanzó el mínimo previsto de 80 casos. El año de llegada
abarca de 1935 a 2023, con mediana en 2012. Dieciséis lenguas figuran como idioma de origen, entre
ellas el guaraní (521 casos), el portugués (301), el quechua (97), el creole haitiano (83) y el
aymara (46).

## Los ponderadores

Los dos ponderadores cumplen funciones distintas y **no son intercambiables**. Ambos suman 4.679, es
decir el tamaño de la muestra, de modo que las sumas ponderadas se expresan en casos y no en
población proyectada.

**`weightvec`** es el ponderador principal, de pesos para estimaciones totales. Equilibra el peso
proporcional según nacionalidad, género, edad, región de residencia y nivel educativo. Corresponde
usarlo siempre que se analicen los datos a nivel del total de la base, y es el que va en
prácticamente cualquier tabulación.

**`weightvec_0`** es el ponderador de pesos para estimaciones por nacionalidad. Calibra por género,
edad agrupada y región de residencia dentro de cada nacionalidad, y solo para las diez más numerosas
del país, que son Paraguay, Bolivia, Perú, Venezuela, Chile, Uruguay, Italia, España, Colombia y
Brasil. Corresponde usarlo únicamente cuando se analiza el comportamiento de una variable al
interior de alguna de esas diez nacionalidades. Para analizar cualquier otra nacionalidad, el
documento metodológico recomienda no aplicar ponderador y trabajar en valores absolutos.

## Cómo leer el archivo

Las variables conservan la numeración del cuestionario, con el prefijo `q` seguido del número de
pregunta y una etiqueta descriptiva, de modo que `q46_estudios` corresponde a la pregunta 46.

Las preguntas de selección simple ocupan una sola variable. Las que admitían además un campo abierto
se desdoblan en dos, como `q3_pais_nacimiento` y `q3_pais_otro`.

Las preguntas de selección múltiple aparecen dos veces y conviene trabajar con la segunda forma. La
variable general guarda las opciones elegidas concatenadas en una sola cadena de texto, lo que
produce cientos de combinaciones distintas y la vuelve poco apta para tabular, mientras que cada
opción tiene además su propia variable indicadora. Así, `q14_motivos` contiene 389 cadenas diferentes
mientras que `q14_motivos_estudio`, `q14_motivos_mejor_trabajo` y las demás del bloque toman valor 1
cuando la opción fue elegida y 0 cuando no. La base contiene 148 variables indicadoras de este tipo.

El archivo maneja dos formas de ausencia que conviene distinguir. La cadena `NA` aparece en 127
variables e indica que la pregunta no fue respondida. La celda vacía aparece en 53 variables y señala
en general que la pregunta no correspondía por el filtro del cuestionario, de modo que las preguntas
filtradas concentran bloques amplios de celdas vacías. Al importar el archivo corresponde declarar
las dos formas como ausentes.

En R:

```r
enma <- read.csv("ENMA2023_anonima_v2.csv",
                 encoding = "UTF-8",
                 na.strings = c("NA", ""))

library(dplyr)
enma %>%
  group_by(nacionalidad_agrup, genero_agrup) %>%
  summarise(casos = sum(weightvec, na.rm = TRUE), .groups = "drop")
```

En Python:

```python
import pandas as pd

enma = pd.read_csv("ENMA2023_anonima_v2.csv",
                   na_values=["NA", ""],
                   keep_default_na=False)

(enma.groupby(["nacionalidad_agrup", "genero_agrup"])["weightvec"]
     .sum()
     .reset_index(name="casos"))
```

## Advertencias de uso

**Representatividad territorial.** La muestra es representativa a nivel de las regiones de
residencia y no de cada provincia. El documento metodológico exceptúa a CABA y a la Provincia de
Buenos Aires, que reúnen casos suficientes para el análisis, aunque esta versión de la base no
incluye la variable provincial y el nivel territorial disponible es el de las seis regiones de
`region_amba_agrup`.

**Edad.** La calibración se realizó sobre los grupos de 18 a 29, 30 a 44, 45 a 64 y 65 y más años,
de modo que la muestra no es representativa en edades simples. La variable `edad_agrup` responde a
otra agrupación, de 18 a 34, 35 a 54 y 55 y más años, que se mantuvo por comparabilidad con la
edición 2020 y no coincide con los grupos de calibración.

**Género.** La calibración utilizó el género binario. Para el análisis por género, y en particular
para cruces bivariados, el documento metodológico sugiere trabajar con las categorías varón y mujer
y tratar la categoría de otros géneros en valores absolutos, dado que reúne 60 casos.

**`migracion_reciente`.** El documento metodológico define la migración reciente como aquella con
menos de tres años en el país, pero en la base la variable coincide exactamente con el tramo de hasta
cinco años de `tiempo_residencia_agrup`, con 1.312 casos que corresponden a las llegadas desde 2018.
Quien necesite el umbral de tres años conviene que lo construya desde `q13_anio_llegada`.

**Comparación con 2020.** Las bases de la ENMA 2020 y de la ENMA 2023 no son integrables de manera
automática, porque los cuestionarios difieren en secciones, preguntas y opciones. El equipo
estadístico de la ENMA trabaja en esa integración.

## Qué no incluye esta versión

La numeración de las variables presenta saltos, por dos motivos distintos.

La fuente ya había excluido de la base de uso público las preguntas 52 y 53, sobre registro laboral,
porque presentaron un problema en la configuración de los filtros del cuestionario y arrojaron datos
erróneos. También retiró la pregunta final, de respuesta abierta, para proteger la privacidad de
quien respondía.

Esta versión retira además las variables que permitían reidentificar a una persona, sea por
combinación con otras o por el contenido mismo de la respuesta. Son la geografía a nivel de
provincia, localidad y barrio, la ocupación declarada en texto libre y las respuestas de redacción
libre de los campos de especificación. El detalle del tratamiento y la medición del riesgo residual
constan en el informe técnico del repositorio.

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
detalla el contexto de producción, el objetivo con que fueron recolectados y el análisis realizado
hasta el momento.

## Fuente y cómo citar

La ENMA se desarrolla desde la Red de Investigaciones en Derechos Humanos del CONICET, en conjunto
con más de 55 organizaciones de migrantes y un amplio colectivo de personas que participaron en las
distintas etapas del proceso. Sitio de la encuesta y documentación:
https://www.encuestamigrante.ar/

Cita de la fuente, en el formato que sugiere el documento metodológico:

> ENMA 2023 (06/2024). Encuesta Nacional Migrante de Argentina 2023 [Base de datos]. Recuperado de
> https://encuestamigrante.ar/

Cita de esta versión de la base:

> Debandi, Natalia (2026). ENMA 2023. Base de datos, versión 1. Centro de Inteligencia Artificial
> Interdisciplinario, Universidad Nacional de San Martín y CONICET.
> https://github.com/natdebandi/ENMA_2023/releases/tag/datos-v1

La cita de esta versión no reemplaza la de la encuesta como fuente primaria.

Licencia: Creative Commons Atribución 4.0 Internacional, cuyo texto consta en
`LICENSE_datos_CC-BY-4.0.txt`. La integridad de la descarga se verifica contra `SHA256SUMS.txt`.
