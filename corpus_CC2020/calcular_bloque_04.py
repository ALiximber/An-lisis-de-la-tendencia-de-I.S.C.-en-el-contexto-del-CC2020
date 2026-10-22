"""Bloque 4 (D046-D060): clasificación auditable de asignaturas y cálculo de coordenadas CC2020.
Utiliza el libro de códigos unificado (`src/codebook.py`) y el motor de coordenadas (`src/coordenadas.py`).
El script original previo a la auditoría se preserva en `datos_originales_backup/scripts_originales/calcular_bloque_04.py`.
"""
from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parent
DEPS_DIR = BASE_DIR / ".deps"
if DEPS_DIR.exists() and str(DEPS_DIR) not in sys.path:
    sys.path.insert(0, str(DEPS_DIR))
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from src.coordenadas import build_full_corpus
from ejecutar_pipeline import export_block_files

if __name__ == "__main__":
    corpus_data = build_full_corpus(BASE_DIR)
    export_block_files(BASE_DIR, corpus_data)
    print("Bloque 4 (D046-D060) procesado con el libro de códigos unificado CC2020.")
