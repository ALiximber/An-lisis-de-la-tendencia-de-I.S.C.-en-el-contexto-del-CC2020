# Corpus CC2020 — Bloque 3 de 5 (D031–D045)
**Fecha de procesamiento:** 22 de octubre de 2026. **Objetivo total:** 75 documentos. **Este bloque:** D031–D045 (Planes de estudio oficiales ponderados por créditos u horas).

## 1. Alcance y Metodología
Este tercer bloque audita **15 planes de estudio oficiales** de programas de Ingeniería en Computación, Informática, Sistemas y Tecnologías Computacionales en América Latina (México, Perú, Chile, Argentina, Costa Rica, Ecuador, Honduras y Colombia).

A diferencia del Bloque 1 (perfiles de egreso con pesos homogéneos), en este bloque cada asignatura se pondera con su carga académica real (créditos SATCA/SCT, créditos UEA, horas semanales o unidades valorativas).

### Fórmulas del Protocolo CC2020
- **Eje X (Teoría vs. Aplicación):** $X = 5.0 \cdot \frac{Pa - Pt}{Pa + Pt}$
- **Eje Y (Hardware vs. Organización):** $Y = 5.0 \cdot \frac{Co - Ch}{Ch + Cs + Co}$
- **Dispersión:** $\Delta X = \sqrt{\max(0, 25 - X^2)}$, $\Delta Y = \sqrt{\max(0, 25 \cdot \frac{Ch + Co}{Ch + Cs + Co} - Y^2)}$
- **Radio de Dispersión:** $Radio = \sqrt{\Delta X^2 + \Delta Y^2}$

### Criterios de Codificación Auditable
- **T (Teoría/Principios):** Ciencias básicas, física, matemática discreta, lógica, estructuras de datos y algoritmos, teoría de la computación, lenguajes formales y compiladores, sistemas inteligentes y arquitectura teórica de computadores.
- **A (Aplicación/Despliegue):** Programación y desarrollo, ingeniería de software, bases de datos, sistemas operativos, redes y telecomunicaciones, seguridad informática, sistemas embebidos, robótica, gestión de proyectos y legislación.
- **Ch (Hardware):** Circuitos, electrónica, física aplicada a hardware, diseño digital, microprocesadores y arquitectura de computadores.
- **Cs (Software y Sistemas):** Algoritmia, programación, software, bases de datos, sistemas operativos, redes, inteligencia artificial y computación gráfica.
- **Co (Organización y Sistemas de Información):** Gestión de proyectos, evaluación de TI, gobernanza, sistemas de información, economía, finanzas, procesos de negocio y factores humanos (HCI).
- **Exclusiones:** Formación transversal (humanidades, idiomas, ética, deportes), asignaturas optativas/electivas sin programa curricular definido en la retícula base, prácticas profesionales y proyectos finales de grado/capstone.

## 2. Tabla de Resultados — Componente 1 (12 Columnas)

| ID | Titulo_Documento | Institucion_Fuente | Pais | Anio | Tipo_Fuente | Coordenada_X | Coordenada_Y | Desviacion_Radio | Proximidad_Disciplina_CC2020 | Resumen_Evidencia_X | Resumen_Evidencia_Y |
|:---|:---|:---|:---|:---|:---|:---:|:---:|:---:|:---:|:---|:---|
| **D031** | [Ingeniería en Computación — plan 2016/2023](https://consejofi.fi-a.unam.mx/planes_estudio/ingenieria%20en%20computacion/FI_Ingenieria-en-Computacion_Tomo-I.pdf) | UNAM — Facultad de Ingeniería | México | 2016 | Plan de Estudios Oficial | -0.72 | -0.83 | 5.78 | `CE` | Pt=190; Pa=142 créditos; cobertura X=81% del total (408) | Ch=60; Cs=134; Co=24 créditos; cobertura Y=53% del total |
| **D032** | [Ingeniería Informática — plan 2026-2](https://facultad-ciencias-ingenieria.pucp.edu.pe/wp-content/uploads/2026/07/INFORMATICA_ppee_FCI-2026-2.pdf) | Pontificia Universidad Católica del Perú (PUCP) | Perú | 2026 | Plan de Estudios Oficial | 3.09 | 1.31 | 4.91 | `IS` | Pt=18.5; Pa=78.5 créditos; cobertura X=76% del total (128) | Ch=7; Cs=53.5; Co=31 créditos; cobertura Y=71% del total |
| **D033** | [Ingeniería Civil en Computación — plan 2019](https://www.dcc.uchile.cl/pregrado/malla) | Universidad de Chile (FCFM-DCC) | Chile | 2019 | Plan de Estudios Oficial | -1.46 | 0.81 | 5.12 | `CS` | Pt=126; Pa=69 créditos; cobertura X=69% del total (283) | Ch=0; Cs=93; Co=18 créditos; cobertura Y=39% del total |
| **D034** | [Ingeniería en Sistemas Computacionales — retícula ISIC-2010-224](https://www.tecnm.mx/oferta-educativa/licenciatura/ingenieria-en-sistemas-computacionales) | Tecnológico Nacional de México (TecNM) | México | 2010 | Retícula Curricular | -0.43 | -0.17 | 5.60 | `CS` | Pt=94; Pa=79 créditos; cobertura X=74% del total (233) | Ch=18; Cs=89; Co=14 créditos; cobertura Y=52% del total |
| **D035** | [Ingeniería en Computación — plan 2024](https://ing.unlp.edu.ar/grado/carreras/ingenieria-computacion/) | Universidad Nacional de La Plata (UNLP) | Argentina | 2024 | Plan de Estudios Oficial | 0.86 | -1.51 | 5.58 | `CE` | Pt=72; Pa=102 horas/créditos; cobertura X=85% del total (204) | Ch=42; Cs=80; Co=4 horas/créditos; cobertura Y=62% del total |
| **D036** | [Bachillerato en Computación con Varios Énfasis — plan 420705](https://www.ecci.ucr.ac.cr/oferta-academica/bachillerato-en-computacion-con-varios-enfasis) | Universidad de Costa Rica (UCR-ECCI) | Costa Rica | 2016 | Plan de Estudios Oficial | -0.71 | -0.31 | 5.39 | `CS` | Pt=48; Pa=36 créditos; cobertura X=75% del total (112) | Ch=8; Cs=52; Co=4 créditos; cobertura Y=57% del total |
| **D037** | [Ingeniería en Tecnologías de la Información — plan 135 créditos](https://utpl.edu.ec/carreras/tecnologiasdelainformacion) | Universidad Técnica Particular de Loja (UTPL) | Ecuador | 2020 | Plan de Estudios Oficial | 1.90 | 0.71 | 5.25 | `SE` | Pt=36; Pa=80 créditos; cobertura X=84% del total (138) | Ch=6; Cs=72; Co=20 créditos; cobertura Y=71% del total |
| **D038** | [Ingeniería en Sistemas Computacionales — nuevo plan](https://is.unah.edu.hn/dmsdocument/19609-ing-sistemas-computacionales-unah-flujograma-pdf) | Universidad Nacional Autónoma de Honduras (UNAH) | Honduras | 2021 | Plan de Estudios Oficial | 0.95 | 0.61 | 5.59 | `SE` | Pt=68; Pa=100 unidades valorativas; cobertura X=79% del total (214) | Ch=12; Cs=92; Co=28 unidades valorativas; cobertura Y=62% del total |
| **D039** | [Ingeniería de Sistemas y Computación — plan ISIS 134](https://sistemas.uniandes.edu.co/es/pregrado/plan-de-estudios) | Universidad de los Andes (UniAndes) | Colombia | 2018 | Plan de Estudios Oficial | -0.24 | 0.67 | 5.28 | `CS` | Pt=33; Pa=30 créditos; cobertura X=70% del total (90) | Ch=0; Cs=39; Co=6 créditos; cobertura Y=50% del total |
| **D040** | [Ingeniería de Sistemas — plan de estudios](https://www.eafit.edu.co/pregrados/ingenieria-de-sistemas/Paginas/plan-de-estudios.aspx) | Universidad EAFIT | Colombia | 2020 | Plan de Estudios Oficial | 0.00 | 0.56 | 5.50 | `CS` | Pt=39; Pa=39 créditos; cobertura X=85% del total (92) | Ch=3; Cs=42; Co=9 créditos; cobertura Y=59% del total |
| **D041** | [Ingeniería en Informática — plan 2020](https://www.fi.uba.ar/grado/carreras/ingenieria-en-informatica/plan-de-estudios) | Universidad de Buenos Aires (UBA - FIUBA) | Argentina | 2020 | Plan de Estudios Oficial | -0.66 | 0.45 | 5.42 | `CS` | Pt=94; Pa=72 créditos; cobertura X=88% del total (188) | Ch=6; Cs=88; Co=16 créditos; cobertura Y=59% del total |
| **D042** | [Licenciatura en Ciencias de la Ingeniería / Civil Computación](https://www.ing.uc.cl/programas-de-estudio/pregrado/licenciatura-en-ingenieria-en-ciencia-de-la-computacion/) | Pontificia Universidad Católica de Chile (PUC Chile) | Chile | 2020 | Plan de Estudios Oficial | -1.36 | 0.00 | 5.19 | `CS` | Pt=140; Pa=80 créditos; cobertura X=85% del total (260) | Ch=10; Cs=110; Co=10 créditos; cobertura Y=50% del total |
| **D043** | [Licenciatura en Ingeniería en Computación — plan UEA](https://academicos.azc.uam.mx/ing_computacion/plan-de-estudios/) | Universidad Autónoma Metropolitana (UAM Azcapotzalco) | México | s. f. | Plan de Estudios Oficial | -1.15 | -1.37 | 5.35 | `CE` | Pt=161; Pa=101 créditos UEA; cobertura X=92% del total (286) | Ch=44; Cs=117; Co=0 créditos UEA; cobertura Y=56% del total |
| **D044** | [Ingeniería en Computación — plan ICOM](https://www.cucei.udg.mx/carreras/computacion/licenciaturas/ingenieria-en-computacion) | Universidad de Guadalajara (UdeG - CUCEI) | México | 2017 | Plan de Estudios Oficial | 0.06 | -0.52 | 5.45 | `CS` | Pt=117; Pa=120 créditos; cobertura X=89% del total (267) | Ch=26; Cs=138; Co=8 créditos; cobertura Y=64% del total |
| **D045** | [Ingeniería en Tecnologías Computacionales — modelo Tec21](https://tec.mx/es/ingenieria-y-ciencias/ingenieria-en-tecnologias-computacionales) | Tecnológico de Monterrey (ITESM) | México | 2019 | Plan de Estudios Oficial | -0.22 | -0.59 | 5.52 | `CS` | Pt=36; Pa=33 créditos; cobertura X=88% del total (78) | Ch=9; Cs=39; Co=3 créditos; cobertura Y=65% del total |

## 3. Desglose Métrico de Carga Académica y Cobertura

| ID | Institución | Total Materias | Peso Total | Pt (Teoría) | Pa (Aplic.) | Ch (Hardw.) | Cs (Softw.) | Co (Org.) | Cobertura X | Cobertura Y |
|:---|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **D031** | UNAM — Facultad de Ingeniería | 44 | 408 créditos | 190 | 142 | 60 | 134 | 24 | 81.4% | 53.4% |
| **D032** | Pontificia Universidad Católica del Perú (PUCP) | 39 | 128 créditos | 18.5 | 78.5 | 7 | 53.5 | 31 | 75.8% | 71.5% |
| **D033** | Universidad de Chile (FCFM-DCC) | 46 | 283 créditos | 126 | 69 | 0 | 93 | 18 | 68.9% | 39.2% |
| **D034** | Tecnológico Nacional de México (TecNM) | 45 | 233 créditos | 94 | 79 | 18 | 89 | 14 | 74.2% | 51.9% |
| **D035** | Universidad Nacional de La Plata (UNLP) | 36 | 204 horas/créditos | 72 | 102 | 42 | 80 | 4 | 85.3% | 61.8% |
| **D036** | Universidad de Costa Rica (UCR-ECCI) | 28 | 112 créditos | 48 | 36 | 8 | 52 | 4 | 75.0% | 57.1% |
| **D037** | Universidad Técnica Particular de Loja (UTPL) | 45 | 138 créditos | 36 | 80 | 6 | 72 | 20 | 84.1% | 71.0% |
| **D038** | Universidad Nacional Autónoma de Honduras (UNAH) | 50 | 214 unidades valorativas | 68 | 100 | 12 | 92 | 28 | 78.5% | 61.7% |
| **D039** | Universidad de los Andes (UniAndes) | 24 | 90 créditos | 33 | 30 | 0 | 39 | 6 | 70.0% | 50.0% |
| **D040** | Universidad EAFIT | 30 | 92 créditos | 39 | 39 | 3 | 42 | 9 | 84.8% | 58.7% |
| **D041** | Universidad de Buenos Aires (UBA - FIUBA) | 28 | 188 créditos | 94 | 72 | 6 | 88 | 16 | 88.3% | 58.5% |
| **D042** | Pontificia Universidad Católica de Chile (PUC Chile) | 25 | 260 créditos | 140 | 80 | 10 | 110 | 10 | 84.6% | 50.0% |
| **D043** | Universidad Autónoma Metropolitana (UAM Azcapotzalco) | 32 | 286 créditos UEA | 161 | 101 | 44 | 117 | 0 | 91.6% | 56.3% |
| **D044** | Universidad de Guadalajara (UdeG - CUCEI) | 31 | 267 créditos | 117 | 120 | 26 | 138 | 8 | 88.8% | 64.4% |
| **D045** | Tecnológico de Monterrey (ITESM) | 25 | 78 créditos | 36 | 33 | 9 | 39 | 3 | 88.5% | 65.4% |

## 4. Diagrama de Dispersión CC2020

![Dispersión del bloque 3](bloque_03_dispersion.png)

## 5. Análisis e Interpretación de Resultados por Documento

### D031 — UNAM — Facultad de Ingeniería (México)
- **Título del Programa:** Ingeniería en Computación — plan 2016/2023
- **Tipo de Fuente y Año:** Plan de Estudios Oficial (2016)
- **URL Oficial:** [https://consejofi.fi-a.unam.mx/planes_estudio/ingenieria%20en%20computacion/FI_Ingenieria-en-Computacion_Tomo-I.pdf](https://consejofi.fi-a.unam.mx/planes_estudio/ingenieria%20en%20computacion/FI_Ingenieria-en-Computacion_Tomo-I.pdf)
- **Coordenadas:** X = -0.72, Y = -0.83 | **Radio:** 5.78 | **Afinidad:** `CE`
- **Diagnóstico Curricular:** Enfocado en fundamentos de ingeniería clásica (física, matemáticas, circuitos) y sistemas digitales con sólida base de hardware, situándolo cerca de Computer Engineering (CE).

### D032 — Pontificia Universidad Católica del Perú (PUCP) (Perú)
- **Título del Programa:** Ingeniería Informática — plan 2026-2
- **Tipo de Fuente y Año:** Plan de Estudios Oficial (2026)
- **URL Oficial:** [https://facultad-ciencias-ingenieria.pucp.edu.pe/wp-content/uploads/2026/07/INFORMATICA_ppee_FCI-2026-2.pdf](https://facultad-ciencias-ingenieria.pucp.edu.pe/wp-content/uploads/2026/07/INFORMATICA_ppee_FCI-2026-2.pdf)
- **Coordenadas:** X = 3.09, Y = 1.31 | **Radio:** 4.91 | **Afinidad:** `IS`
- **Diagnóstico Curricular:** Fuerte orientación al despliegue en organizaciones, sistemas de información empresarial y gestión tecnológica, clasificándolo con proximidad a Information Systems (IS).

### D033 — Universidad de Chile (FCFM-DCC) (Chile)
- **Título del Programa:** Ingeniería Civil en Computación — plan 2019
- **Tipo de Fuente y Año:** Plan de Estudios Oficial (2019)
- **URL Oficial:** [https://www.dcc.uchile.cl/pregrado/malla](https://www.dcc.uchile.cl/pregrado/malla)
- **Coordenadas:** X = -1.46, Y = 0.81 | **Radio:** 5.12 | **Afinidad:** `CS`
- **Diagnóstico Curricular:** Marcado énfasis teórico-formal en ciencias de la computación, algoritmos, métodos cuantitativos y modelos matemáticos (Computer Science - CS).

### D034 — Tecnológico Nacional de México (TecNM) (México)
- **Título del Programa:** Ingeniería en Sistemas Computacionales — retícula ISIC-2010-224
- **Tipo de Fuente y Año:** Retícula Curricular (2010)
- **URL Oficial:** [https://www.tecnm.mx/oferta-educativa/licenciatura/ingenieria-en-sistemas-computacionales](https://www.tecnm.mx/oferta-educativa/licenciatura/ingenieria-en-sistemas-computacionales)
- **Coordenadas:** X = -0.43, Y = -0.17 | **Radio:** 5.60 | **Afinidad:** `CS`
- **Diagnóstico Curricular:** Plan nacional con equilibrio entre desarrollo de software, redes y fundamentos físicos, ubicándose en la zona central con afinidad Computer Science (CS).

### D035 — Universidad Nacional de La Plata (UNLP) (Argentina)
- **Título del Programa:** Ingeniería en Computación — plan 2024
- **Tipo de Fuente y Año:** Plan de Estudios Oficial (2024)
- **URL Oficial:** [https://ing.unlp.edu.ar/grado/carreras/ingenieria-computacion/](https://ing.unlp.edu.ar/grado/carreras/ingenieria-computacion/)
- **Coordenadas:** X = 0.86, Y = -1.51 | **Radio:** 5.58 | **Afinidad:** `CE`
- **Diagnóstico Curricular:** Alta carga de electrónica, sistemas digitales, microprocesadores y arquitectura de computadoras en interacción con software de bajo nivel (Computer Engineering - CE).

### D036 — Universidad de Costa Rica (UCR-ECCI) (Costa Rica)
- **Título del Programa:** Bachillerato en Computación con Varios Énfasis — plan 420705
- **Tipo de Fuente y Año:** Plan de Estudios Oficial (2016)
- **URL Oficial:** [https://www.ecci.ucr.ac.cr/oferta-academica/bachillerato-en-computacion-con-varios-enfasis](https://www.ecci.ucr.ac.cr/oferta-academica/bachillerato-en-computacion-con-varios-enfasis)
- **Coordenadas:** X = -0.71, Y = -0.31 | **Radio:** 5.39 | **Afinidad:** `CS`
- **Diagnóstico Curricular:** Estructura formativa balanceada en ciencias de la computación, estructuras discretas, programación y sistemas (Computer Science - CS).

### D037 — Universidad Técnica Particular de Loja (UTPL) (Ecuador)
- **Título del Programa:** Ingeniería en Tecnologías de la Información — plan 135 créditos
- **Tipo de Fuente y Año:** Plan de Estudios Oficial (2020)
- **URL Oficial:** [https://utpl.edu.ec/carreras/tecnologiasdelainformacion](https://utpl.edu.ec/carreras/tecnologiasdelainformacion)
- **Coordenadas:** X = 1.90, Y = 0.71 | **Radio:** 5.25 | **Afinidad:** `SE`
- **Diagnóstico Curricular:** Énfasis notable en desarrollo de software aplicado, metodologías ágiles, bases de datos y arquitectura de aplicaciones (Software Engineering - SE).

### D038 — Universidad Nacional Autónoma de Honduras (UNAH) (Honduras)
- **Título del Programa:** Ingeniería en Sistemas Computacionales — nuevo plan
- **Tipo de Fuente y Año:** Plan de Estudios Oficial (2021)
- **URL Oficial:** [https://is.unah.edu.hn/dmsdocument/19609-ing-sistemas-computacionales-unah-flujograma-pdf](https://is.unah.edu.hn/dmsdocument/19609-ing-sistemas-computacionales-unah-flujograma-pdf)
- **Coordenadas:** X = 0.95, Y = 0.61 | **Radio:** 5.59 | **Afinidad:** `SE`
- **Diagnóstico Curricular:** Perfil equilibrado con predominio de ingeniería de software, desarrollo aplicado y bases de datos (Software Engineering - SE).

### D039 — Universidad de los Andes (UniAndes) (Colombia)
- **Título del Programa:** Ingeniería de Sistemas y Computación — plan ISIS 134
- **Tipo de Fuente y Año:** Plan de Estudios Oficial (2018)
- **URL Oficial:** [https://sistemas.uniandes.edu.co/es/pregrado/plan-de-estudios](https://sistemas.uniandes.edu.co/es/pregrado/plan-de-estudios)
- **Coordenadas:** X = -0.24, Y = 0.67 | **Radio:** 5.28 | **Afinidad:** `CS`
- **Diagnóstico Curricular:** Fuerte núcleo algorítmico, teoría de la computación, estructuras y sistemas (Computer Science - CS).

### D040 — Universidad EAFIT (Colombia)
- **Título del Programa:** Ingeniería de Sistemas — plan de estudios
- **Tipo de Fuente y Año:** Plan de Estudios Oficial (2020)
- **URL Oficial:** [https://www.eafit.edu.co/pregrados/ingenieria-de-sistemas/Paginas/plan-de-estudios.aspx](https://www.eafit.edu.co/pregrados/ingenieria-de-sistemas/Paginas/plan-de-estudios.aspx)
- **Coordenadas:** X = 0.00, Y = 0.56 | **Radio:** 5.50 | **Afinidad:** `CS`
- **Diagnóstico Curricular:** Enfoque integrado entre ciencias computacionales, algoritmos, infraestructura y proyectos de software (Computer Science - CS).

### D041 — Universidad de Buenos Aires (UBA - FIUBA) (Argentina)
- **Título del Programa:** Ingeniería en Informática — plan 2020
- **Tipo de Fuente y Año:** Plan de Estudios Oficial (2020)
- **URL Oficial:** [https://www.fi.uba.ar/grado/carreras/ingenieria-en-informatica/plan-de-estudios](https://www.fi.uba.ar/grado/carreras/ingenieria-en-informatica/plan-de-estudios)
- **Coordenadas:** X = -0.66, Y = 0.45 | **Radio:** 5.42 | **Afinidad:** `CS`
- **Diagnóstico Curricular:** Plan riguroso con base formal en algoritmos, sistemas operativos, redes y compiladores (Computer Science - CS).

### D042 — Pontificia Universidad Católica de Chile (PUC Chile) (Chile)
- **Título del Programa:** Licenciatura en Ciencias de la Ingeniería / Civil Computación
- **Tipo de Fuente y Año:** Plan de Estudios Oficial (2020)
- **URL Oficial:** [https://www.ing.uc.cl/programas-de-estudio/pregrado/licenciatura-en-ingenieria-en-ciencia-de-la-computacion/](https://www.ing.uc.cl/programas-de-estudio/pregrado/licenciatura-en-ingenieria-en-ciencia-de-la-computacion/)
- **Coordenadas:** X = -1.36, Y = 0.00 | **Radio:** 5.19 | **Afinidad:** `CS`
- **Diagnóstico Curricular:** Tradición de ingeniería civil matemática con alta concentración en fundamentos de ciencias computacionales y algoritmos (Computer Science - CS).

### D043 — Universidad Autónoma Metropolitana (UAM Azcapotzalco) (México)
- **Título del Programa:** Licenciatura en Ingeniería en Computación — plan UEA
- **Tipo de Fuente y Año:** Plan de Estudios Oficial (s. f.)
- **URL Oficial:** [https://academicos.azc.uam.mx/ing_computacion/plan-de-estudios/](https://academicos.azc.uam.mx/ing_computacion/plan-de-estudios/)
- **Coordenadas:** X = -1.15, Y = -1.37 | **Radio:** 5.35 | **Afinidad:** `CE`
- **Diagnóstico Curricular:** Fuerte presencia de electrónica analógica/digital, electromagnetismo, señales y circuitos (Computer Engineering - CE).

### D044 — Universidad de Guadalajara (UdeG - CUCEI) (México)
- **Título del Programa:** Ingeniería en Computación — plan ICOM
- **Tipo de Fuente y Año:** Plan de Estudios Oficial (2017)
- **URL Oficial:** [https://www.cucei.udg.mx/carreras/computacion/licenciaturas/ingenieria-en-computacion](https://www.cucei.udg.mx/carreras/computacion/licenciaturas/ingenieria-en-computacion)
- **Coordenadas:** X = 0.06, Y = -0.52 | **Radio:** 5.45 | **Afinidad:** `CS`
- **Diagnóstico Curricular:** Orientación equilibrada de ingeniería en computación cubriendo algoritmos, arquitectura y software (Computer Science - CS).

### D045 — Tecnológico de Monterrey (ITESM) (México)
- **Título del Programa:** Ingeniería en Tecnologías Computacionales — modelo Tec21
- **Tipo de Fuente y Año:** Plan de Estudios Oficial (2019)
- **URL Oficial:** [https://tec.mx/es/ingenieria-y-ciencias/ingenieria-en-tecnologias-computacionales](https://tec.mx/es/ingenieria-y-ciencias/ingenieria-en-tecnologias-computacionales)
- **Coordenadas:** X = -0.22, Y = -0.59 | **Radio:** 5.52 | **Afinidad:** `CS`
- **Diagnóstico Curricular:** Modelo de retos Tec21 con fuerte base de ciencias fundamentales, algoritmia y modelación matemática computacional (Computer Science - CS).

## 6. Advertencias y Limitaciones Metodológicas
1. **Auditabilidad y Reglas:** Las coordenadas son el resultado de un conjunto explícito y público de expresiones regulares aplicadas a las asignaturas del plan. Modificaciones razonables en las reglas pueden desplazar los puntos.
2. **Afinidad Disciplinar Provisional:** Las categorías (CS, CE, SE, IT, IS) responden a umbrales de composición relativa de áreas ($Ch, Cs, Co, Pt, Pa$) y no constituyen certificaciones oficiales de ACM/IEEE CC2020.
3. **Interpretación del Radio:** El radio describe la dispersión interna entre componentes curriculares polares en el espacio conceptual, no un error de muestreo ni intervalo de confianza estadística.
4. **Heterogeneidad de Métricas de Peso:** Mientras instituciones como UBA, UNLP y UNLPam reportan horas reloj, otras como UNAM, TecNM, PUCP y UniAndes reportan créditos académicos. El análisis compara las proporciones normalizadas internas de cada programa.