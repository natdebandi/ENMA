# Depósito de la base en Zenodo

Nota de procedimiento para el depósito de la base anonimizada de la ENMA 2023. El paquete se
encuentra armado y verificado en `~/investigacion/Workspace_R/ENMA_publico/deposito/`.

## Estado

La apertura de la base quedó resuelta el 2026-09-13 y la versión anonimizada se publicó como release
del repositorio, en https://github.com/natdebandi/ENMA_2023/releases/tag/datos-v1 . El depósito en
Zenodo queda pendiente de que el servicio vuelva a estar en línea y su valor es el identificador
persistente para citación, dado que el release no provee DOI. Una vez concretado, el release funciona
como espejo.

## Procedimiento

1. Ingresar a https://zenodo.org e iniciar sesión. La cuenta institucional presenta la ventaja de
   que Zenodo asocia el depósito a la afiliación declarada.

2. Ir a https://zenodo.org/uploads/new y seleccionar la opción de nueva carga.

3. Cargar el archivo `deposito/ENMA2023_anonima_v2.zip`, que reúne el archivo de datos, la nota del
   conjunto y la licencia.

4. Completar los metadatos. El servicio solicita, como mínimo:

   - Tipo de recurso: conjunto de datos.
   - Título: `ENMA 2023 — Base anonimizada (Encuesta Nacional Migrante de Argentina)`.
   - Autores: Natalia Debandi, ORCID 0000-0002-2619-6270, con afiliación en el Centro de
     Inteligencia Artificial Interdisciplinario (CIAI), Universidad Nacional de San Martín y
     CONICET. La descripción señala que la encuesta corresponde al colectivo ENMA.
   - Descripción: el contenido de `deposito/README_dataset.md`, en formato Markdown.
   - Licencia: Creative Commons Attribution 4.0 International.
   - Palabras clave: migración, Argentina, ENMA, microdatos, anonimización.
   - Idioma: español.

5. Guardar. El depósito queda en estado de borrador y admite edición. La publicación se concreta
   con la opción correspondiente.

6. Al publicar, Zenodo asigna un identificador persistente (DOI). Ese identificador se incorpora al
   README del repositorio y a este informe.

## Sobre los archivos

El archivo original `ENMA2023_final_public.csv` conserva provincia, localidad y barrio, y es el que
produce el 95,3 % de reidentificación, de modo que queda fuera del depósito.

La opción de acceso restringido corresponde a otra modalidad de publicación. Si en el futuro se
considera una versión con condiciones de acceso, se tramita como depósito independiente.

## Verificación

El paquete se generó y controló en el directorio del proyecto:

```
sha256  ENMA2023_anonima_v2.csv
sha256  ENMA2023_anonima_v2.zip
```

Ambos resúmenes criptográficos constan en `SHA256SUMS.txt`. La base reúne 4.679 registros y 228
variables, sin identificadores directos, geografía fina, ocupación en texto libre ni las doce
columnas de respuesta libre detectadas por regla.
