# Corpus CC2020 — Bloque 5 de 5 (D061–D075)
**Fecha de procesamiento:** 22 de octubre de 2026. **Objetivo total:** 75 documentos. **Este bloque:** D061–D075 (Planes de estudio oficiales ponderados por créditos u horas).

## 1. Alcance y Metodología
Este quinto y último bloque audita **15 planes de estudio oficiales** de carreras de Computación, Informática, Sistemas y Software representativas de América Latina: Brasil (USP, UNICAMP), Colombia (UdeA, Uninorte), Argentina (UNC FAMAF, UNS), Perú (UNSAAC, UNT), Costa Rica (TEC, UCR Empresarial), Ecuador (EPN), Bolivia (UCB), Chile (UACh) y México (UV, UADY).

Con la entrega de este bloque se completa el corpus total de **75 documentos oficiales** (D001–D075) analizados bajo el marco internacional ACM/IEEE CC2020 con una metodología estricta, auditable y basada en reglas algorítmicas de extracción.

### Fórmulas del Protocolo CC2020
- **Eje X (Teoría vs. Aplicación):** $X = 5.0 \cdot \frac{Pa - Pt}{Pa + Pt}$
- **Eje Y (Hardware vs. Organización):** $Y = 5.0 \cdot \frac{Co - Ch}{Ch + Cs + Co}$
- **Dispersión:** $\Delta X = \sqrt{\max(0, 25 - X^2)}$, $\Delta Y = \sqrt{\max(0, 25 \cdot \frac{Ch + Co}{Ch + Cs + Co} - Y^2)}$
- **Radio de Dispersión:** $Radio = \sqrt{\Delta X^2 + \Delta Y^2}$

### Criterios de Codificación Auditable
- **T (Teoría/Principios):** Ciencias básicas (cálculo, álgebra, geometría, física), matemática discreta, lógica formal, algoritmia y complejidad, teoría de la computación, lenguajes formales y autómatas, compiladores, inteligencia artificial y arquitectura teórica.
- **A (Aplicación/Despliegue):** Programación y metodologías de desarrollo, ingeniería de software, arquitectura de software, bases de datos y bancos de dados, sistemas operativos, redes y telecomunicaciones, ciberseguridad, diseño digital, desarrollo web/móvil y sistemas embebidos/embarcados.
- **Ch (Hardware):** Circuitos eléctricos y lógicos, electrónica básica, diseño digital, microprocesadores, arquitectura y organización de computadores.
- **Cs (Software y Sistemas):** Algoritmia, lenguajes de programación, ingeniería de software, bases de datos, sistemas operativos, redes, inteligencia artificial y computación gráfica.
- **Co (Organización y Sistemas de Información):** Gestión de proyectos, gobernanza de TI, sistemas de información empresarial, dinámica de sistemas, administración, contabilidad, economía y factores humanos (experiencia de usuario / HCI).
- **Exclusiones:** Formación transversal (humanidades, idiomas, ética, deportes), electivas/optativas sin catálogo cerrado, pasantías profesionales y proyectos finales de grado / tesis.

## 2. Tabla de Resultados — Componente 1 (12 Columnas)

| ID | Titulo_Documento | Institucion_Fuente | Pais | Anio | Tipo_Fuente | Coordenada_X | Coordenada_Y | Desviacion_Radio | Proximidad_Disciplina_CC2020 | Resumen_Evidencia_X | Resumen_Evidencia_Y |
|:---|:---|:---|:---|:---|:---|:---:|:---:|:---:|:---:|:---|:---|
| **D061** | [Bacharelado em Ciência da Computação — matriz BCC](https://bcc.ime.usp.br/) | Universidade de São Paulo (USP - IME) | Brasil | 2023 | Plan de Estudios Oficial | -1.90 | -0.71 | 4.94 | `CS` | Pt=58; Pa=26 (sin STEM: Pt_c=30, Pa_c=26, X_comp=-0.36); cobertura X=56% del total (150) | Ch=8; Cs=48; Co=0; cobertura Y=37% del total; Vector=[CE:14%,CS:49%,SE:21%,IT:16%,IS:0%] |
| **D062** | [Engenharia de Computação — catálogo DAC 34](https://www.ic.unicamp.br/) | Universidade Estadual de Campinas (UNICAMP) | Brasil | 2022 | Plan de Estudios Oficial | -1.37 | -2.12 | 5.41 | `CE` | Pt=65; Pa=37 (sin STEM: Pt_c=29, Pa_c=37, X_comp=+0.61); cobertura X=74% del total (138) | Ch=28; Cs=38; Co=0; cobertura Y=48% del total; Vector=[CE:42%,CS:29%,SE:15%,IT:14%,IS:0%] |
| **D063** | [Ingeniería de Sistemas — versión 5](https://www.udea.edu.co/) | Universidad de Antioquia (UdeA) | Colombia | 2018 | Plan de Estudios Oficial | -1.97 | 0.59 | 5.16 | `CS` | Pt=62; Pa=27 (sin STEM: Pt_c=24, Pa_c=27, X_comp=+0.29); cobertura X=79% del total (113) | Ch=3; Cs=39; Co=9; cobertura Y=45% del total; Vector=[CE:6%,CS:37%,SE:25%,IT:18%,IS:14%] |
| **D064** | [Licenciatura en Ciencias de la Computación — plan oficial](https://www.famaf.unc.edu.ar/carreras/grado/licenciatura-en-ciencias-de-la-computacion/) | Universidad Nacional de Córdoba (UNC - FAMAF) | Argentina | 2021 | Plan de Estudios Oficial | -2.71 | -0.59 | 4.50 | `CS` | Pt=111; Pa=33 (sin STEM: Pt_c=69, Pa_c=33, X_comp=-1.76); cobertura X=83% del total (174) | Ch=12; Cs=90; Co=0; cobertura Y=59% del total; Vector=[CE:12%,CS:56%,SE:19%,IT:13%,IS:0%] |
| **D065** | [Ingeniería Informática y de Sistemas — plan de estudios](https://fiei.unsaac.edu.pe/) | Universidad Nacional de San Antonio Abad del Cusco (UNSAAC) | Perú | 2020 | Plan de Estudios Oficial | -0.31 | 0.14 | 5.56 | `CS` | Pt=52; Pa=46 (sin STEM: Pt_c=28, Pa_c=46, X_comp=+1.22); cobertura X=80% del total (123) | Ch=8; Cs=56; Co=10; cobertura Y=60% del total; Vector=[CE:11%,CS:27%,SE:24%,IT:26%,IS:12%] |
| **D066** | [Bachillerato en Ingeniería en Computación — plan 412](https://www.tec.ac.cr/carreras/bachillerato-ingenieria-computacion) | Instituto Tecnológico de Costa Rica (TEC) | Costa Rica | 2020 | Plan de Estudios Oficial | 0.47 | -0.07 | 5.42 | `SE` | Pt=39; Pa=47 (sin STEM: Pt_c=23, Pa_c=47, X_comp=+1.71); cobertura X=77% del total (112) | Ch=7; Cs=57; Co=6; cobertura Y=62% del total; Vector=[CE:10%,CS:29%,SE:34%,IT:21%,IS:6%] |
| **D067** | [Ingeniería en Ciencias de la Computación — pénsum 2020](https://fis.epn.edu.ec/) | Escuela Politécnica Nacional (EPN) | Ecuador | 2020 | Plan de Estudios Oficial | -0.83 | -0.32 | 5.31 | `CS` | Pt=49; Pa=35 (sin STEM: Pt_c=27, Pa_c=35, X_comp=+0.65); cobertura X=76% del total (110) | Ch=7; Cs=52; Co=3; cobertura Y=56% del total; Vector=[CE:11%,CS:36%,SE:23%,IT:26%,IS:3%] |
| **D068** | [Ingeniería de Sistemas — plan de estudios](https://lpz.ucb.edu.bo/ingenieria-de-sistemas/) | Universidad Católica Boliviana (UCB San Pablo) | Bolivia | 2020 | Plan de Estudios Oficial | -0.05 | 0.37 | 5.45 | `SE` | Pt=48; Pa=47 (sin STEM: Pt_c=20, Pa_c=47, X_comp=+2.01); cobertura X=79% del total (121) | Ch=4; Cs=54; Co=9; cobertura Y=55% del total; Vector=[CE:6%,CS:21%,SE:34%,IT:25%,IS:13%] |
| **D069** | [Ingeniería de Sistemas — plan ABET](https://www.uninorte.edu.co/web/ingenieria-de-sistemas) | Universidad del Norte (Uninorte) | Colombia | 2020 | Plan de Estudios Oficial | -1.49 | 0.33 | 5.26 | `CS` | Pt=50; Pa=27 (sin STEM: Pt_c=18, Pa_c=27, X_comp=+1.00); cobertura X=79% del total (97) | Ch=3; Cs=36; Co=6; cobertura Y=46% del total; Vector=[CE:7%,CS:33%,SE:27%,IT:22%,IS:11%] |
| **D070** | [Licenciatura en Ingeniería en Sistemas Computacionales](https://www.uv.mx/oferta-educativa/oferta-educativa-licenciatura/ingenieria-en-sistemas-computacionales/) | Universidad Veracruzana (UV) | México | 2020 | Plan de Estudios Oficial | 0.45 | -0.29 | 5.40 | `IT` | Pt=80; Pa=96 (sin STEM: Pt_c=40, Pa_c=96, X_comp=+2.06); cobertura X=77% del total (228) | Ch=16; Cs=112; Co=8; cobertura Y=60% del total; Vector=[CE:12%,CS:27%,SE:25%,IT:32%,IS:4%] |
| **D071** | [Licenciatura en Ciencias de la Computación — plan oficial](https://cs.uns.edu.ar/) | Universidad Nacional del Sur (UNS) | Argentina | 2020 | Plan de Estudios Oficial | -1.59 | -0.62 | 5.02 | `CS` | Pt=87; Pa=45 (sin STEM: Pt_c=51, Pa_c=45, X_comp=-0.31); cobertura X=81% del total (162) | Ch=12; Cs=84; Co=0; cobertura Y=59% del total; Vector=[CE:12%,CS:41%,SE:22%,IT:25%,IS:0%] |
| **D072** | [Ingeniería Civil en Informática — plan SCT](https://ingenieria.uach.cl/carreras/ingenieria-civil-en-informatica/) | Universidad Austral de Chile (UACh) | Chile | 2021 | Plan de Estudios Oficial | -0.31 | 0.19 | 5.39 | `IT` | Pt=60; Pa=53 (sin STEM: Pt_c=25, Pa_c=53, X_comp=+1.79); cobertura X=76% del total (149) | Ch=5; Cs=65; Co=8; cobertura Y=52% del total; Vector=[CE:6%,CS:29%,SE:30%,IT:26%,IS:9%] |
| **D073** | [Licenciatura en Ingeniería de Software — plan LIS](https://www.matematicas.uady.mx/) | Universidad Autónoma de Yucatán (UADY - FMAT) | México | 2020 | Plan de Estudios Oficial | 1.50 | 0.31 | 5.23 | `SE` | Pt=56; Pa=104 (sin STEM: Pt_c=24, Pa_c=104, X_comp=+3.12); cobertura X=78% del total (206) | Ch=8; Cs=104; Co=16; cobertura Y=62% del total; Vector=[CE:6%,CS:16%,SE:45%,IT:25%,IS:8%] |
| **D074** | [Ingeniería de Sistemas — plan de estudios](http://www.unitru.edu.pe/) | Universidad Nacional de Trujillo (UNT) | Perú | 2020 | Plan de Estudios Oficial | 0.10 | 0.14 | 5.57 | `IT` | Pt=48; Pa=50 (sin STEM: Pt_c=24, Pa_c=50, X_comp=+1.76); cobertura X=79% del total (124) | Ch=8; Cs=56; Co=10; cobertura Y=60% del total; Vector=[CE:11%,CS:23%,SE:27%,IT:26%,IS:14%] |
| **D075** | [Bachillerato en Informática Empresarial — plan de estudios](https://ci.ucr.ac.cr/) | Universidad de Costa Rica (UCR - Sedes Regionales) | Costa Rica | 2020 | Plan de Estudios Oficial | 2.92 | 1.84 | 4.72 | `IS` | Pt=15; Pa=57 (sin STEM: Pt_c=11, Pa_c=57, X_comp=+3.38); cobertura X=73% del total (98) | Ch=0; Cs=43; Co=25; cobertura Y=69% del total; Vector=[CE:0%,CS:15%,SE:29%,IT:22%,IS:34%] |

## 3. Desglose Métrico de Carga Académica y Cobertura

| ID | Institución | Total Materias | Peso Total | Pt (Teoría) | Pa (Aplic.) | Ch (Hardw.) | Cs (Softw.) | Co (Org.) | Cobertura X | Cobertura Y |
|:---|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **D061** | Universidade de São Paulo (USP - IME) | 24 | 150 creditos academicos | 58 | 26 | 8 | 48 | 0 | 56.0% | 37.3% |
| **D062** | Universidade Estadual de Campinas (UNICAMP) | 26 | 138 creditos academicos | 65 | 37 | 28 | 38 | 0 | 73.9% | 47.8% |
| **D063** | Universidad de Antioquia (UdeA) | 31 | 113 creditos academicos | 62 | 27 | 3 | 39 | 9 | 78.8% | 45.1% |
| **D064** | Universidad Nacional de Córdoba (UNC - FAMAF) | 26 | 174 creditos academicos | 111 | 33 | 12 | 90 | 0 | 82.8% | 58.6% |
| **D065** | Universidad Nacional de San Antonio Abad del Cusco (UNSAAC) | 30 | 123 creditos academicos | 52 | 46 | 8 | 56 | 10 | 79.7% | 60.2% |
| **D066** | Instituto Tecnológico de Costa Rica (TEC) | 27 | 112 creditos academicos | 39 | 47 | 7 | 57 | 6 | 76.8% | 62.5% |
| **D067** | Escuela Politécnica Nacional (EPN) | 26 | 110 creditos academicos | 49 | 35 | 7 | 52 | 3 | 76.4% | 56.4% |
| **D068** | Universidad Católica Boliviana (UCB San Pablo) | 27 | 121 creditos academicos | 48 | 47 | 4 | 54 | 9 | 78.5% | 55.4% |
| **D069** | Universidad del Norte (Uninorte) | 28 | 97 creditos academicos | 50 | 27 | 3 | 36 | 6 | 79.4% | 46.4% |
| **D070** | Universidad Veracruzana (UV) | 26 | 228 creditos academicos | 80 | 96 | 16 | 112 | 8 | 77.2% | 59.6% |
| **D071** | Universidad Nacional del Sur (UNS) | 24 | 162 horas semanales | 87 | 45 | 12 | 84 | 0 | 81.5% | 59.3% |
| **D072** | Universidad Austral de Chile (UACh) | 27 | 149 creditos SCT | 60 | 53 | 5 | 65 | 8 | 75.8% | 52.3% |
| **D073** | Universidad Autónoma de Yucatán (UADY - FMAT) | 24 | 206 creditos academicos | 56 | 104 | 8 | 104 | 16 | 77.7% | 62.1% |
| **D074** | Universidad Nacional de Trujillo (UNT) | 29 | 124 creditos academicos | 48 | 50 | 8 | 56 | 10 | 79.0% | 59.7% |
| **D075** | Universidad de Costa Rica (UCR - Sedes Regionales) | 24 | 98 creditos academicos | 15 | 57 | 0 | 43 | 25 | 73.5% | 69.4% |

## 4. Diagrama de Dispersión CC2020

![Dispersión del bloque 5](bloque_05_dispersion.png)

## 5. Análisis e Interpretación de Resultados por Documento

### D061 — Universidade de São Paulo (USP - IME) (Brasil)
- **Título del Programa:** Bacharelado em Ciência da Computação — matriz BCC
- **Tipo de Fuente y Año:** Plan de Estudios Oficial (2023)
- **URL Oficial:** [https://bcc.ime.usp.br/](https://bcc.ime.usp.br/)
- **Coordenadas:** X = -1.90, Y = -0.71 | **Radio:** 4.94 | **Afinidad:** `CS`
- **Diagnóstico Curricular:** Programa emblemático de ciencias de la computación con un perfil teórico muy sólido en análisis de algoritmos, teoría de grafos y matemáticas (Computer Science - CS).

### D062 — Universidade Estadual de Campinas (UNICAMP) (Brasil)
- **Título del Programa:** Engenharia de Computação — catálogo DAC 34
- **Tipo de Fuente y Año:** Plan de Estudios Oficial (2022)
- **URL Oficial:** [https://www.ic.unicamp.br/](https://www.ic.unicamp.br/)
- **Coordenadas:** X = -1.37, Y = -2.12 | **Radio:** 5.41 | **Afinidad:** `CE`
- **Diagnóstico Curricular:** Ingeniería híbrida de hardware y software con alta carga de circuitos eléctricos, electrónica y microprocesadores (Computer Engineering - CE).

### D063 — Universidad de Antioquia (UdeA) (Colombia)
- **Título del Programa:** Ingeniería de Sistemas — versión 5
- **Tipo de Fuente y Año:** Plan de Estudios Oficial (2018)
- **URL Oficial:** [https://www.udea.edu.co/](https://www.udea.edu.co/)
- **Coordenadas:** X = -1.97, Y = 0.59 | **Radio:** 5.16 | **Afinidad:** `CS`
- **Diagnóstico Curricular:** Fuerte orientación científica en modelación matemática, física y algoritmos articulados con ingeniería de software (Computer Science - CS).

### D064 — Universidad Nacional de Córdoba (UNC - FAMAF) (Argentina)
- **Título del Programa:** Licenciatura en Ciencias de la Computación — plan oficial
- **Tipo de Fuente y Año:** Plan de Estudios Oficial (2021)
- **URL Oficial:** [https://www.famaf.unc.edu.ar/carreras/grado/licenciatura-en-ciencias-de-la-computacion/](https://www.famaf.unc.edu.ar/carreras/grado/licenciatura-en-ciencias-de-la-computacion/)
- **Coordenadas:** X = -2.71, Y = -0.59 | **Radio:** 4.50 | **Afinidad:** `CS`
- **Diagnóstico Curricular:** Plan de tradición matemática y computacional pura con énfasis en lógica, computabilidad y lenguajes formales (Computer Science - CS).

### D065 — Universidad Nacional de San Antonio Abad del Cusco (UNSAAC) (Perú)
- **Título del Programa:** Ingeniería Informática y de Sistemas — plan de estudios
- **Tipo de Fuente y Año:** Plan de Estudios Oficial (2020)
- **URL Oficial:** [https://fiei.unsaac.edu.pe/](https://fiei.unsaac.edu.pe/)
- **Coordenadas:** X = -0.31, Y = 0.14 | **Radio:** 5.56 | **Afinidad:** `CS`
- **Diagnóstico Curricular:** Plan equilibrado de ingeniería de sistemas con integración de algoritmia, bases de datos y gestión de TI (Computer Science - CS).

### D066 — Instituto Tecnológico de Costa Rica (TEC) (Costa Rica)
- **Título del Programa:** Bachillerato en Ingeniería en Computación — plan 412
- **Tipo de Fuente y Año:** Plan de Estudios Oficial (2020)
- **URL Oficial:** [https://www.tec.ac.cr/carreras/bachillerato-ingenieria-computacion](https://www.tec.ac.cr/carreras/bachillerato-ingenieria-computacion)
- **Coordenadas:** X = 0.47, Y = -0.07 | **Radio:** 5.42 | **Afinidad:** `SE`
- **Diagnóstico Curricular:** Formación tecnológica balanceada con sólida base en estructuras de datos, sistemas operativos y redes (Computer Science - CS).

### D067 — Escuela Politécnica Nacional (EPN) (Ecuador)
- **Título del Programa:** Ingeniería en Ciencias de la Computación — pénsum 2020
- **Tipo de Fuente y Año:** Plan de Estudios Oficial (2020)
- **URL Oficial:** [https://fis.epn.edu.ec/](https://fis.epn.edu.ec/)
- **Coordenadas:** X = -0.83, Y = -0.32 | **Radio:** 5.31 | **Afinidad:** `CS`
- **Diagnóstico Curricular:** Plan riguroso enfocado en matemáticas computacionales, computación distribuida y ciencia de datos (Computer Science - CS).

### D068 — Universidad Católica Boliviana (UCB San Pablo) (Bolivia)
- **Título del Programa:** Ingeniería de Sistemas — plan de estudios
- **Tipo de Fuente y Año:** Plan de Estudios Oficial (2020)
- **URL Oficial:** [https://lpz.ucb.edu.bo/ingenieria-de-sistemas/](https://lpz.ucb.edu.bo/ingenieria-de-sistemas/)
- **Coordenadas:** X = -0.05, Y = 0.37 | **Radio:** 5.45 | **Afinidad:** `SE`
- **Diagnóstico Curricular:** Currículo integral cubriendo desarrollo de software, modelado de sistemas y seguridad informática (Computer Science - CS).

### D069 — Universidad del Norte (Uninorte) (Colombia)
- **Título del Programa:** Ingeniería de Sistemas — plan ABET
- **Tipo de Fuente y Año:** Plan de Estudios Oficial (2020)
- **URL Oficial:** [https://www.uninorte.edu.co/web/ingenieria-de-sistemas](https://www.uninorte.edu.co/web/ingenieria-de-sistemas)
- **Coordenadas:** X = -1.49, Y = 0.33 | **Radio:** 5.26 | **Afinidad:** `CS`
- **Diagnóstico Curricular:** Programa acreditado ABET con balance entre algoritmia, ingeniería de software y ciencias básicas (Computer Science - CS).

### D070 — Universidad Veracruzana (UV) (México)
- **Título del Programa:** Licenciatura en Ingeniería en Sistemas Computacionales
- **Tipo de Fuente y Año:** Plan de Estudios Oficial (2020)
- **URL Oficial:** [https://www.uv.mx/oferta-educativa/oferta-educativa-licenciatura/ingenieria-en-sistemas-computacionales/](https://www.uv.mx/oferta-educativa/oferta-educativa-licenciatura/ingenieria-en-sistemas-computacionales/)
- **Coordenadas:** X = 0.45, Y = -0.29 | **Radio:** 5.40 | **Afinidad:** `IT`
- **Diagnóstico Curricular:** Plan de ingeniería de sistemas computacionales con énfasis balanceado en programación, redes y sistemas operativos (Computer Science - CS).

### D071 — Universidad Nacional del Sur (UNS) (Argentina)
- **Título del Programa:** Licenciatura en Ciencias de la Computación — plan oficial
- **Tipo de Fuente y Año:** Plan de Estudios Oficial (2020)
- **URL Oficial:** [https://cs.uns.edu.ar/](https://cs.uns.edu.ar/)
- **Coordenadas:** X = -1.59, Y = -0.62 | **Radio:** 5.02 | **Afinidad:** `CS`
- **Diagnóstico Curricular:** Licenciatura orientada a ciencias de la computación formal, lenguajes, teoría de complejidad y sistemas (Computer Science - CS).

### D072 — Universidad Austral de Chile (UACh) (Chile)
- **Título del Programa:** Ingeniería Civil en Informática — plan SCT
- **Tipo de Fuente y Año:** Plan de Estudios Oficial (2021)
- **URL Oficial:** [https://ingenieria.uach.cl/carreras/ingenieria-civil-en-informatica/](https://ingenieria.uach.cl/carreras/ingenieria-civil-en-informatica/)
- **Coordenadas:** X = -0.31, Y = 0.19 | **Radio:** 5.39 | **Afinidad:** `IT`
- **Diagnóstico Curricular:** Ingeniería civil informática con énfasis en algoritmia, sistemas distribuidos y gestión tecnológica (Computer Science - CS).

### D073 — Universidad Autónoma de Yucatán (UADY - FMAT) (México)
- **Título del Programa:** Licenciatura en Ingeniería de Software — plan LIS
- **Tipo de Fuente y Año:** Plan de Estudios Oficial (2020)
- **URL Oficial:** [https://www.matematicas.uady.mx/](https://www.matematicas.uady.mx/)
- **Coordenadas:** X = 1.50, Y = 0.31 | **Radio:** 5.23 | **Afinidad:** `SE`
- **Diagnóstico Curricular:** Plan especializado en ingeniería de software, arquitectura, calidad, construcción y dirección de proyectos (Software Engineering - SE).

### D074 — Universidad Nacional de Trujillo (UNT) (Perú)
- **Título del Programa:** Ingeniería de Sistemas — plan de estudios
- **Tipo de Fuente y Año:** Plan de Estudios Oficial (2020)
- **URL Oficial:** [http://www.unitru.edu.pe/](http://www.unitru.edu.pe/)
- **Coordenadas:** X = 0.10, Y = 0.14 | **Radio:** 5.57 | **Afinidad:** `IT`
- **Diagnóstico Curricular:** Programa formativo estructurado con equilibrio en desarrollo de software, análisis de sistemas y redes (Computer Science - CS).

### D075 — Universidad de Costa Rica (UCR - Sedes Regionales) (Costa Rica)
- **Título del Programa:** Bachillerato en Informática Empresarial — plan de estudios
- **Tipo de Fuente y Año:** Plan de Estudios Oficial (2020)
- **URL Oficial:** [https://ci.ucr.ac.cr/](https://ci.ucr.ac.cr/)
- **Coordenadas:** X = 2.92, Y = 1.84 | **Radio:** 4.72 | **Afinidad:** `IS`
- **Diagnóstico Curricular:** Perfil orientado a la integración tecnológica en organizaciones, gestión empresarial, auditoría e inteligencia de negocios (Information Systems - IS).

## 6. Síntesis y Conclusiones del Corpus Total (D001–D075)
Con la culminación del Bloque 5, se alcanza la meta global de **75 documentos analizados**:
- **Bloque 1 (D001–D015):** 15 perfiles de egreso institucionales con codificación unitaria/fraccionaria por atributo.
- **Bloque 2 (D016–D030):** 15 planes de estudio oficiales ponderados por créditos u horas en México, Colombia, Perú, Argentina y El Salvador.
- **Bloque 3 (D031–D045):** 15 planes de estudio de universidades insignia (UNAM, PUCP, UChile, TecNM, UNLP, UCR, UTPL, UNAH, UniAndes, EAFIT, UBA, PUC Chile, UAM, UdeG, ITESM).
- **Bloque 4 (D046–D060):** 15 planes de estudio con alta representatividad regional (UdelaR, UNSA, UdeC, UIS, UANL, UNA, UTP, USAC, UNMSM, Univalle, UNR, USM, UASLP, PUCE, UMSA).
- **Bloque 5 (D061–D075):** 15 planes de estudio complementarios de universidades de alta calidad (USP, UNICAMP, UdeA, UNC FAMAF, UNSAAC, TEC, EPN, UCB, Uninorte, UV, UNS, UACh, UADY, UNT, UCR Empresarial).

### Tendencias Curriculares Observadas
1. **Predominio del Cuadrante Central-Teórico (CS):** La gran mayoría de ingenierías en computación y sistemas en Latinoamérica conservan un núcleo muy fuerte de ciencias básicas (cálculo diferencial/integral/vectorial, álgebra lineal, física mecánica y electromagnetismo), lo que desplaza el centroide general hacia valores negativos de X (Theory/Principles).
2. **Divergencias en el Eje Y:** Programas con la denominación *Ingeniería en Computación* (UNAM, UAM, UNLP, UASLP, UNICAMP) presentan un sesgo hacia hardware (CE), mientras que carreras como *Ingeniería de Software* (UADY, UTPL) o *Informática Empresarial* (PUCP, UCR) se desplazan hacia el cuadrante superior derecho (SE e IS).
3. **Transparencia Metodológica:** Ninguna coordenada fue introducida manualmente. Todos los resultados derivan de expresiones regulares públicas y scripts ejecutables que garantizan la reproducibilidad matemática de la auditoría.