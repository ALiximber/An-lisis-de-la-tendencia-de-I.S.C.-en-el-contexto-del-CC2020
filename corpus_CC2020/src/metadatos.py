"""Metadatos normalizados, auditoría de fuentes y clasificación de granularidad documental (D001-D075)."""
from __future__ import annotations
from pathlib import Path
from typing import Dict, Any
from urllib.parse import urlparse
import json

# Pares exactos Perfil (Bloque 1) <-> Plan de Estudios (Bloques 2-3) del mismo programa académico
PARES_PERFIL_PLAN = {
    "D001": "D017",  # IPN — ESCOM: Ingeniería en Sistemas Computacionales (Plan 2020)
    "D017": "D001",
    "D003": "D034",  # TecNM: Ingeniería en Sistemas Computacionales (Plan ISIC-2010-224)
    "D034": "D003",
}

# Instituciones que aparecen en más de un documento (con el mismo o distinto programa)
MAPA_INSTITUCION_UNICA = {
    "D001": "INST_IPN_ESCOM",
    "D017": "INST_IPN_ESCOM",
    "D003": "INST_TECNM",
    "D034": "INST_TECNM",
    "D036": "INST_UCR",
    "D075": "INST_UCR",
}

# Programas académicos únicos (D001==D017 y D003==D034 son el mismo programa en la misma institución;
# D036 y D075 son dos programas distintos dentro de la Universidad de Costa Rica)
MAPA_PROGRAMA_UNICO = {
    "D001": "PROG_IPN_ESCOM_ISC2020",
    "D017": "PROG_IPN_ESCOM_ISC2020",
    "D003": "PROG_TECNM_ISIC2010",
    "D034": "PROG_TECNM_ISIC2010",
}

# Correcciones y normalizaciones documentales verificadas contra fuentes primarias
ANIO_NORMALIZADO = {
    "D019": ("2021", "Inferido de ruta del PDF oficial UPN (2021-07)"),
    "D023": ("2023", "Verificado en texto oficial: Resolución Nº 012-2023-CU (impreso en 2024)"),
    "D024": ("2025", "Inferido de ruta de malla UNAD (2025)"),
    "D031": ("2016", "Plan 2016 actualizado/vigente 2023 (Tomo I FI-UNAM)"),
    "D032": ("2026", "Plan de estudios FCI 2026-2 (prospectivo/vigente desde 2026)"),
}


def clasificar_familia_programa(titulo: str) -> str:
    """Clasifica el título del programa en 5 familias de denominación académica en América Latina."""
    t = titulo.lower()
    if "sistemas computacionales" in t:
        return "ISC_Sistemas_Computacionales"
    if (
        "software" in t
        or "tecnologias de la informacion" in t
        or "tecnologías de la información" in t
        or "informatica empresarial" in t
        or "informática empresarial" in t
        or "sistemas de informacion" in t
        or "sistemas de información" in t
    ):
        return "ISW_TI_Software_Tecnologias"
    if (
        "ciencias de la comput" in t
        or "ciencia da comput" in t
        or "ciencia de la comput" in t
        or "ingenieria en computacion" in t
        or "ingeniería en computación" in t
        or "engenharia de comput" in t
        or "civil en computacion" in t
        or "civil en computación" in t
        or "civil computacion" in t
        or "bachillerato en computacion" in t
        or "bachillerato en computación" in t
        or "tecnologias computacionales" in t
        or "tecnologías computacionales" in t
    ):
        return "IC_Ciencias_Ingenieria_Computacion"
    if "informatica" in t or "informática" in t:
        return "II_Ingenieria_Informatica"
    return "IS_Ingenieria_Sistemas"


def normalize_unit_system(doc_id: str, bloque_num: int, unidad_raw: str) -> str:
    if bloque_num == 1:
        return "declaraciones_competenciales"
    if doc_id in ("D056", "D060", "D071"):
        return "horas_semanales"
    if unidad_raw == "horas":
        return "horas_reloj_totales"
    if "horas/créditos" in unidad_raw:
        return "horas_semanales_creditos"
    if "unidades valorativas" in unidad_raw:
        return "unidades_valorativas"
    if "sct" in unidad_raw.lower():
        return "creditos_SCT"
    if "uea" in unidad_raw.lower():
        return "creditos_UEA"
    return "creditos_academicos"


def evaluar_calidad_documental(
    doc_id: str,
    bloque_num: int,
    total_peso: float,
    url: str,
) -> tuple[str, str, bool, str]:
    parsed = urlparse(url or "")
    if parsed.path in ("", "/"):
        calidad_url = "Dominio_Institucional_Raiz"
    elif (
        parsed.path.lower().endswith(".pdf")
        or "dmsdocument" in parsed.path.lower()
        or "download" in parsed.path.lower()
    ):
        calidad_url = "Documento_PDF_Directo"
    else:
        calidad_url = "Pagina_Oficial_Carrera"

    if bloque_num == 1:
        if doc_id == "D004":
            gran = "Perfil_Indexado_Parcial"
            lim = "Perfil breve (2 unidades); texto recuperado de caché/índice web por error HTTP 500 en origen."
        elif total_peso <= 3:
            gran = "Perfil_Competencias_Breve"
            lim = f"Perfil sintético con sólo {total_peso:g} unidades técnicas codificables; alta discretización."
        else:
            gran = "Perfil_Competencias_Completo"
            lim = "Declaración discursiva de competencias de egreso sin ponderación en créditos."
        return gran, calidad_url, False, lim

    if doc_id == "D032":
        return (
            "Malla_Parcial_Especialidad",
            calidad_url,
            False,
            "El PDF oficial de facultad (FCI) comprende los ciclos 5 a 10 (128 cr.) y omite Estudios Generales Ciencias (ciclos 1 a 4, ~72 cr. de ciencias básicas), desplazando X artificialmente hacia aplicación.",
        )

    if doc_id in {f"D{i:03d}" for i in range(16, 39)}:
        return (
            "Malla_Curricular_Completa",
            calidad_url,
            True,
            "Malla curricular oficial completa verificada asignatura por asignatura.",
        )

    lim = "Núcleo troncal obligatorio transcrito (24–38 registros) con agrupación de optativas en bloque."
    if calidad_url == "Dominio_Institucional_Raiz":
        lim += " La URL registrada apunta al dominio raíz institucional."
    return ("Malla_Troncal_Sintetizada", calidad_url, True, lim)


def get_enriched_metadata(base_dir: Path) -> Dict[str, Dict[str, Any]]:
    """Construye el diccionario maestro de metadatos enriquecidos y auditados para D001-D075."""
    backup_dir = base_dir / "datos_originales_backup"
    meta_map: Dict[str, Dict[str, Any]] = {}

    for b in range(1, 6):
        f_json = backup_dir / f"bloque_0{b}_datos.json"
        if not f_json.exists():
            f_json = base_dir / f"bloque_0{b}_datos.json"
        rows = json.loads(f_json.read_text(encoding="utf-8"))
        for r in rows:
            doc_id = r["ID"]
            titulo = r.get("Titulo_Documento", "")
            inst = r.get("Institucion_Fuente", "")
            pais = r.get("Pais", "")
            anio_orig = str(r.get("Anio", "s. f."))
            anio_norm = ANIO_NORMALIZADO.get(doc_id, (anio_orig, ""))[0]
            tipo = r.get("Tipo_Fuente", "")
            url = r.get("URL", "")
            unidad_orig = r.get("Unidad_Peso", "competencias" if b == 1 else "créditos")
            total_peso = float(r.get("Total_Peso", r.get("Pt", 0) + r.get("Pa", 0)))

            gran, cal_url, comp_estricta, lim = evaluar_calidad_documental(
                doc_id, b, total_peso, url
            )
            inst_id = MAPA_INSTITUCION_UNICA.get(doc_id, f"INST_{doc_id}")
            prog_id = MAPA_PROGRAMA_UNICO.get(doc_id, f"PROG_{doc_id}")
            par_id = PARES_PERFIL_PLAN.get(doc_id, "")
            fam = clasificar_familia_programa(titulo)
            unidad_est = normalize_unit_system(doc_id, b, unidad_orig)

            # Extraer nombre limpio del programa académico
            prog_clean = titulo.split("—")[0].strip()

            meta_map[doc_id] = {
                "ID": doc_id,
                "Bloque": b,
                "Poblacion": "Perfiles_Egreso" if b == 1 else "Planes_Estudio",
                "Documento": titulo,
                "Programa_Academico": prog_clean,
                "Programa_ID": prog_id,
                "Institucion": inst,
                "Institucion_ID": inst_id,
                "Familia_Denominacion": fam,
                "Par_Perfil_Plan": par_id,
                "Pais": pais,
                "Anio": anio_norm,
                "Anio_Original": anio_orig,
                "Tipo_Fuente": tipo,
                "Granularidad_Curricular": gran,
                "Comparable_Estrictamente": comp_estricta,
                "Unidad_Original": unidad_orig,
                "Unidad_Estandarizada": unidad_est,
                "URL_Fuente": url,
                "Calidad_URL": cal_url,
                "Limitaciones_Evidencia": lim,
            }

    return meta_map

