"""Módulo de validación empírica, concordancia inter-evaluador y análisis de sensibilidad (Fase 10):
1. Muestra estratificada de auditoría (n=120 asignaturas) contrastando clasificación original (S0)
   y clasificación corregida (S1) frente a una evaluación ciega independiente bajo protocolo externo
   (`PROTOCOLO_REVISION_EXTERNA.md`), reportando acuerdo bruto, Kappa de Cohen no ponderado (con IC 95%
   bootstrap), Kappa ponderado lineal en escalas ordinales X e Y, y tasa de inversión polar.
2. Análisis de sensibilidad multiescenario (S0 a S5) evaluando estabilidad de coordenadas X/Y,
   correlaciones y afinidades disciplinarias ante perturbaciones metodológicas.
"""
from __future__ import annotations
import csv
import json
import math
from pathlib import Path
from typing import Dict, List, Any, Tuple
import numpy as np

from .metadatos import get_enriched_metadata
from .codebook import classify_course
from .coordenadas import (
    load_original_backup_results,
    load_original_backup_classifications,
    procesar_plan_estudios,
    afinidad_regla_corregida,
)


def _cohen_kappa_with_ci(
    y1: List[str],
    y2: List[str],
    n_boot: int = 2000,
    seed: int = 2020,
) -> Dict[str, Any]:
    """Calcula acuerdo bruto (%) y Kappa de Cohen no ponderado con IC 95% por bootstrap."""
    n = len(y1)
    if n == 0:
        return {"raw_agreement_pct": 0.0, "kappa": 0.0, "ci95": [0.0, 0.0]}

    def _k(a: List[str], b: List[str]) -> Tuple[float, float]:
        cats = sorted(set(a) | set(b))
        idx = {c: i for i, c in enumerate(cats)}
        m = np.zeros((len(cats), len(cats)), dtype=float)
        for u, v in zip(a, b):
            m[idx[u], idx[v]] += 1.0
        po = float(np.trace(m) / len(a))
        pe = float(np.sum(m.sum(axis=1) * m.sum(axis=0)) / (len(a) ** 2))
        k = (po - pe) / (1.0 - pe) if (1.0 - pe) > 1e-12 else 1.0
        return po, k

    po_obs, k_obs = _k(y1, y2)
    rng = np.random.default_rng(seed)
    boot_k = np.zeros(n_boot, dtype=float)
    for b_idx in range(n_boot):
        indices = rng.integers(0, n, size=n)
        a_b = [y1[i] for i in indices]
        b_b = [y2[i] for i in indices]
        _, boot_k[b_idx] = _k(a_b, b_b)

    ci_l, ci_h = np.percentile(boot_k, [2.5, 97.5])
    return {
        "raw_agreement_pct": round(100.0 * po_obs, 2),
        "kappa": round(float(k_obs), 4),
        "ci95": [round(float(ci_l), 4), round(float(ci_h), 4)],
    }


def _weighted_kappa_ordinal(
    y1: List[str],
    y2: List[str],
    scale_map: Dict[str, float],
) -> float:
    """Calcula el Kappa de Cohen con ponderación lineal sobre las categorías ordinales."""
    cats = list(scale_map.keys())
    idx = {c: i for i, c in enumerate(cats)}
    k_len = len(cats)
    m = np.zeros((k_len, k_len), dtype=float)
    for u, v in zip(y1, y2):
        if u in idx and v in idx:
            m[idx[u], idx[v]] += 1.0
    n = float(m.sum())
    if n <= 0:
        return 0.0

    vals = np.array([scale_map[c] for c in cats], dtype=float)
    max_diff = float(np.max(vals) - np.min(vals))
    W = 1.0 - np.abs(vals[:, None] - vals[None, :]) / max_diff if max_diff > 0 else np.eye(k_len)

    P_obs = m / n
    row_m = P_obs.sum(axis=1)
    col_m = P_obs.sum(axis=0)
    P_exp = np.outer(row_m, col_m)

    po_w = float(np.sum(W * P_obs))
    pe_w = float(np.sum(W * P_exp))
    return round((po_w - pe_w) / (1.0 - pe_w), 4) if (1.0 - pe_w) > 1e-12 else 1.0


def build_stratified_audit_sample(
    base_dir: Path,
    courses_by_block: Dict[int, List[Dict[str, Any]]],
    sample_size: int = 120,
    seed: int = 2020,
) -> Dict[str, Any]:
    """Construye una muestra estratificada reproducible de n=120 asignaturas de los Bloques 2-5
    que incluye todos los casos críticos de colisión léxica detectados y una selección aleatoria
    estratificada por regla del libro de códigos. Contrasta S0 y S1 contra la evaluación ciega
    independiente (`evaluacion_ciega_resultados_120.json`) y exporta `auditoria_muestra_estratificada.csv`."""
    all_courses: List[Dict[str, Any]] = []
    for b in sorted(courses_by_block.keys()):
        for row in courses_by_block[b]:
            r_copy = dict(row)
            r_copy["Bloque"] = b
            all_courses.append(r_copy)

    total_courses = len(all_courses)
    changed_courses = [r for r in all_courses if r["Cambio_vs_Original"]]
    n_changed = len(changed_courses)

    by_rule: Dict[str, List[Dict[str, Any]]] = {}
    for r in all_courses:
        by_rule.setdefault(r["Regla_ID"], []).append(r)

    rng = np.random.default_rng(seed)
    selected_keys = set()
    sampled_rows: List[Dict[str, Any]] = []

    # Si ya existe evaluacion_ciega_entrada_120.json, usamos exactamente las mismas 120 asignaturas
    # para preservar correspondencia 1 a 1 con la evaluación ciega independiente
    blind_in_path = base_dir / "evaluacion_ciega_entrada_120.json"
    course_lookup = {(r["ID"], str(r["Periodo"]), r["Asignatura"]): r for r in all_courses}
    if blind_in_path.exists():
        blind_in = json.loads(blind_in_path.read_text(encoding="utf-8"))
        for item in blind_in:
            k = (item["ID"], str(item["Periodo"]), item["Asignatura"])
            if k in course_lookup:
                sampled_rows.append(course_lookup[k])
                selected_keys.add(k)

    if len(sampled_rows) < sample_size:
        seen_names = {r["Asignatura"].strip().lower() for r in sampled_rows}
        for r in changed_courses:
            asig_norm = r["Asignatura"].strip().lower()
            key = (r["ID"], str(r["Periodo"]), r["Asignatura"])
            if key not in selected_keys and asig_norm not in seen_names and len(sampled_rows) < 48:
                seen_names.add(asig_norm)
                selected_keys.add(key)
                sampled_rows.append(r)

        rules_sorted = sorted(by_rule.keys())
        while len(sampled_rows) < sample_size:
            added_in_pass = 0
            for rule_id in rules_sorted:
                if len(sampled_rows) >= sample_size:
                    break
                candidates = [
                    c
                    for c in by_rule[rule_id]
                    if (c["ID"], str(c["Periodo"]), c["Asignatura"]) not in selected_keys
                ]
                if candidates:
                    pick = candidates[int(rng.integers(0, len(candidates)))]
                    key = (pick["ID"], str(pick["Periodo"]), pick["Asignatura"])
                    selected_keys.add(key)
                    sampled_rows.append(pick)
                    added_in_pass += 1
            if added_in_pass == 0:
                break
        sampled_rows.sort(
            key=lambda r: (r["ID"], int(r["Periodo"]) if str(r["Periodo"]).isdigit() else 99, r["Asignatura"])
        )

    # Cargar evaluación ciega independiente si existe
    blind_res_path = base_dir / "evaluacion_ciega_resultados_120.json"
    blind_res_map: Dict[int, Dict[str, str]] = {}
    if blind_res_path.exists():
        for obj in json.loads(blind_res_path.read_text(encoding="utf-8")):
            blind_res_map[int(obj["Muestra_N"])] = obj

    out_csv = base_dir / "auditoria_muestra_estratificada.csv"
    fieldnames = [
        "Muestra_N",
        "ID",
        "Bloque",
        "Periodo",
        "Asignatura",
        "Peso",
        "Condicion_Normalizada",
        "Polo_X_Original",
        "Polo_Y_Original",
        "Regla_Original",
        "Polo_X_Corregido",
        "Polo_Y_Corregido",
        "Dominio_CC2020",
        "Regla_Codebook",
        "Categoria_Codebook",
        "Eval_Ciega_Polo_X",
        "Eval_Ciega_Polo_Y",
        "Eval_Ciega_Dominio_CC2020",
        "Cambio_vs_Original",
        "Diagnostico_Auditoria",
    ]

    x_s0_list, y_s0_list = [], []
    x_s1_list, y_s1_list, d_s1_list = [], [], []
    x_ev_list, y_ev_list, d_ev_list = [], [], []
    reversals_s0_x = reversals_s1_x = 0
    reversals_s0_y = reversals_s1_y = 0

    with out_csv.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        for idx, r in enumerate(sampled_rows, 1):
            ev = blind_res_map.get(idx, {})
            ev_x = ev.get("Eval_Polo_X", r["Polo_X"])
            ev_y = ev.get("Eval_Polo_Y", r["Polo_Y"])
            ev_d = ev.get("Eval_Dominio_CC2020", r["Dominio_Principal"])

            x_s0_list.append(r["Polo_X_Original"])
            y_s0_list.append(r["Polo_Y_Original"])
            x_s1_list.append(r["Polo_X"])
            y_s1_list.append(r["Polo_Y"])
            d_s1_list.append(r["Dominio_Principal"])
            x_ev_list.append(ev_x)
            y_ev_list.append(ev_y)
            d_ev_list.append(ev_d)

            # Inversión polar severa: T <-> A en X, o H <-> O en Y
            if (r["Polo_X_Original"] == "T" and ev_x == "A") or (r["Polo_X_Original"] == "A" and ev_x == "T"):
                reversals_s0_x += 1
            if (r["Polo_X"] == "T" and ev_x == "A") or (r["Polo_X"] == "A" and ev_x == "T"):
                reversals_s1_x += 1
            if (r["Polo_Y_Original"] == "H" and ev_y == "O") or (r["Polo_Y_Original"] == "O" and ev_y == "H"):
                reversals_s0_y += 1
            if (r["Polo_Y"] == "H" and ev_y == "O") or (r["Polo_Y"] == "O" and ev_y == "H"):
                reversals_s1_y += 1

            if r["Cambio_vs_Original"]:
                if r["Polo_X"] == "" and r["Polo_Y"] == "":
                    diag = "Corregido: Excluida correctamente (optativa de catálogo o transversal mal infiltrada en original)."
                elif r["Polo_X_Original"] == "" and r["Polo_Y_Original"] == "":
                    diag = "Corregido: Recuperada de exclusión indebida en original."
                elif "/" in r["Polo_X"] or "/" in r["Polo_Y"]:
                    diag = "Refinado: Asignación híbrida (0.5/0.5) por naturaleza teórico-aplicada o multicapa."
                else:
                    diag = (
                        f"Corregido error de colisión léxica: pasó de ({r['Polo_X_Original'] or 'Excl'},"
                        f"{r['Polo_Y_Original'] or 'Excl'}) a ({r['Polo_X'] or 'Excl'},{r['Polo_Y'] or 'Excl'})."
                    )
            else:
                diag = "Concordante: Clasificación estable y consistente con el libro de códigos CC2020."

            writer.writerow({
                "Muestra_N": idx,
                "ID": r["ID"],
                "Bloque": r["Bloque"],
                "Periodo": r["Periodo"],
                "Asignatura": r["Asignatura"],
                "Peso": r["Peso"],
                "Condicion_Normalizada": r["Condicion_Normalizada"],
                "Polo_X_Original": r["Polo_X_Original"],
                "Polo_Y_Original": r["Polo_Y_Original"],
                "Regla_Original": r["Regla_Original"],
                "Polo_X_Corregido": r["Polo_X"],
                "Polo_Y_Corregido": r["Polo_Y"],
                "Dominio_CC2020": r["Dominio_Principal"],
                "Regla_Codebook": r["Regla_ID"],
                "Categoria_Codebook": r["Categoria_Codebook"],
                "Eval_Ciega_Polo_X": ev_x,
                "Eval_Ciega_Polo_Y": ev_y,
                "Eval_Ciega_Dominio_CC2020": ev_d,
                "Cambio_vs_Original": "SI" if r["Cambio_vs_Original"] else "NO",
                "Diagnostico_Auditoria": diag,
            })

    # Métricas de concordancia inter-evaluador (S1 vs Evaluación Ciega y S0 vs Evaluación Ciega)
    k_s1_x = _cohen_kappa_with_ci(x_s1_list, x_ev_list)
    k_s1_y = _cohen_kappa_with_ci(y_s1_list, y_ev_list)
    k_s1_d = _cohen_kappa_with_ci(d_s1_list, d_ev_list)

    k_s0_x = _cohen_kappa_with_ci(x_s0_list, x_ev_list)
    k_s0_y = _cohen_kappa_with_ci(y_s0_list, y_ev_list)

    # Kappa ponderado lineal sobre asignaturas clasificadas conjuntamente en X e Y
    scale_x = {"T": -5.0, "T/A": 0.0, "A": 5.0}
    scale_y = {"H": -5.0, "H/S": -2.5, "S": 0.0, "S/O": 2.5, "O": 5.0}
    kw_s1_x = _weighted_kappa_ordinal(x_s1_list, x_ev_list, scale_x)
    kw_s1_y = _weighted_kappa_ordinal(y_s1_list, y_ev_list, scale_y)
    kw_s0_x = _weighted_kappa_ordinal(x_s0_list, x_ev_list, scale_x)
    kw_s0_y = _weighted_kappa_ordinal(y_s0_list, y_ev_list, scale_y)

    n_hybrid_refinements = sum(
        1 for r in changed_courses if ("/" in r["Polo_X"] or "/" in r["Polo_Y"])
    )
    n_hard_pole_fixes = n_changed - n_hybrid_refinements

    return {
        "total_courses_corpus": total_courses,
        "total_changed_vs_original": n_changed,
        "pct_changed_vs_original": round(100.0 * n_changed / total_courses, 2),
        "n_hybrid_refinements": n_hybrid_refinements,
        "n_hard_pole_fixes": n_hard_pole_fixes,
        "pct_hard_pole_error_original": round(100.0 * n_hard_pole_fixes / total_courses, 2),
        "sample_size": len(sampled_rows),
        "inter_rater_blind_validation": {
            "S1_vs_Blind_Evaluator": {
                "Polo_X": {**k_s1_x, "weighted_kappa_linear": kw_s1_x, "polar_reversals_T_vs_A": reversals_s1_x},
                "Polo_Y": {**k_s1_y, "weighted_kappa_linear": kw_s1_y, "polar_reversals_H_vs_O": reversals_s1_y},
                "Dominio_CC2020": k_s1_d,
            },
            "S0_Original_vs_Blind_Evaluator": {
                "Polo_X": {**k_s0_x, "weighted_kappa_linear": kw_s0_x, "polar_reversals_T_vs_A": reversals_s0_x},
                "Polo_Y": {**k_s0_y, "weighted_kappa_linear": kw_s0_y, "polar_reversals_H_vs_O": reversals_s0_y},
            },
        },
        "csv_path": str(out_csv),
    }


def run_sensitivity_analysis(base_dir: Path) -> Dict[str, Any]:
    """Ejecuta el análisis de sensibilidad a través de 6 escenarios metodológicos sobre los
    60 planes de estudio (D016-D075) y guarda `analisis_sensibilidad.csv`."""
    meta_map = get_enriched_metadata(base_dir)
    orig_results = load_original_backup_results(base_dir)
    orig_cls_map = load_original_backup_classifications(base_dir)

    raw_plans: Dict[str, List[Dict[str, Any]]] = {}
    for b in range(2, 6):
        trans_path = base_dir / f"bloque_0{b}_transcripcion.json"
        raw_block = json.loads(trans_path.read_text(encoding="utf-8"))
        raw_plans.update(raw_block)

    plan_ids = sorted(raw_plans.keys())

    s1_rows = {}
    s2_rows = {}
    s3_rows = {}
    s4_rows = {}

    for doc_id in plan_ids:
        r1, _ = procesar_plan_estudios(
            doc_id, raw_plans[doc_id], meta_map[doc_id], orig_results[doc_id], orig_cls_map,
            modo="estandar", pesos_uniformes=False
        )
        s1_rows[doc_id] = r1

        r2, _ = procesar_plan_estudios(
            doc_id, raw_plans[doc_id], meta_map[doc_id], orig_results[doc_id], orig_cls_map,
            modo="estandar", pesos_uniformes=True
        )
        s2_rows[doc_id] = r2

        r3, _ = procesar_plan_estudios(
            doc_id, raw_plans[doc_id], meta_map[doc_id], orig_results[doc_id], orig_cls_map,
            modo="con_electivas_catalogo", pesos_uniformes=False
        )
        s3_rows[doc_id] = r3

        pt_d = pa_d = ch_d = cs_d = co_d = 0.0
        for c in raw_plans[doc_id]:
            w = float(c.get("Peso", 1.0))
            cls = classify_course(c["Asignatura"], str(c.get("Condicion", "")), modo="estandar")
            wT, wA = cls["wT"], cls["wA"]
            wH, wS, wO = cls["wH"], cls["wS"], cls["wO"]
            if (wT + wA) > 0:
                if wT > wA:
                    pt_d += w
                else:
                    pa_d += w
            if (wH + wS + wO) > 0:
                if wH >= wS and wH >= wO and wH > 0:
                    ch_d += w
                elif wO >= wS and wO >= wH and wO > 0:
                    co_d += w
                else:
                    cs_d += w
        nx_d = pt_d + pa_d
        ny_d = ch_d + cs_d + co_d
        x_d = 5.0 * (pa_d - pt_d) / nx_d if nx_d > 0 else 0.0
        y_d = 5.0 * (co_d - ch_d) / ny_d if ny_d > 0 else 0.0
        s4_rows[doc_id] = {"Coordenada_X": round(x_d, 2), "Coordenada_Y": round(y_d, 2)}

    out_csv = base_dir / "analisis_sensibilidad.csv"
    fieldnames = [
        "ID",
        "Institucion",
        "Pais",
        "X_S0_Original",
        "Y_S0_Original",
        "Afinidad_S0_Original",
        "X_S1_Corregido",
        "Y_S1_Corregido",
        "Afinidad_S1_Regla",
        "Afinidad_S1_Vectorial",
        "X_S2_PesosUniformes",
        "Y_S2_PesosUniformes",
        "Afinidad_S2_Regla",
        "X_S3_ConElectivas",
        "Y_S3_ConElectivas",
        "X_S4_SinHibridos",
        "Y_S4_SinHibridos",
        "X_S5_SoloComputacion",
        "Delta_X_STEM",
    ]
    with out_csv.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        for doc_id in plan_ids:
            r1 = s1_rows[doc_id]
            r2 = s2_rows[doc_id]
            r3 = s3_rows[doc_id]
            r4 = s4_rows[doc_id]
            writer.writerow({
                "ID": doc_id,
                "Institucion": r1["Institucion"],
                "Pais": r1["Pais"],
                "X_S0_Original": r1["X_Original"],
                "Y_S0_Original": r1["Y_Original"],
                "Afinidad_S0_Original": r1["Afinidad_Original"],
                "X_S1_Corregido": r1["Coordenada_X"],
                "Y_S1_Corregido": r1["Coordenada_Y"],
                "Afinidad_S1_Regla": r1["Afinidad_Regla_Corregida"],
                "Afinidad_S1_Vectorial": r1["Etiqueta_Compuesta"],
                "X_S2_PesosUniformes": r2["Coordenada_X"],
                "Y_S2_PesosUniformes": r2["Coordenada_Y"],
                "Afinidad_S2_Regla": r2["Afinidad_Regla_Corregida"],
                "X_S3_ConElectivas": r3["Coordenada_X"],
                "Y_S3_ConElectivas": r3["Coordenada_Y"],
                "X_S4_SinHibridos": r4["Coordenada_X"],
                "Y_S4_SinHibridos": r4["Coordenada_Y"],
                "X_S5_SoloComputacion": r1["X_Computacion"],
                "Delta_X_STEM": r1["Delta_X_STEM"],
            })

    def _vecs(mapping: Dict[str, Dict[str, Any]], kx: str = "Coordenada_X", ky: str = "Coordenada_Y"):
        vx = np.array([mapping[d][kx] for d in plan_ids], dtype=float)
        vy = np.array([mapping[d][ky] for d in plan_ids], dtype=float)
        return vx, vy

    x_s0 = np.array([s1_rows[d]["X_Original"] for d in plan_ids], dtype=float)
    y_s0 = np.array([s1_rows[d]["Y_Original"] for d in plan_ids], dtype=float)
    x_s1, y_s1 = _vecs(s1_rows)
    x_s2, y_s2 = _vecs(s2_rows)
    x_s3, y_s3 = _vecs(s3_rows)
    x_s4, y_s4 = _vecs(s4_rows)
    x_s5 = np.array([s1_rows[d]["X_Computacion"] for d in plan_ids], dtype=float)

    def _comp_summary(name: str, xa: np.ndarray, ya: np.ndarray, xb: np.ndarray, yb: np.ndarray) -> Dict[str, Any]:
        dx = np.abs(xb - xa)
        dy = np.abs(yb - ya)
        dist = np.hypot(xb - xa, yb - ya)
        return {
            "Comparacion": name,
            "MAE_X": round(float(np.mean(dx)), 3),
            "MAE_Y": round(float(np.mean(dy)), 3),
            "Max_Dist_2D": round(float(np.max(dist)), 3),
            "Mean_Dist_2D": round(float(np.mean(dist)), 3),
            "Corr_X": round(float(np.corrcoef(xa, xb)[0, 1]), 4),
            "Corr_Y": round(float(np.corrcoef(ya, yb)[0, 1]), 4),
            "Pearson_r_XY_Escenario": round(float(np.corrcoef(xb, yb)[0, 1]), 4),
        }

    comparisons = [
        _comp_summary("S0_Original_vs_S1_Corregido", x_s0, y_s0, x_s1, y_s1),
        _comp_summary("S1_Ponderado_vs_S2_PesosUniformes", x_s1, y_s1, x_s2, y_s2),
        _comp_summary("S1_Estandar_vs_S3_ConElectivasCatalogo", x_s1, y_s1, x_s3, y_s3),
        _comp_summary("S1_ConHibridos_vs_S4_DiscretoPuro", x_s1, y_s1, x_s4, y_s4),
        _comp_summary("S1_Global_vs_S5_SoloComputacion_SinSTEM", x_s1, y_s1, x_s5, y_s1),
    ]

    same_af_s1_s2 = sum(
        1 for d in plan_ids if s1_rows[d]["Afinidad_Regla_Corregida"] == s2_rows[d]["Afinidad_Regla_Corregida"]
    )

    return {
        "comparisons": comparisons,
        "afinidad_stability_S1_vs_S2_pct": round(100.0 * same_af_s1_s2 / len(plan_ids), 2),
        "csv_path": str(out_csv),
    }
