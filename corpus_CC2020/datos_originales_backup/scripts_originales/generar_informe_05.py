"""Genera bloque_05_analisis.md a partir de bloque_05_datos.json y bloque_05_transcripcion.json."""
from pathlib import Path
import json

B = Path(__file__).resolve().parent
datos = json.loads((B / "bloque_05_datos.json").read_text(encoding="utf-8"))
trans = json.loads((B / "bloque_05_transcripcion.json").read_text(encoding="utf-8"))

L = [
    "# Corpus CC2020 — Bloque 5 de 5 (D061–D075)",
    "**Fecha de procesamiento:** 22 de octubre de 2026. **Objetivo total:** 75 documentos. **Este bloque:** D061–D075 (Planes de estudio oficiales ponderados por créditos u horas).",
    "",
    "## 1. Alcance y Metodología",
    "Este quinto y último bloque audita **15 planes de estudio oficiales** de carreras de Computación, Informática, Sistemas y Software representativas de América Latina: Brasil (USP, UNICAMP), Colombia (UdeA, Uninorte), Argentina (UNC FAMAF, UNS), Perú (UNSAAC, UNT), Costa Rica (TEC, UCR Empresarial), Ecuador (EPN), Bolivia (UCB), Chile (UACh) y México (UV, UADY).",
    "",
    "Con la entrega de este bloque se completa el corpus total de **75 documentos oficiales** (D001–D075) analizados bajo el marco internacional ACM/IEEE CC2020 con una metodología estricta, auditable y basada en reglas algorítmicas de extracción.",
    "",
    "### Fórmulas del Protocolo CC2020",
    "- **Eje X (Teoría vs. Aplicación):** $X = 5.0 \\cdot \\frac{Pa - Pt}{Pa + Pt}$",
    "- **Eje Y (Hardware vs. Organización):** $Y = 5.0 \\cdot \\frac{Co - Ch}{Ch + Cs + Co}$",
    "- **Dispersión:** $\\Delta X = \\sqrt{\\max(0, 25 - X^2)}$, $\\Delta Y = \\sqrt{\\max(0, 25 \\cdot \\frac{Ch + Co}{Ch + Cs + Co} - Y^2)}$",
    "- **Radio de Dispersión:** $Radio = \\sqrt{\\Delta X^2 + \\Delta Y^2}$",
    "",
    "### Criterios de Codificación Auditable",
    "- **T (Teoría/Principios):** Ciencias básicas (cálculo, álgebra, geometría, física), matemática discreta, lógica formal, algoritmia y complejidad, teoría de la computación, lenguajes formales y autómatas, compiladores, inteligencia artificial y arquitectura teórica.",
    "- **A (Aplicación/Despliegue):** Programación y metodologías de desarrollo, ingeniería de software, arquitectura de software, bases de datos y bancos de dados, sistemas operativos, redes y telecomunicaciones, ciberseguridad, diseño digital, desarrollo web/móvil y sistemas embebidos/embarcados.",
    "- **Ch (Hardware):** Circuitos eléctricos y lógicos, electrónica básica, diseño digital, microprocesadores, arquitectura y organización de computadores.",
    "- **Cs (Software y Sistemas):** Algoritmia, lenguajes de programación, ingeniería de software, bases de datos, sistemas operativos, redes, inteligencia artificial y computación gráfica.",
    "- **Co (Organización y Sistemas de Información):** Gestión de proyectos, gobernanza de TI, sistemas de información empresarial, dinámica de sistemas, administración, contabilidad, economía y factores humanos (experiencia de usuario / HCI).",
    "- **Exclusiones:** Formación transversal (humanidades, idiomas, ética, deportes), electivas/optativas sin catálogo cerrado, pasantías profesionales y proyectos finales de grado / tesis.",
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
    "![Dispersión del bloque 5](bloque_05_dispersion.png)",
    "",
    "## 5. Análisis e Interpretación de Resultados por Documento",
    "",
]

descripciones = {
    "D061": "Programa emblemático de ciencias de la computación con un perfil teórico muy sólido en análisis de algoritmos, teoría de grafos y matemáticas (Computer Science - CS).",
    "D062": "Ingeniería híbrida de hardware y software con alta carga de circuitos eléctricos, electrónica y microprocesadores (Computer Engineering - CE).",
    "D063": "Fuerte orientación científica en modelación matemática, física y algoritmos articulados con ingeniería de software (Computer Science - CS).",
    "D064": "Plan de tradición matemática y computacional pura con énfasis en lógica, computabilidad y lenguajes formales (Computer Science - CS).",
    "D065": "Plan equilibrado de ingeniería de sistemas con integración de algoritmia, bases de datos y gestión de TI (Computer Science - CS).",
    "D066": "Formación tecnológica balanceada con sólida base en estructuras de datos, sistemas operativos y redes (Computer Science - CS).",
    "D067": "Plan riguroso enfocado en matemáticas computacionales, computación distribuida y ciencia de datos (Computer Science - CS).",
    "D068": "Currículo integral cubriendo desarrollo de software, modelado de sistemas y seguridad informática (Computer Science - CS).",
    "D069": "Programa acreditado ABET con balance entre algoritmia, ingeniería de software y ciencias básicas (Computer Science - CS).",
    "D070": "Plan de ingeniería de sistemas computacionales con énfasis balanceado en programación, redes y sistemas operativos (Computer Science - CS).",
    "D071": "Licenciatura orientada a ciencias de la computación formal, lenguajes, teoría de complejidad y sistemas (Computer Science - CS).",
    "D072": "Ingeniería civil informática con énfasis en algoritmia, sistemas distribuidos y gestión tecnológica (Computer Science - CS).",
    "D073": "Plan especializado en ingeniería de software, arquitectura, calidad, construcción y dirección de proyectos (Software Engineering - SE).",
    "D074": "Programa formativo estructurado con equilibrio en desarrollo de software, análisis de sistemas y redes (Computer Science - CS).",
    "D075": "Perfil orientado a la integración tecnológica en organizaciones, gestión empresarial, auditoría e inteligencia de negocios (Information Systems - IS).",
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
    "## 6. Síntesis y Conclusiones del Corpus Total (D001–D075)",
    "Con la culminación del Bloque 5, se alcanza la meta global de **75 documentos analizados**:",
    "- **Bloque 1 (D001–D015):** 15 perfiles de egreso institucionales con codificación unitaria/fraccionaria por atributo.",
    "- **Bloque 2 (D016–D030):** 15 planes de estudio oficiales ponderados por créditos u horas en México, Colombia, Perú, Argentina y El Salvador.",
    "- **Bloque 3 (D031–D045):** 15 planes de estudio de universidades insignia (UNAM, PUCP, UChile, TecNM, UNLP, UCR, UTPL, UNAH, UniAndes, EAFIT, UBA, PUC Chile, UAM, UdeG, ITESM).",
    "- **Bloque 4 (D046–D060):** 15 planes de estudio con alta representatividad regional (UdelaR, UNSA, UdeC, UIS, UANL, UNA, UTP, USAC, UNMSM, Univalle, UNR, USM, UASLP, PUCE, UMSA).",
    "- **Bloque 5 (D061–D075):** 15 planes de estudio complementarios de universidades de alta calidad (USP, UNICAMP, UdeA, UNC FAMAF, UNSAAC, TEC, EPN, UCB, Uninorte, UV, UNS, UACh, UADY, UNT, UCR Empresarial).",
    "",
    "### Tendencias Curriculares Observadas",
    "1. **Predominio del Cuadrante Central-Teórico (CS):** La gran mayoría de ingenierías en computación y sistemas en Latinoamérica conservan un núcleo muy fuerte de ciencias básicas (cálculo diferencial/integral/vectorial, álgebra lineal, física mecánica y electromagnetismo), lo que desplaza el centroide general hacia valores negativos de X (Theory/Principles).",
    "2. **Divergencias en el Eje Y:** Programas con la denominación *Ingeniería en Computación* (UNAM, UAM, UNLP, UASLP, UNICAMP) presentan un sesgo hacia hardware (CE), mientras que carreras como *Ingeniería de Software* (UADY, UTPL) o *Informática Empresarial* (PUCP, UCR) se desplazan hacia el cuadrante superior derecho (SE e IS).",
    "3. **Transparencia Metodológica:** Ninguna coordenada fue introducida manualmente. Todos los resultados derivan de expresiones regulares públicas y scripts ejecutables que garantizan la reproducibilidad matemática de la auditoría.",
]

(B / "bloque_05_analisis.md").write_text("\n".join(L), encoding="utf-8")
print("bloque_05_analisis.md generado exitosamente.")
