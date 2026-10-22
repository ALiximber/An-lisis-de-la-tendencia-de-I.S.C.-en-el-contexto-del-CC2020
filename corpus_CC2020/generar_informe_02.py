"""Genera bloque_02_analisis.md a partir de bloque_02_datos.json (sin transcribir cifras a mano)."""
from pathlib import Path
import json

B = Path(__file__).resolve().parent
d = json.loads((B / "bloque_02_datos.json").read_text(encoding="utf-8"))
L = ["# Bloque 2/5: D016–D030", "",
     "Coordenadas calculadas con las fórmulas del protocolo "
     "(X = 5·(Pa−Pt)/(Pa+Pt); Y = 5·(Co−Ch)/(Ch+Cs+Co)). Pesos en créditos, unidades valorativas u horas según la fuente.",
     "Las reglas de clasificación están en `calcular_bloque_02.py`; la clasificación materia por materia, "
     "en `bloque_02_clasificacion.csv`.", "",
     "| ID | Institución | País | Año | X | Y | Radio | Afin. | Pt / Pa | Ch / Cs / Co | Cobertura X / Y |",
     "|---|---|---|---|---|---|---|---|---|---|---|"]
for r in d:
    t = r["Total_Peso"]
    cx = (r["Pt"] + r["Pa"]) / t
    cy = (r["Ch"] + r["Cs"] + r["Co"]) / t
    L.append(f"| {r['ID']} | [{r['Institucion_Fuente']}]({r['URL']}) | {r['Pais']} | {r['Anio']} | "
             f"{r['Coordenada_X']:.2f} | {r['Coordenada_Y']:.2f} | {r['Desviacion_Radio']:.2f} | "
             f"{r['Proximidad_Disciplina_CC2020']} | {r['Pt']:g} / {r['Pa']:g} | "
             f"{r['Ch']:g} / {r['Cs']:g} / {r['Co']:g} | {cx:.0%} / {cy:.0%} |")
L += ["", "## Criterios de codificación", "",
      "- **T (teoría/principios):** ciencias básicas, matemática discreta, algoritmos y estructuras de datos, "
      "teoría de la computación, lenguajes y compiladores, IA/aprendizaje, circuitos y arquitectura de computadores.",
      "- **A (aplicación/despliegue):** programación, desarrollo, bases de datos, sistemas operativos, redes, "
      "seguridad, sistemas digitales y embebidos, gestión, economía y legislación.",
      "- **Ch / Cs / Co:** hardware y bajo nivel / software, datos, redes y sistemas / gestión de TI, sistemas de "
      "información, negocio y factores humanos. Las ciencias básicas puntúan en X pero no en Y.",
      "- **Excluidos (peso registrado como no clasificado):** optativas y electivas sin contenido, idiomas, "
      "humanidades, comunicación, ética, emprendimiento, prácticas, trabajos de grado y materias introductorias genéricas.",
      "", "## Advertencias", "",
      "- Las coordenadas dependen de las reglas de codificación; un cambio razonable en ellas puede mover los puntos. "
      "No son mediciones oficiales de CC2020.",
      "- La afinidad (CS/CE/SE/IT/IS) es provisional: sale de umbrales fijados en `afinidad()`, no de centroides oficiales.",
      "- El radio usa la fórmula del bloque 1 y mide dispersión entre categorías, no un intervalo de confianza.",
      "- Los años entre paréntesis salen de la URL o de la fecha de impresión del PDF; los \"s. f.\" no se verificaron.",
      "- Los nombres de programa de varias fuentes se infirieron de la URL o del documento; conviene verificarlos.",
      "- Coberturas bajas (p. ej. D024 en X, D029 en Y) indican mucha formación transversal o electivas: "
      "esas coordenadas representan una parte menor del plan.",
      "- D025–D027 usan horas; D022, D030 y el resto, créditos o unidades por asignatura. "
      "Sólo se comparan proporciones dentro de cada plan.",
      "", "![Dispersión del bloque 2](bloque_02_dispersion.png)"]
(B / "bloque_02_analisis.md").write_text("\n".join(L), encoding="utf-8")
print("bloque_02_analisis.md generado")
