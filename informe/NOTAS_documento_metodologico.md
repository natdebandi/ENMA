# Lo que el documento metodológico corrige y agrega

Notas de lectura del `Documento metodológico ENMA 2023.pdf` (julio 2024), ubicado en
`~/investigacion/proyectos/ENMA ENCUESTA/2023/`, contrastadas contra la base
`ENMA2023_anonima_v2.csv`. Cada punto está verificado contra el archivo de datos o citado del
documento. Corresponde incorporarlos a `deposito/README_dataset.md`.

## 1. Los ponderadores no son intercambiables

Es la corrección más importante, porque la documentación previa sugería usar cualquiera de los dos
en toda tabulación y eso produce estimaciones mal calibradas.

`weightvec` es el ponderador principal, de pesos para estimaciones totales. Equilibra el peso
proporcional según nacionalidad, género, edad, región de residencia y nivel educativo. El documento
indica que corresponde usarlo siempre que se analicen los datos a nivel del total de la base.

`weightvec_0` es el ponderador de pesos para estimaciones por nacionalidad. Calibra por género, edad
agrupada y región de residencia dentro de cada nacionalidad, y solo para las diez más numerosas del
país, que son Paraguay, Bolivia, Perú, Venezuela, Chile, Uruguay, Italia, España, Colombia y Brasil.
El documento indica que corresponde usarlo únicamente para analizar el comportamiento de una variable
al interior de alguna de esas diez nacionalidades, y que para cualquier otra nacionalidad conviene no
aplicar ponderador y trabajar en valores absolutos.

Verificado sobre la base: ambos vectores presentan 454 valores distintos y suman 4.679, de modo que
las sumas ponderadas se expresan en casos y no en población proyectada.

## 2. La variable `migracion_reciente` no coincide con su definición

El documento define la migración reciente como aquella con menos de tres años en el país. En la base,
sin embargo, la variable coincide exactamente con el tramo de hasta cinco años de
`tiempo_residencia_agrup`.

| Umbral sobre `q13_anio_llegada` | Casos |
|---|---:|
| Llegadas desde 2021, menos de 3 años | 475 |
| Llegadas desde 2020 | 564 |
| Llegadas desde 2019 | 886 |
| Llegadas desde 2018, hasta 5 años | 1.312 |
| `migracion_reciente == "Si"` | 1.312 |

El cruce con `tiempo_residencia_agrup` es perfecto, sin casos discordantes. Quien necesite el umbral
de tres años debe construirlo desde `q13_anio_llegada`. Conviene además avisar al equipo estadístico
de la ENMA, porque la discrepancia afecta a cualquier publicación que haya usado la variable
entendiéndola según su definición documentada.

## 3. La numeración tiene saltos por dos motivos distintos

La documentación previa atribuía todos los saltos a la anonimización, y no es así.

La fuente ya excluyó de la base pública las preguntas 52 y 53, sobre registro laboral, porque
presentaron un problema en la configuración de los filtros del cuestionario y arrojaron datos
erróneos. También retiró la pregunta final, de respuesta abierta, por protección de la privacidad, y
señala que ese campo se habilita mediante pedidos específicos y fundados.

Esta versión retiró además la geografía a nivel de provincia, localidad y barrio, la ocupación en
texto libre y las respuestas de redacción libre.

El cuestionario final tuvo 73 preguntas, no 72, organizadas en once bloques temáticos.

## 4. El diseño es por cuotas y la representatividad tiene límites precisos

El diseño muestral emplea un enfoque de cuotas, con calibración por nacionalidad, género, edad,
región de residencia y nivel educativo. El nivel educativo se incorporó al calibrador final, no al
diseño inicial, y se tomó del censo 2010.

La muestra es representativa a nivel de las regiones de residencia y no de cada provincia. El
documento exceptúa a CABA y a la Provincia de Buenos Aires, que reúnen casos suficientes, aunque esta
versión de la base no conserva la variable provincial y el nivel territorial disponible es el de las
seis regiones de `region_amba_agrup`.

La calibración por edad se hizo sobre los grupos de 18 a 29, 30 a 44, 45 a 64 y 65 y más años, de
modo que la muestra no es representativa en edades simples. La variable `edad_agrup` de la base
responde a otra agrupación, de 18 a 34, 35 a 54 y 55 y más, que se mantuvo por comparabilidad con la
edición 2020 y no coincide con los grupos de calibración. Conviene decirlo, porque invita a leer
`edad_agrup` como si fuera el eje de calibración.

La calibración por género utilizó el género binario. El documento sugiere trabajar los cruces con las
categorías varón y mujer y tratar la categoría de otros géneros en valores absolutos, que reúne 60
casos en la base.

El diseño buscó un sobremuestreo de Haití, Senegal, China, República Dominicana y Cuba. Solo Haití
alcanzó el mínimo previsto de 80 casos.

## 5. Discrepancia menor en el conteo de Paraguay

El documento consigna 960 casos de Paraguay y la base tiene 956. El total coincide en 4.679 y el
resto de las nacionalidades principales también. No está claro el origen de la diferencia y conviene
preguntarlo antes de publicar un cuadro que contradiga al documento de la fuente.

## 6. Las ediciones 2020 y 2023 no son integrables de manera automática

Los cuestionarios difieren en secciones, preguntas y opciones. El documento señala que el equipo
estadístico de la ENMA está trabajando en la integración. Corresponde advertirlo, porque la
comparación entre ediciones es el uso más previsible de la base.

## 7. La fuente pide no redistribuir los datos

Es el punto que excede a la documentación y toca la decisión de publicar.

El documento afirma que los datos de la ENMA son abiertos, pero que para acceder se solicita siempre
completar el registro de solicitud, de modo de poder hacer un seguimiento del uso que se les da.
Agrega de manera explícita que se solicita no transferir los datos a otras personas de manera directa
sino indicarle a la persona que realice su propia solicitud.

Publicar la base como descarga abierta, incluso anonimizada y con otro nombre de archivo, hace
exactamente lo que la fuente pide no hacer, y desactiva el seguimiento de uso que la ENMA declara
como razón del registro. La anonimización responde al riesgo de reidentificación, que era el problema
técnico, pero no al pedido de la fuente, que es un problema de acuerdo colectivo.

La medición de riesgo y esta versión anonimizada son un buen insumo para plantearlo al equipo de la
ENMA. La decisión sobre la publicación conviene que salga de esa conversación y no de este
repositorio.

## 8. La publicación del código sí está prevista por la fuente

El documento anuncia, bajo el título de sintaxis abierta, que la sintaxis en R del análisis realizado
para el Anuario Migratorio Argentino 2023 sería publicada en formato abierto para su reutilización.
Los ocho capítulos de este repositorio son justamente eso, de modo que su publicación acompaña lo que
la fuente anunció.

## Material disponible en el home

`~/investigacion/proyectos/ENMA ENCUESTA/2023/` reúne el documento metodológico, el cuestionario en
pdf y docx, el Anuario Migratorio Argentino 2023 y el de 2020, el documento metodológico de la
edición 2020, el resumen ejecutivo, el documento de buenas prácticas y el informe de la Provincia de
Buenos Aires 2024. La carpeta `ENMA2026` contiene el cuestionario y los instrumentos de la edición en
curso.
