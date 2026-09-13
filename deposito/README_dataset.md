# ENMA 2023 — Base anonimizada para publicación

## Qué es este archivo

`ENMA2023_anonima_v2.csv` es una versión anonimizada de los microdatos de la Encuesta Nacional
Migrante de Argentina, edición 2023. Contiene 4.679 registros y 228 variables. Se genera desde el
archivo `ENMA2023_final_public.csv` con el script `scripts/anonimizar_enma.py`, disponible en
https://github.com/natdebandi/ENMA_2023

## Tratamiento aplicado

Se eliminaron diecinueve columnas, en dos capas.

**Eliminación explícita.** Los identificadores directos `ID` y `fecha`, donde la fecha es un
timestamp con milisegundos y tiene un valor distinto por registro. La geografía fina
`q8_provincia_res`, `q9_localidad`, `q10_barrio` y `q11_otra_provincia`. Y la ocupación declarada en
texto libre `q54_ocupacion`, con 1.964 valores distintos.

**Detección por regla de testimonios.** Doce columnas de respuesta libre donde los valores no vacíos
son casi todos distintos y de largo medio superior a doce caracteres. Se detectan automáticamente
con el criterio definido en el script: al menos diez valores no vacíos, más del 75 % distintos. Son
relatos dictados palabra por palabra, no categorías, y no pueden recodificarse sin destruir la
información. La lista completa está en el informe técnico.

## Riesgo residual

Medido sobre las claves cuasi-identificadoras disponibles, la proporción de combinaciones con una
sola persona baja de 95,3 % en el archivo original a 22,7 % en esta versión. El riesgo no es nulo y
es propio de una encuesta con esta cantidad de variables. No quedan identificadores directos,
geografía fina ni texto libre.

## Advertencia de uso

Este archivo no es una liberación oficial de la ENMA. Fue tratado por la responsable del repositorio
a partir de datos obtenidos mediante el formulario de solicitud de la fuente. Quien lo use debe
respetar el marco de la fuente original: los lineamientos del Comité de Ética de CONICET y la Ley de
Protección de Datos Personales (N.º 25.326). Ver el informe técnico para el detalle de las
decisiones y el script para reproducir el tratamiento.

## Cita

Ver el DOI del depósito. La encuesta es una iniciativa del CONICET y organizaciones de migrantes y
de derechos humanos. Sitio de la fuente: https://www.encuestamigrante.ar/
