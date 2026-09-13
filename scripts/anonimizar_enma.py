#!/usr/bin/env python3
"""Genera la version anonimizada de la ENMA 2023 para publicacion.

Entrada: data/ENMA2023_final_public.csv (original, NUNCA se toca).
Salida:  data/ENMA2023_anonima_v2.csv + reporte de riesgo en stdout.

Criterio, en dos capas:

1. Eliminacion explicita: identificadores directos, geografia fina y campos de
   texto libre ya conocidos por su alta cardinalidad.

2. Deteccion de testimonios: cualquier columna donde los valores no vacios sean
   casi todos distintos y largos. Son respuestas dictadas palabra por palabra
   ("Vivo en un hotel tomado", "Ilegal"). No reidentifican por combinacion de
   variables sino por contenido, y contradicen la promesa de anonimato con que
   se levanto la encuesta. Se detectan con una regla, no a mano, para que el
   criterio sea auditable y reproducible.
"""
import csv, collections, hashlib, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(BASE, "data", "ENMA2023_final_public.csv")
OUT = os.path.join(BASE, "data", "ENMA2023_anonima_v2.csv")

# Capa 1: eliminacion explicita
ELIMINAR = {
    "ID": "identificador correlativo del registro",
    "fecha": "timestamp exacto de la encuesta (4679 valores unicos)",
    "q8_provincia_res": "provincia de residencia",
    "q9_localidad": "localidad de residencia",
    "q10_barrio": "barrio de residencia",
    "q11_otra_provincia": "provincia de residencia previa",
    "q54_ocupacion": "ocupacion en texto libre (1964 valores unicos)",
}

# Capa 2: regla de deteccion de testimonios
MIN_NO_VACIOS = 10
MIN_LARGO = 12
RATIO_UNICOS = 0.75


def cargar(p):
    with open(p, newline="", encoding="utf-8", errors="replace") as f:
        r = csv.DictReader(f)
        return r.fieldnames, list(r)


def es_testimonio(rows, col):
    """True si la columna es texto casi unico por caso: un relato, no una categoria."""
    vals = [r[col].strip() for r in rows]
    ne = [v for v in vals if v]
    if len(ne) < MIN_NO_VACIOS:
        return False, 0, 0.0
    ratio = len(set(ne)) / len(ne)
    largo = sum(len(v) for v in ne) / len(ne)
    return (ratio > RATIO_UNICOS and largo > MIN_LARGO), len(ne), ratio


def riesgo(rows, cols):
    cols = [c for c in cols if c in rows[0]]
    if not cols:
        return None
    g = collections.Counter(tuple(r[c] for c in cols) for r in rows)
    s = sum(1 for v in g.values() if v == 1)
    return 100 * s / len(g), s, len(g)


def main():
    hdr, rows = cargar(SRC)
    print(f"ORIGEN : {os.path.relpath(SRC, BASE)}")
    print(f"         {len(rows)} filas x {len(hdr)} columnas\n")

    faltan = [c for c in ELIMINAR if c not in hdr]
    if faltan:
        sys.exit(f"ERROR: columnas esperadas ausentes: {faltan}")

    print("CAPA 1 - ELIMINACION EXPLICITA:")
    for c, why in ELIMINAR.items():
        print(f"  - {c:36s} {why}")

    print("\nCAPA 2 - TESTIMONIOS DETECTADOS POR REGLA:")
    testimonios = []
    for c in hdr:
        if c in ELIMINAR:
            continue
        hit, ne, ratio = es_testimonio(rows, c)
        if hit:
            testimonios.append(c)
            ejemplo = next((r[c].strip() for r in rows if r[c].strip()), "")
            print(f"  - {c:36s} {ne:4d} no vacios, {ratio:.0%} unicos | ej: {ejemplo[:52]}")

    print(f"\n  regla: >= {MIN_NO_VACIOS} no vacios, > {RATIO_UNICOS:.0%} unicos, largo medio > {MIN_LARGO}")

    eliminar = set(ELIMINAR) | set(testimonios)
    nuevas = [c for c in hdr if c not in eliminar]
    out_rows = [{c: r[c] for c in nuevas} for r in rows]

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=nuevas)
        w.writeheader()
        w.writerows(out_rows)

    QI_ANTES = ["q8_provincia_res", "q9_localidad", "q10_barrio",
                "q4_genero", "q3_pais_nacimiento", "q2_edad"]
    QI_DESPUES = ["region_amba_agrup", "genero_agrup", "edad_agrup", "nacionalidad_agrup"]
    r1 = riesgo(rows, QI_ANTES)
    r2 = riesgo(out_rows, QI_DESPUES)

    print("\nRIESGO POR COMBINACION DE VARIABLES (celdas con una sola persona)")
    print(f"  antes   {r1[0]:5.1f}%  ({r1[1]:,} de {r1[2]:,})")
    print(f"  despues {r2[0]:5.1f}%  ({r2[1]:,} de {r2[2]:,})")

    h = hashlib.sha256(open(OUT, "rb").read()).hexdigest()
    print(f"\nSALIDA : {os.path.relpath(OUT, BASE)}")
    print(f"         {len(out_rows)} filas x {len(nuevas)} columnas")
    print(f"         {len(eliminar)} columnas eliminadas")
    print(f"         sha256 {h[:32]}...")


if __name__ == "__main__":
    main()
