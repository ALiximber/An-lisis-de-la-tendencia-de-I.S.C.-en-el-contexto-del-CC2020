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
| **D031** | [Ingeniería en Computación — plan 2016/2023](https://consejofi.fi-a.unam.mx/planes_estudio/ingenieria%20en%20computacion/FI_Ingenieria-en-Computacion_Tomo-I.pdf) | UNAM — Facultad de Ingeniería | México | 2016 | Plan de Estudios Oficial | -0.87 | -0.94 | 5.69 | `CE` | Pt=195; Pa=137 (sin STEM: Pt_c=81, Pa_c=137, X_comp=+1.28); cobertura X=81% del total (408) | Ch=60; Cs=139; Co=19; cobertura Y=53% del total; Vector=[CE:28%,CS:29%,SE:17%,IT:18%,IS:9%] |
| **D032** | [Ingeniería Informática — plan 2026-2](https://facultad-ciencias-ingenieria.pucp.edu.pe/wp-content/uploads/2026/07/INFORMATICA_ppee_FCI-2026-2.pdf) | Pontificia Universidad Católica del Perú (PUCP) | Perú | 2026 | Plan de Estudios Oficial | 3.15 | 1.80 | 4.76 | `IS` | Pt=18.5; Pa=81.5 (sin STEM: Pt_c=13, Pa_c=81.5, X_comp=+3.62); cobertura X=78% del total (128) | Ch=3.5; Cs=53.5; Co=37.5; cobertura Y=74% del total; Vector=[CE:4%,CS:13%,SE:31%,IT:14%,IS:39%] |
| **D033** | [Ingeniería Civil en Computación — plan 2019](https://www.dcc.uchile.cl/pregrado/malla) | Universidad de Chile (FCFM-DCC) | Chile | 2019 | Plan de Estudios Oficial | -1.38 | 0.79 | 5.14 | `CS` | Pt=132; Pa=75 (sin STEM: Pt_c=39, Pa_c=75, X_comp=+1.58); cobertura X=73% del total (283) | Ch=0; Cs=96; Co=18; cobertura Y=40% del total; Vector=[CE:0%,CS:39%,SE:35%,IT:12%,IS:14%] |
| **D034** | [Ingeniería en Sistemas Computacionales — retícula ISIC-2010-224](https://www.tecnm.mx/oferta-educativa/licenciatura/ingenieria-en-sistemas-computacionales) | Tecnológico Nacional de México (TecNM) | México | 2010 | Retícula Curricular | -0.06 | 0.08 | 5.64 | `SE` | Pt=89.5; Pa=87.5 (sin STEM: Pt_c=37.5, Pa_c=87.5, X_comp=+2.00); cobertura X=76% del total (233) | Ch=16; Cs=91; Co=18; cobertura Y=54% del total; Vector=[CE:13%,CS:26%,SE:24%,IT:24%,IS:13%] |
| **D035** | [Ingeniería en Computación — plan 2024](https://ing.unlp.edu.ar/grado/carreras/ingenieria-computacion/) | Universidad Nacional de La Plata (UNLP) | Argentina | 2024 | Plan de Estudios Oficial | 0.96 | -1.31 | 5.66 | `CE` | Pt=72; Pa=106 (sin STEM: Pt_c=24, Pa_c=106, X_comp=+3.15); cobertura X=87% del total (204) | Ch=42; Cs=80; Co=8; cobertura Y=64% del total; Vector=[CE:32%,CS:7%,SE:30%,IT:24%,IS:6%] |
| **D036** | [Bachillerato en Computación con Varios Énfasis — plan 420705](https://www.ecci.ucr.ac.cr/oferta-academica/bachillerato-en-computacion-con-varios-enfasis) | Universidad de Costa Rica (UCR-ECCI) | Costa Rica | 2016 | Plan de Estudios Oficial | -0.25 | -0.17 | 5.39 | `CS` | Pt=42; Pa=38 (sin STEM: Pt_c=22, Pa_c=38, X_comp=+1.33); cobertura X=71% del total (112) | Ch=6; Cs=50; Co=4; cobertura Y=54% del total; Vector=[CE:10%,CS:33%,SE:33%,IT:20%,IS:5%] |
| **D037** | [Ingeniería en Tecnologías de la Información — plan 135 créditos](https://utpl.edu.ec/carreras/tecnologiasdelainformacion) | Universidad Técnica Particular de Loja (UTPL) | Ecuador | 2020 | Plan de Estudios Oficial | 2.41 | 0.92 | 5.01 | `IT` | Pt=30; Pa=86 (sin STEM: Pt_c=15, Pa_c=86, X_comp=+3.51); cobertura X=84% del total (138) | Ch=4.5; Cs=73.5; Co=23; cobertura Y=73% del total; Vector=[CE:4%,CS:12%,SE:34%,IT:30%,IS:20%] |
| **D038** | [Ingeniería en Sistemas Computacionales — nuevo plan](https://is.unah.edu.hn/dmsdocument/19609-ing-sistemas-computacionales-unah-flujograma-pdf) | Universidad Nacional Autónoma de Honduras (UNAH) | Honduras | 2021 | Plan de Estudios Oficial | 0.95 | 0.61 | 5.59 | `IT` | Pt=68; Pa=100 (sin STEM: Pt_c=32, Pa_c=100, X_comp=+2.58); cobertura X=79% del total (214) | Ch=12; Cs=92; Co=28; cobertura Y=62% del total; Vector=[CE:9%,CS:23%,SE:23%,IT:25%,IS:19%] |
| **D039** | [Ingeniería de Sistemas y Computación — plan ISIS 134](https://sistemas.uniandes.edu.co/es/pregrado/plan-de-estudios) | Universidad de los Andes (UniAndes) | Colombia | 2018 | Plan de Estudios Oficial | 0.24 | 0.67 | 5.28 | `IT` | Pt=30; Pa=33 (sin STEM: Pt_c=12, Pa_c=33, X_comp=+2.33); cobertura X=70% del total (90) | Ch=0; Cs=39; Co=6; cobertura Y=50% del total; Vector=[CE:0%,CS:31%,SE:31%,IT:27%,IS:11%] |
| **D040** | [Ingeniería de Sistemas — plan de estudios](https://www.eafit.edu.co/pregrados/ingenieria-de-sistemas/Paginas/plan-de-estudios.aspx) | Universidad EAFIT | Colombia | 2020 | Plan de Estudios Oficial | 0.00 | 0.56 | 5.50 | `SE` | Pt=39; Pa=39 (sin STEM: Pt_c=15, Pa_c=39, X_comp=+2.22); cobertura X=85% del total (92) | Ch=3; Cs=42; Co=9; cobertura Y=59% del total; Vector=[CE:6%,CS:26%,SE:34%,IT:22%,IS:12%] |
| **D041** | [Ingeniería en Informática — plan 2020](https://www.fi.uba.ar/grado/carreras/ingenieria-en-informatica/plan-de-estudios) | Universidad de Buenos Aires (UBA - FIUBA) | Argentina | 2020 | Plan de Estudios Oficial | -1.02 | 0.18 | 5.25 | `CS` | Pt=100; Pa=66 (sin STEM: Pt_c=44, Pa_c=66, X_comp=+1.00); cobertura X=88% del total (188) | Ch=6; Cs=94; Co=10; cobertura Y=59% del total; Vector=[CE:5%,CS:37%,SE:30%,IT:20%,IS:7%] |
| **D042** | [Licenciatura en Ciencias de la Ingeniería / Civil Computación](https://www.ing.uc.cl/programas-de-estudio/pregrado/licenciatura-en-ingenieria-en-ciencia-de-la-computacion/) | Pontificia Universidad Católica de Chile (PUC Chile) | Chile | 2020 | Plan de Estudios Oficial | -0.83 | 0.00 | 5.26 | `SE` | Pt=140; Pa=100 (sin STEM: Pt_c=50, Pa_c=100, X_comp=+1.67); cobertura X=92% del total (260) | Ch=10; Cs=130; Co=10; cobertura Y=58% del total; Vector=[CE:7%,CS:31%,SE:36%,IT:22%,IS:5%] |
| **D043** | [Licenciatura en Ingeniería en Computación — plan UEA](https://academicos.azc.uam.mx/ing_computacion/plan-de-estudios/) | Universidad Autónoma Metropolitana (UAM Azcapotzalco) | México | s. f. | Plan de Estudios Oficial | -1.15 | -1.37 | 5.35 | `CE` | Pt=161; Pa=101 (sin STEM: Pt_c=60, Pa_c=101, X_comp=+1.27); cobertura X=92% del total (286) | Ch=44; Cs=117; Co=0; cobertura Y=56% del total; Vector=[CE:27%,CS:29%,SE:19%,IT:24%,IS:0%] |
| **D044** | [Ingeniería en Computación — plan ICOM](https://www.cucei.udg.mx/carreras/computacion/licenciaturas/ingenieria-en-computacion) | Universidad de Guadalajara (UdeG - CUCEI) | México | 2017 | Plan de Estudios Oficial | 0.06 | -0.52 | 5.45 | `IT` | Pt=117; Pa=120 (sin STEM: Pt_c=52, Pa_c=120, X_comp=+1.98); cobertura X=89% del total (267) | Ch=26; Cs=138; Co=8; cobertura Y=64% del total; Vector=[CE:15%,CS:30%,SE:25%,IT:27%,IS:3%] |
| **D045** | [Ingeniería en Tecnologías Computacionales — modelo Tec21](https://tec.mx/es/ingenieria-y-ciencias/ingenieria-en-tecnologias-computacionales) | Tecnológico de Monterrey (ITESM) | México | 2019 | Plan de Estudios Oficial | 0.00 | -0.39 | 5.43 | `CS` | Pt=34.5; Pa=34.5 (sin STEM: Pt_c=22.5, Pa_c=34.5, X_comp=+1.05); cobertura X=88% del total (78) | Ch=7.5; Cs=46.5; Co=3; cobertura Y=73% del total; Vector=[CE:13%,CS:31%,SE:28%,IT:24%,IS:4%] |

## 3. Desglose Métrico de Carga Académica y Cobertura

| ID | Institución | Total Materias | Peso Total | Pt (Teoría) | Pa (Aplic.) | Ch (Hardw.) | Cs (Softw.) | Co (Org.) | Cobertura X | Cobertura Y |
|:---|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **D031** | UNAM — Facultad de Ingeniería | 44 | 408 creditos academicos | 195 | 137 | 60 | 139 | 19 | 81.4% | 53.4% |
| **D032** | Pontificia Universidad Católica del Perú (PUCP) | 39 | 128 creditos academicos | 18.5 | 81.5 | 3.5 | 53.5 | 37.5 | 78.1% | 73.8% |
| **D033** | Universidad de Chile (FCFM-DCC) | 46 | 283 creditos academicos | 132 | 75 | 0 | 96 | 18 | 73.1% | 40.3% |
| **D034** | Tecnológico Nacional de México (TecNM) | 45 | 233 creditos academicos | 89.5 | 87.5 | 16 | 91 | 18 | 76.0% | 53.6% |
| **D035** | Universidad Nacional de La Plata (UNLP) | 36 | 204 horas semanales creditos | 72 | 106 | 42 | 80 | 8 | 87.3% | 63.7% |
| **D036** | Universidad de Costa Rica (UCR-ECCI) | 28 | 112 creditos academicos | 42 | 38 | 6 | 50 | 4 | 71.4% | 53.6% |
| **D037** | Universidad Técnica Particular de Loja (UTPL) | 45 | 138 creditos academicos | 30 | 86 | 4.5 | 73.5 | 23 | 84.1% | 73.2% |
| **D038** | Universidad Nacional Autónoma de Honduras (UNAH) | 50 | 214 unidades valorativas | 68 | 100 | 12 | 92 | 28 | 78.5% | 61.7% |
| **D039** | Universidad de los Andes (UniAndes) | 24 | 90 creditos academicos | 30 | 33 | 0 | 39 | 6 | 70.0% | 50.0% |
| **D040** | Universidad EAFIT | 30 | 92 creditos academicos | 39 | 39 | 3 | 42 | 9 | 84.8% | 58.7% |
| **D041** | Universidad de Buenos Aires (UBA - FIUBA) | 28 | 188 creditos academicos | 100 | 66 | 6 | 94 | 10 | 88.3% | 58.5% |
| **D042** | Pontificia Universidad Católica de Chile (PUC Chile) | 25 | 260 creditos academicos | 140 | 100 | 10 | 130 | 10 | 92.3% | 57.7% |
| **D043** | Universidad Autónoma Metropolitana (UAM Azcapotzalco) | 32 | 286 creditos UEA | 161 | 101 | 44 | 117 | 0 | 91.6% | 56.3% |
| **D044** | Universidad de Guadalajara (UdeG - CUCEI) | 31 | 267 creditos academicos | 117 | 120 | 26 | 138 | 8 | 88.8% | 64.4% |
| **D045** | Tecnológico de Monterrey (ITESM) | 25 | 78 creditos academicos | 34.5 | 34.5 | 7.5 | 46.5 | 3 | 88.5% | 73.1% |

## 4. Diagrama de Dispersión CC2020

![Dispersión del bloque 3](bloque_03_dispersion.png)

## 5. Análisis e Interpretación de Resultados por Documento

### D031 — UNAM — Facultad de Ingeniería (México)
- **Título del Programa:** Ingeniería en Computación — plan 2016/2023
- **Tipo de Fuente y Año:** Plan de Estudios Oficial (2016)
- **URL Oficial:** [https://consejofi.fi-a.unam.mx/planes_estudio/ingenieria%20en%20computacion/FI_Ingenieria-en-Computacion_Tomo-I.pdf](https://consejofi.fi-a.unam.mx/planes_estudio/ingenieria%20en%20computacion/FI_Ingenieria-en-Computacion_Tomo-I.pdf)
- **Coordenadas:** X = -0.87, Y = -0.94 | **Radio:** 5.69 | **Afinidad:** `CE`
- **Diagnóstico Curricular:** Enfocado en fundamentos de ingeniería clásica (física, matemáticas, circuitos) y sistemas digitales con sólida base de hardware, situándolo cerca de Computer Engineering (CE).

### D032 — Pontificia Universidad Católica del Perú (PUCP) (Perú)
- **Título del Programa:** Ingeniería Informática — plan 2026-2
- **Tipo de Fuente y Año:** Plan de Estudios Oficial (2026)
- **URL Oficial:** [https://facultad-ciencias-ingenieria.pucp.edu.pe/wp-content/uploads/2026/07/INFORMATICA_ppee_FCI-2026-2.pdf](https://facultad-ciencias-ingenieria.pucp.edu.pe/wp-content/uploads/2026/07/INFORMATICA_ppee_FCI-2026-2.pdf)
- **Coordenadas:** X = 3.15, Y = 1.80 | **Radio:** 4.76 | **Afinidad:** `IS`
- **Diagnóstico Curricular:** Fuerte orientación al despliegue en organizaciones, sistemas de información empresarial y gestión tecnológica, clasificándolo con proximidad a Information Systems (IS).

### D033 — Universidad de Chile (FCFM-DCC) (Chile)
- **Título del Programa:** Ingeniería Civil en Computación — plan 2019
- **Tipo de Fuente y Año:** Plan de Estudios Oficial (2019)
- **URL Oficial:** [https://www.dcc.uchile.cl/pregrado/malla](https://www.dcc.uchile.cl/pregrado/malla)
- **Coordenadas:** X = -1.38, Y = 0.79 | **Radio:** 5.14 | **Afinidad:** `CS`
- **Diagnóstico Curricular:** Marcado énfasis teórico-formal en ciencias de la computación, algoritmos, métodos cuantitativos y modelos matemáticos (Computer Science - CS).

### D034 — Tecnológico Nacional de México (TecNM) (México)
- **Título del Programa:** Ingeniería en Sistemas Computacionales — retícula ISIC-2010-224
- **Tipo de Fuente y Año:** Retícula Curricular (2010)
- **URL Oficial:** [https://www.tecnm.mx/oferta-educativa/licenciatura/ingenieria-en-sistemas-computacionales](https://www.tecnm.mx/oferta-educativa/licenciatura/ingenieria-en-sistemas-computacionales)
- **Coordenadas:** X = -0.06, Y = 0.08 | **Radio:** 5.64 | **Afinidad:** `SE`
- **Diagnóstico Curricular:** Plan nacional con equilibrio entre desarrollo de software, redes y fundamentos físicos, ubicándose en la zona central con afinidad Computer Science (CS).

### D035 — Universidad Nacional de La Plata (UNLP) (Argentina)
- **Título del Programa:** Ingeniería en Computación — plan 2024
- **Tipo de Fuente y Año:** Plan de Estudios Oficial (2024)
- **URL Oficial:** [https://ing.unlp.edu.ar/grado/carreras/ingenieria-computacion/](https://ing.unlp.edu.ar/grado/carreras/ingenieria-computacion/)
- **Coordenadas:** X = 0.96, Y = -1.31 | **Radio:** 5.66 | **Afinidad:** `CE`
- **Diagnóstico Curricular:** Alta carga de electrónica, sistemas digitales, microprocesadores y arquitectura de computadoras en interacción con software de bajo nivel (Computer Engineering - CE).

### D036 — Universidad de Costa Rica (UCR-ECCI) (Costa Rica)
- **Título del Programa:** Bachillerato en Computación con Varios Énfasis — plan 420705
- **Tipo de Fuente y Año:** Plan de Estudios Oficial (2016)
- **URL Oficial:** [https://www.ecci.ucr.ac.cr/oferta-academica/bachillerato-en-computacion-con-varios-enfasis](https://www.ecci.ucr.ac.cr/oferta-academica/bachillerato-en-computacion-con-varios-enfasis)
- **Coordenadas:** X = -0.25, Y = -0.17 | **Radio:** 5.39 | **Afinidad:** `CS`
- **Diagnóstico Curricular:** Estructura formativa balanceada en ciencias de la computación, estructuras discretas, programación y sistemas (Computer Science - CS).

### D037 — Universidad Técnica Particular de Loja (UTPL) (Ecuador)
- **Título del Programa:** Ingeniería en Tecnologías de la Información — plan 135 créditos
- **Tipo de Fuente y Año:** Plan de Estudios Oficial (2020)
- **URL Oficial:** [https://utpl.edu.ec/carreras/tecnologiasdelainformacion](https://utpl.edu.ec/carreras/tecnologiasdelainformacion)
- **Coordenadas:** X = 2.41, Y = 0.92 | **Radio:** 5.01 | **Afinidad:** `IT`
- **Diagnóstico Curricular:** Énfasis notable en desarrollo de software aplicado, metodologías ágiles, bases de datos y arquitectura de aplicaciones (Software Engineering - SE).

### D038 — Universidad Nacional Autónoma de Honduras (UNAH) (Honduras)
- **Título del Programa:** Ingeniería en Sistemas Computacionales — nuevo plan
- **Tipo de Fuente y Año:** Plan de Estudios Oficial (2021)
- **URL Oficial:** [https://is.unah.edu.hn/dmsdocument/19609-ing-sistemas-computacionales-unah-flujograma-pdf](https://is.unah.edu.hn/dmsdocument/19609-ing-sistemas-computacionales-unah-flujograma-pdf)
- **Coordenadas:** X = 0.95, Y = 0.61 | **Radio:** 5.59 | **Afinidad:** `IT`
- **Diagnóstico Curricular:** Perfil equilibrado con predominio de ingeniería de software, desarrollo aplicado y bases de datos (Software Engineering - SE).

### D039 — Universidad de los Andes (UniAndes) (Colombia)
- **Título del Programa:** Ingeniería de Sistemas y Computación — plan ISIS 134
- **Tipo de Fuente y Año:** Plan de Estudios Oficial (2018)
- **URL Oficial:** [https://sistemas.uniandes.edu.co/es/pregrado/plan-de-estudios](https://sistemas.uniandes.edu.co/es/pregrado/plan-de-estudios)
- **Coordenadas:** X = 0.24, Y = 0.67 | **Radio:** 5.28 | **Afinidad:** `IT`
- **Diagnóstico Curricular:** Fuerte núcleo algorítmico, teoría de la computación, estructuras y sistemas (Computer Science - CS).

### D040 — Universidad EAFIT (Colombia)
- **Título del Programa:** Ingeniería de Sistemas — plan de estudios
- **Tipo de Fuente y Año:** Plan de Estudios Oficial (2020)
- **URL Oficial:** [https://www.eafit.edu.co/pregrados/ingenieria-de-sistemas/Paginas/plan-de-estudios.aspx](https://www.eafit.edu.co/pregrados/ingenieria-de-sistemas/Paginas/plan-de-estudios.aspx)
- **Coordenadas:** X = 0.00, Y = 0.56 | **Radio:** 5.50 | **Afinidad:** `SE`
- **Diagnóstico Curricular:** Enfoque integrado entre ciencias computacionales, algoritmos, infraestructura y proyectos de software (Computer Science - CS).

### D041 — Universidad de Buenos Aires (UBA - FIUBA) (Argentina)
- **Título del Programa:** Ingeniería en Informática — plan 2020
- **Tipo de Fuente y Año:** Plan de Estudios Oficial (2020)
- **URL Oficial:** [https://www.fi.uba.ar/grado/carreras/ingenieria-en-informatica/plan-de-estudios](https://www.fi.uba.ar/grado/carreras/ingenieria-en-informatica/plan-de-estudios)
- **Coordenadas:** X = -1.02, Y = 0.18 | **Radio:** 5.25 | **Afinidad:** `CS`
- **Diagnóstico Curricular:** Plan riguroso con base formal en algoritmos, sistemas operativos, redes y compiladores (Computer Science - CS).

### D042 — Pontificia Universidad Católica de Chile (PUC Chile) (Chile)
- **Título del Programa:** Licenciatura en Ciencias de la Ingeniería / Civil Computación
- **Tipo de Fuente y Año:** Plan de Estudios Oficial (2020)
- **URL Oficial:** [https://www.ing.uc.cl/programas-de-estudio/pregrado/licenciatura-en-ingenieria-en-ciencia-de-la-computacion/](https://www.ing.uc.cl/programas-de-estudio/pregrado/licenciatura-en-ingenieria-en-ciencia-de-la-computacion/)
- **Coordenadas:** X = -0.83, Y = 0.00 | **Radio:** 5.26 | **Afinidad:** `SE`
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
- **Coordenadas:** X = 0.06, Y = -0.52 | **Radio:** 5.45 | **Afinidad:** `IT`
- **Diagnóstico Curricular:** Orientación equilibrada de ingeniería en computación cubriendo algoritmos, arquitectura y software (Computer Science - CS).

### D045 — Tecnológico de Monterrey (ITESM) (México)
- **Título del Programa:** Ingeniería en Tecnologías Computacionales — modelo Tec21
- **Tipo de Fuente y Año:** Plan de Estudios Oficial (2019)
- **URL Oficial:** [https://tec.mx/es/ingenieria-y-ciencias/ingenieria-en-tecnologias-computacionales](https://tec.mx/es/ingenieria-y-ciencias/ingenieria-en-tecnologias-computacionales)
- **Coordenadas:** X = 0.00, Y = -0.39 | **Radio:** 5.43 | **Afinidad:** `CS`
- **Diagnóstico Curricular:** Modelo de retos Tec21 con fuerte base de ciencias fundamentales, algoritmia y modelación matemática computacional (Computer Science - CS).

## 6. Advertencias y Limitaciones Metodológicas
1. **Auditabilidad y Reglas:** Las coordenadas son el resultado de un conjunto explícito y público de expresiones regulares aplicadas a las asignaturas del plan. Modificaciones razonables en las reglas pueden desplazar los puntos.
2. **Afinidad Disciplinar Provisional:** Las categorías (CS, CE, SE, IT, IS) responden a umbrales de composición relativa de áreas ($Ch, Cs, Co, Pt, Pa$) y no constituyen certificaciones oficiales de ACM/IEEE CC2020.
3. **Interpretación del Radio:** El radio describe la dispersión interna entre componentes curriculares polares en el espacio conceptual, no un error de muestreo ni intervalo de confianza estadística.
4. **Heterogeneidad de Métricas de Peso:** Mientras instituciones como UBA, UNLP y UNLPam reportan horas reloj, otras como UNAM, TecNM, PUCP y UniAndes reportan créditos académicos. El análisis compara las proporciones normalizadas internas de cada programa.