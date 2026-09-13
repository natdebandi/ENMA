# ENMA 2023 - Base anonimizada

## Contenido

El archivo `ENMA2023_anonima_v2.csv` reúne 4.679 registros y 228 variables de la Encuesta Nacional
Migrante de Argentina, edición 2023, en una versión anonimizada. Se genera desde el archivo original
con el script `scripts/anonimizar_enma.py`, del repositorio
https://github.com/natdebandi/ENMA_2023

## Tratamiento aplicado

Se eliminaron diecinueve columnas, en dos etapas.

La primera comprende los identificadores directos, que son `ID` y `fecha`, donde la fecha es un
registro de tiempo con milisegundos y presenta un valor distinto por caso. Comprende además la
geografía fina, esto es `q8_provincia_res`, `q9_localidad`, `q10_barrio` y `q11_otra_provincia`, y la
ocupación declarada en texto libre, `q54_ocupacion`, con 1.964 valores distintos.

La segunda etapa abarca doce columnas de respuesta libre cuyos valores no vacíos son en casi todos
los casos distintos y de extensión media superior a doce caracteres. Se detectan con un criterio
definido en el script, que alcanza a las columnas con al menos diez valores no vacíos y más del 75 %
de valores distintos. Corresponden a respuestas redactadas por las personas encuestadas y no a
categorías, de modo que no admiten recodificación sin perder su contenido. El listado completo
consta en el informe técnico.

## Riesgo residual

Medido sobre las variables cuasi identificadoras disponibles, la proporción de combinaciones
asociadas a una sola persona desciende de 95,3 % en el archivo original a 22,7 % en esta versión. El
riesgo no es nulo, situación propia de una encuesta con esta cantidad de variables. La base no
conserva identificadores directos, geografía fina ni campos de texto libre.

## Marco de uso

La base no constituye una liberación oficial de la ENMA. Fue tratada a partir de datos obtenidos
mediante el formulario de solicitud de la fuente. Su uso se enmarca en los lineamientos del Comité
de Ética de CONICET y en la Ley de Protección de Datos Personales (N.º 25.326), que son el marco
declarado por la encuesta para la circulación de sus datos.

## Cómo citar

Base anonimizada, versión 1:
https://github.com/natdebandi/ENMA_2023/releases/tag/datos-v1

La encuesta es una iniciativa del CONICET y de organizaciones de migrantes y de derechos humanos.
Sitio de la fuente: https://www.encuestamigrante.ar/
