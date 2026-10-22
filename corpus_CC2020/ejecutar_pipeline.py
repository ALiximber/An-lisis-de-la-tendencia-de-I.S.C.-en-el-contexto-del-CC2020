"""Script maestro reproducible para ejecutar toda la canalización (pipeline) del proyecto CC2020:
1. Procesamiento unificado de metadatos y clasificación curricular auditable (D001-D075).
2. Cálculo de coordenadas globales, coordenadas de núcleo de computación (sin STEM),
   vectores de competencias en 6 y 5 dominios, índice HHI, entropía y PCA.
3. Actualización de `bloque_02..05_datos.json`, `bloque_02..05_resultados.csv`,
   `bloque_02..05_clasificacion.csv` y `bloque_02..05_analisis.md`, además de los ficheros
   consolidados (`corpus_CC2020_consolidado_75.csv`, `corpus_CC2020_planes_60.csv`,
   `corpus_CC2020_perfiles_15.csv`).
4. Validación empírica (muestra estratificada n=120) y análisis de sensibilidad (escenarios S0-S5).
5. Auditoría estadística completa (KDE 2D HDR, Nadaraya-Watson LOOCV + Bootstrap IC 95%,
   pruebas de correlación por permutación y Kruskal-Wallis por familia y país).
6. Generación de todas las visualizaciones científicas en alta resolución (300 DPI).
"""
from __future__ import annotations
import csv
import json
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DEPS_DIR = BASE_DIR / ".deps"
if DEPS_DIR.exists() and str(DEPS_DIR) not in sys.path:
    sys.path.insert(0, str(DEPS_DIR))
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from src.coordenadas import build_full_corpus
from src.estadistica import run_complete_statistical_audit
from src.validacion_empirica import build_stratified_audit_sample, run_sensitivity_analysis
from src.visualizaciones import generate_all_visualizations


def export_block_files(base_dir: Path, corpus_data: dict) -> None:
    """Actualiza los archivos JSON y CSV por bloque manteniendo compatibilidad con el esquema
    de 12 columnas e incorporando los metadatos y métricas corregidas."""
    all_docs = corpus_data["all_docs"]
    courses_by_block = corpus_data["courses_by_block"]

    cols_12 = [
        "ID",
        "Titulo_Documento",
        "Institucion_Fuente",
        "Pais",
        "Anio",
        "Tipo_Fuente",
        "Coordenada_X",
        "Coordenada_Y",
        "Desviacion_Radio",
        "Proximidad_Disciplina_CC2020",
        "Resumen_Evidencia_X",
        "Resumen_Evidencia_Y",
    ]

    for b in range(2, 6):
        b_docs = [r for r in all_docs if r["Bloque"] == b]
        json_rows = []
        csv_12_rows = []

        for r in b_docs:
            tot = r["Peso_Total_Bruto"]
            cob_x = (r["Pt"] + r["Pa"]) / tot if tot > 0 else 0.0
            cob_y = (r["Ch"] + r["Cs"] + r["Co"]) / tot if tot > 0 else 0.0
            u_orig = r["Unidad_Medida"].replace("_", " ")
            res_x = (
                f"Pt={r['Pt']:g}; Pa={r['Pa']:g} (sin STEM: Pt_c={r['Pt_Comp']:g}, Pa_c={r['Pa_Comp']:g}, "
                f"X_comp={r['X_Computacion']:+.2f}); cobertura X={cob_x:.0%} del total ({tot:g})"
            )
            res_y = (
                f"Ch={r['Ch']:g}; Cs={r['Cs']:g}; Co={r['Co']:g}; cobertura Y={cob_y:.0%} del total; "
                f"Vector=[CE:{r['vec_CE']:.0f}%,CS:{r['vec_CS']:.0f}%,SE:{r['vec_SE']:.0f}%,IT:{r['vec_IT']:.0f}%,IS:{r['vec_IS']:.0f}%]"
            )

            j_obj = {
                "ID": r["ID"],
                "Titulo_Documento": r["Documento"],
                "Institucion_Fuente": r["Institucion"],
                "Institucion_ID": r["Institucion_ID"],
                "Programa_ID": r["Programa_ID"],
                "Familia_Denominacion": r["Familia_Denominacion"],
                "Pais": r["Pais"],
                "Anio": r["Anio"],
                "Tipo_Fuente": r["Tipo_Fuente"],
                "Granularidad_Curricular": r["Granularidad_Curricular"],
                "Coordenada_X": r["Coordenada_X"],
                "Coordenada_Y": r["Coordenada_Y"],
                "X_Computacion": r["X_Computacion"],
                "Delta_X_STEM": r["Delta_X_STEM"],
                "Desviacion_Radio": r["Desviacion_Radio"],
                "Radio_Real": r["Radio_Real"],
                "Proximidad_Disciplina_CC2020": r["Afinidad_CC2020"],
                "Afinidad_Vectorial": r["Etiqueta_Compuesta"],
                "Similitud_Vectorial": r["Similitud_Principal"],
                "Margen_Vectorial": r["Margen_Afinidad"],
                "Afinidad_Original": r["Afinidad_Original"],
                "X_Original": r["X_Original"],
                "Y_Original": r["Y_Original"],
                "Resumen_Evidencia_X": res_x,
                "Resumen_Evidencia_Y": res_y,
                "Pt": r["Pt"],
                "Pa": r["Pa"],
                "Pt_Comp": r["Pt_Comp"],
                "Pa_Comp": r["Pa_Comp"],
                "Ch": r["Ch"],
                "Cs": r["Cs"],
                "Co": r["Co"],
                "vec_CE": r["vec_CE"],
                "vec_CS": r["vec_CS"],
                "vec_SE": r["vec_SE"],
                "vec_IT": r["vec_IT"],
                "vec_IS": r["vec_IS"],
                "pct_STEM": r["pct_STEM"],
                "Total_Peso": r["Peso_Total_Bruto"],
                "Peso_Obligatorio": r["Peso_Obligatorio"],
                "Delta_X": r["Delta_X"],
                "Delta_Y": r["Delta_Y"],
                "URL": r["URL_Fuente"],
                "Calidad_URL": r["Calidad_URL"],
                "Unidad_Peso": u_orig,
            }
            json_rows.append(j_obj)
            csv_12_rows.append({k: j_obj[k] for k in cols_12})

        (base_dir / f"bloque_0{b}_datos.json").write_text(
            json.dumps(json_rows, ensure_ascii=False, indent=2), encoding="utf-8"
        )

        with (base_dir / f"bloque_0{b}_resultados.csv").open("w", encoding="utf-8", newline="") as fh:
            writer = csv.DictWriter(fh, fieldnames=cols_12)
            writer.writeheader()
            writer.writerows(csv_12_rows)

        # Clasificación asignatura por asignatura del bloque
        c_rows = courses_by_block[b]
        if c_rows:
            c_fields = list(c_rows[0].keys())
            with (base_dir / f"bloque_0{b}_clasificacion.csv").open("w", encoding="utf-8", newline="") as fh:
                writer = csv.DictWriter(fh, fieldnames=c_fields)
                writer.writeheader()
                writer.writerows(c_rows)

    # Exportar tablas maestras consolidadas (incluyendo actualización de corpus_CC2020_completo_75.csv/.json)
    all_fields = list(all_docs[0].keys())
    for fname, subset in [
        ("corpus_CC2020_consolidado_75.csv", all_docs),
        ("corpus_CC2020_completo_75.csv", all_docs),
        ("corpus_CC2020_planes_60.csv", corpus_data["plan_docs"]),
        ("corpus_CC2020_perfiles_15.csv", corpus_data["profile_docs"]),
    ]:
        with (base_dir / fname).open("w", encoding="utf-8", newline="") as fh:
            writer = csv.DictWriter(fh, fieldnames=all_fields)
            writer.writeheader()
            writer.writerows(subset)

    (base_dir / "corpus_CC2020_completo_75.json").write_text(
        json.dumps(all_docs, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def main() -> None:
    print("1. Construyendo corpus unificado y auditado (D001-D075)...")
    corpus_data = build_full_corpus(BASE_DIR)
    export_block_files(BASE_DIR, corpus_data)

    print("2. Generando muestra estratificada de validación empírica (n=120)...")
    audit_sample_info = build_stratified_audit_sample(
        BASE_DIR, corpus_data["courses_by_block"], sample_size=120, seed=2020
    )

    print("3. Ejecutando análisis de sensibilidad multiescenario (S0-S5)...")
    sens_info = run_sensitivity_analysis(BASE_DIR)

    print("4. Ejecutando auditoría estadística completa (KDE HDR, NW LOOCV + Bootstrap, Kruskal-Wallis)...")
    stats_info = run_complete_statistical_audit(corpus_data)

    print("5. Generando visualizaciones científicas en alta resolución...")
    generated_figs = generate_all_visualizations(BASE_DIR, corpus_data, stats_info, sens_info)

    # Guardar resumen estructurado de auditoría en JSON (excluyendo grillas numpy de KDE/NW)
    stats_serializable = {
        "pca_6domains": corpus_data["pca_info"],
        "correlaciones": stats_info["correlaciones"],
        "nadaraya_watson_summary": {
            "loocv_60": stats_info["nadaraya_watson"]["loocv_60"],
            "loocv_59": stats_info["nadaraya_watson"]["loocv_59"],
            "r2_60_opt": stats_info["nadaraya_watson"]["fit_60_opt"]["r2_in_sample"],
            "r2_59_opt": stats_info["nadaraya_watson"]["fit_59_opt"]["r2_in_sample"],
        },
        "kde_summary": {
            k: v for k, v in stats_info["kde"].items() if k != "_objects"
        },
        "pares_exactos": stats_info["pares_exactos"],
        "kruskal_familia_X": stats_info["kruskal_familia_X"],
        "kruskal_familia_Y": stats_info["kruskal_familia_Y"],
        "kruskal_pais_X": stats_info["kruskal_pais_X"],
        "kruskal_pais_Y": stats_info["kruskal_pais_Y"],
        "validacion_empirica": audit_sample_info,
        "sensibilidad": sens_info,
        "figuras_generadas": generated_figs,
    }
    (BASE_DIR / "auditoria_estadistica_resumen.json").write_text(
        json.dumps(stats_serializable, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print("Pipeline completado exitosamente. Resumen guardado en auditoria_estadistica_resumen.json.")


if __name__ == "__main__":
    main()

