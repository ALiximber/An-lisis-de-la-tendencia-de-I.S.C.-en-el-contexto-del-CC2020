"""Genera bloque_03_analisis.md a partir de bloque_03_datos.json y bloque_03_transcripcion.json."""
from pathlib import Path
import json

B = Path(__file__).resolve().parent
datos = json.loads((B / "bloque_03_datos.json").read_text(encoding="utf-8"))
trans = json.loads((B / "bloque_03_transcripcion.json").read_text(encoding="utf-8"))

L = [
    "# Corpus CC2020 — Bloque 3 de 5 (D031–D045)",
    "**Fecha de procesamiento:** 22 de octubre de 2026. **Objetivo total:** 75 documentos. **Este bloque:** D031–D045 (Planes de estudio oficiales ponderados por créditos u horas).",
    "",
    "## 1. Alcance y Metodología",
    "Este tercer bloque audita **15 planes de estudio oficiales** de programas de Ingeniería en Computación, Informática, Sistemas y Tecnologías Computacionales en América Latina (México, Perú, Chile, Argentina, Costa Rica, Ecuador, Honduras y Colombia).",
    "",
    "A diferencia del Bloque 1 (perfiles de egreso con pesos homogéneos), en este bloque cada asignatura se pondera con su carga académica real (créditos SATCA/SCT, créditos UEA, horas semanales o unidades valorativas).",
    "",
    "### Fórmulas del Protocolo CC2020",
    "- **Eje X (Teoría vs. Aplicación):** $X = 5.0 \\cdot \\frac{Pa - Pt}{Pa + Pt}$",
    "- **Eje Y (Hardware vs. Organización):** $Y = 5.0 \\cdot \\frac{Co - Ch}{Ch + Cs + Co}$",
    "- **Dispersión:** $\\Delta X = \\sqrt{\\max(0, 25 - X^2)}$, $\\Delta Y = \\sqrt{\\max(0, 25 \\cdot \\frac{Ch + Co}{Ch + Cs + Co} - Y^2)}$",
    "- **Radio de Dispersión:** $Radio = \\sqrt{\\Delta X^2 + \\Delta Y^2}$",
    "",
    "### Criterios de Codificación Auditable",
    "- **T (Teoría/Principios):** Ciencias básicas, física, matemática discreta, lógica, estructuras de datos y algoritmos, teoría de la computación, lenguajes formales y compiladores, sistemas inteligentes y arquitectura teórica de computadores.",
    "- **A (Aplicación/Despliegue):** Programación y desarrollo, ingeniería de software, bases de datos, sistemas operativos, redes y telecomunicaciones, seguridad informática, sistemas embebidos, robótica, gestión de proyectos y legislación.",
    "- **Ch (Hardware):** Circuitos, electrónica, física aplicada a hardware, diseño digital, microprocesadores y arquitectura de computadores.",
    "- **Cs (Software y Sistemas):** Algoritmia, programación, software, bases de datos, sistemas operativos, redes, inteligencia artificial y computación gráfica.",
    "- **Co (Organización y Sistemas de Información):** Gestión de proyectos, evaluación de TI, gobernanza, sistemas de información, economía, finanzas, procesos de negocio y factores humanos (HCI).",
    "- **Exclusiones:** Formación transversal (humanidades, idiomas, ética, deportes), asignaturas optativas/electivas sin programa curricular definido en la retícula base, prácticas profesionales y proyectos finales de grado/capstone.",
    "",
    "## 2. Tabla de Resultados — Componente 1 (12 Columnas)",
    "",
    "| ID | Titulo_Documento | Institucion_Fuente | Pais | Anio | Tipo_Fuente | Coordenada_X | Coordenada_Y | Desviacion_Radio | Proximidad_Disciplina_CC2020 | Resumen_Evidencia_X | Resumen_Evidencia_Y |",
    "|:---|:---|:---|:---|:---|:---|:---:|:---:|:---:|:---:|:---|:---|",
]

for r in datos:
    L.append(
        f"| **{r['ID']}** | [{r['Titulo_Documento']}]({r['URL']}) | {r['Institucion_Fuente']} | {r['Pais']} | {r['Anio']} | {r['Tipo_Fuente']} | "
        f"{r['Coordenada_X']:.2f} | {r['Coordenada_Y']:.2f} | {r['Desviacion_Radio']:.2f} | `{r['Proximidad_Disciplina_CC2020']}` | "
        f"{r['Resumen_Evidencia_X']} | {r['Resumen_Evidencia_Y']} |"
    )

L += [
    "",
    "## 3. Desglose Métrico de Carga Académica y Cobertura",
    "",
    "| ID | Institución | Total Materias | Peso Total | Pt (Teoría) | Pa (Aplic.) | Ch (Hardw.) | Cs (Softw.) | Co (Org.) | Cobertura X | Cobertura Y |",
    "|:---|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|",
]

for r in datos:
    t = r["Total_Peso"]
    cx = (r["Pt"] + r["Pa"]) / t
    cy = (r["Ch"] + r["Cs"] + r["Co"]) / t
    n_mat = len(trans.get(r["ID"], []))
    L.append(
        f"| **{r['ID']}** | {r['Institucion_Fuente']} | {n_mat} | {t:g} {r['Unidad_Peso']} | "
        f"{r['Pt']:g} | {r['Pa']:g} | {r['Ch']:g} | {r['Cs']:g} | {r['Co']:g} | {cx:.1%} | {cy:.1%} |"
    )

L += [
    "",
    "## 4. Diagrama de Dispersión CC2020",
    "",
    "![Dispersión del bloque 3](bloque_03_dispersion.png)",
    "",
    "## 5. Análisis e Interpretación de Resultados por Documento",
    "",
]

descripciones = {
    "D031": "Enfocado en fundamentos de ingeniería clásica (física, matemáticas, circuitos) y sistemas digitales con sólida base de hardware, situándolo cerca de Computer Engineering (CE).",
    "D032": "Fuerte orientación al despliegue en organizaciones, sistemas de información empresarial y gestión tecnológica, clasificándolo con proximidad a Information Systems (IS).",
    "D033": "Marcado énfasis teórico-formal en ciencias de la computación, algoritmos, métodos cuantitativos y modelos matemáticos (Computer Science - CS).",
    "D034": "Plan nacional con equilibrio entre desarrollo de software, redes y fundamentos físicos, ubicándose en la zona central con afinidad Computer Science (CS).",
    "D035": "Alta carga de electrónica, sistemas digitales, microprocesadores y arquitectura de computadoras en interacción con software de bajo nivel (Computer Engineering - CE).",
    "D036": "Estructura formativa balanceada en ciencias de la computación, estructuras discretas, programación y sistemas (Computer Science - CS).",
    "D037": "Énfasis notable en desarrollo de software aplicado, metodologías ágiles, bases de datos y arquitectura de aplicaciones (Software Engineering - SE).",
    "D038": "Perfil equilibrado con predominio de ingeniería de software, desarrollo aplicado y bases de datos (Software Engineering - SE).",
    "D039": "Fuerte núcleo algorítmico, teoría de la computación, estructuras y sistemas (Computer Science - CS).",
    "D040": "Enfoque integrado entre ciencias computacionales, algoritmos, infraestructura y proyectos de software (Computer Science - CS).",
    "D041": "Plan riguroso con base formal en algoritmos, sistemas operativos, redes y compiladores (Computer Science - CS).",
    "D042": "Tradición de ingeniería civil matemática con alta concentración en fundamentos de ciencias computacionales y algoritmos (Computer Science - CS).",
    "D043": "Fuerte presencia de electrónica analógica/digital, electromagnetismo, señales y circuitos (Computer Engineering - CE).",
    "D044": "Orientación equilibrada de ingeniería en computación cubriendo algoritmos, arquitectura y software (Computer Science - CS).",
    "D045": "Modelo de retos Tec21 con fuerte base de ciencias fundamentales, algoritmia y modelación matemática computacional (Computer Science - CS).",
}

for r in datos:
    doc = r["ID"]
    L.append(f"### {doc} — {r['Institucion_Fuente']} ({r['Pais']})")
    L.append(f"- **Título del Programa:** {r['Titulo_Documento']}")
    L.append(f"- **Tipo de Fuente y Año:** {r['Tipo_Fuente']} ({r['Anio']})")
    L.append(f"- **URL Oficial:** [{r['URL']}]({r['URL']})")
    L.append(f"- **Coordenadas:** X = {r['Coordenada_X']:.2f}, Y = {r['Coordenada_Y']:.2f} | **Radio:** {r['Desviacion_Radio']:.2f} | **Afinidad:** `{r['Proximidad_Disciplina_CC2020']}`")
    L.append(f"- **Diagnóstico Curricular:** {descripciones[doc]}")
    L.append("")

L += [
    "## 6. Advertencias y Limitaciones Metodológicas",
    "1. **Auditabilidad y Reglas:** Las coordenadas son el resultado de un conjunto explícito y público de expresiones regulares aplicadas a las asignaturas del plan. Modificaciones razonables en las reglas pueden desplazar los puntos.",
    "2. **Afinidad Disciplinar Provisional:** Las categorías (CS, CE, SE, IT, IS) responden a umbrales de composición relativa de áreas ($Ch, Cs, Co, Pt, Pa$) y no constituyen certificaciones oficiales de ACM/IEEE CC2020.",
    "3. **Interpretación del Radio:** El radio describe la dispersión interna entre componentes curriculares polares en el espacio conceptual, no un error de muestreo ni intervalo de confianza estadística.",
    "4. **Heterogeneidad de Métricas de Peso:** Mientras instituciones como UBA, UNLP y UNLPam reportan horas reloj, otras como UNAM, TecNM, PUCP y UniAndes reportan créditos académicos. El análisis compara las proporciones normalizadas internas de cada programa.",
]

(B / "bloque_03_analisis.md").write_text("\n".join(L), encoding="utf-8")
print("bloque_03_analisis.md generado exitosamente.")
