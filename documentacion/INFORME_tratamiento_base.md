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
preparación, con `data/ENMA2023_anonima_v2.csv` como resultado de 4.679 filas por 228 columnas. El
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

La versión definitiva elimina diecinueve columnas en dos etapas. La primera comprende los
identificadores directos `ID` y `fecha`, las cuatro variables de geografía fina y la ocupación en
texto libre. La segunda comprende las doce columnas de respuesta libre detectadas con una regla
explícita, que alcanza a las columnas con al menos diez valores no vacíos, más del 75 % de valores
distintos y extensión media superior a doce caracteres. El criterio es auditable y no responde a una
selección manual.

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

El código de procesamiento se subió a `natdebandi/ENMA_2023`, que contiene los ocho capítulos con su
versión html, este informe y la documentación del depósito. La verificación contra la interfaz de
GitHub confirma que no hay archivos de datos en el árbol versionado. El `.gitignore`
excluye `data/`, las extensiones `csv`, `xls`, `xlsx`, `sav` y `dta`, y los archivos `zip`, dado que
el paquete de publicación lleva la base en su interior.

La base anonimizada se publicó como adjunto de la versión `datos-v1` del repositorio, en
https://github.com/natdebandi/ENMA_2023/releases/tag/datos-v1, con el archivo comprimido, el archivo
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
por Natalia Debandi, en su carácter de integrante del equipo de la ENMA, sobre tres consideraciones.
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

## 8. Puntos abiertos

1. La recodificación de la ocupación en grupos, en caso de que el análisis ocupacional desagregado
   resulte central para los capítulos.
2. El destino del repositorio `research_migration`, cuya división por tema se presenta como la vía
   razonable.
3. El depósito en Zenodo con identificador persistente, pendiente de que el servicio vuelva a estar
   en línea. Los metadatos de autoría ya constan en la guía correspondiente.
4. El aviso al equipo estadístico de la ENMA sobre la desalineación de `migracion_reciente` y sobre
   la diferencia de cuatro casos en el conteo de Paraguay entre el documento metodológico y la base.
5. El respaldo remoto del trabajo sin publicar que permanece en `enma2023_git`.
