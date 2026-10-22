# Bloque 2/5: D016–D030

Coordenadas calculadas con las fórmulas del protocolo (X = 5·(Pa−Pt)/(Pa+Pt); Y = 5·(Co−Ch)/(Ch+Cs+Co)). Pesos en créditos, unidades valorativas u horas según la fuente.
Las reglas de clasificación están en `calcular_bloque_02.py`; la clasificación materia por materia, en `bloque_02_clasificacion.csv`.

| ID | Institución | País | Año | X | Y | Radio | Afin. | Pt / Pa | Ch / Cs / Co | Cobertura X / Y |
|---|---|---|---|---|---|---|---|---|---|---|
| D016 | [Universidad de las Américas Puebla (UDLAP)](https://www.udlap.mx/ofertaacademica/SistemasComputacionales/PlanEstudios) | México | s. f. | 0.37 | -0.06 | 5.57 | CS | 95 / 110 | 20 / 116 / 18 | 68% / 51% |
| D017 | [IPN — ESCOM](https://www.escom.ipn.mx/docs/oferta/mapaCurricularISC2020.pdf) | México | 2020 | -0.35 | -0.51 | 5.91 | CE | 162 / 141 | 60 / 138 / 36 | 78% / 60% |
| D018 | [Universidad Autónoma de Baja California (Mexicali)](https://ingenieria.mxl.uabc.mx/pe_lsc/wp-content/uploads/2024/04/plan2023-2_lsc.pdf) | México | 2023 | 2.53 | 1.28 | 5.00 | SE | 60 / 183 | 7 / 146 / 62 | 69% / 61% |
| D019 | [Universidad Privada del Norte (UPN)](https://www.upn.edu.pe/sites/default/files/2021-07/pe-ingenieria-sistemas-computacionales.pdf) | Perú | 2021 (fecha en la URL) | -0.08 | 0.00 | 5.57 | CS | 65 / 63 | 11 / 70 / 11 | 64% / 46% |
| D020 | [Universidad Nacional de Colombia (Bogotá)](https://ingenieria.bogota.unal.edu.co/images/recursos/pregrado/ingenieriaSistemas/Malla_Plan_de_estudios_flexible_2023.pdf) | Colombia | 2023 | -0.70 | 0.55 | 5.53 | CS | 69 / 52 | 6 / 61 / 15 | 72% / 49% |
| D021 | [Pontificia Universidad Javeriana Cali](https://www.javerianacali.edu.co/media/94/download) | Colombia | s. f. | -0.96 | 0.20 | 5.39 | CS | 59 / 40 | 6 / 59 / 9 | 58% / 44% |
| D022 | [Universidad de Sonsonate](https://admin.usonsonate.edu.sv/uploads/pensums_todos_ff4ca0fa71.pdf) | El Salvador | s. f. | 0.80 | 0.23 | 5.71 | SE | 66 / 91 | 16 / 74 / 21 | 87% / 61% |
| D023 | [Universidad Nacional del Callao (FIIS)](https://fiis.unac.edu.pe/wp-content/uploads/2024/06/Imprimir-Plan-Academico-13-06-2024-10_33_18.pdf) | Perú | 2024 (fecha de impresión) | 1.60 | 1.53 | 5.70 | IS | 65 / 126 | 14 / 74 / 59 | 85% / 66% |
| D024 | [Universidad Nacional Abierta y a Distancia (UNAD)](https://estudios.unad.edu.co/images/2025/mallas-pdf/Plan-de-estudios-Ingenieria-de-sistemas.pdf) | Colombia | 2025 (ruta de la URL) | 0.87 | 0.64 | 5.45 | SE | 31 / 44 | 3 / 42 / 10 | 50% / 37% |
| D025 | [UTN — Facultad Regional Buenos Aires](https://frba.utn.edu.ar/sistemas/plan-de-estudios-2023/) | Argentina | 2023 | -0.08 | 1.48 | 5.85 | IS | 1536 / 1488 | 168 / 1152 / 792 | 76% / 53% |
| D026 | [Universidad Nacional de La Pampa (UNLPam)](https://www.ing.unlpam.edu.ar/planestudio?pk=11&pl=22) | Argentina | 2023 | 0.91 | 0.63 | 5.38 | SE | 1316 / 1904 | 96 / 1920 / 400 | 84% / 63% |
| D027 | [UNICEN — Facultad de Ciencias Exactas](https://exa.unicen.edu.ar/sistemas/) | Argentina | 2023 | 0.03 | -0.07 | 5.41 | CS | 1440 / 1455 | 210 / 1875 / 180 | 80% / 63% |
| D028 | [Universidad de los Llanos (Unillanos)](https://eis.unillanos.edu.co/fcbi/is/) | Colombia | 2018 | -0.77 | -0.08 | 5.79 | CS | 64 / 47 | 12 / 40 / 11 | 67% / 38% |
| D029 | [Universidad EAN](https://universidadean.edu.co/sites/default/files/oferta-academica/planes-de-estudio/carrera-en-ingenieria-de-sistemas-presencial.pdf) | Colombia | s. f. | -1.51 | 0.26 | 5.39 | CS | 54 / 29 | 4 / 29 / 6 | 58% / 27% |
| D030 | [UNIR México](https://mexico.unir.net/ingenieria/licenciatura-ingenieria-sistemas-computacionales/) | México | s. f. | 1.57 | 0.47 | 5.27 | SE | 108 / 207 | 18 / 225 / 45 | 97% / 89% |

## Criterios de codificación

- **T (teoría/principios):** ciencias básicas, matemática discreta, algoritmos y estructuras de datos, teoría de la computación, lenguajes y compiladores, IA/aprendizaje, circuitos y arquitectura de computadores.
- **A (aplicación/despliegue):** programación, desarrollo, bases de datos, sistemas operativos, redes, seguridad, sistemas digitales y embebidos, gestión, economía y legislación.
- **Ch / Cs / Co:** hardware y bajo nivel / software, datos, redes y sistemas / gestión de TI, sistemas de información, negocio y factores humanos. Las ciencias básicas puntúan en X pero no en Y.
- **Excluidos (peso registrado como no clasificado):** optativas y electivas sin contenido, idiomas, humanidades, comunicación, ética, emprendimiento, prácticas, trabajos de grado y materias introductorias genéricas.

## Advertencias

- Las coordenadas dependen de las reglas de codificación; un cambio razonable en ellas puede mover los puntos. No son mediciones oficiales de CC2020.
- La afinidad (CS/CE/SE/IT/IS) es provisional: sale de umbrales fijados en `afinidad()`, no de centroides oficiales.
- El radio usa la fórmula del bloque 1 y mide dispersión entre categorías, no un intervalo de confianza.
- Los años entre paréntesis salen de la URL o de la fecha de impresión del PDF; los "s. f." no se verificaron.
- Los nombres de programa de varias fuentes se infirieron de la URL o del documento; conviene verificarlos.
- Coberturas bajas (p. ej. D024 en X, D029 en Y) indican mucha formación transversal o electivas: esas coordenadas representan una parte menor del plan.
- D025–D027 usan horas; D022, D030 y el resto, créditos o unidades por asignatura. Sólo se comparan proporciones dentro de cada plan.

![Dispersión del bloque 2](bloque_02_dispersion.png)