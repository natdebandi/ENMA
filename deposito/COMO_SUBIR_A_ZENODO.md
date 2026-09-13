# Cómo subir la base a Zenodo

Guía para el depósito de la base anonimizada de la ENMA 2023. Son unos diez minutos.
El paquete ya está armado y verificado en `~/investigacion/Workspace_R/ENMA_publico/deposito/`.

## Antes de empezar

Hay una decisión que conviene tomar con el equipo de la ENMA antes de publicar, aunque sea en
borrador. Zenodo permite crear el depósito sin publicarlo, así que se puede avanzar y dejar la
consulta para después. La pregunta concreta es si el colectivo de la encuesta está de acuerdo con que
una versión anonimizada se distribuya fuera del formulario de solicitud. Los lineamientos que la
propia página menciona, el Comité de Ética de CONICET y la Ley 25.326, apuntan a que la decisión es
de la fuente, no de quien procesa los datos.

## Paso a paso

1. Entrar a https://zenodo.org y crear cuenta o iniciar sesión. Conviene usar la cuenta
   institucional si la hay, porque Zenodo asocia el depósito a la afiliación.

2. Ir a https://zenodo.org/uploads/new y elegir **New upload**.

3. Arrastrar el archivo `deposito/ENMA2023_anonima_v2.zip`. Es el que conviene subir y no el CSV
   suelto, porque el zip ya trae adentro el CSV, el README del dataset y la licencia.

4. Completar los metadatos. Lo mínimo que Zenodo pide:

   - **Resource type**: Dataset.
   - **Title**: `ENMA 2023 — Base anonimizada (Encuesta Nacional Migrante de Argentina)`.
   - **Creators**: agregar las autoras y autores. Acá hace falta el ORCID de cada uno; Zenodo lo
     busca por nombre. La autoría de la base es de quien la produjo, pero corresponde mencionar en
     la descripción que la encuesta es del colectivo ENMA.
   - **Description**: pegar el contenido de `deposito/README_dataset.md`. Es Markdown y Zenodo lo
     respeta si se marca el formato.
   - **License**: Creative Commons Attribution 4.0 International.
   - **Keywords**: migración, Argentina, ENMA, microdatos, anonimización.
   - **Language**: Spanish.

5. Guardar. El depósito queda en **borrador** y todavía se puede editar. Revisar la vista previa y
   recién ahí apretar **Publish**.

6. Al publicar, Zenodo asigna un **DOI**. Copiarlo y avisarme: hay que agregarlo al README del
   repositorio de GitHub para que el código apunte a los datos, y para que quede en el informe.

## Lo que no conviene hacer

No subir el CSV de microdatos original, el `ENMA2023_final_public.csv`. Ese archivo tiene provincia,
localidad y barrio, y es el que produce el 95,3 % de reidentificación.

No usar la opción de acceso restringido para esta versión. Si más adelante se quiere una versión con
condiciones, eso es otro depósito.

## Verificación previa ya hecha

El paquete se generó y se controló desde acá:

```
sha256  7.9M  ENMA2023_anonima_v2.csv   a17216b1e33f93d63183db580187db40...
sha256  631K  ENMA2023_anonima_v2.zip   e0ed23733adfd0313c3f473dbe4b8c51...
```

El script que genera el CSV es reproducible y está en el repositorio. La base tiene 4.679 registros y
228 variables. Se eliminaron los identificadores directos, la geografía fina, la ocupación en texto
libre y doce columnas de testimonio detectadas por regla.
