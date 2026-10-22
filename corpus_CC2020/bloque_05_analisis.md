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
| **D061** | [Bacharelado em Ciência da Computação — matriz BCC](https://bcc.ime.usp.br/) | Universidade de São Paulo (USP - IME) | Brasil | 2023 | Plan de Estudios Oficial | -1.82 | -0.67 | 4.96 | `CS` | Pt=60; Pa=28 créditos; cobertura X=59% del total (150) | Ch=8; Cs=52; Co=0 créditos; cobertura Y=40% del total |
| **D062** | [Engenharia de Computação — catálogo DAC 34](https://www.ic.unicamp.br/) | Universidade Estadual de Campinas (UNICAMP) | Brasil | 2022 | Plan de Estudios Oficial | -1.27 | -2.12 | 5.43 | `CE` | Pt=64; Pa=38 créditos; cobertura X=74% del total (138) | Ch=28; Cs=38; Co=0 créditos; cobertura Y=48% del total |
| **D063** | [Ingeniería de Sistemas — versión 5](https://www.udea.edu.co/) | Universidad de Antioquia (UdeA) | Colombia | 2018 | Plan de Estudios Oficial | -1.97 | 0.59 | 5.16 | `CS` | Pt=62; Pa=27 créditos; cobertura X=79% del total (113) | Ch=3; Cs=39; Co=9 créditos; cobertura Y=45% del total |
| **D064** | [Licenciatura en Ciencias de la Computación — plan oficial](https://www.famaf.unc.edu.ar/carreras/grado/licenciatura-en-ciencias-de-la-computacion/) | Universidad Nacional de Córdoba (UNC - FAMAF) | Argentina | 2021 | Plan de Estudios Oficial | -2.92 | -0.59 | 4.37 | `CS` | Pt=114; Pa=30 créditos; cobertura X=83% del total (174) | Ch=12; Cs=90; Co=0 créditos; cobertura Y=59% del total |
| **D065** | [Ingeniería Informática y de Sistemas — plan de estudios](https://fiei.unsaac.edu.pe/) | Universidad Nacional de San Antonio Abad del Cusco (UNSAAC) | Perú | 2020 | Plan de Estudios Oficial | -0.31 | 0.14 | 5.56 | `CS` | Pt=52; Pa=46 créditos; cobertura X=80% del total (123) | Ch=8; Cs=56; Co=10 créditos; cobertura Y=60% del total |
| **D066** | [Bachillerato en Ingeniería en Computación — plan 412](https://www.tec.ac.cr/carreras/bachillerato-ingenieria-computacion) | Instituto Tecnológico de Costa Rica (TEC) | Costa Rica | 2020 | Plan de Estudios Oficial | 0.00 | -0.07 | 5.44 | `CS` | Pt=43; Pa=43 créditos; cobertura X=77% del total (112) | Ch=7; Cs=57; Co=6 créditos; cobertura Y=62% del total |
| **D067** | [Ingeniería en Ciencias de la Computación — pénsum 2020](https://fis.epn.edu.ec/) | Escuela Politécnica Nacional (EPN) | Ecuador | 2020 | Plan de Estudios Oficial | -0.83 | -0.32 | 5.31 | `CS` | Pt=49; Pa=35 créditos; cobertura X=76% del total (110) | Ch=7; Cs=52; Co=3 créditos; cobertura Y=56% del total |
| **D068** | [Ingeniería de Sistemas — plan de estudios](https://lpz.ucb.edu.bo/ingenieria-de-sistemas/) | Universidad Católica Boliviana (UCB San Pablo) | Bolivia | 2020 | Plan de Estudios Oficial | -0.05 | 0.22 | 5.39 | `CS` | Pt=48; Pa=47 créditos; cobertura X=79% del total (121) | Ch=4; Cs=56; Co=7 créditos; cobertura Y=55% del total |
| **D069** | [Ingeniería de Sistemas — plan ABET](https://www.uninorte.edu.co/web/ingenieria-de-sistemas) | Universidad del Norte (Uninorte) | Colombia | 2020 | Plan de Estudios Oficial | -1.10 | 0.33 | 5.35 | `CS` | Pt=47; Pa=30 créditos; cobertura X=79% del total (97) | Ch=3; Cs=36; Co=6 créditos; cobertura Y=46% del total |
| **D070** | [Licenciatura en Ingeniería en Sistemas Computacionales](https://www.uv.mx/oferta-educativa/oferta-educativa-licenciatura/ingenieria-en-sistemas-computacionales/) | Universidad Veracruzana (UV) | México | 2020 | Plan de Estudios Oficial | 0.00 | -0.59 | 5.53 | `CS` | Pt=88; Pa=88 créditos; cobertura X=77% del total (228) | Ch=24; Cs=104; Co=8 créditos; cobertura Y=60% del total |
| **D071** | [Licenciatura en Ciencias de la Computación — plan oficial](https://cs.uns.edu.ar/) | Universidad Nacional del Sur (UNS) | Argentina | 2020 | Plan de Estudios Oficial | -1.36 | -0.62 | 5.09 | `CS` | Pt=84; Pa=48 horas; cobertura X=81% del total (162) | Ch=12; Cs=84; Co=0 horas; cobertura Y=59% del total |
| **D072** | [Ingeniería Civil en Informática — plan SCT](https://ingenieria.uach.cl/carreras/ingenieria-civil-en-informatica/) | Universidad Austral de Chile (UACh) | Chile | 2021 | Plan de Estudios Oficial | -0.31 | 0.19 | 5.39 | `CS` | Pt=60; Pa=53 créditos SCT; cobertura X=76% del total (149) | Ch=5; Cs=65; Co=8 créditos SCT; cobertura Y=52% del total |
| **D073** | [Licenciatura en Ingeniería de Software — plan LIS](https://www.matematicas.uady.mx/) | Universidad Autónoma de Yucatán (UADY - FMAT) | México | 2020 | Plan de Estudios Oficial | 1.50 | 0.31 | 5.23 | `SE` | Pt=56; Pa=104 créditos; cobertura X=78% del total (206) | Ch=8; Cs=104; Co=16 créditos; cobertura Y=62% del total |
| **D074** | [Ingeniería de Sistemas — plan de estudios](http://www.unitru.edu.pe/) | Universidad Nacional de Trujillo (UNT) | Perú | 2020 | Plan de Estudios Oficial | 0.10 | 0.14 | 5.57 | `CS` | Pt=48; Pa=50 créditos; cobertura X=79% del total (124) | Ch=8; Cs=56; Co=10 créditos; cobertura Y=60% del total |
| **D075** | [Bachillerato en Informática Empresarial — plan de estudios](https://ci.ucr.ac.cr/) | Universidad de Costa Rica (UCR - Sedes Regionales) | Costa Rica | 2020 | Plan de Estudios Oficial | 2.60 | 1.76 | 4.89 | `IS` | Pt=18; Pa=57 créditos; cobertura X=77% del total (98) | Ch=0; Cs=46; Co=25 créditos; cobertura Y=72% del total |

## 3. Desglose Métrico de Carga Académica y Cobertura

| ID | Institución | Total Materias | Peso Total | Pt (Teoría) | Pa (Aplic.) | Ch (Hardw.) | Cs (Softw.) | Co (Org.) | Cobertura X | Cobertura Y |
|:---|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **D061** | Universidade de São Paulo (USP - IME) | 24 | 150 créditos | 60 | 28 | 8 | 52 | 0 | 58.7% | 40.0% |
| **D062** | Universidade Estadual de Campinas (UNICAMP) | 26 | 138 créditos | 64 | 38 | 28 | 38 | 0 | 73.9% | 47.8% |
| **D063** | Universidad de Antioquia (UdeA) | 31 | 113 créditos | 62 | 27 | 3 | 39 | 9 | 78.8% | 45.1% |
| **D064** | Universidad Nacional de Córdoba (UNC - FAMAF) | 26 | 174 créditos | 114 | 30 | 12 | 90 | 0 | 82.8% | 58.6% |
| **D065** | Universidad Nacional de San Antonio Abad del Cusco (UNSAAC) | 30 | 123 créditos | 52 | 46 | 8 | 56 | 10 | 79.7% | 60.2% |
| **D066** | Instituto Tecnológico de Costa Rica (TEC) | 27 | 112 créditos | 43 | 43 | 7 | 57 | 6 | 76.8% | 62.5% |
| **D067** | Escuela Politécnica Nacional (EPN) | 26 | 110 créditos | 49 | 35 | 7 | 52 | 3 | 76.4% | 56.4% |
| **D068** | Universidad Católica Boliviana (UCB San Pablo) | 27 | 121 créditos | 48 | 47 | 4 | 56 | 7 | 78.5% | 55.4% |
| **D069** | Universidad del Norte (Uninorte) | 28 | 97 créditos | 47 | 30 | 3 | 36 | 6 | 79.4% | 46.4% |
| **D070** | Universidad Veracruzana (UV) | 26 | 228 créditos | 88 | 88 | 24 | 104 | 8 | 77.2% | 59.6% |
| **D071** | Universidad Nacional del Sur (UNS) | 24 | 162 horas | 84 | 48 | 12 | 84 | 0 | 81.5% | 59.3% |
| **D072** | Universidad Austral de Chile (UACh) | 27 | 149 créditos SCT | 60 | 53 | 5 | 65 | 8 | 75.8% | 52.3% |
| **D073** | Universidad Autónoma de Yucatán (UADY - FMAT) | 24 | 206 créditos | 56 | 104 | 8 | 104 | 16 | 77.7% | 62.1% |
| **D074** | Universidad Nacional de Trujillo (UNT) | 29 | 124 créditos | 48 | 50 | 8 | 56 | 10 | 79.0% | 59.7% |
| **D075** | Universidad de Costa Rica (UCR - Sedes Regionales) | 24 | 98 créditos | 18 | 57 | 0 | 46 | 25 | 76.5% | 72.4% |

## 4. Diagrama de Dispersión CC2020

![Dispersión del bloque 5](bloque_05_dispersion.png)

## 5. Análisis e Interpretación de Resultados por Documento

### D061 — Universidade de São Paulo (USP - IME) (Brasil)
- **Título del Programa:** Bacharelado em Ciência da Computação — matriz BCC
- **Tipo de Fuente y Año:** Plan de Estudios Oficial (2023)
- **URL Oficial:** [https://bcc.ime.usp.br/](https://bcc.ime.usp.br/)
- **Coordenadas:** X = -1.82, Y = -0.67 | **Radio:** 4.96 | **Afinidad:** `CS`
- **Diagnóstico Curricular:** Programa emblemático de ciencias de la computación con un perfil teórico muy sólido en análisis de algoritmos, teoría de grafos y matemáticas (Computer Science - CS).

### D062 — Universidade Estadual de Campinas (UNICAMP) (Brasil)
- **Título del Programa:** Engenharia de Computação — catálogo DAC 34
- **Tipo de Fuente y Año:** Plan de Estudios Oficial (2022)
- **URL Oficial:** [https://www.ic.unicamp.br/](https://www.ic.unicamp.br/)
- **Coordenadas:** X = -1.27, Y = -2.12 | **Radio:** 5.43 | **Afinidad:** `CE`
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
- **Coordenadas:** X = -2.92, Y = -0.59 | **Radio:** 4.37 | **Afinidad:** `CS`
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
- **Coordenadas:** X = 0.00, Y = -0.07 | **Radio:** 5.44 | **Afinidad:** `CS`
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
- **Coordenadas:** X = -0.05, Y = 0.22 | **Radio:** 5.39 | **Afinidad:** `CS`
- **Diagnóstico Curricular:** Currículo integral cubriendo desarrollo de software, modelado de sistemas y seguridad informática (Computer Science - CS).

### D069 — Universidad del Norte (Uninorte) (Colombia)
- **Título del Programa:** Ingeniería de Sistemas — plan ABET
- **Tipo de Fuente y Año:** Plan de Estudios Oficial (2020)
- **URL Oficial:** [https://www.uninorte.edu.co/web/ingenieria-de-sistemas](https://www.uninorte.edu.co/web/ingenieria-de-sistemas)
- **Coordenadas:** X = -1.10, Y = 0.33 | **Radio:** 5.35 | **Afinidad:** `CS`
- **Diagnóstico Curricular:** Programa acreditado ABET con balance entre algoritmia, ingeniería de software y ciencias básicas (Computer Science - CS).

### D070 — Universidad Veracruzana (UV) (México)
- **Título del Programa:** Licenciatura en Ingeniería en Sistemas Computacionales
- **Tipo de Fuente y Año:** Plan de Estudios Oficial (2020)
- **URL Oficial:** [https://www.uv.mx/oferta-educativa/oferta-educativa-licenciatura/ingenieria-en-sistemas-computacionales/](https://www.uv.mx/oferta-educativa/oferta-educativa-licenciatura/ingenieria-en-sistemas-computacionales/)
- **Coordenadas:** X = 0.00, Y = -0.59 | **Radio:** 5.53 | **Afinidad:** `CS`
- **Diagnóstico Curricular:** Plan de ingeniería de sistemas computacionales con énfasis balanceado en programación, redes y sistemas operativos (Computer Science - CS).

### D071 — Universidad Nacional del Sur (UNS) (Argentina)
- **Título del Programa:** Licenciatura en Ciencias de la Computación — plan oficial
- **Tipo de Fuente y Año:** Plan de Estudios Oficial (2020)
- **URL Oficial:** [https://cs.uns.edu.ar/](https://cs.uns.edu.ar/)
- **Coordenadas:** X = -1.36, Y = -0.62 | **Radio:** 5.09 | **Afinidad:** `CS`
- **Diagnóstico Curricular:** Licenciatura orientada a ciencias de la computación formal, lenguajes, teoría de complejidad y sistemas (Computer Science - CS).

### D072 — Universidad Austral de Chile (UACh) (Chile)
- **Título del Programa:** Ingeniería Civil en Informática — plan SCT
- **Tipo de Fuente y Año:** Plan de Estudios Oficial (2021)
- **URL Oficial:** [https://ingenieria.uach.cl/carreras/ingenieria-civil-en-informatica/](https://ingenieria.uach.cl/carreras/ingenieria-civil-en-informatica/)
- **Coordenadas:** X = -0.31, Y = 0.19 | **Radio:** 5.39 | **Afinidad:** `CS`
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
- **Coordenadas:** X = 0.10, Y = 0.14 | **Radio:** 5.57 | **Afinidad:** `CS`
- **Diagnóstico Curricular:** Programa formativo estructurado con equilibrio en desarrollo de software, análisis de sistemas y redes (Computer Science - CS).

### D075 — Universidad de Costa Rica (UCR - Sedes Regionales) (Costa Rica)
- **Título del Programa:** Bachillerato en Informática Empresarial — plan de estudios
- **Tipo de Fuente y Año:** Plan de Estudios Oficial (2020)
- **URL Oficial:** [https://ci.ucr.ac.cr/](https://ci.ucr.ac.cr/)
- **Coordenadas:** X = 2.60, Y = 1.76 | **Radio:** 4.89 | **Afinidad:** `IS`
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