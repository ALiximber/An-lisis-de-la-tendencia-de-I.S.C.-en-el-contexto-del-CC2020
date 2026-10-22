"""Genera bloque_04_analisis.md a partir de bloque_04_datos.json y bloque_04_transcripcion.json."""
from pathlib import Path
import json

B = Path(__file__).resolve().parent
datos = json.loads((B / "bloque_04_datos.json").read_text(encoding="utf-8"))
trans = json.loads((B / "bloque_04_transcripcion.json").read_text(encoding="utf-8"))

L = [
    "# Corpus CC2020 — Bloque 4 de 5 (D046–D060)",
    "**Fecha de procesamiento:** 22 de octubre de 2026. **Objetivo total:** 75 documentos. **Este bloque:** D046–D060 (Planes de estudio oficiales ponderados por créditos u horas).",
    "",
    "## 1. Alcance y Metodología",
    "Este cuarto bloque audita **15 planes de estudio oficiales** de carreras de Computación, Informática y Sistemas representativas de 11 países de América Latina: Uruguay (UdelaR), Perú (UNSA, UNMSM), Chile (UdeC, USM), Colombia (UIS, Univalle), México (UANL, UASLP), Paraguay (UNA), Panamá (UTP), Guatemala (USAC), Argentina (UNR), Ecuador (PUCE) y Bolivia (UMSA).",
    "",
    "Al igual que en los bloques 2 y 3, cada materia se pondera con su valor formal en créditos académicos (SCT, SATCA, créditos de facultad) o carga horaria cuatrimestral/semanal, garantizando auditabilidad estricta y reproducibilidad algorítmica sin asignación manual de coordenadas.",
    "",
    "### Fórmulas del Protocolo CC2020",
    "- **Eje X (Teoría vs. Aplicación):** $X = 5.0 \\cdot \\frac{Pa - Pt}{Pa + Pt}$",
    "- **Eje Y (Hardware vs. Organización):** $Y = 5.0 \\cdot \\frac{Co - Ch}{Ch + Cs + Co}$",
    "- **Dispersión:** $\\Delta X = \\sqrt{\\max(0, 25 - X^2)}$, $\\Delta Y = \\sqrt{\\max(0, 25 \\cdot \\frac{Ch + Co}{Ch + Cs + Co} - Y^2)}$",
    "- **Radio de Dispersión:** $Radio = \\sqrt{\\Delta X^2 + \\Delta Y^2}$",
    "",
    "### Criterios de Codificación Auditable",
    "- **T (Teoría/Principios):** Ciencias básicas (cálculo, álgebra, física, química), matemática discreta, lógica formal, algoritmia y estructuras de datos, lenguajes formales y computabilidad, teoría de compiladores, inteligencia artificial y arquitecturas teóricas.",
    "- **A (Aplicación/Despliegue):** Programación y metodologías de desarrollo, ingeniería de software, bases de datos y administración de datos, sistemas operativos, redes y telecomunicaciones, ciberseguridad, diseño digital, desarrollo web/móvil y gestión de TI.",
    "- **Ch (Hardware):** Circuitos, electrónica, física aplicada, diseño digital, microprocesadores y arquitectura de computadores.",
    "- **Cs (Software y Sistemas):** Algoritmia, lenguajes de programación, software, bases de datos, sistemas operativos, redes, inteligencia artificial y computación científica.",
    "- **Co (Organización y Sistemas de Información):** Gestión de proyectos, evaluación de TI, gobernanza, sistemas de información empresarial, dinámica de sistemas, economía, finanzas y factores humanos (experiencia de usuario / HCI).",
    "- **Exclusiones:** Formación general y transversal (humanidades, idiomas, ética, deportes), asignaturas optativas/electivas sin catálogo de retícula fija, prácticas profesionales/pasantías y trabajos terminales de graduación / tesis.",
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
    "![Dispersión del bloque 4](bloque_04_dispersion.png)",
    "",
    "## 5. Análisis e Interpretación de Resultados por Documento",
    "",
]

descripciones = {
    "D046": "Sólida formación en fundamentos matemáticos y computación teórica con balance equilibrado en desarrollo de software y sistemas (Computer Science - CS).",
    "D047": "Plan bajo lineamientos ABET con un fuerte sesgo hacia ingeniería de software, arquitectura empresarial y gestión tecnológica de proyectos (Software Engineering - SE).",
    "D048": "Formación rigurosa en ciencias de la ingeniería con balance entre algoritmia formal, sistemas computacionales y desarrollo de software (Computer Science - CS).",
    "D049": "Estructura curricular de 10 semestres con amplio núcleo de ciencias duras y sistemas, equilibrando desarrollo e infraestructura (Computer Science - CS).",
    "D050": "Plan de ingeniería enfocado en desarrollo sistemático de software, con fuerte soporte en física y matemáticas para ingeniería (Computer Science - CS).",
    "D051": "Plan tradicional con sólida base en matemáticas discretas, algoritmia avanzada, arquitectura y redes (Computer Science - CS).",
    "D052": "Programa equilibrado de ingeniería de sistemas con integración de algoritmia, bases de datos y ciencias de la ingeniería (Computer Science - CS).",
    "D053": "Énfasis notable en ciencias de la computación, organización de lenguajes, compiladores y sistemas operativos (Computer Science - CS).",
    "D054": "Fuerte presencia de teoría de sistemas, modelado dinámico, gestión de procesos de negocio e ingeniería de software (Computer Science - CS).",
    "D055": "Orientación contemporánea en desarrollo interactivo, algoritmos y sistemas organizacionales (Computer Science - CS).",
    "D056": "Licenciatura formal orientada puramente a ciencias de la computación, teoría de autómatas, compiladores y semántica formal (Computer Science - CS).",
    "D057": "Plan de tradición científica con alta concentración en optimización, ciencias de datos y sistemas distribuidos (Computer Science - CS).",
    "D058": "Alta carga de circuitos eléctricos, electrónica semiconductora, diseño digital y señales acopladas a computación (Computer Engineering - CE).",
    "D059": "Enfoque pragmático en infraestructura de redes, plataformas de software y tecnologías aplicadas (Software Engineering - SE).",
    "D060": "Currículo clásico de ciencias de la computación e informática pura con base analítica y desarrollo de software (Computer Science - CS).",
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
    "1. **Reglas Explícitas:** Las clasificaciones se derivan de expresiones regulares preestablecidas y auditables aplicadas al nombre de cada asignatura; ninguna coordenada es asignada por estimación manual.",
    "2. **Afinidad Provisional:** Las etiquetas disciplinarias (CS, CE, SE, IT, IS) responden a proporciones de carga académica y umbrales operacionales del script, no a acreditaciones gremiales oficiales de CC2020.",
    "3. **Heterogeneidad de Métricas:** Se utilizan las unidades formales del plan publicado (créditos SCT, SATCA, créditos de facultad u horas cátedra); los análisis calculan proporciones relativas internas normalizadas.",
    "4. **Significado de la Dispersión:** El radio modela la polarización interna del plan respecto a los extremos teóricos/aplicados y hardware/organización, sin constituir un intervalo de error estadístico.",
]

(B / "bloque_04_analisis.md").write_text("\n".join(L), encoding="utf-8")
print("bloque_04_analisis.md generado exitosamente.")
