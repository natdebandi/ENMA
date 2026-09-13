"""Mide el riesgo de reidentificacion del microdato ENMA 2023 y el efecto de quitar geografia.
Entrada: ENMA2023_final_public.csv (original, sin tocar).
Salida: tabla por escenario, a stdout.
"""
import csv, collections, sys

SRC = "/home/natdebandi/investigacion/Workspace_R/ENMA_publico/data/ENMA2023_final_public.csv"

with open(SRC, newline="", encoding="utf-8", errors="replace") as f:
    rows = list(csv.DictReader(f))

print(f"registros: {len(rows)}  |  columnas: {len(rows[0])}")
print()
print("columnas completas:")
for i, c in enumerate(rows[0].keys()):
    print(f"  {i:3d} {c}")
print()

def riesgo(nombre, cols):
    cols = [c for c in cols if c in rows[0]]
    faltan = [c for c in cols if c not in rows[0]]
    grupos = collections.Counter(tuple(r[c] for c in cols) for r in rows)
    singles = sum(1 for v in grupos.values() if v == 1)
    n = len(grupos)
    print(f"{nombre}")
    print(f"   claves: {cols}")
    print(f"   combinaciones: {n:,}  |  con 1 sola persona: {singles:,}  ({100*singles/n:.1f}%)")
    return 100*singles/n

print("=== ESCENARIOS ===")
riesgo("A. Como esta hoy (geografia + demo)", ["q8_provincia_res","q9_localidad","q10_barrio","q4_genero","q3_pais_nacimiento","q2_edad"])
riesgo("B. Geografia sin barrio", ["q8_provincia_res","q9_localidad","q4_genero","q3_pais_nacimiento"])
riesgo("C. Solo provincia", ["q8_provincia_res","q4_genero","q3_pais_nacimiento"])
riesgo("D. SIN geografia, edad exacta", ["q4_genero","q3_pais_nacimiento","q2_edad"])
riesgo("E. SIN geografia, edad en quinquenios", ["q4_genero","q3_pais_nacimiento"])
