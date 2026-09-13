# ENMA_2023

Encuesta Nacional Migrante de Argentina 2023

Este repositorio contiene el procesamiento de los datos de la ENMA 2023 en R correspondientes al
Anuario Migratorio Argentino 2024
(https://www.encuestamigrante.ar/wp-content/uploads/documentos/anuario_enma_2023_vf.pdf)

## Contenido

- `Cap1_v2.Rmd` a `Cap8_v2.Rmd` — los capítulos del Anuario, con su `html` renderizado.
- `scripts/anonimizar_enma.py` — genera la versión anonimizada para publicación.
- `scripts/medir_reidentificacion.py` — mide el riesgo de reidentificación por escenario de claves.
- `informe/INFORME_enma2023.md` — criterio de anonimización y decisiones pendientes.

## Datos

Los microdatos **no** están en este repositorio y no deben estar. La ENMA no se distribuye como
descarga abierta: se solicita por formulario desde https://www.encuestamigrante.ar/ y su uso se
enmarca en la Ley de Protección de Datos Personales (N.º 25.326) y en los lineamientos del Comité
de Ética de CONICET.

Para reproducir los capítulos hay que solicitar los microdatos a la fuente y colocarlos en
`data/ENMA2023_final_public.csv`. El `.gitignore` bloquea `data/` de modo que no entren por
descuido.

La versión anonimizada que se publica se genera desde ese original:

```
python3 scripts/anonimizar_enma.py
```

## Origen

La encuesta es una iniciativa del CONICET y organizaciones de migrantes y de derechos humanos.
Más información en https://www.encuestamigrante.ar/
