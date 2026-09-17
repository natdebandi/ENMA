# ENMA 2020: anonimización y publicación

Informe de trabajo. 2026-09-17.

## 1. El punto de partida

La base de la edición 2020 de la ENMA se encontraba en el disco como `ENMA_2020_final.csv`, con
3.114 filas y 213 columnas, separador de punto y coma y coma decimal en los dos ponderadores. El
mismo archivo aparecía en cuatro ubicaciones del home y las cuatro copias son idénticas, con resumen
criptográfico `c076eb5c…`. No estaba publicado en ningún repositorio: la revisión de las
dieciocho repositorios de la cuenta no encontró ninguna versión versionada ni publicada.

Como la edición 2023, esta base no se distribuye por descarga abierta. El documento metodológico de
2020 señala que la encuesta se aplicó de manera totalmente anónima, sin solicitar ni registrar
información que permitiera identificar a quien respondía, y que los campos abiertos fueron
sustituidos por la opción de relleno porque frecuentemente contienen información sensible. Esos
campos, agrega, quedan reservados al equipo de la RIOSP bajo controles de resguardo de la
privacidad.

El tratamiento se aplicó sobre una copia de trabajo en `data/`, dentro del proyecto. El original, en
`~/investigacion/proyectos/ENMA ENCUESTA/`, no se modificó: conserva el resumen criptográfico y la
fecha de modificación previos.

## 2. La regla de detección de texto libre, y por qué hubo que recalibrarla

La edición 2023 se anonimizó con una regla explícita: se elimina toda columna con al menos diez
valores no vacíos, más del 75 % de valores distintos y extensión media superior a doce caracteres.
Aplicada sin cambios a la base de 2020, esa regla deja pasar el campo de ocupación.

En 2023 la ocupación en texto libre se llamaba `q54_ocupacion` y estaba en la lista de eliminación
explícita, de modo que la regla nunca tuvo que detectarla. En 2020 el equivalente se llama
`q44_ocupacion_otra` y no está en ninguna lista. Sus valores son 783 no vacíos con 537 distintos y
un ratio de 0,69, por debajo del umbral de 0,75: la regla no lo marca. Son oficios y actividades
declaradas en texto libre, del tipo «Kiosko en Espacio deportivo», «Manicurista» o «Música
Sinfonica, orquestas profesionales». Un oficio poco frecuente junto a cualquier geografía identifica
a una persona.

El motivo del desvío es que el ratio se calculaba sobre todos los valores no vacíos, y el rótulo de
relleno con que la fuente sustituyó el texto original infla la frecuencia del valor más común y
arrastra el ratio hacia abajo. La regla de esta edición descuenta primero los comodines de la opción
abierta —otro, otros, otra, ninguno, nada, no, nunca y sus variantes— y mide el ratio sobre lo que
queda, con el umbral en 0,60. Con ese criterio el campo de ocupación se detecta por sí solo, sin
nombrarlo.

La regla detectó siete columnas, con estos perfiles:

| Columna | No vacíos | Distintos | Ratio | Extensión media |
|---|---:|---:|---:|---:|
| `q36_covidvivienda_otro` | 104 | 106 | 98 % | 62 |
| `q40_inscripcion_otros` | 28 | 30 | 100 % | 114 |
| `q41_otro` | 36 | 36 | 100 % | 49 |
| `q44_ocupacion_otra` | 713 | 537 | 74 % | 18 |
| `q52_programas_otro` | 108 | 103 | 87 % | 22 |
| `q54_lugares_otros` | 218 | 211 | 92 % | 31 |
| `q57_participacion_otra` | 88 | 90 | 99 % | 32 |

El criterio es reproducible y no responde a una selección manual. `q5_otro`, con 79 no vacíos, 54
distintos y extensión media de 8 caracteres, no alcanza el umbral de extensión y se conserva: son
nombres de lenguas, un dato que la fuente publica en su propia lista de variables y que no reidentifica
por contenido.

## 3. La variable de región

La base de 2020 no trae una variable de región de residencia, y sin ella no hay análisis territorial
ni comparación posible con 2023. Esta versión incorpora `region_amba_agrup`, con las mismas
categorías que publica la edición 2023.

La asignación se resolvió en dos pasos. Las veintitrés provincias distintas de la Provincia de
Buenos Aires se asignaron por pertenencia regional directa. La Provincia de Buenos Aires, con 902
casos, se desdobló entre AMBA y Región Pampeana según la localidad declarada. Para ese corte no se
construyó una clasificación propia: se recuperó la que la propia fuente aplicó en la edición 2023,
que está disponible en la base de ese año, y se le agregó un suplemento para los nombres de localidad
que aparecen en 2020 y no en 2023. El crosstab de provincia contra región publicada cierra sin casos
perdidos.

| Región | Casos | % |
|---|---:|---:|
| AMBA | 2.081 | 66,8 |
| Región Pampeana | 545 | 17,5 |
| Patagonia | 169 | 5,4 |
| NOA | 143 | 4,6 |
| NEA | 62 | 2,0 |
| Cuyo | 57 | 1,8 |
| Sin clasificar | 57 | 1,8 |

La categoría sin clasificar reúne los casos de la Provincia de Buenos Aires sin localidad declarada
o con nombres ilegibles, ambiguos o con errores de carga, que no admiten asignación sin forzar el
dato. Se declara como residual en lugar de distribuir esos casos por criterio.

Del total de nombres de localidad que la clasificación maneja para la Provincia de Buenos Aires, 52
no figuran en la lista que la fuente aplicó en 2023 y su asignación es criterio de este trabajo. La
mayoría son barrios y localidades del conurbano cuya pertenencia al AMBA no ofrece duda, como Haedo,
Bernal, Munro, Villa Lynch, Tortuguitas, Remedios de Escalada o Dock Sud. Tres casos conviene
señalarlos aparte, porque son decisiones que otra persona podría resolver de otro modo: Zárate, que
no figura en la lista de 2023 y se asignó al AMBA siguiendo el tratamiento que la fuente dio a
Campana y a Escobar, contiguos y clasificados como AMBA en ese año; y Pontevedra y Villa Elisa, del
partido de La Plata, que se asignaron al AMBA por pertenecer a un partido que la lista de 2023 ubica
allí.

## 4. El tratamiento aplicado

La versión publicada es `data/ENMA2020_anonima_v1.csv`, de 3.114 filas por 202 columnas. Elimina
doce columnas en dos etapas.

La eliminación explícita comprende el identificador correlativo del registro, la fecha exacta de la
encuesta, la provincia y la localidad de residencia y el historial de residencia previa en otra
provincia. La segunda etapa comprende las siete columnas de respuesta libre detectadas por la regla.

El script de preparación quedó como utilitario local en `scripts/` y no integra el repositorio, que
publica la base y la documentación y no las herramientas que las produjeron. El script no edita el
original y su ejecución documenta el tratamiento: imprime las columnas eliminadas con su motivo, la
distribución de la variable de región y la medición del riesgo antes y después.

También normaliza los dos ponderadores de coma a punto decimal, para que cualquier lector de datos
los reconozca como numéricos sin intervención.

## 5. La medición del riesgo

El riesgo se midió con el criterio de celdas con una sola persona, el mismo que se usó en 2023.

| Momento | Claves | Combinaciones | Con una sola persona |
|---|---|---:|---:|
| Antes | provincia + localidad + género + país + edad | 3.020 | 2.936 (97,2 %) |
| Después | región + género agrupado + edad agrupada + nivel educativo | 187 | 42 (22,5 %) |

El descenso de 97,2 % a 22,5 % deja la edición 2020 en un nivel comparable al de 2023, que quedó en
22,7 % sobre sus variables agrupadas. El riesgo no llega a cero, situación propia de una encuesta
con esta cantidad de variables. La medición se hizo sobre las claves agregadas que reemplazan a las
eliminadas, y no sobre el total de las 202 columnas, que arrojaría un valor sin sentido.

## 6. Exposición residual detectada en la edición 2023, y su corrección

Al comparar la regla nueva con la que se aplicó a la edición 2023 apareció una diferencia que
correspondía informar, y que se resolvió antes de cerrar este trabajo.

La base de 2023 que estaba publicada conservaba la columna `q5_descendencia_otro_descrip`, con 242
valores no vacíos, 155 distintos, un ratio de 0,64 y una extensión media de 14,2 caracteres. Con el
umbral de 0,75 que se usó entonces no se detectó; con el criterio que se aplicó ahora, que descuenta
el relleno y baja el umbral a 0,60, la columna se marca para eliminación. Sus valores son
descripciones de ascendencia redactadas por las personas encuestadas, del tipo «Comunidad de los
valles», «Grupo de Chapacos», «Mayor de la tercera edad de origen paraguayo» o «Inmigrante paraguaya
de la tercera edad». De los 155 valores distintos, 134 aparecen una sola vez y 141 no superan los
dos casos.

El efecto de esa columna sobre el riesgo medido es considerable. Las variables agrupadas de 2023 dan
22,7 %; incorporando `q5_descendencia_otro_descrip` el valor asciende a 72,2 %, y la columna por sí
sola alcanza 86,1 %.

La columna no estaba documentada en `BASE_enma2023.md` ni mencionada en el informe de tratamiento de
esa edición, que declaraba retirados los campos de redacción libre. La decisión se tomó el
2026-09-17: se corrigió la edición 2023 con el mismo criterio que la de 2020 y se republicó, para
que las dos bases publicadas en el repositorio reciban un tratamiento equivalente. El detalle consta
en la sección 8 de `documentacion/INFORME_tratamiento_base.md`.

Antes de corregir la edición 2023 se auditó el archivo completo con la regla nueva, para no sustituir
una columna omitida por otra. La auditoría no encontró ninguna otra: sobre las 247 columnas del
original, la regla corregida agrega exactamente una a las trece que la regla anterior ya detectaba.
La comparación de la versión nueva con la publicada da cero diferencias de celda sobre las 227
columnas comunes, de modo que la única modificación es la eliminación de esa columna.

## 7. Estado de la publicación

El repositorio pasó de `natdebandi/ENMA_2023` a `natdebandi/ENMA`, para que el nombre cubra las dos
ediciones que aloja. La redirección de GitHub verifica en 301 hacia la dirección nueva y el release
de 2023 sigue descargándose por la dirección anterior con el mismo resumen criptográfico.

El tratamiento de 2020 se aplicó sobre la edición 2023 en un solo sentido: la base nueva hereda las
categorías de región y el criterio de medición de riesgo, para que las dos ediciones publicadas en el
mismo repositorio sean legibles con las mismas convenciones. Con la corrección de la sección 6 el
movimiento pasó a ser en los dos sentidos, porque la regla corregida se aplicó también a la edición
2023. La regla vive en un único archivo, `scripts/regla_anonimizacion.py`, de modo que las dos
ediciones no puedan divergir.

## 8. Puntos abiertos

1. El depósito en Zenodo con identificador persistente, pendiente de que el servicio vuelva a estar
   en línea y del token y el ORCID de Natalia.
2. La recodificación de la ocupación en grupos, si el análisis ocupacional desagregado resulta
   central. En 2020 la pérdida es menor que en 2023, porque `q44_ocupacion` conserva catorce
   categorías cerradas y solo se retira el campo abierto.
3. El aviso al equipo estadístico de la ENMA sobre la diferencia entre los seis tramos de edad que
   declara el documento metodológico de 2020 y los tres que trae la variable agrupada de la base.
