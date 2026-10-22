# Corpus CC2020 — Bloque 4 de 5 (D046–D060)
**Fecha de procesamiento:** 22 de octubre de 2026. **Objetivo total:** 75 documentos. **Este bloque:** D046–D060 (Planes de estudio oficiales ponderados por créditos u horas).

## 1. Alcance y Metodología
Este cuarto bloque audita **15 planes de estudio oficiales** de carreras de Computación, Informática y Sistemas representativas de 11 países de América Latina: Uruguay (UdelaR), Perú (UNSA, UNMSM), Chile (UdeC, USM), Colombia (UIS, Univalle), México (UANL, UASLP), Paraguay (UNA), Panamá (UTP), Guatemala (USAC), Argentina (UNR), Ecuador (PUCE) y Bolivia (UMSA).

Al igual que en los bloques 2 y 3, cada materia se pondera con su valor formal en créditos académicos (SCT, SATCA, créditos de facultad) o carga horaria cuatrimestral/semanal, garantizando auditabilidad estricta y reproducibilidad algorítmica sin asignación manual de coordenadas.

### Fórmulas del Protocolo CC2020
- **Eje X (Teoría vs. Aplicación):** $X = 5.0 \cdot \frac{Pa - Pt}{Pa + Pt}$
- **Eje Y (Hardware vs. Organización):** $Y = 5.0 \cdot \frac{Co - Ch}{Ch + Cs + Co}$
- **Dispersión:** $\Delta X = \sqrt{\max(0, 25 - X^2)}$, $\Delta Y = \sqrt{\max(0, 25 \cdot \frac{Ch + Co}{Ch + Cs + Co} - Y^2)}$
- **Radio de Dispersión:** $Radio = \sqrt{\Delta X^2 + \Delta Y^2}$

### Criterios de Codificación Auditable
- **T (Teoría/Principios):** Ciencias básicas (cálculo, álgebra, física, química), matemática discreta, lógica formal, algoritmia y estructuras de datos, lenguajes formales y computabilidad, teoría de compiladores, inteligencia artificial y arquitecturas teóricas.
- **A (Aplicación/Despliegue):** Programación y metodologías de desarrollo, ingeniería de software, bases de datos y administración de datos, sistemas operativos, redes y telecomunicaciones, ciberseguridad, diseño digital, desarrollo web/móvil y gestión de TI.
- **Ch (Hardware):** Circuitos, electrónica, física aplicada, diseño digital, microprocesadores y arquitectura de computadores.
- **Cs (Software y Sistemas):** Algoritmia, lenguajes de programación, software, bases de datos, sistemas operativos, redes, inteligencia artificial y computación científica.
- **Co (Organización y Sistemas de Información):** Gestión de proyectos, evaluación de TI, gobernanza, sistemas de información empresarial, dinámica de sistemas, economía, finanzas y factores humanos (experiencia de usuario / HCI).
- **Exclusiones:** Formación general y transversal (humanidades, idiomas, ética, deportes), asignaturas optativas/electivas sin catálogo de retícula fija, prácticas profesionales/pasantías y trabajos terminales de graduación / tesis.

## 2. Tabla de Resultados — Componente 1 (12 Columnas)

| ID | Titulo_Documento | Institucion_Fuente | Pais | Anio | Tipo_Fuente | Coordenada_X | Coordenada_Y | Desviacion_Radio | Proximidad_Disciplina_CC2020 | Resumen_Evidencia_X | Resumen_Evidencia_Y |
|:---|:---|:---|:---|:---|:---|:---:|:---:|:---:|:---:|:---|:---|
| **D046** | [Ingeniería en Computación — plan oficial FING](https://www.fing.edu.uy/es/carreras/grado/ingenieria-en-computacion) | Universidad de la República (UdelaR) | Uruguay | 1997 | Plan de Estudios Oficial | -0.41 | -0.36 | 5.15 | `CS` | Pt=131; Pa=111 (sin STEM: Pt_c=55, Pa_c=111, X_comp=+1.69); cobertura X=70% del total (347) | Ch=12; Cs=154; Co=0; cobertura Y=48% del total; Vector=[CE:7%,CS:34%,SE:35%,IT:24%,IS:0%] |
| **D047** | [Ingeniería de Sistemas — plan ABET](https://fips.unsa.edu.pe/sistemas/) | Universidad Nacional de San Agustín de Arequipa (UNSA) | Perú | 2025 | Plan de Estudios Oficial | 0.60 | 0.47 | 5.42 | `IT` | Pt=44; Pa=56 (sin STEM: Pt_c=19, Pa_c=56, X_comp=+2.47); cobertura X=87% del total (115) | Ch=4; Cs=60; Co=11; cobertura Y=65% del total; Vector=[CE:5%,CS:22%,SE:30%,IT:29%,IS:13%] |
| **D048** | [Ingeniería Civil Informática — malla 2023](https://www.inf.udec.cl/carreras/ingenieria-civil-informatica/) | Universidad de Concepción (UdeC) | Chile | 2023 | Plan de Estudios Oficial | -0.81 | 0.00 | 5.25 | `SE` | Pt=61; Pa=44 (sin STEM: Pt_c=18, Pa_c=44, X_comp=+2.10); cobertura X=77% del total (137) | Ch=4; Cs=54; Co=4; cobertura Y=45% del total; Vector=[CE:6%,CS:32%,SE:43%,IT:15%,IS:5%] |
| **D049** | [Ingeniería de Sistemas — plan 10 niveles](https://ingsistemas.uis.edu.co/) | Universidad Industrial de Santander (UIS) | Colombia | 2022 | Plan de Estudios Oficial | -0.91 | 0.12 | 5.66 | `SE` | Pt=78; Pa=54 (sin STEM: Pt_c=28, Pa_c=54, X_comp=+1.59); cobertura X=82% del total (160) | Ch=12; Cs=56; Co=14; cobertura Y=51% del total; Vector=[CE:15%,CS:22%,SE:24%,IT:22%,IS:17%] |
| **D050** | [Ingeniero en Tecnología de Software — plan 440](https://www.fime.uanl.mx/its/) | Universidad Autónoma de Nuevo León (UANL - FIME) | México | 2020 | Plan de Estudios Oficial | -1.39 | -0.94 | 5.50 | `CE` | Pt=57.5; Pa=32.5 (sin STEM: Pt_c=12.5, Pa_c=32.5, X_comp=+2.22); cobertura X=68% del total (132) | Ch=11.5; Cs=30.5; Co=3; cobertura Y=34% del total; Vector=[CE:26%,CS:24%,SE:33%,IT:13%,IS:3%] |
| **D051** | [Ingeniería en Informática — plan de estudios](https://www.pol.una.py/carreras/grado/ingenieria-en-informatica/) | Universidad Nacional de Asunción (UNA - FP-UNA) | Paraguay | 2021 | Plan de Estudios Oficial | -0.37 | -0.14 | 5.38 | `CS` | Pt=72; Pa=62 (sin STEM: Pt_c=42, Pa_c=62, X_comp=+0.96); cobertura X=77% del total (175) | Ch=10; Cs=87; Co=7; cobertura Y=59% del total; Vector=[CE:10%,CS:34%,SE:25%,IT:26%,IS:6%] |
| **D052** | [Licenciatura en Ingeniería de Sistemas y Computación](https://fisc.utp.ac.pa/licenciatura-en-ingenieria-de-sistemas-y-computacion) | Universidad Tecnológica de Panamá (UTP - FISC) | Panamá | 2021 | Plan de Estudios Oficial | -1.00 | 0.39 | 5.33 | `CS` | Pt=72; Pa=48 (sin STEM: Pt_c=29, Pa_c=48, X_comp=+1.23); cobertura X=89% del total (135) | Ch=4; Cs=63; Co=10; cobertura Y=57% del total; Vector=[CE:5%,CS:30%,SE:30%,IT:25%,IS:10%] |
| **D053** | [Ingeniería en Ciencias y Sistemas — pénsum](https://ingenieria.usac.edu.gt/carreras/sistemas/) | Universidad de San Carlos de Guatemala (USAC) | Guatemala | 2020 | Plan de Estudios Oficial | -1.29 | -0.72 | 5.26 | `SE` | Pt=83; Pa=49 (sin STEM: Pt_c=34, Pa_c=49, X_comp=+0.90); cobertura X=84% del total (157) | Ch=14; Cs=67; Co=2; cobertura Y=53% del total; Vector=[CE:17%,CS:26%,SE:31%,IT:24%,IS:2%] |
| **D054** | [Ingeniería de Sistemas — plan de estudios](https://sistemas.unmsm.edu.pe/) | Universidad Nacional Mayor de San Marcos (UNMSM - FISI) | Perú | 2020 | Plan de Estudios Oficial | -0.16 | 1.13 | 5.67 | `SE` | Pt=47; Pa=44 (sin STEM: Pt_c=27, Pa_c=44, X_comp=+1.20); cobertura X=76% del total (120) | Ch=4; Cs=47; Co=20; cobertura Y=59% del total; Vector=[CE:6%,CS:23%,SE:24%,IT:21%,IS:27%] |
| **D055** | [Ingeniería de Sistemas — Resolución 047](https://eisc.univalle.edu.co/programas/pregrado/ingenieria-de-sistemas) | Universidad del Valle (Univalle - EISC) | Colombia | 2020 | Plan de Estudios Oficial | -0.92 | 0.35 | 5.41 | `SE` | Pt=45; Pa=31 (sin STEM: Pt_c=12, Pa_c=31, X_comp=+2.21); cobertura X=75% del total (101) | Ch=3; Cs=34; Co=6; cobertura Y=43% del total; Vector=[CE:7%,CS:26%,SE:33%,IT:23%,IS:12%] |
| **D056** | [Licenciatura en Ciencias de la Computación — Plan TO 2024](https://web.fceia.unr.edu.ar/es/carreras/grado/205-licenciatura-en-ciencias-de-la-computacion.html) | Universidad Nacional de Rosario (UNR - FCEIA) | Argentina | 2024 | Plan de Estudios Oficial | -1.90 | -0.24 | 4.75 | `CS` | Pt=138; Pa=62 (sin STEM: Pt_c=64, Pa_c=62, X_comp=-0.08); cobertura X=84% del total (238) | Ch=6; Cs=120; Co=0; cobertura Y=53% del total; Vector=[CE:5%,CS:50%,SE:26%,IT:19%,IS:0%] |
| **D057** | [Ingeniería Civil Informática — plan oficial](https://usm.cl/carreras/ingenieria-civil-informatica/) | Universidad Técnica Federico Santa María (USM) | Chile | 2021 | Plan de Estudios Oficial | -1.05 | 0.69 | 5.40 | `CS` | Pt=98; Pa=64 (sin STEM: Pt_c=44, Pa_c=64, X_comp=+0.93); cobertura X=81% del total (200) | Ch=5; Cs=83; Co=20; cobertura Y=54% del total; Vector=[CE:5%,CS:35%,SE:30%,IT:15%,IS:16%] |
| **D058** | [Ingeniería en Computación — plan de estudios](https://www.ingenieria.uaslp.mx/computacion/) | Universidad Autónoma de San Luis Potosí (UASLP) | México | 2020 | Plan de Estudios Oficial | -0.92 | -1.45 | 5.41 | `CE` | Pt=148; Pa=102 (sin STEM: Pt_c=84, Pa_c=102, X_comp=+0.48); cobertura X=93% del total (270) | Ch=54; Cs=132; Co=0; cobertura Y=69% del total; Vector=[CE:29%,CS:30%,SE:27%,IT:14%,IS:0%] |
| **D059** | [Ingeniería en Tecnologías de la Información](https://www.puce.edu.ec/carreras/tecnologias-de-la-informacion/) | Pontificia Universidad Católica del Ecuador (PUCE) | Ecuador | 2020 | Plan de Estudios Oficial | 1.56 | -0.35 | 5.13 | `IT` | Pt=31; Pa=59 (sin STEM: Pt_c=13, Pa_c=59, X_comp=+3.19); cobertura X=87% del total (104) | Ch=8; Cs=61; Co=3; cobertura Y=69% del total; Vector=[CE:11%,CS:16%,SE:28%,IT:41%,IS:4%] |
| **D060** | [Licenciatura en Informática — pensum](https://informatica.umsa.bo/) | Universidad Mayor de San Andrés (UMSA) | Bolivia | 2021 | Plan de Estudios Oficial | -1.14 | -0.54 | 5.28 | `SE` | Pt=81; Pa=51 (sin STEM: Pt_c=33, Pa_c=51, X_comp=+1.07); cobertura X=76% del total (174) | Ch=12; Cs=69; Co=3; cobertura Y=48% del total; Vector=[CE:14%,CS:27%,SE:30%,IT:25%,IS:4%] |

## 3. Desglose Métrico de Carga Académica y Cobertura

| ID | Institución | Total Materias | Peso Total | Pt (Teoría) | Pa (Aplic.) | Ch (Hardw.) | Cs (Softw.) | Co (Org.) | Cobertura X | Cobertura Y |
|:---|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **D046** | Universidad de la República (UdelaR) | 24 | 347 creditos academicos | 131 | 111 | 12 | 154 | 0 | 69.7% | 47.8% |
| **D047** | Universidad Nacional de San Agustín de Arequipa (UNSA) | 31 | 115 creditos academicos | 44 | 56 | 4 | 60 | 11 | 87.0% | 65.2% |
| **D048** | Universidad de Concepción (UdeC) | 30 | 137 creditos academicos | 61 | 44 | 4 | 54 | 4 | 76.6% | 45.3% |
| **D049** | Universidad Industrial de Santander (UIS) | 39 | 160 creditos academicos | 78 | 54 | 12 | 56 | 14 | 82.5% | 51.2% |
| **D050** | Universidad Autónoma de Nuevo León (UANL - FIME) | 32 | 132 creditos academicos | 57.5 | 32.5 | 11.5 | 30.5 | 3 | 68.2% | 34.1% |
| **D051** | Universidad Nacional de Asunción (UNA - FP-UNA) | 31 | 175 creditos academicos | 72 | 62 | 10 | 87 | 7 | 76.6% | 59.4% |
| **D052** | Universidad Tecnológica de Panamá (UTP - FISC) | 32 | 135 creditos academicos | 72 | 48 | 4 | 63 | 10 | 88.9% | 57.0% |
| **D053** | Universidad de San Carlos de Guatemala (USAC) | 30 | 157 creditos academicos | 83 | 49 | 14 | 67 | 2 | 84.1% | 52.9% |
| **D054** | Universidad Nacional Mayor de San Marcos (UNMSM - FISI) | 29 | 120 creditos academicos | 47 | 44 | 4 | 47 | 20 | 75.8% | 59.2% |
| **D055** | Universidad del Valle (Univalle - EISC) | 29 | 101 creditos academicos | 45 | 31 | 3 | 34 | 6 | 75.2% | 42.6% |
| **D056** | Universidad Nacional de Rosario (UNR - FCEIA) | 30 | 238 horas semanales | 138 | 62 | 6 | 120 | 0 | 84.0% | 52.9% |
| **D057** | Universidad Técnica Federico Santa María (USM) | 38 | 200 creditos SCT | 98 | 64 | 5 | 83 | 20 | 81.0% | 54.0% |
| **D058** | Universidad Autónoma de San Luis Potosí (UASLP) | 32 | 270 creditos academicos | 148 | 102 | 54 | 132 | 0 | 92.6% | 68.9% |
| **D059** | Pontificia Universidad Católica del Ecuador (PUCE) | 26 | 104 creditos academicos | 31 | 59 | 8 | 61 | 3 | 86.5% | 69.2% |
| **D060** | Universidad Mayor de San Andrés (UMSA) | 26 | 174 horas semanales | 81 | 51 | 12 | 69 | 3 | 75.9% | 48.3% |

## 4. Diagrama de Dispersión CC2020

![Dispersión del bloque 4](bloque_04_dispersion.png)

## 5. Análisis e Interpretación de Resultados por Documento

### D046 — Universidad de la República (UdelaR) (Uruguay)
- **Título del Programa:** Ingeniería en Computación — plan oficial FING
- **Tipo de Fuente y Año:** Plan de Estudios Oficial (1997)
- **URL Oficial:** [https://www.fing.edu.uy/es/carreras/grado/ingenieria-en-computacion](https://www.fing.edu.uy/es/carreras/grado/ingenieria-en-computacion)
- **Coordenadas:** X = -0.41, Y = -0.36 | **Radio:** 5.15 | **Afinidad:** `CS`
- **Diagnóstico Curricular:** Sólida formación en fundamentos matemáticos y computación teórica con balance equilibrado en desarrollo de software y sistemas (Computer Science - CS).

### D047 — Universidad Nacional de San Agustín de Arequipa (UNSA) (Perú)
- **Título del Programa:** Ingeniería de Sistemas — plan ABET
- **Tipo de Fuente y Año:** Plan de Estudios Oficial (2025)
- **URL Oficial:** [https://fips.unsa.edu.pe/sistemas/](https://fips.unsa.edu.pe/sistemas/)
- **Coordenadas:** X = 0.60, Y = 0.47 | **Radio:** 5.42 | **Afinidad:** `IT`
- **Diagnóstico Curricular:** Plan bajo lineamientos ABET con un fuerte sesgo hacia ingeniería de software, arquitectura empresarial y gestión tecnológica de proyectos (Software Engineering - SE).

### D048 — Universidad de Concepción (UdeC) (Chile)
- **Título del Programa:** Ingeniería Civil Informática — malla 2023
- **Tipo de Fuente y Año:** Plan de Estudios Oficial (2023)
- **URL Oficial:** [https://www.inf.udec.cl/carreras/ingenieria-civil-informatica/](https://www.inf.udec.cl/carreras/ingenieria-civil-informatica/)
- **Coordenadas:** X = -0.81, Y = 0.00 | **Radio:** 5.25 | **Afinidad:** `SE`
- **Diagnóstico Curricular:** Formación rigurosa en ciencias de la ingeniería con balance entre algoritmia formal, sistemas computacionales y desarrollo de software (Computer Science - CS).

### D049 — Universidad Industrial de Santander (UIS) (Colombia)
- **Título del Programa:** Ingeniería de Sistemas — plan 10 niveles
- **Tipo de Fuente y Año:** Plan de Estudios Oficial (2022)
- **URL Oficial:** [https://ingsistemas.uis.edu.co/](https://ingsistemas.uis.edu.co/)
- **Coordenadas:** X = -0.91, Y = 0.12 | **Radio:** 5.66 | **Afinidad:** `SE`
- **Diagnóstico Curricular:** Estructura curricular de 10 semestres con amplio núcleo de ciencias duras y sistemas, equilibrando desarrollo e infraestructura (Computer Science - CS).

### D050 — Universidad Autónoma de Nuevo León (UANL - FIME) (México)
- **Título del Programa:** Ingeniero en Tecnología de Software — plan 440
- **Tipo de Fuente y Año:** Plan de Estudios Oficial (2020)
- **URL Oficial:** [https://www.fime.uanl.mx/its/](https://www.fime.uanl.mx/its/)
- **Coordenadas:** X = -1.39, Y = -0.94 | **Radio:** 5.50 | **Afinidad:** `CE`
- **Diagnóstico Curricular:** Plan de ingeniería enfocado en desarrollo sistemático de software, con fuerte soporte en física y matemáticas para ingeniería (Computer Science - CS).

### D051 — Universidad Nacional de Asunción (UNA - FP-UNA) (Paraguay)
- **Título del Programa:** Ingeniería en Informática — plan de estudios
- **Tipo de Fuente y Año:** Plan de Estudios Oficial (2021)
- **URL Oficial:** [https://www.pol.una.py/carreras/grado/ingenieria-en-informatica/](https://www.pol.una.py/carreras/grado/ingenieria-en-informatica/)
- **Coordenadas:** X = -0.37, Y = -0.14 | **Radio:** 5.38 | **Afinidad:** `CS`
- **Diagnóstico Curricular:** Plan tradicional con sólida base en matemáticas discretas, algoritmia avanzada, arquitectura y redes (Computer Science - CS).

### D052 — Universidad Tecnológica de Panamá (UTP - FISC) (Panamá)
- **Título del Programa:** Licenciatura en Ingeniería de Sistemas y Computación
- **Tipo de Fuente y Año:** Plan de Estudios Oficial (2021)
- **URL Oficial:** [https://fisc.utp.ac.pa/licenciatura-en-ingenieria-de-sistemas-y-computacion](https://fisc.utp.ac.pa/licenciatura-en-ingenieria-de-sistemas-y-computacion)
- **Coordenadas:** X = -1.00, Y = 0.39 | **Radio:** 5.33 | **Afinidad:** `CS`
- **Diagnóstico Curricular:** Programa equilibrado de ingeniería de sistemas con integración de algoritmia, bases de datos y ciencias de la ingeniería (Computer Science - CS).

### D053 — Universidad de San Carlos de Guatemala (USAC) (Guatemala)
- **Título del Programa:** Ingeniería en Ciencias y Sistemas — pénsum
- **Tipo de Fuente y Año:** Plan de Estudios Oficial (2020)
- **URL Oficial:** [https://ingenieria.usac.edu.gt/carreras/sistemas/](https://ingenieria.usac.edu.gt/carreras/sistemas/)
- **Coordenadas:** X = -1.29, Y = -0.72 | **Radio:** 5.26 | **Afinidad:** `SE`
- **Diagnóstico Curricular:** Énfasis notable en ciencias de la computación, organización de lenguajes, compiladores y sistemas operativos (Computer Science - CS).

### D054 — Universidad Nacional Mayor de San Marcos (UNMSM - FISI) (Perú)
- **Título del Programa:** Ingeniería de Sistemas — plan de estudios
- **Tipo de Fuente y Año:** Plan de Estudios Oficial (2020)
- **URL Oficial:** [https://sistemas.unmsm.edu.pe/](https://sistemas.unmsm.edu.pe/)
- **Coordenadas:** X = -0.16, Y = 1.13 | **Radio:** 5.67 | **Afinidad:** `SE`
- **Diagnóstico Curricular:** Fuerte presencia de teoría de sistemas, modelado dinámico, gestión de procesos de negocio e ingeniería de software (Computer Science - CS).

### D055 — Universidad del Valle (Univalle - EISC) (Colombia)
- **Título del Programa:** Ingeniería de Sistemas — Resolución 047
- **Tipo de Fuente y Año:** Plan de Estudios Oficial (2020)
- **URL Oficial:** [https://eisc.univalle.edu.co/programas/pregrado/ingenieria-de-sistemas](https://eisc.univalle.edu.co/programas/pregrado/ingenieria-de-sistemas)
- **Coordenadas:** X = -0.92, Y = 0.35 | **Radio:** 5.41 | **Afinidad:** `SE`
- **Diagnóstico Curricular:** Orientación contemporánea en desarrollo interactivo, algoritmos y sistemas organizacionales (Computer Science - CS).

### D056 — Universidad Nacional de Rosario (UNR - FCEIA) (Argentina)
- **Título del Programa:** Licenciatura en Ciencias de la Computación — Plan TO 2024
- **Tipo de Fuente y Año:** Plan de Estudios Oficial (2024)
- **URL Oficial:** [https://web.fceia.unr.edu.ar/es/carreras/grado/205-licenciatura-en-ciencias-de-la-computacion.html](https://web.fceia.unr.edu.ar/es/carreras/grado/205-licenciatura-en-ciencias-de-la-computacion.html)
- **Coordenadas:** X = -1.90, Y = -0.24 | **Radio:** 4.75 | **Afinidad:** `CS`
- **Diagnóstico Curricular:** Licenciatura formal orientada puramente a ciencias de la computación, teoría de autómatas, compiladores y semántica formal (Computer Science - CS).

### D057 — Universidad Técnica Federico Santa María (USM) (Chile)
- **Título del Programa:** Ingeniería Civil Informática — plan oficial
- **Tipo de Fuente y Año:** Plan de Estudios Oficial (2021)
- **URL Oficial:** [https://usm.cl/carreras/ingenieria-civil-informatica/](https://usm.cl/carreras/ingenieria-civil-informatica/)
- **Coordenadas:** X = -1.05, Y = 0.69 | **Radio:** 5.40 | **Afinidad:** `CS`
- **Diagnóstico Curricular:** Plan de tradición científica con alta concentración en optimización, ciencias de datos y sistemas distribuidos (Computer Science - CS).

### D058 — Universidad Autónoma de San Luis Potosí (UASLP) (México)
- **Título del Programa:** Ingeniería en Computación — plan de estudios
- **Tipo de Fuente y Año:** Plan de Estudios Oficial (2020)
- **URL Oficial:** [https://www.ingenieria.uaslp.mx/computacion/](https://www.ingenieria.uaslp.mx/computacion/)
- **Coordenadas:** X = -0.92, Y = -1.45 | **Radio:** 5.41 | **Afinidad:** `CE`
- **Diagnóstico Curricular:** Alta carga de circuitos eléctricos, electrónica semiconductora, diseño digital y señales acopladas a computación (Computer Engineering - CE).

### D059 — Pontificia Universidad Católica del Ecuador (PUCE) (Ecuador)
- **Título del Programa:** Ingeniería en Tecnologías de la Información
- **Tipo de Fuente y Año:** Plan de Estudios Oficial (2020)
- **URL Oficial:** [https://www.puce.edu.ec/carreras/tecnologias-de-la-informacion/](https://www.puce.edu.ec/carreras/tecnologias-de-la-informacion/)
- **Coordenadas:** X = 1.56, Y = -0.35 | **Radio:** 5.13 | **Afinidad:** `IT`
- **Diagnóstico Curricular:** Enfoque pragmático en infraestructura de redes, plataformas de software y tecnologías aplicadas (Software Engineering - SE).

### D060 — Universidad Mayor de San Andrés (UMSA) (Bolivia)
- **Título del Programa:** Licenciatura en Informática — pensum
- **Tipo de Fuente y Año:** Plan de Estudios Oficial (2021)
- **URL Oficial:** [https://informatica.umsa.bo/](https://informatica.umsa.bo/)
- **Coordenadas:** X = -1.14, Y = -0.54 | **Radio:** 5.28 | **Afinidad:** `SE`
- **Diagnóstico Curricular:** Currículo clásico de ciencias de la computación e informática pura con base analítica y desarrollo de software (Computer Science - CS).

## 6. Advertencias y Limitaciones Metodológicas
1. **Reglas Explícitas:** Las clasificaciones se derivan de expresiones regulares preestablecidas y auditables aplicadas al nombre de cada asignatura; ninguna coordenada es asignada por estimación manual.
2. **Afinidad Provisional:** Las etiquetas disciplinarias (CS, CE, SE, IT, IS) responden a proporciones de carga académica y umbrales operacionales del script, no a acreditaciones gremiales oficiales de CC2020.
3. **Heterogeneidad de Métricas:** Se utilizan las unidades formales del plan publicado (créditos SCT, SATCA, créditos de facultad u horas cátedra); los análisis calculan proporciones relativas internas normalizadas.
4. **Significado de la Dispersión:** El radio modela la polarización interna del plan respecto a los extremos teóricos/aplicados y hardware/organización, sin constituir un intervalo de error estadístico.