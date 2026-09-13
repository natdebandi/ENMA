# ENMA 2023: consolidación, anonimización y publicación

Informe de trabajo. Fecha: 2026-09-13. Elaborado a partir de la revisión del home de Guanábana y
del estado de los repositorios en GitHub.

## 1. El problema de fondo

La ENMA 2023 no se distribuye como descarga abierta. El sitio de la encuesta pide completar un
formulario de solicitud y enmarca el uso en la Ley de Protección de Datos Personales (N.º 25.326) y
en los lineamientos de ética del Comité de CONICET. Eso significa que el archivo llamado
`ENMA2023_final_public.csv` no es una liberación abierta de la fuente y que redistribuirlo sin
tratamiento no corresponde.

El riesgo no es teórico. Medido sobre el archivo tal como está hoy:

| Claves usadas | Combinaciones | Con una sola persona |
|---|---:|---:|
| provincia + localidad + barrio + género + país + edad | 4.438 | 4.230 (95,3 %) |
| provincia + localidad + género + país | 1.822 | 1.379 (75,7 %) |
| provincia + género + país | 377 | 138 (36,6 %) |
| género + país + edad, sin geografía | 1.224 | 509 (41,6 %) |

Con barrio incluido, prácticamente cada registro queda solo. El barrio no aporta nada analítico que
la región no aporte, y es lo que produce la reidentificación.

Hay además tres columnas que reidentifican por contenido, no por combinación. `q54_ocupacion` con
1.964 valores distintos en texto libre, `q14_motivos_otros_detalle` con 436 y
`q51_situacion_ocupacional_esp` con 157. Un oficio poco común más una localidad alcanza para
identificar a una persona.

## 2. Estado de las dos carpetas

Existen dos carpetas de ENMA en `Workspace_R`, y no son versiones de lo mismo.

La carpeta `ENMA_publico` es la vigente para los datos. Contiene el archivo
`ENMA2023_final_public.csv` con fecha 2025-01-30, el más reciente de todos los que hay en el home, y
los capítulos `Cap1_v2` a `Cap8_v2` del Anuario Migratorio 2024, trabajados hasta junio de 2025. El
sufijo `_public` coincide con el nombre del archivo.

La carpeta `enma2023_git` es de una etapa anterior. Su último trabajo real es de abril y junio de
2024 y contiene material que no está en la otra, en particular la subcarpeta `preparatorios` con los
guiones de procesamiento de pedidos por capítulo. Vale conservarla, pero no es la que se publica.

Su repositorio remoto apunta a `github.com/natdebandi/enma2023`, que ya no existe. La verificación
devuelve `Repository not found`. Es decir que esa carpeta tiene trabajo sin respaldo remoto.

El repositorio que sí existe es `natdebandi/ENMA_2023`, público, con la descripción de la encuesta y
un solo archivo adentro, el `README.md`. Está vacío y esperando contenido. Es el destino natural.

Las dos copias del archivo público que hay en el disco, la de `ENMA_publico` y la de
`research_migration`, no son idénticas. Difieren en 30 filas y la diferencia son finales de línea. La
de `ENMA_publico` usa CRLF y la de `research_migration` usa LF. Conviene partir de la primera.

## 3. Versión anonimizada generada

Se generó una versión tratada, reproducible, en `~/investigacion/Workspace_R/ENMA_publico/`:

- `scripts/anonimizar_enma.py` produce el archivo desde el original y nunca lo modifica.
- `data/ENMA2023_anonima_v2.csv` es el resultado, 4.679 filas por 228 columnas.

Hay un punto que apareció al auditar el archivo antes de publicarlo y que cambió el criterio. La
primera versión eliminaba siete columnas y dejaba 237. Al revisar el resultado quedó a la vista que
sobrevivían doce campos que no reidentifican por combinación de variables sino por contenido. Son
respuestas dictadas palabra por palabra, del tipo «Vivo en un hotel tomado», «No tengo ningún
trámite hecho» o «Me la facilitan unos parientes». No hay forma de recodificarlas sin destruirlas, y
su publicación contradice la promesa con que se levantó la encuesta. El Documento metodológico lo
dice textual: la convocatoria hacía énfasis en que era ANÓNIMA, «no te preguntan nada que permita tu
identificación personal».

Por eso la v2 elimina diecinueve columnas. Las siete de la eliminación explícita, que son `ID`,
`fecha`, las cuatro geográficas finas y `q54_ocupacion`, y doce más que se detectan por regla: se
marcan las columnas donde al menos diez valores no están vacíos, más del 75 % de los no vacíos son
distintos y el largo medio supera los doce caracteres. La regla está en el script y es auditable; no
se eligieron a mano.

La versión conserva las columnas agregadas que la propia base ya traía, de modo que los cruces
habituales siguen siendo posibles. Quedan `region_amba_agrup` con seis regiones, `genero_agrup`,
`edad_agrup` en tramos, `nacionalidad_agrup` y `nacionalidad_var`, más los ponderadores `weightvec` y
`weightvec_0`.

El riesgo baja de 95,3 % a 22,7 % sobre las claves agregadas. No llega a cero y conviene decirlo, es
propio de una encuesta con esta cantidad de variables; la diferencia es que ya no hay un barrio ni
un oficio con nombre y apellido apuntando a una persona.

Un costo que hay que decidir. Al quitar `q54_ocupacion` se pierde el análisis ocupacional
desagregado. La base conserva `q51_situacion_ocupacional` con once categorías, que es un sustituto
razonable pero más grueso. Si el análisis ocupacional es central, la alternativa es recodificar la
ocupación a grupos en lugar de eliminarla, y eso hay que hacerlo con criterio.

## 4. Dónde publicar

La pregunta de dónde van los datos abiertos tiene tres respuestas buenas y conviene separar el
código de los datos.

El código de procesamiento va al repositorio `natdebandi/ENMA_2023`, que ya existe y está vacío. El
`.gitignore` debe bloquear `data/` desde el primer commit, y con él `.RData`, `.Rhistory` y
`.Rproj.user`.

Los datos anonimizados no deberían vivir en Git. La opción que recomiendo es Zenodo, que es gratuito,
del CERN, permite versiones sucesivas y entrega un DOI citable. Para datos de encuesta en ciencias
sociales es la práctica estándar y resuelve la citación, que es lo que un repositorio de Git no hace
bien. OSF es la alternativa natural, igualmente gratuita y muy usada en el campo, con la ventaja de
manejar el flujo de solicitudes de acceso restringido si más adelante se quiere una versión con
condiciones. HuggingFace Datasets sirve y es cómodo para trabajar, pero no da DOI.

Lo que NO conviene es subir el archivo a un repositorio de GitHub público. Git guarda todo el
historial, de modo que un archivo publicado ahí no se despublica borrándolo; queda en los commits.

## 5. Exposición: resuelta

El repositorio `natdebandi/research_migration` estaba público y tenía adentro
`data/ENMA2023_final_public.csv` con provincia, localidad y barrio. Esa era la exposición real, y es
la que produce el 95,3 %.

Se pasó a privado el 2026-09-13. Antes se hizo un respaldo local completo en
`~/laboratorio/github-backup-2026-09-13/research_migration` (35 archivos, 1 commit). La verificación
posterior devuelve `visibility: PRIVATE`.

Queda por decidir el destino de ese repositorio. Tiene 35 archivos y un solo commit, «Creado con
Colab», del 2025-09-04. Además del CSV de la ENMA hay un notebook de flujos migratorios y cruces con
el Censo. Buena parte de ese material se solapa con los proyectos de movilidad que ya existen en
`Workspace/`, así que la opción razonable es dividirlo por tema en lugar de mantenerlo como está,
que mezcla microdatos de la ENMA con análisis de flujos regionales. No se tocó nada más que la
visibilidad.

## 6. Publicación: decisiones de Natalia y estado

Definido el 2026-09-13: el código va al repositorio `natdebandi/ENMA_2023` y la base anonimizada va a
Zenodo. Natalia además quiere ofrecer la base desde la página de la ENMA sin el formulario de
solicitud.

Sobre ese último punto hay algo que conviene mirar antes de hacerlo. La página ya declara que los
datos se publican con fines de investigación y encuadra el uso en la Ley 25.326 y en los
lineamientos del Comité de Ética de CONICET. Ofrecer la base sin solicitud no es incompatible con
eso, pero sí cambia la relación con la fuente: la ENMA es un colectivo, no un archivo propio, y
publicar una versión anonimizada de sus datos sin acuerdo previo es distinto de redistribuir un
archivo en un repositorio personal. Corresponde conversarlo con el equipo de la encuesta antes de
subirlo. La versión que generamos es un buen punto de partida para esa conversación, no el final.

Sobre la ciudadanía de los datos, hay un punto técnico. Zenodo permite reservar un DOI antes de
publicar, lo que resuelve la citación cruzada: el repositorio de código puede referenciar el DOI
antes de que el depósito exista, y el depósito puede citar el repositorio. Conviene crear el depósito
primero, aunque sea en borrador.

## 7. Lo que queda pendiente

1. Recodificar la ocupación en lugar de eliminarla, si el análisis ocupacional es central.
2. Decidir el destino de `research_migration`, idealmente dividiéndolo por tema.
3. Verificar el apartado legal con el equipo de la ENMA antes de publicar la base en su web.
4. Dar respaldo remoto al trabajo que quedó sin pushear en `enma2023_git`.
5. Definir licencia para los datos (CC BY 4.0 es lo habitual en el campo) y para el código.
