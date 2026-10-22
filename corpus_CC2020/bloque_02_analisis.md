# Bloque 2/5: D016–D030

Coordenadas calculadas con las fórmulas del protocolo (X = 5·(Pa−Pt)/(Pa+Pt); Y = 5·(Co−Ch)/(Ch+Cs+Co)). Pesos en créditos, unidades valorativas u horas según la fuente.
Las reglas de clasificación están en `calcular_bloque_02.py`; la clasificación materia por materia, en `bloque_02_clasificacion.csv`.

| ID | Institución | País | Año | X | Y | Radio | Afin. | Pt / Pa | Ch / Cs / Co | Cobertura X / Y |
|---|---|---|---|---|---|---|---|---|---|---|
| D016 | [Universidad de las Américas Puebla (UDLAP)](https://www.udlap.mx/ofertaacademica/SistemasComputacionales/PlanEstudios) | México | s. f. | 0.22 | -0.06 | 5.58 | IT | 98 / 107 | 20 / 116 / 18 | 68% / 51% |
| D017 | [IPN — ESCOM](https://www.escom.ipn.mx/docs/oferta/mapaCurricularISC2020.pdf) | México | 2020 | -0.35 | -0.51 | 5.91 | CE | 162 / 141 | 60 / 138 / 36 | 78% / 60% |
| D018 | [Universidad Autónoma de Baja California (Mexicali)](https://ingenieria.mxl.uabc.mx/pe_lsc/wp-content/uploads/2024/04/plan2023-2_lsc.pdf) | México | 2023 | 2.57 | 1.35 | 4.99 | IS | 60 / 187 | 7 / 146 / 66 | 71% / 63% |
| D019 | [Universidad Privada del Norte (UPN)](https://www.upn.edu.pe/sites/default/files/2021-07/pe-ingenieria-sistemas-computacionales.pdf) | Perú | 2021 | 0.23 | 0.00 | 5.56 | SE | 61 / 67 | 11 / 70 / 11 | 64% / 46% |
| D020 | [Universidad Nacional de Colombia (Bogotá)](https://ingenieria.bogota.unal.edu.co/images/recursos/pregrado/ingenieriaSistemas/Malla_Plan_de_estudios_flexible_2023.pdf) | Colombia | 2023 | -0.33 | 0.44 | 5.60 | SE | 64.5 / 56.5 | 7.5 / 62.5 / 15 | 72% / 51% |
| D021 | [Pontificia Universidad Javeriana Cali](https://www.javerianacali.edu.co/media/94/download) | Colombia | s. f. | -0.66 | 0.19 | 5.42 | CS | 56 / 43 | 6 / 62 / 9 | 58% / 45% |
| D022 | [Universidad de Sonsonate](https://admin.usonsonate.edu.sv/uploads/pensums_todos_ff4ca0fa71.pdf) | El Salvador | s. f. | 0.88 | 0.35 | 5.73 | SE | 66 / 94 | 16 / 74 / 24 | 88% / 63% |
| D023 | [Universidad Nacional del Callao (FIIS)](https://fiis.unac.edu.pe/wp-content/uploads/2024/06/Imprimir-Plan-Academico-13-06-2024-10_33_18.pdf) | Perú | 2023 | 1.27 | 1.50 | 5.87 | IS | 59 / 99 | 14 / 56 / 50 | 71% / 54% |
| D024 | [Universidad Nacional Abierta y a Distancia (UNAD)](https://estudios.unad.edu.co/images/2025/mallas-pdf/Plan-de-estudios-Ingenieria-de-sistemas.pdf) | Colombia | 2025 | 1.17 | 1.02 | 5.48 | SE | 31 / 50 | 3 / 45 / 16 | 54% / 43% |
| D025 | [UTN — Facultad Regional Buenos Aires](https://frba.utn.edu.ar/sistemas/plan-de-estudios-2023/) | Argentina | 2023 | -0.08 | 1.48 | 5.85 | IS | 1536 / 1488 | 168 / 1152 / 792 | 76% / 53% |
| D026 | [Universidad Nacional de La Pampa (UNLPam)](https://www.ing.unlpam.edu.ar/planestudio?pk=11&pl=22) | Argentina | 2023 | 0.91 | 0.63 | 5.38 | IT | 1316 / 1904 | 96 / 1920 / 400 | 84% / 63% |
| D027 | [UNICEN — Facultad de Ciencias Exactas](https://exa.unicen.edu.ar/sistemas/) | Argentina | 2023 | 0.03 | -0.07 | 5.41 | CS | 1440 / 1455 | 210 / 1875 / 180 | 80% / 63% |
| D028 | [Universidad de los Llanos (Unillanos)](https://eis.unillanos.edu.co/fcbi/is/) | Colombia | 2018 | -0.75 | -0.08 | 5.77 | SE | 65 / 48 | 12 / 42 / 11 | 68% / 39% |
| D029 | [Universidad EAN](https://universidadean.edu.co/sites/default/files/oferta-academica/planes-de-estudio/carrera-en-ingenieria-de-sistemas-presencial.pdf) | Colombia | s. f. | -0.88 | 1.20 | 5.55 | IT | 53.5 / 37.5 | 2 / 34 / 14 | 63% / 35% |
| D030 | [UNIR México](https://mexico.unir.net/ingenieria/licenciatura-ingenieria-sistemas-computacionales/) | México | s. f. | 1.29 | 0.47 | 5.35 | IT | 117 / 198 | 18 / 225 / 45 | 97% / 89% |

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