# ENMA 2023: consolidación, anonimización y publicación

Informe de trabajo. 2026-09-13.

## 1. El punto de partida

Los microdatos de la ENMA 2023 no se distribuyen como descarga abierta. El sitio de la encuesta
solicita completar un formulario de solicitud y enmarca el uso en la Ley de Protección de Datos
Personales (N.º 25.326) y en los lineamientos del Comité de Ética de CONICET. El archivo que
circulaba en el disco con el nombre `ENMA2023_final_public.csv` no constituye por eso una liberación
abierta de la fuente, de modo que su redistribución sin tratamiento previo resultaba problemática.

El riesgo se midió sobre ese archivo antes de intervenirlo:

| Claves consideradas | Combinaciones | Con una sola persona |
|---|---:|---:|
| provincia + localidad + barrio + género + país + edad | 4.438 | 4.230 (95,3 %) |
| provincia + localidad + género + país | 1.822 | 1.379 (75,7 %) |
| provincia + género + país | 377 | 138 (36,6 %) |
| género + país + edad, sin geografía | 1.224 | 509 (41,6 %) |

Con el barrio incluido, la casi totalidad de los registros queda aislada. El barrio no aporta al
análisis nada que la región no aporte y es lo que produce la reidentificación.

A eso se sumaba un segundo mecanismo, distinto del anterior. Tres columnas reidentifican por su
contenido y no por la combinación de variables. `q54_ocupacion` reúne 1.964 valores distintos en
texto libre, `q14_motivos_otros_detalle` 436 y `q51_situacion_ocupacional_esp` 157. Un oficio poco
frecuente junto a una localidad alcanza para identificar a una persona.

## 2. Estado de las carpetas de trabajo

En `Workspace_R` existían dos carpetas de la ENMA que no eran versiones de lo mismo.

La carpeta `ENMA_publico` resultó la vigente. Contiene el archivo `ENMA2023_final_public.csv` con
fecha 2025-01-30, el más reciente del home, y los capítulos `Cap1_v2` a `Cap8_v2` del Anuario
Migratorio 2024, trabajados hasta junio de 2025.

La carpeta `enma2023_git` corresponde a una etapa anterior, con trabajo de abril y junio de 2024.
Contiene material que no está en la otra, en particular la subcarpeta `preparatorios` con los guiones
de procesamiento de pedidos por capítulo. Su repositorio remoto apuntaba a
`github.com/natdebandi/enma2023`, que ya no existe, de modo que ese trabajo se encontraba sin
respaldo remoto.

El repositorio existente, `natdebandi/ENMA_2023`, estaba público y vacío, con un único `README.md`.

Las dos copias del archivo original presentes en el disco, la de `ENMA_publico` y la de
`research_migration`, difieren en 30 filas y la diferencia son finales de línea. La primera usa CRLF
y la segunda LF. El trabajo se hizo sobre la primera.

## 3. La versión anonimizada

La versión tratada se generó en `~/investigacion/Workspace_R/ENMA_publico/` mediante un script de
preparación, con `data/ENMA2023_anonima_v3.csv` como resultado de 4.679 filas por 227 columnas. El
script quedó como utilitario local y no integra el repositorio, que publica la base y el
procesamiento del Anuario y no las herramientas que los produjeron.

El criterio se corrigió durante el trabajo. La primera versión eliminaba siete columnas y conservaba
237. Al auditar el resultado aparecieron doce campos que no reidentifican por combinación de
variables sino por contenido, con respuestas redactadas palabra por palabra, del tipo «Vivo en un
hotel tomado», «No tengo ningún trámite hecho» o «Me la facilitan unos parientes». No admiten
recodificación sin perder su contenido y su publicación contradice el carácter anónimo con que se
levantó la encuesta. El Documento metodológico lo consigna de manera explícita, al señalar que la
convocatoria hacía énfasis en que la encuesta era anónima y que no se preguntaba nada que permitiera
la identificación personal de quien respondía.

La versión definitiva elimina **diecinueve** columnas en dos etapas. La primera comprende los
identificadores directos `ID` y `fecha`, las tres variables de geografía de residencia
(`q8_provincia_res`, `q9_localidad` y `q10_barrio`) y la ocupación en texto libre. La segunda
comprende las trece columnas de respuesta libre detectadas con una regla
explícita, que alcanza a las columnas con al menos diez valores no vacíos, más del 60 % de valores
distintos y extensión media superior a doce caracteres. El porcentaje de valores distintos se mide
sobre los valores que quedan después de descontar el rótulo de relleno de la opción abierta, según
se explica en la sección 8. El criterio es auditable y no responde a una selección manual.

La versión conserva las variables agregadas que la base ya traía, de modo que los cruces habituales
siguen siendo posibles. Se mantienen `region_amba_agrup` con seis regiones, `genero_agrup`,
`edad_agrup` en tramos, `nacionalidad_agrup` y `nacionalidad_var`, junto con los ponderadores
`weightvec` y `weightvec_0`.

El riesgo desciende de 95,3 % a 22,7 % sobre las claves agregadas. No llega a cero, situación propia
de una encuesta con esta cantidad de variables, aunque ya no queda un barrio ni un oficio
identificando a una persona. La versión anterior fue descartada y conservada en
`~/laboratorio/papelera-2026-09-13/`.

## 4. Exposición detectada y resuelta

El repositorio `natdebandi/research_migration` era público y contenía el archivo original con
provincia, localidad y barrio, que es la combinación que produce el 95,3 % de reidentificación. Ese
repositorio pasó a privado el 2026-09-13, con respaldo local previo en
`~/laboratorio/github-backup-2026-09-13/research_migration`, de 35 archivos y un commit. La
verificación posterior devuelve visibilidad privada.

Su contenido queda por definir. Reúne el archivo de la ENMA, un notebook de flujos migratorios
regionales y cruces con el Censo, material que se solapa en parte con los proyectos de movilidad
existentes en `Workspace/`. La mezcla de microdatos de la ENMA con análisis de flujos regionales en
un mismo repositorio sugiere una división por tema. No se modificó nada más que la visibilidad.

## 5. Estado de la publicación

El código de procesamiento se subió a `natdebandi/ENMA`, que contiene los ocho capítulos con su
versión html, este informe y la documentación del depósito. La verificación contra la interfaz de
GitHub confirma que no hay archivos de datos en el árbol versionado. El `.gitignore`
excluye `data/`, las extensiones `csv`, `xls`, `xlsx`, `sav` y `dta`, y los archivos `zip`, dado que
el paquete de publicación lleva la base en su interior.

La base anonimizada se publicó como adjunto de la versión `datos-2023-v2` del repositorio, en
https://github.com/natdebandi/ENMA/releases/tag/datos-2023-v2, con el archivo comprimido, el archivo
separado por comas y un listado de verificación de integridad. La descarga se comprobó de forma
anónima, sin credencial, con resultado 200 y coincidencia del resumen criptográfico con la copia
local.

El depósito en Zenodo no se concretó porque el servicio se encontraba fuera de línea en la fecha de
trabajo, con respuesta nula en `zenodo.org`. Se verificaron alternativas activas, entre ellas OSF,
HuggingFace y Dataverse, todas accesibles. La publicación mediante la versión de GitHub resuelve la
accesibilidad inmediata, aunque no provee identificador persistente. El depósito con identificador
queda como tarea pendiente.

## 6. La decisión de abrir la base

La publicación de la base como descarga abierta se resolvió el 2026-09-13. La decisión fue tomada
desde el equipo de la ENMA, sobre tres consideraciones.
La base circuló durante años mediante el formulario de solicitud, de modo que la apertura no
anticipa una difusión que la encuesta no hubiera tenido. La edición 2026 se encuentra próxima a
publicarse, y la apertura de la edición anterior acompaña ese ciclo. Y la ciencia abierta figura
entre los objetivos declarados de la ENMA, que se propone dar acceso libre a la información
producida y favorecer su apropiación social por parte de las personas migrantes y sus
organizaciones.

Corresponde registrar el punto que la decisión resuelve. El documento metodológico de la edición
señala que los datos son abiertos pero que para acceder se solicita completar el registro, de modo
de poder hacer un seguimiento del uso, y pide no transferirlos de manera directa a otras personas
sino indicarles que realicen su propia solicitud. Una descarga abierta desactiva ese seguimiento.
La decisión adoptada distingue por eso dos objetos. La versión anonimizada, sin geografía fina ni
campos de texto, se publica de manera abierta. Los microdatos completos permanecen disponibles
únicamente mediante el formulario de la fuente, y así consta en la documentación de la base y en el
README del repositorio.

## 7. Precisiones incorporadas del documento metodológico

La lectura del documento metodológico de la edición, de julio de 2024, corrigió varios puntos de la
documentación, cada uno verificado contra el archivo de datos. Los de mayor consecuencia son el
criterio de uso de cada ponderador, que no son intercambiables, la desalineación entre la definición
documentada de `migracion_reciente` y su contenido efectivo, y los límites de la representatividad
por provincia y por edades simples. Las advertencias que se desprenden de ellos constan en
`documentacion/BASE_enma2023.md`, y el documento de la fuente se incluye en `documentacion/`.

## 8. Corrección de la regla y segunda versión de la base

Ese mismo trabajo sobre la edición 2020 puso en evidencia un defecto de la regla con que se generó la
versión publicada en septiembre de 2026, según se detalla en
`documentacion/INFORME_tratamiento_ENMA2020.md`.

La regla anterior medía el porcentaje de valores distintos sobre todos los valores no vacíos de cada
columna. Ese cálculo deja fuera los campos abiertos cuyo rótulo de relleno se repite, porque el
rótulo infla la frecuencia del valor más común y arrastra el porcentaje por debajo del umbral. El
documento metodológico de la edición declara que la fuente sustituyó el texto de los campos abiertos
por la opción de relleno, y ese rótulo sobrevive en la base.

El caso concreto es `q5_descendencia_otro_descrip`, la descripción de ascendencia de la pregunta 5.
Reúne 242 valores no vacíos, 155 distintos y una extensión media de 14 caracteres, con un porcentaje
de valores distintos de 0,64 que la regla anterior no alcanzaba a detectar. Sus valores son
descripciones redactadas por las personas encuestadas, del tipo «Comunidad de los valles», «Grupo de
Chapacos» o «Inmigrante paraguaya de la tercera edad». De los 155 valores distintos, 134 aparecen una
sola vez.

La regla corregida descuenta el rótulo de relleno antes de medir el porcentaje, que es lo que separa
el contenido que sobrevivió del rótulo, y baja el umbral a 0,60 porque ya no necesita compensar ese
arrastre. Con ese criterio la columna se detecta por su propia forma, sin nombrarla. La definición
vive en un único archivo compartido por las dos ediciones, de modo que las reglas no puedan divergir
otra vez.

La corrección se auditó sobre la totalidad del archivo y agrega una sola columna a las trece que la
regla ya detectaba. La versión corregida es `data/ENMA2023_anonima_v3.csv`, de 4.679 filas por 227
columnas, idéntica a la publicada en las 227 columnas comunes celda por celda y con el mismo orden de
variables. El riesgo sobre las claves agregadas se mantiene en 22,7 %. Se publicó como versión
`datos-2023-v2`, que reemplaza a `datos-v1`.

Para que el reemplazo no pierda el rastro de lo que estuvo publicado, se deja constancia de los
resúmenes criptográficos de la versión sustituida: el archivo separado por comas era
`a17216b1e33f93d63183db580187db4025ded9e76bf176be1fedb6daf6f53e48` y el comprimido,
`91a826c9b60aeb677d36c442b94352773574dbf858f04fc54144a37e56adf71d`. Al momento del reemplazo la
versión anterior había registrado tres descargas del archivo separado por comas y dos del comprimido,
de modo que pudo haber circulado fuera del repositorio.

La versión `datos-v1` se retiró el mismo día, con su etiqueta. La copia de lo que estuvo publicado se
conserva en `~/laboratorio/papelera-2026-09-17/`, con una nota que advierte que la base no debe
publicarse ni distribuirse, porque es la que conserva la columna retirada. La etiqueta apuntaba a un
commit que permanece en el historial de la rama principal y su árbol no contenía ningún archivo de
datos, de modo que su eliminación no retiró nada más que el acceso al adjunto.

## 9. Tercera versión de la base: reposición de `q11_otra_provincia`

La versión `v3` publicada en `datos-2023-v2` retiraba una columna que no debía retirar. La capa de
eliminación explícita la incluía con esta descripción:

```python
"q11_otra_provincia": "provincia de residencia previa",
```

La descripción no corresponde al contenido. La columna es **binaria**: dos valores, `Si` y `No`, sobre
4.598 casos no vacíos, y ninguno de ellos nombra una provincia. La pregunta de origen, la número 11
del cuestionario, dentro de la sección «Trayectorias y proyecto migratorio», es: «Antes de instalarse
en su lugar de residencia actual, ¿vivió más de tres meses en otra u otras provincias de Argentina?».
No hay texto libre ni geografía fina, y no aporta riesgo de reidentificación.

A diferencia de `q8_provincia_res`, `q9_localidad` y `q10_barrio`, que son la residencia actual y sí
identifican, `q11` registra un hecho binario sobre el pasado. Quedó retirada por el rótulo con que se
la describió en la lista, no por su contenido.

### El costo de haberla retirado

La sección 1.11 del capítulo 1 del Anuario Migratorio 2024 usa esa columna. Al quedar fuera de la
base publicada, la sección dejó de poder reproducirse desde el archivo que el release entrega: el
capítulo solo corre contra los microdatos sin tratar.

### La versión `v4`

Un utilitario local, que no integra el repositorio por la misma razón que los anteriores, genera
`data/ENMA2023_anonima_v4.csv`. Reproduce las dos capas de
la regla sin cambios, con `q11_otra_provincia` fuera de la lista de eliminación explícita y con un
control que aborta si la capa de texto libre la detectara.

| | v3 (publicada) | v4 |
|---|---:|---:|
| Columnas | 227 | 228 |
| Filas | 4.679 | 4.679 |
| Preguntas del cuestionario | 215 | 216 |
| Riesgo sobre claves agregadas | 22,7 % | 22,7 % |
| Riesgo sumando `q11` | — | 25,6 % |

Las 227 columnas comunes son **idénticas celda por celda**, verificado columna por columna. La única
diferencia es la columna repuesta.

El riesgo sobre las claves agregadas no cambia. Sumarle `q11` lo lleva de 22,7 % a 25,6 %, un
movimiento dentro del mismo orden y muy lejos del 95,3 % de partida: la columna no reidentifica.

### Los capítulos

Los ocho capítulos leían `data/ENMA2023_final_public.csv`, que es el nombre de los microdatos **sin
anonimizar** y no el de la base publicada. Se actualizaron los ocho a `data/ENMA2023_anonima_v4.csv` y
se volvieron a generar los HTML. La verificación comparó, para cada capítulo, todas las celdas
numéricas de sus tablas contra la versión anterior: **idénticas en los ocho**, 284, 179, 80, 114, 200,
189, 120 y 96 celdas respectivamente. Ningún número del anuario cambia.

Efecto lateral buscado: los HTML se generan con `echo=T`, de modo que el código fuente queda visible
en el cuerpo. Hasta esta versión enseñaban el nombre del archivo sin anonimizar. Ahora nombran el que
el release publica.

## 10. Puntos abiertos

1. La recodificación de la ocupación en grupos, en caso de que el análisis ocupacional desagregado
   resulte central para los capítulos.
2. ~~El destino del repositorio `research_migration`~~. Resuelto el 2026-09-18: el repositorio se
   eliminó, junto con otros seis del mismo período. El contenido que solo vivía ahí, los catorce Rmd
   de cruces ENMA/CENSO y el notebook de flujos, se conserva en el clon local y en un espejo
   verificado en `~/laboratorio/github-backup-2026-09-18/`.
3. El depósito en Zenodo con identificador persistente, pendiente de que el servicio vuelva a estar
   en línea. Los metadatos del depósito se acreditan a la ENMA como equipo y constan en la guía
   correspondiente. Debe depositarse la `v4`, no la `v3`, para no publicar con DOI una base que no
   reproduce la sección 1.11 del anuario.
4. El aviso al equipo estadístico de la ENMA sobre la desalineación de `migracion_reciente` y sobre
   la diferencia de cuatro casos en el conteo de Paraguay entre el documento metodológico y la base.
5. El respaldo remoto del trabajo sin publicar que permanece en `enma2023_git`.
