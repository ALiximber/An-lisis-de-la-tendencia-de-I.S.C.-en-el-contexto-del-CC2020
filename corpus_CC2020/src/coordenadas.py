"""Módulo de cálculo de coordenadas X/Y, vectores de competencias CC2020,
afinidad disciplinaria multicriterio y análisis de componentes principales (PCA).

Implementa las Fases 3, 5, 6 y 7 de la auditoría metodológica.
"""
from __future__ import annotations
import csv
import json
import math
from pathlib import Path
from typing import Dict, List, Any, Tuple
import numpy as np

from .metadatos import get_enriched_metadata, normalize_unit_system
from .codebook import classify_course

# Perfiles arquetípicos de referencia en el espacio de 5 dominios de computación
# (CE, CS, SE, IT, IS), derivados de la distribución conceptual del informe CC2020
# (ACM/IEEE-CS, 2020, Cap. 2 y 4) para programas especializados en cada disciplina.
CC2020_ARCHETYPES: Dict[str, np.ndarray] = {
    "CE": np.array([0.55, 0.20, 0.15, 0.05, 0.05], dtype=float),
    "CS": np.array([0.10, 0.55, 0.25, 0.05, 0.05], dtype=float),
    "SE": np.array([0.05, 0.20, 0.55, 0.10, 0.10], dtype=float),
    "IT": np.array([0.10, 0.10, 0.20, 0.45, 0.15], dtype=float),
    "IS": np.array([0.02, 0.08, 0.20, 0.15, 0.55], dtype=float),
}
DOMAINS_5 = ["CE", "CS", "SE", "IT", "IS"]
DOMAINS_6 = ["STEM", "CE", "CS", "SE", "IT", "IS"]


def afinidad_original(pt: float, pa: float, ch: float, cs: float, co: float) -> str:
    """Regla heurística escalonada original de los scripts calcular_bloque_02..05.py."""
    nx = pt + pa
    ny = ch + cs + co
    if nx <= 0 or ny <= 0:
        return "ND"
    if co / ny >= 0.30:
        return "IS"
    if ch / ny >= 0.25:
        return "CE"
    if pt / nx >= 0.45:
        return "CS"
    if cs / ny >= 0.55:
        return "SE"
    return "IT"


def afinidad_regla_corregida(
    pt_comp: float,
    pa_comp: float,
    ch: float,
    cs: float,
    co: float,
    p_comp: Dict[str, float],
) -> str:
    """Regla heurística corregida sin el sesgo de ciencias básicas (STEM) ni el bloqueo algebraico de IT."""
    nx_comp = pt_comp + pa_comp
    ny = ch + cs + co
    if nx_comp <= 0 or ny <= 0:
        return "ND"
    # 1. Fuerte orientación organizacional / sistemas de información
    if co / ny >= 0.30 or p_comp.get("IS", 0.0) >= 0.28:
        return "IS"
    # 2. Fuerte componente de hardware, sistemas digitales y arquitectura física
    if ch / ny >= 0.24 or p_comp.get("CE", 0.0) >= 0.22:
        return "CE"
    # 3. Predominio teórico-algorítmico dentro de las ciencias de la computación (sin inflar por cálculo/física)
    if (pt_comp / nx_comp >= 0.36 and p_comp.get("CS", 0.0) >= p_comp.get("SE", 0.0)) or p_comp.get("CS", 0.0) >= 0.32:
        return "CS"
    # 4. Énfasis en infraestructura, redes, administración de sistemas, seguridad, nube y soporte (IT)
    if p_comp.get("IT", 0.0) >= 0.255 or (
        p_comp.get("IT", 0.0) >= 0.23
        and co / ny >= 0.16
        and p_comp.get("IT", 0.0) >= p_comp.get("SE", 0.0) - 0.03
    ):
        return "IT"
    # 5. Predominio de ingeniería y desarrollo de software
    return "SE"


def calcular_similitud_arquetipos(p_comp: Dict[str, float]) -> Dict[str, Any]:
    """Calcula la similitud coseno contra los 5 arquetipos CC2020 y determina afinidad principal,
    secundaria, margen de separación y carácter híbrido."""
    vec = np.array([p_comp.get(d, 0.0) for d in DOMAINS_5], dtype=float)
    norm_v = float(np.linalg.norm(vec))
    if norm_v <= 1e-12:
        return {
            "Afinidad_CC2020_Principal": "ND",
            "Afinidad_CC2020_Secundaria": "ND",
            "Similitud_Principal": 0.0,
            "Similitud_Secundaria": 0.0,
            "Margen_Afinidad": 0.0,
            "Es_Hibrido": False,
            "Etiqueta_Compuesta": "ND",
            "Similitudes": {d: 0.0 for d in DOMAINS_5},
        }

    sims: Dict[str, float] = {}
    for d, arch in CC2020_ARCHETYPES.items():
        norm_a = float(np.linalg.norm(arch))
        sims[d] = float(np.dot(vec, arch) / (norm_v * norm_a))

    ordered = sorted(sims.items(), key=lambda kv: kv[1], reverse=True)
    d1, s1 = ordered[0]
    d2, s2 = ordered[1]
    margin = s1 - s2
    is_hybrid = margin < 0.08
    etiqueta = f"{d1}/{d2}" if is_hybrid else d1

    return {
        "Afinidad_CC2020_Principal": d1,
        "Afinidad_CC2020_Secundaria": d2,
        "Similitud_Principal": round(s1, 4),
        "Similitud_Secundaria": round(s2, 4),
        "Margen_Afinidad": round(margin, 4),
        "Es_Hibrido": is_hybrid,
        "Etiqueta_Compuesta": etiqueta,
        "Similitudes": {k: round(v, 4) for k, v in sims.items()},
    }


def load_original_backup_results(base_dir: Path) -> Dict[str, Dict[str, Any]]:
    """Carga los resultados originales desde datos_originales_backup para trazabilidad exacta."""
    backup_dir = base_dir / "datos_originales_backup"
    orig: Dict[str, Dict[str, Any]] = {}
    for b in range(1, 6):
        f_json = backup_dir / f"bloque_0{b}_datos.json"
        if not f_json.exists():
            f_json = base_dir / f"bloque_0{b}_datos.json"
        data = json.loads(f_json.read_text(encoding="utf-8"))
        for row in data:
            orig[row["ID"]] = row
    return orig


def load_original_backup_classifications(base_dir: Path) -> Dict[Tuple[str, str], Dict[str, str]]:
    """Carga las clasificaciones materia por materia originales desde datos_originales_backup."""
    backup_dir = base_dir / "datos_originales_backup"
    orig_cls: Dict[Tuple[str, str], Dict[str, str]] = {}
    for b in range(2, 6):
        f_csv = backup_dir / f"bloque_0{b}_clasificacion.csv"
        if not f_csv.exists():
            continue
        with f_csv.open("r", encoding="utf-8-sig") as fh:
            reader = csv.DictReader(fh)
            for r in reader:
                doc_id = r.get("ID") or r.get("\ufeffID") or ""
                asig = r.get("Asignatura", "")
                key = (doc_id, asig)
                orig_cls[key] = r
    return orig_cls


def procesar_plan_estudios(
    doc_id: str,
    courses: List[Dict[str, Any]],
    meta_enriq: Dict[str, Any],
    orig_row: Dict[str, Any],
    orig_cls_map: Dict[Tuple[str, str, str], Dict[str, str]],
    modo: str = "estandar",
    pesos_uniformes: bool = False,
) -> Tuple[Dict[str, Any], List[Dict[str, Any]]]:
    """Procesa un plan de estudios (D016-D075) bajo el libro de códigos unificado CC2020."""
    pt_glob = pa_glob = 0.0
    pt_puro = pa_puro = 0.0
    pt_comp = pa_comp = 0.0
    ch = cs = co = 0.0
    ch_puro = co_puro = 0.0

    total_peso_bruto = 0.0
    peso_obligatorio = 0.0
    peso_optativo_excluido = 0.0
    peso_transversal_excluido = 0.0
    peso_clasificado_xy = 0.0
    peso_no_clasificado = 0.0

    dom_weights: Dict[str, float] = {d: 0.0 for d in DOMAINS_6}
    course_audit_rows: List[Dict[str, Any]] = []

    n_materias_total = len(courses)
    n_materias_clasificadas = 0
    n_materias_hibridas = 0

    for c in courses:
        asig = c["Asignatura"]
        per = c.get("Periodo", "")
        cond_raw = str(c.get("Condicion", ""))
        peso_raw = float(c.get("Peso", 1.0))
        w = 1.0 if pesos_uniformes else peso_raw
        total_peso_bruto += w

        cls = classify_course(asig, cond_raw, modo=modo)
        cond_norm = cls["Condicion_Normalizada"]
        regla_id = cls["Regla_ID"]

        wT, wA = cls["wT"], cls["wA"]
        wH, wS, wO = cls["wH"], cls["wS"], cls["wO"]
        doms = cls["Dominios"]

        if cond_norm in ("Optativa_Generica", "Optativa_Catalogo"):
            peso_optativo_excluido += w
        else:
            peso_obligatorio += w

        if regla_id == "R00_UNMATCHED":
            peso_no_clasificado += w
        elif (wT + wA) == 0.0 and (wH + wS + wO) == 0.0:
            if cond_norm not in ("Optativa_Generica", "Optativa_Catalogo"):
                peso_transversal_excluido += w
        else:
            peso_clasificado_xy += w
            n_materias_clasificadas += 1
            if cls["Es_Hibrida"]:
                n_materias_hibridas += 1

            # Acumulación en X global
            pt_glob += w * wT
            pa_glob += w * wA
            if wT == 1.0 and wA == 0.0:
                pt_puro += w
            elif wA == 1.0 and wT == 0.0:
                pa_puro += w

            # Acumulación en X solo computación (excluyendo ciencias básicas generales R27_STEM_BASIC)
            if regla_id != "R27_STEM_BASIC":
                pt_comp += w * wT
                pa_comp += w * wA

            # Acumulación en Y
            ch += w * wH
            cs += w * wS
            co += w * wO
            if wH == 1.0 and wS == 0.0 and wO == 0.0:
                ch_puro += w
            elif wO == 1.0 and wH == 0.0 and wS == 0.0:
                co_puro += w

            # Acumulación en dominios CC2020
            for d, share in doms.items():
                if d in dom_weights:
                    dom_weights[d] += w * share

        orig_c = orig_cls_map.get((doc_id, asig), {})
        orig_x = orig_c.get("X", orig_c.get("Polo_X", ""))
        orig_y = orig_c.get("Y", orig_c.get("Polo_Y", ""))
        orig_regla = orig_c.get("Regla", "")
        cambio_polo = (orig_x != cls["Pole_X"]) or (orig_y != cls["Pole_Y"])

        course_audit_rows.append({
            "ID": doc_id,
            "Periodo": per,
            "Asignatura": asig,
            "Peso": round(peso_raw, 2) if not peso_raw.is_integer() else int(peso_raw),
            "Unidad": meta_enriq["Unidad_Original"],
            "Condicion_Original": cond_raw,
            "Condicion_Normalizada": cond_norm,
            "Polo_X": cls["Pole_X"],
            "Polo_Y": cls["Pole_Y"],
            "wT": wT,
            "wA": wA,
            "wH": wH,
            "wS": wS,
            "wO": wO,
            "Dominio_Principal": cls["Dominio_Principal"],
            "Regla_ID": regla_id,
            "Categoria_Codebook": cls["Categoria"],
            "Es_Hibrida": cls["Es_Hibrida"],
            "Polo_X_Original": orig_x,
            "Polo_Y_Original": orig_y,
            "Regla_Original": orig_regla,
            "Cambio_vs_Original": cambio_polo,
        })

    # Cálculo de coordenadas X/Y globales
    nx_glob = pt_glob + pa_glob
    ny_corr = ch + cs + co
    x_glob = 5.0 * (pa_glob - pt_glob) / nx_glob if nx_glob > 0 else 0.0
    y_corr = 5.0 * (co - ch) / ny_corr if ny_corr > 0 else 0.0

    # Dispersión binaria estándar (compatible con la fórmula original de los CSV)
    dx_bin = math.sqrt(max(0.0, 25.0 - x_glob * x_glob)) if nx_glob > 0 else 0.0
    dy_bin = math.sqrt(max(0.0, 25.0 * (ch + co) / ny_corr - y_corr * y_corr)) if ny_corr > 0 else 0.0
    r_bin = math.hypot(dx_bin, dy_bin)

    # Dispersión real considerando asignaturas híbridas en x_i = 0, y_i = +-2.5
    # Para x_i in {-5, 0, +5}: E[X^2] = 25*(pt_puro + pa_puro)/nx_glob
    ex2_real = 25.0 * (pt_puro + pa_puro) / nx_glob if nx_glob > 0 else 0.0
    # Para y_i in {-5, -2.5, 0, +2.5, +5}: aproximación exacta por pesos puros e híbridos
    ey2_real = 25.0 * (ch_puro + co_puro + 0.25 * ((ch - ch_puro) + (co - co_puro)) * 2.0) / ny_corr if ny_corr > 0 else 0.0
    dx_real = math.sqrt(max(0.0, ex2_real - x_glob * x_glob))
    dy_real = math.sqrt(max(0.0, ey2_real - y_corr * y_corr))
    r_real = math.hypot(dx_real, dy_real)

    # Coordenada X exclusiva del núcleo de computación (sin STEM básico)
    nx_comp = pt_comp + pa_comp
    x_comp = 5.0 * (pa_comp - pt_comp) / nx_comp if nx_comp > 0 else 0.0
    delta_x_stem = x_comp - x_glob

    # Proporciones en los 6 dominios curriculares (sobre peso clasificado total)
    sum_dom6 = sum(dom_weights.values())
    pct_dom6 = {
        d: (dom_weights[d] / sum_dom6 if sum_dom6 > 0 else 0.0)
        for d in DOMAINS_6
    }

    # Vector normalizado en los 5 dominios de computación (excluyendo STEM)
    sum_dom5 = sum(dom_weights[d] for d in DOMAINS_5)
    p_comp = {
        d: (dom_weights[d] / sum_dom5 if sum_dom5 > 0 else 0.0)
        for d in DOMAINS_5
    }

    # Índice Herfindahl-Hirschman (HHI) y Entropía de Shannon normalizada sobre los 5 dominios
    hhi = sum(v * v for v in p_comp.values()) if sum_dom5 > 0 else 0.0
    entropy = 0.0
    if sum_dom5 > 0:
        for v in p_comp.values():
            if v > 1e-12:
                entropy -= v * math.log(v)
        entropy /= math.log(len(DOMAINS_5))

    # Afinidades disciplinarias bajo los 3 métodos
    af_orig_recalc = afinidad_original(pt_glob, pa_glob, ch, cs, co)
    af_regla_corr = afinidad_regla_corregida(pt_comp, pa_comp, ch, cs, co, p_comp)
    sim_info = calcular_similitud_arquetipos(p_comp)

    cobertura_obligatoria = (
        100.0 * peso_clasificado_xy / peso_obligatorio if peso_obligatorio > 0 else 0.0
    )
    cobertura_bruta = (
        100.0 * peso_clasificado_xy / total_peso_bruto if total_peso_bruto > 0 else 0.0
    )

    nota_auditoria = (
        f"Método auditable CC2020 ({meta_enriq['Unidad_Original']}): "
        f"Pt={pt_glob:.1f}, Pa={pa_glob:.1f} (X_glob={x_glob:+.2f}; sin STEM: Pt_c={pt_comp:.1f}, Pa_c={pa_comp:.1f}, X_comp={x_comp:+.2f}); "
        f"Ch={ch:.1f}, Cs={cs:.1f}, Co={co:.1f} (Y={y_corr:+.2f}); "
        f"Vector CC2020=[CE:{100*p_comp['CE']:.0f}%, CS:{100*p_comp['CS']:.0f}%, SE:{100*p_comp['SE']:.0f}%, IT:{100*p_comp['IT']:.0f}%, IS:{100*p_comp['IS']:.0f}%]; "
        f"Afinidad Regla={af_regla_corr}, Vectorial={sim_info['Etiqueta_Compuesta']} (sim={sim_info['Similitud_Principal']:.2f}, margen={sim_info['Margen_Afinidad']:.2f}); "
        f"cobertura X/Y={peso_clasificado_xy:.1f}/{total_peso_bruto:.1f} ({cobertura_bruta:.1f}% bruto, {cobertura_obligatoria:.1f}% de obligatorio)."
    )

    summary_row = {
        "ID": doc_id,
        "Bloque": meta_enriq["Bloque"],
        "Poblacion": meta_enriq["Poblacion"],
        "Documento": meta_enriq["Documento"],
        "Institucion": meta_enriq["Institucion"],
        "Institucion_ID": meta_enriq["Institucion_ID"],
        "Programa_Academico": meta_enriq["Programa_Academico"],
        "Programa_ID": meta_enriq["Programa_ID"],
        "Familia_Denominacion": meta_enriq["Familia_Denominacion"],
        "Par_Perfil_Plan": meta_enriq["Par_Perfil_Plan"],
        "Pais": meta_enriq["Pais"],
        "Anio": meta_enriq["Anio"],
        "Anio_Original": meta_enriq["Anio_Original"],
        "Tipo_Fuente": meta_enriq["Tipo_Fuente"],
        "Granularidad_Curricular": meta_enriq["Granularidad_Curricular"],
        "Comparable_Estrictamente": meta_enriq["Comparable_Estrictamente"],
        "Unidad_Medida": meta_enriq["Unidad_Estandarizada"],
        "URL_Fuente": meta_enriq["URL_Fuente"],
        "Calidad_URL": meta_enriq["Calidad_URL"],
        # Pesos y conteos
        "N_Materias_Total": n_materias_total,
        "N_Materias_Clasificadas": n_materias_clasificadas,
        "N_Materias_Hibridas": n_materias_hibridas,
        "Peso_Total_Bruto": round(total_peso_bruto, 2),
        "Peso_Obligatorio": round(peso_obligatorio, 2),
        "Peso_Optativo_Excluido": round(peso_optativo_excluido, 2),
        "Peso_Transversal_Excluido": round(peso_transversal_excluido, 2),
        "Peso_Clasificado_XY": round(peso_clasificado_xy, 2),
        "Peso_No_Clasificado": round(peso_no_clasificado, 2),
        "Cobertura_Bruta_Pct": round(cobertura_bruta, 2),
        "Cobertura_Obligatoria_Pct": round(cobertura_obligatoria, 2),
        # Pesos polares corregidos
        "Pt": round(pt_glob, 2),
        "Pa": round(pa_glob, 2),
        "Pt_Comp": round(pt_comp, 2),
        "Pa_Comp": round(pa_comp, 2),
        "Ch": round(ch, 2),
        "Cs": round(cs, 2),
        "Co": round(co, 2),
        # Coordenadas originales (backup)
        "X_Original": float(orig_row["Coordenada_X"]),
        "Y_Original": float(orig_row["Coordenada_Y"]),
        "Radio_Original": round(float(orig_row["Desviacion_Radio"]), 2),
        "Afinidad_Original": orig_row.get("Proximidad_Disciplina_CC2020", orig_row.get("Afinidad_CC2020", "")),
        # Coordenadas corregidas globales (compatibles con esquema de 12 columnas)
        "Coordenada_X": round(x_glob, 2),
        "Coordenada_Y": round(y_corr, 2),
        "Delta_X": round(dx_bin, 2),
        "Delta_Y": round(dy_bin, 2),
        "Desviacion_Radio": round(r_bin, 2),
        "Delta_X_Real": round(dx_real, 2),
        "Delta_Y_Real": round(dy_real, 2),
        "Radio_Real": round(r_real, 2),
        # Coordenada X solo computación (sin sesgo de ciencias básicas STEM)
        "X_Computacion": round(x_comp, 2),
        "Delta_X_STEM": round(delta_x_stem, 2),
        # Diferencias respecto al cálculo original
        "Shift_X": round(x_glob - float(orig_row["Coordenada_X"]), 2),
        "Shift_Y": round(y_corr - float(orig_row["Coordenada_Y"]), 2),
        "Shift_Distancia": round(
            math.hypot(
                x_glob - float(orig_row["Coordenada_X"]),
                y_corr - float(orig_row["Coordenada_Y"]),
            ),
            2,
        ),
        # Proporciones en los 6 dominios (sobre total clasificado)
        "pct_STEM": round(100.0 * pct_dom6["STEM"], 2),
        "pct_CE": round(100.0 * pct_dom6["CE"], 2),
        "pct_CS": round(100.0 * pct_dom6["CS"], 2),
        "pct_SE": round(100.0 * pct_dom6["SE"], 2),
        "pct_IT": round(100.0 * pct_dom6["IT"], 2),
        "pct_IS": round(100.0 * pct_dom6["IS"], 2),
        # Vector normalizado en los 5 dominios de computación (suma 100%)
        "vec_CE": round(100.0 * p_comp["CE"], 2),
        "vec_CS": round(100.0 * p_comp["CS"], 2),
        "vec_SE": round(100.0 * p_comp["SE"], 2),
        "vec_IT": round(100.0 * p_comp["IT"], 2),
        "vec_IS": round(100.0 * p_comp["IS"], 2),
        "HHI_Computacion": round(hhi, 4),
        "Entropia_Normalizada": round(entropy, 4),
        # Afinidades disciplinarias
        "Afinidad_Regla_Original_Recalc": af_orig_recalc,
        "Afinidad_Regla_Corregida": af_regla_corr,
        "Afinidad_CC2020": af_regla_corr,  # Etiqueta principal para el esquema de 12 columnas
        "Afinidad_Vectorial_Principal": sim_info["Afinidad_CC2020_Principal"],
        "Afinidad_Vectorial_Secundaria": sim_info["Afinidad_CC2020_Secundaria"],
        "Similitud_Principal": sim_info["Similitud_Principal"],
        "Similitud_Secundaria": sim_info["Similitud_Secundaria"],
        "Margen_Afinidad": sim_info["Margen_Afinidad"],
        "Es_Hibrido": sim_info["Es_Hibrido"],
        "Etiqueta_Compuesta": sim_info["Etiqueta_Compuesta"],
        "Limitaciones_Evidencia": meta_enriq["Limitaciones_Evidencia"],
        "Notas_Criterio": nota_auditoria,
    }
    return summary_row, course_audit_rows


def procesar_perfil_egreso(
    doc_id: str,
    meta_enriq: Dict[str, Any],
    orig_row: Dict[str, Any],
) -> Dict[str, Any]:
    """Estandariza un registro del Bloque 1 (D001-D015, perfiles de egreso declarativos),
    manteniendo sus coordenadas declarativas documentadas pero separándolo explícitamente
    de la población de mallas curriculares."""
    x_orig = round(float(orig_row["Coordenada_X"]), 2)
    y_orig = round(float(orig_row["Coordenada_Y"]), 2)
    r_orig = round(float(orig_row["Desviacion_Radio"]), 2)
    af_orig = orig_row.get("Proximidad_Disciplina_CC2020", orig_row.get("Afinidad_CC2020", ""))
    pt_b1 = float(orig_row.get("Pt", 0.0))
    pa_b1 = float(orig_row.get("Pa", 0.0))
    ch_b1 = float(orig_row.get("Ch", 0.0))
    cs_b1 = float(orig_row.get("Cs", 0.0))
    co_b1 = float(orig_row.get("Co", 0.0))
    dx_b1 = round(float(orig_row.get("Delta_X", r_orig / math.sqrt(2.0))), 2)
    dy_b1 = round(float(orig_row.get("Delta_Y", r_orig / math.sqrt(2.0))), 2)

    return {
        "ID": doc_id,
        "Bloque": 1,
        "Poblacion": "Perfiles_Egreso",
        "Documento": meta_enriq["Documento"],
        "Institucion": meta_enriq["Institucion"],
        "Institucion_ID": meta_enriq["Institucion_ID"],
        "Programa_Academico": meta_enriq["Programa_Academico"],
        "Programa_ID": meta_enriq["Programa_ID"],
        "Familia_Denominacion": meta_enriq["Familia_Denominacion"],
        "Par_Perfil_Plan": meta_enriq["Par_Perfil_Plan"],
        "Pais": meta_enriq["Pais"],
        "Anio": meta_enriq["Anio"],
        "Anio_Original": meta_enriq["Anio_Original"],
        "Tipo_Fuente": meta_enriq["Tipo_Fuente"],
        "Granularidad_Curricular": meta_enriq["Granularidad_Curricular"],
        "Comparable_Estrictamente": False,
        "Unidad_Medida": "declaraciones_competenciales",
        "URL_Fuente": meta_enriq["URL_Fuente"],
        "Calidad_URL": meta_enriq["Calidad_URL"],
        "N_Materias_Total": int(pt_b1 + pa_b1),
        "N_Materias_Clasificadas": int(pt_b1 + pa_b1),
        "N_Materias_Hibridas": 0,
        "Peso_Total_Bruto": pt_b1 + pa_b1,
        "Peso_Obligatorio": pt_b1 + pa_b1,
        "Peso_Optativo_Excluido": 0.0,
        "Peso_Transversal_Excluido": 0.0,
        "Peso_Clasificado_XY": pt_b1 + pa_b1,
        "Peso_No_Clasificado": 0.0,
        "Cobertura_Bruta_Pct": 100.0,
        "Cobertura_Obligatoria_Pct": 100.0,
        "Pt": pt_b1,
        "Pa": pa_b1,
        "Pt_Comp": pt_b1,
        "Pa_Comp": pa_b1,
        "Ch": ch_b1,
        "Cs": cs_b1,
        "Co": co_b1,
        "X_Original": x_orig,
        "Y_Original": y_orig,
        "Radio_Original": r_orig,
        "Afinidad_Original": af_orig,
        "Coordenada_X": x_orig,
        "Coordenada_Y": y_orig,
        "Delta_X": dx_b1,
        "Delta_Y": dy_b1,
        "Desviacion_Radio": r_orig,
        "Delta_X_Real": dx_b1,
        "Delta_Y_Real": dy_b1,
        "Radio_Real": r_orig,
        "X_Computacion": x_orig,
        "Delta_X_STEM": 0.0,
        "Shift_X": 0.0,
        "Shift_Y": 0.0,
        "Shift_Distancia": 0.0,
        "pct_STEM": 0.0,
        "pct_CE": 0.0,
        "pct_CS": 0.0,
        "pct_SE": 0.0,
        "pct_IT": 0.0,
        "pct_IS": 0.0,
        "vec_CE": 0.0,
        "vec_CS": 0.0,
        "vec_SE": 0.0,
        "vec_IT": 0.0,
        "vec_IS": 0.0,
        "HHI_Computacion": 0.0,
        "Entropia_Normalizada": 0.0,
        "Afinidad_Regla_Original_Recalc": af_orig,
        "Afinidad_Regla_Corregida": af_orig,
        "Afinidad_CC2020": af_orig,
        "Afinidad_Vectorial_Principal": af_orig.split("/")[0],
        "Afinidad_Vectorial_Secundaria": af_orig.split("/")[1] if "/" in af_orig else af_orig,
        "Similitud_Principal": 0.0,
        "Similitud_Secundaria": 0.0,
        "Margen_Afinidad": 0.0,
        "Es_Hibrido": "/" in af_orig,
        "Etiqueta_Compuesta": af_orig,
        "Limitaciones_Evidencia": meta_enriq["Limitaciones_Evidencia"],
        "Notas_Criterio": orig_row.get("Codificacion", orig_row.get("Notas_Criterio", "")),
    }


def compute_pca_6domains(plan_rows: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Ejecuta un Análisis de Componentes Principales (PCA) sobre la matriz estandarizada
    de 6 dominios curriculares (STEM, CE, CS, SE, IT, IS) en los 60 planes de estudio,
    añadiendo PC1 y PC2 a cada registro y devolviendo los autovalores y cargas."""
    cols = ["pct_STEM", "pct_CE", "pct_CS", "pct_SE", "pct_IT", "pct_IS"]
    mat = np.array([[r[c] for c in cols] for r in plan_rows], dtype=float)
    means = mat.mean(axis=0)
    stds = mat.std(axis=0, ddof=1)
    stds_safe = np.where(stds > 1e-12, stds, 1.0)
    Z = (mat - means) / stds_safe

    cov = np.cov(Z, rowvar=False, ddof=1)
    eigvals, eigvecs = np.linalg.eigh(cov)
    idx = np.argsort(eigvals)[::-1]
    eigvals = eigvals[idx]
    eigvecs = eigvecs[:, idx]

    # Asegurar orientación consistente: PC1 positivo hacia Aplicado/IS/IT (derecha en X)
    if eigvecs[0, 0] > 0:  # si STEM carga positivo en PC1, invertimos para alinear con X
        eigvecs[:, 0] *= -1.0
    if eigvecs[5, 1] < 0:  # si IS carga negativo en PC2, invertimos para alinear con Y
        eigvecs[:, 1] *= -1.0

    scores = Z @ eigvecs
    total_var = float(np.sum(eigvals))
    explained_ratio = [float(v / total_var) for v in eigvals]

    for i, r in enumerate(plan_rows):
        r["PC1"] = round(float(scores[i, 0]), 4)
        r["PC2"] = round(float(scores[i, 1]), 4)
        r["PC3"] = round(float(scores[i, 2]), 4)

    loadings = {
        cols[j]: {
            "PC1": round(float(eigvecs[j, 0]), 4),
            "PC2": round(float(eigvecs[j, 1]), 4),
            "PC3": round(float(eigvecs[j, 2]), 4),
        }
        for j in range(len(cols))
    }

    # Correlación de Pearson entre (PC1, PC2) y (Coordenada_X, Coordenada_Y)
    x_vec = np.array([r["Coordenada_X"] for r in plan_rows], dtype=float)
    y_vec = np.array([r["Coordenada_Y"] for r in plan_rows], dtype=float)
    r_pc1_x = float(np.corrcoef(scores[:, 0], x_vec)[0, 1])
    r_pc2_y = float(np.corrcoef(scores[:, 1], y_vec)[0, 1])

    return {
        "Eigenvalues": [round(float(v), 4) for v in eigvals],
        "Explained_Variance_Ratio": [round(100.0 * v, 2) for v in explained_ratio],
        "Cumulative_PC1_PC2_Pct": round(100.0 * (explained_ratio[0] + explained_ratio[1]), 2),
        "Loadings": loadings,
        "Corr_PC1_X": round(r_pc1_x, 4),
        "Corr_PC2_Y": round(r_pc2_y, 4),
    }


def build_full_corpus(base_dir: Path) -> Dict[str, Any]:
    """Procesa los 75 documentos del corpus (D001-D015 perfiles y D016-D075 planes),
    calcula PCA y devuelve todas las tablas listas para exportación y análisis."""
    meta_map = get_enriched_metadata(base_dir)
    orig_results = load_original_backup_results(base_dir)
    orig_cls_map = load_original_backup_classifications(base_dir)

    all_docs: List[Dict[str, Any]] = []
    plan_docs: List[Dict[str, Any]] = []
    profile_docs: List[Dict[str, Any]] = []
    courses_by_block: Dict[int, List[Dict[str, Any]]] = {2: [], 3: [], 4: [], 5: []}

    # Bloque 1: D001-D015
    for idx in range(1, 16):
        doc_id = f"D{idx:03d}"
        row = procesar_perfil_egreso(doc_id, meta_map[doc_id], orig_results[doc_id])
        row["PC1"] = 0.0
        row["PC2"] = 0.0
        row["PC3"] = 0.0
        profile_docs.append(row)
        all_docs.append(row)

    # Bloques 2 a 5: D016-D075
    for b in range(2, 6):
        trans_path = base_dir / f"bloque_0{b}_transcripcion.json"
        raw_block = json.loads(trans_path.read_text(encoding="utf-8"))
        for doc_id in sorted(raw_block.keys()):
            summary_row, audit_rows = procesar_plan_estudios(
                doc_id=doc_id,
                courses=raw_block[doc_id],
                meta_enriq=meta_map[doc_id],
                orig_row=orig_results[doc_id],
                orig_cls_map=orig_cls_map,
                modo="estandar",
                pesos_uniformes=False,
            )
            plan_docs.append(summary_row)
            all_docs.append(summary_row)
            courses_by_block[b].extend(audit_rows)

    pca_info = compute_pca_6domains(plan_docs)

    return {
        "all_docs": all_docs,
        "profile_docs": profile_docs,
        "plan_docs": plan_docs,
        "courses_by_block": courses_by_block,
        "pca_info": pca_info,
    }
