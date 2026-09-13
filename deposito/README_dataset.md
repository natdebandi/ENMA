# ENMA 2023. Base de datos

`ENMA2023_anonima_v2.csv` reúne 4.679 casos y 228 variables de la segunda edición de la Encuesta
Nacional Migrante de Argentina, levantada en 2023. Cada fila corresponde a una persona migrante,
solicitante de asilo o refugiada mayor de 18 años residente en el país, que respondió el cuestionario
de manera anónima y voluntaria. El archivo está separado por comas, con codificación UTF-8 y una
fila de encabezado.

La ENMA es una iniciativa de la Red de Investigaciones en Derechos Humanos del CONICET junto a
organizaciones de migrantes e investigadoras e investigadores de todo el país, que se realiza cada
tres años desde 2020 con un enfoque práctico de derechos humanos. Mide condiciones de vida,
trayectorias y acceso efectivo a derechos, con cobertura nacional y representatividad regional. La
descripción del diseño, del trabajo de campo y del esquema de ponderación consta en el documento
metodológico de la edición, disponible en https://www.encuestamigrante.ar/

## Composición de la muestra

La muestra sobrerrepresenta al Área Metropolitana de Buenos Aires, a las mujeres y a las
nacionalidades del MERCOSUR, en relación con la modalidad de captación de la encuesta. Los
ponderadores corrigen esa distribución para las estimaciones.

| Dimensión | Distribución de casos |
|---|---|
| Región de residencia | AMBA 3.211 (68,6 %), Región Pampeana 483 (10,3 %), Cuyo 399 (8,5 %), Patagonia 276 (5,9 %), NEA 173 (3,7 %), NOA 137 (2,9 %) |
| Género | Mujer 3.103 (66,3 %), Varón 1.501 (32,1 %), otras identidades 60 (1,3 %), prefiere no responder 15 (0,3 %) |
| Edad | 18 a 34 años 1.609 (34,4 %), 35 a 54 años 2.285 (48,8 %), 55 y más 785 (16,8 %). Rango de 18 a 100 años, mediana de 39 |
| Agrupamiento de nacionalidad | MERCOSUR 4.103 (87,7 %), extra MERCOSUR no europeas 425 (9,1 %), extra MERCOSUR europeas 150 (3,2 %), apátrida 1 |
| Tiempo de residencia | Hasta 5 años 1.312 (28,0 %), entre 5 y 9 años 753 (16,1 %), más de 10 años 2.584 (55,2 %), sin dato 30 |
| Nivel educativo alcanzado | Superior completo y más 1.843 (39,4 %), secundario completo 1.708 (36,5 %), hasta secundario incompleto 1.083 (23,1 %), sin dato 45 |

El país de nacimiento registra veinticuatro países declarados más una categoría de resto,
encabezados por Venezuela (1.001 casos), Paraguay (956), Bolivia (636), Perú (398), Colombia (357),
Brasil (304) y Chile (249). El año de llegada abarca de 1935 a 2023 con mediana en 2012, y 1.312
personas llegaron a partir de 2018, lo que permite distinguir la migración reciente de la de larga
residencia. Dieciséis lenguas figuran como idioma de origen, entre ellas el guaraní (521 casos), el
portugués (301), el quechua (97), el creole haitiano (83) y el aymara (46).

## Organización de las variables

Las variables conservan la numeración del cuestionario con el prefijo `q` seguido del número de
pregunta y una etiqueta descriptiva, de modo que `q46_estudios` corresponde a la pregunta 46. Los
bloques temáticos son los siguientes.

| Bloque | Preguntas | Variables |
|---|---|---:|
| Perfil sociodemográfico, descendencia e idioma | q2 a q7 | 15 |
| Trayectoria migratoria, modo de ingreso y motivos | q12 a q16 | 17 |
| Situación documentaria, asilo y naturalización | q17 a q25 | 18 |
| Hogar, convivencia e hijos e hijas | q26 a q31 | 7 |
| Escolarización de hijos e hijas | q32 a q35 | 11 |
| Salud, cobertura y acceso | q36 a q40 | 26 |
| Vivienda, tenencia y servicios | q41 a q45 | 24 |
| Educación de la persona respondiente | q46 a q50 | 18 |
| Trabajo, experiencia y dificultades de inserción | q51 a q57 | 16 |
| Ingresos, remesas, endeudamiento y transferencias | q58 a q61 | 28 |
| Discriminación y violencia | q62 a q65 | 14 |
| Participación en organizaciones y elecciones | q66 a q71 | 21 |
| Percepción de la propia situación a dos años | q72 | 1 |
| Variables derivadas y ponderadores | | 12 |

La numeración presenta saltos porque la base no incluye las preguntas de geografía a nivel de
provincia, localidad y barrio ni la ocupación declarada en texto libre, que son los campos retirados
para preservar el anonimato. Tampoco contiene identificadores directos ni las respuestas abiertas de
redacción libre. El detalle de ese tratamiento y la medición del riesgo residual constan en el
informe técnico del repositorio.

Las doce variables derivadas vienen construidas en la base y son las que utilizan los capítulos del
Anuario. Comprenden `genero_agrup`, `edad_agrup`, `nacionalidad_var`, `nacionalidad_agrup`,
`region_amba_agrup`, `niveled_agrup`, `sec_completo_agrup`, `tiempo_residencia_agrup`,
`migracion_reciente`, `circuitos_laborales` y los dos ponderadores. La variable
`circuitos_laborales` clasifica la inserción laboral en cinco circuitos y deja 710 casos sin
asignación. La variable `region_amba_agrup` es la única de localización disponible, de modo que los
análisis territoriales admiten el nivel de las seis regiones y no el provincial.

## Preguntas de respuesta múltiple

Las preguntas que admitían más de una opción aparecen dos veces en la base y conviene trabajar con
la segunda forma. La variable madre guarda las opciones elegidas concatenadas en una sola cadena de
texto, lo que produce cientos de combinaciones distintas y la vuelve poco apta para tabular. Junto a
ella, cada opción tiene su propia variable dicotómica con el sufijo correspondiente. Así,
`q14_motivos` contiene 389 cadenas diferentes mientras que `q14_motivos_estudio`,
`q14_motivos_mejor_trabajo` y las demás del bloque toman valor 1 cuando la opción fue elegida y 0
cuando no. La base contiene 148 variables dicotómicas de este tipo.

## Valores ausentes

El archivo maneja dos formas de ausencia que conviene distinguir al leerlo. La cadena `NA` aparece en
127 variables e indica que la pregunta no fue respondida. La celda vacía aparece en 53 variables y
señala en general que la pregunta no correspondía por el filtro del cuestionario. Las preguntas
filtradas concentran por eso bloques amplios de celdas vacías, como `q63_discriminacion` con 2.326
casos que no reportaron situaciones de discriminación en la pregunta previa, o
`q34_asistencia_educacion_razon` con 3.797 casos sin hijos e hijas en edad escolar. Al importar el
archivo corresponde declarar las dos formas como ausentes, por ejemplo con
`read.csv(..., na.strings = c("NA", ""))` en R o
`pd.read_csv(..., na_values = ["NA", ""], keep_default_na = False)` en Python.

## Ponderadores

La base trae dos vectores de ponderación, `weightvec` y `weightvec_0`. Ambos presentan 454 valores
distintos y suman 4.679, es decir el tamaño de la muestra, de modo que las sumas ponderadas se
expresan en casos y no en población proyectada. Los dos responden a calibraciones diferentes y los
capítulos del Anuario los emplean según el cuadro, por lo que la elección entre uno y otro
corresponde seguir lo que indica el documento metodológico de la edición. Las estimaciones de
proporciones requieren aplicar el ponderador y no el recuento simple de casos.

## Marco de uso

Esta versión no constituye una liberación oficial de la ENMA. Se elaboró a partir del archivo de
origen de la encuesta y se publica con fines de investigación académica y social. Su uso se enmarca
en los Lineamientos para el Comportamiento Ético en las Ciencias Sociales y Humanidades del Comité de
Ética de CONICET (Res. 2857/2006), en la Guía para Investigaciones con Seres Humanos (Res.
Ministerio de Salud 1480/2011) y en la Ley de Protección de Datos Personales (N.º 25.326). La
encuesta fue diseñada desde una perspectiva de derechos humanos y su uso debe resguardar la
información de las personas que respondieron, lo que excluye todo intento de reidentificación y todo
cruce con otras fuentes orientado a ese fin.

El archivo se distribuye bajo licencia Creative Commons Atribución 4.0 Internacional, cuyo texto
consta en `LICENSE_datos_CC-BY-4.0.txt`. La integridad de la descarga se verifica contra
`SHA256SUMS.txt`.

## Cómo citar

Debandi, Natalia (2026). ENMA 2023. Base de datos anonimizada, versión 1. Centro de Inteligencia
Artificial Interdisciplinario, Universidad Nacional de San Martín y CONICET.
https://github.com/natdebandi/ENMA_2023/releases/tag/datos-v1

La cita de la base no reemplaza la de la encuesta. Corresponde que los trabajos que la utilicen
referencien también a la Encuesta Nacional Migrante de Argentina como fuente primaria, en
https://www.encuestamigrante.ar/
