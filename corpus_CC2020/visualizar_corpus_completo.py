"""Visualización maestra consolidada del corpus CC2020 (D001-D075).
Delega el cálculo estadístico y la generación gráfica al módulo unificado y auditado `src`
para garantizar la separación de poblaciones documentales (Perfiles vs. Planes),
regiones HDR de probabilidad acumulada (50%, 80%, 95%) y regresión Nadaraya-Watson
restringida al soporte empírico válido con bandas bootstrap al 95%.
(El script original previo a la auditoría se conserva íntegro en `datos_originales_backup/scripts_originales/`).
"""
from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parent
DEPS_DIR = BASE_DIR / ".deps"
if DEPS_DIR.exists() and str(DEPS_DIR) not in sys.path:
    sys.path.insert(0, str(DEPS_DIR))
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from ejecutar_pipeline import main

if __name__ == "__main__":
    main()
