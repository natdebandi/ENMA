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

La versión tratada se generó en `~/investigacion/Workspace_R/ENMA_publico/`, con
`scripts/anonimizar_enma.py` como script productor y `data/ENMA2023_anonima_v2.csv` como resultado de
4.679 filas por 228 columnas.

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
texto libre. La segunda comprende las doce columnas de respuesta libre detectadas con un criterio
definido en el script, que alcanza a las columnas con al menos diez valores no vacíos, más del 75 %
de valores distintos y extensión media superior a doce caracteres. El criterio es auditable y no
responde a una selección manual.

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
versión html, los dos scripts, este informe y la documentación del depósito. La verificación contra
la interfaz de GitHub confirma que no hay archivos de datos en el árbol versionado. El `.gitignore`
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
accesibilidad inmediata, aunque no provee identificador persistente. La guía para concretar el
depósito, con los metadatos y el procedimiento, consta en `deposito/COMO_SUBIR_A_ZENODO.md`.

## 6. Consideraciones sobre el destino en la web de la ENMA

La propuesta de ofrecer la base desde la página de la encuesta sin el formulario de solicitud
presenta una particularidad. La página ya declara que los datos se publican con fines de
investigación y encuadra su uso en la Ley 25.326 y en los lineamientos del Comité de Ética de
CONICET. Ofrecer la base sin solicitud no resulta incompatible con ese marco, pero modifica la
relación con la fuente, dado que la ENMA es una iniciativa colectiva y no un archivo propio. La
versión anonimizada y la medición de riesgo constituyen un insumo para esa conversación con el
equipo de la encuesta.

## 7. Puntos abiertos

1. La recodificación de la ocupación en grupos, en caso de que el análisis ocupacional desagregado
   resulte central para los capítulos.
2. El destino del repositorio `research_migration`, cuya división por tema se presenta como la vía
   razonable.
3. La consulta al equipo de la ENMA sobre la publicación de la base en su sitio.
4. El depósito en Zenodo con identificador persistente, para el cual resta el registro de autoría y
   el ORCID correspondiente.
5. El respaldo remoto del trabajo sin publicar que permanece en `enma2023_git`.
