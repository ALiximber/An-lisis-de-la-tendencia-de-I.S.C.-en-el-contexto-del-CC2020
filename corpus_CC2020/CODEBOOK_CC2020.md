# LIBRO DE CÓDIGOS UNIFICADO CC2020 (`CODEBOOK_CC2020.md`)

## 1. Propósito y Fundamento Conceptual

Este libro de códigos establece el sistema formal, determinista y auditable para clasificar las **2,109 asignaturas** de los 60 planes de estudio (`D016`–`D075`) del corpus latinoamericano de programas de computación, implementado computacionalmente en [`src/codebook.py`](src/codebook.py).

Siguiendo el marco **Computing Curricula 2020 (CC2020)** de ACM e IEEE-CS (2020, Capítulos 2 y 4), cada asignatura obligatoria o de elección cerrada se proyecta simultáneamente sobre:

1. **Dos ejes bidimensionales de operacionalización propia $(X, Y)$:**
   - **Eje $X$ (Naturaleza epistemológica):**
     - **Polo Teórico ($T$, valor $-5$):** Principios matemáticos, fundamentos físicos, teoría de la computación, algoritmia formal, arquitectura teórica de computadores y modelos matemáticos/estadísticos.
     - **Polo Aplicado ($A$, valor $+5$):** Construcción, implementación, ingeniería de software, despliegue de infraestructura, administración de datos/redes y gestión organizacional de TI.
     - **Asignación Híbrida ($T/A$, pesos $w_T = 0.5, w_A = 0.5$, valor $0$):** Asignaturas cuya estructura epistémica combina de manera indisociable formalización matemática/algorítmica y desarrollo/implementación práctica (p. ej., *Algoritmos y Programación Inicial*, *Arquitectura de Computadoras y Sistemas Operativos*, *Principios Eléctricos y Aplicaciones Digitales*, *Fundamentos de Telecomunicaciones*).
   - **Eje $Y$ (Estrato del sistema sociotécnico):**
     - **Polo Hardware ($H$, valor $-5$):** Electrónica, circuitos, sistemas digitales, arquitectura física de procesadores, sistemas embebidos y capa física de comunicaciones.
     - **Estrato Central de Software y Sistemas ($S$, valor $0$):** Algoritmos, estructuras de datos, desarrollo de software, bases de datos, sistemas operativos, redes de computadoras, ciberseguridad e inteligencia artificial.
     - **Polo Organizacional ($O$, valor $+5$):** Sistemas de información empresarial, procesos de negocio, gobierno y gestión de proyectos de TI, economía/finanzas, auditoría/legislación informática y factores humanos (HCI/UX).
     - **Asignaciones Híbridas en $Y$ ($H/S$ con valor $-2.5$; $S/O$ con valor $+2.5$):** Asignaturas que integran dos estratos sociotécnicos explícitos (p. ej., *Arquitectura de Computadores y Sistemas Operativos* en $H/S$; *Seguridad y Auditoría de Sistemas* o *Computación Gráfica e Interacción Humano-Computadora* en $S/O$).
     - **Exclusión de Eje $Y$ ($\text{None}$):** Ciencias básicas generales (`STEM`: Cálculo, Álgebra Lineal, Física General, Química, Biología, Probabilidad y Estadística, Métodos Numéricos), las cuales aportan fundamento teórico general en $X$ ($w_T = 1.0$) pero son transversales al espectro Hardware–Software–Organización.

2. **Seis dominios curriculares de referencia (`DOMAINS_6`):**
   - `STEM`: Ciencias Básicas y Matemáticas Generales de Ingeniería.
   - `CE`: *Computer Engineering* (Hardware, Electrónica, Sistemas Digitales, Arquitectura de Computadores, Sistemas Embebidos/IoT).
   - `CS`: *Computer Science* (Matemática Discreta, Lógica, Algoritmos y Estructuras de Datos, Teoría de la Computación, Compiladores, Inteligencia Artificial, Ciencia de Datos, Computación Científica/Gráfica).
   - `SE`: *Software Engineering* (Programación Aplicada, Ingeniería de Requisitos, Diseño y Arquitectura de Software, Pruebas, Calidad, DevOps y Construcción de Software).
   - `IT`: *Information Technology* (Administración de Sistemas Operativos y Servidores, Bases de Datos, Redes e Infraestructura, Ciberseguridad Operativa, Computación en la Nube, Desarrollo Web/Móvil e Integración de Plataformas).
   - `IS`: *Information Systems* (Sistemas de Información Empresarial, Inteligencia de Negocios, Procesos Organizacionales, Gestión de Proyectos y Gobierno de TI, Interacción Humano-Computador, Economía y Administración).

---

## 2. Tratamiento de la Condición Curricular (Obligatorias vs. Optativas)

La función `normalize_condition(asignatura, condicion_raw)` en [`src/codebook.py`](src/codebook.py) clasifica cada registro en una de tres categorías antes de evaluar las reglas temáticas:

1. **`Obligatoria`:** Asignatura troncal fija del plan de estudios (se incluye íntegramente en el cálculo).
2. **`Obligatoria_Eleccion_Cerrada`:** Asignatura obligatoria donde el estudiante elige entre dos cursos equivalentes del mismo dominio científico (p. ej., en `D021` PUJ Cali: *«Optativa: Cálculo Multivariable o Ecuaciones Diferenciales»* y *«Optativa: Electricidad y Magnetismo o Física Térmica y Ondulatoria»*). Se conserva en el cálculo porque el crédito es obligatorio dentro del área de Ciencias Básicas (`R27_STEM_BASIC`).
3. **`Optativa_Generica` / `Optativa_Catalogo`:**
   - `Optativa_Generica`: Espacios abiertos sin temática fija (*«Optativa I»*, *«Electiva Profesional»*, *«Libre Elección»*).
   - `Optativa_Catalogo`: Asignaturas listadas con nombre específico pero marcadas con `Condicion = "Electivo"` dentro de un catálogo de múltiples líneas donde el alumno solo cursa una fracción (caso de las 12 electivas de `D023` UNAC Callao). En el modo estándar (`modo="estandar"`), se excluyen del denominador obligatorio para impedir el triple conteo de líneas electivas; en el análisis de sensibilidad (`modo="con_electivas_catalogo"`, Escenario S3), se evalúan temáticamente para medir su impacto.

---

## 3. Catálogo Exacto de las 27 Reglas Jerárquicas (`R01` a `R27`)

Las 27 reglas definidas en `CODEBOOK_RULES` dentro de [`src/codebook.py`](src/codebook.py) se evalúan en orden estricto de especificidad semántica (de `R01` a `R27`) para evitar que términos genéricos (*«aplicaciones»*, *«sistemas»*, *«organización»*, *«calidad»*, *«comunicaciones»*) capturen asignaturas de ciencias básicas, hardware o gestión empresarial.

| ID Regla (`codebook.py`) | Categoría Curricular | Pesos $X$ $(w_T, w_A)$ | Pesos $Y$ $(w_H, w_S, w_O)$ | Reparto en Dominios (`DOMAINS_6`) | Criterio de Decisión y Ejemplos del Corpus |
| :--- | :--- | :---: | :---: | :--- | :--- |
| **`R01_EXCL_OPT`** | Optativas y electivas sin contenido fijo desagregado | $(0, 0)$ | $(0, 0, 0)$ | Excluida (`EXCL`) | Espacios de elección abierta (*Optativa I*, *Electiva de Profundización*, *Temas Selectos* sin área). |
| **`R02_EXCL_CAPSTONE`** | Prácticas profesionales, servicio social y trabajos terminales de titulación | $(0, 0)$ | $(0, 0, 0)$ | Excluida (`EXCL`) | Espacios integradores o administrativos (*Práctica Profesional*, *Servicio Social*, *Tesis*, *Proyecto Final de Carrera*). Usa delimitadores para no excluir *Aplicación Práctica de Programación* (`D050`). |
| **`R03_EXCL_TRANSV`** | Formación humanística, idiomas, comunicación, ética y habilidades blandas | $(0, 0)$ | $(0, 0, 0)$ | Excluida (`EXCL`) | *Inglés*, *Comunicación Oral y Escrita*, *Ética Profesional*, *Metodología de la Investigación*, *Ingeniería y Sociedad*. |
| **`R04_EXCL_INTRO_GEN`** | Introducciones generales a la carrera y herramientas ofimáticas | $(0, 0)$ | $(0, 0, 0)$ | Excluida (`EXCL`) | Cursos de ambientación vocacional (*Introducción a la Ingeniería en Sistemas*, *Herramientas Informáticas*). |
| **`R05_HYB_ARCH_OS`** | Híbrida: Arquitectura de Computadoras + Sistemas Operativos / Bajo Nivel | $(0.5, 0.5)$ | $(0.5, 0.5, 0.0)$ | `CE: 0.50, IT: 0.50` | Integra explícitamente arquitectura/bajo nivel ($H$) y sistemas operativos ($S$): *Arquitectura de Computadores y Sistemas Operativos*, *Lenguajes Ensambladores y Sistemas Operativos*. |
| **`R06_HYB_GFX_HCI`** | Híbrida: Computación Gráfica + Interacción Humano-Computadora | $(0.5, 0.5)$ | $(0.0, 0.5, 0.5)$ | `CS: 0.50, IS: 0.50` | Integra algoritmos de graficación por computadora ($T, S$) y factores humanos/HCI ($A, O$): *Computación Gráfica e Interacción Humano-Computadora*. |
| **`R07_HYB_SEC_AUD`** | Híbrida: Ciberseguridad Técnica + Auditoría Organizacional de Sistemas | $(0.0, 1.0)$ | $(0.0, 0.5, 0.5)$ | `IT: 0.50, IS: 0.50` | Integra seguridad informática técnica ($A, S$) y auditoría organizacional de TI ($A, O$): *Seguridad y Auditoría de Sistemas*. |
| **`R08_HYB_ELEC_DIG`** | Híbrida: Principios Físicos/Arquitectura + Diseño Digital/Assembly | $(0.5, 0.5)$ | $(1.0, 0.0, 0.0)$ | `CE: 1.00` | Combina fundamentos físicos/arquitectura teórica ($T, H$) y aplicación digital/bajo nivel ($A, H$): *Principios Eléctricos y Aplicaciones Digitales* (`D034`), *Organização Básica de Computadores e Assembly*. |
| **`R09_HYB_TELECOM`** | Híbrida: Fundamentos de Telecomunicaciones y Transmisión de Datos | $(0.5, 0.5)$ | $(0.5, 0.5, 0.0)$ | `CE: 0.50, IT: 0.50` | Combina teoría de transmisión/señales físicas ($T, H$) y protocolos de comunicación de redes ($A, S$): *Fundamentos de Telecomunicaciones* (`D034`), *Transmisión y Comunicación de Datos*. |
| **`R10_HW_THEORY`** | Hardware Teórico: Circuitos, Electrónica, Señales y Sistemas de Comunicaciones | $(1.0, 0.0)$ | $(1.0, 0.0, 0.0)$ | `CE: 1.00` | *Circuitos Eléctricos*, *Electrónica Analógica*, *Procesamiento Digital de Señales*, *Sistemas de Comunicaciones*, *Fundamentos Físicos de la Informática*. |
| **`R11_HW_ARCH`** | Arquitectura y Organización de Computadoras | $(1.0, 0.0)$ | $(1.0, 0.0, 0.0)$ | `CE: 1.00` | Captura tanto *Organización y Arquitectura de Computadores* como *Arquitectura y Organización de Computadores* (`D047`, `D057`), evitando que `organizacion` caiga en Administración. |
| **`R12_HW_APPLIED`** | Hardware Aplicado: Sistemas Digitales, Microprocesadores, Embebidos y Robótica | $(0.0, 1.0)$ | $(1.0, 0.0, 0.0)$ | `CE: 1.00` | *Sistemas Digitales*, *Diseño Lógico*, *Microprocesadores*, *Microcontroladores*, *Sistemas Embebidos*, *Lenguajes de Interfaz*, *Robótica y Automatización*. |
| **`R13_IS_SYS_THEORY`** | Teoría de Sistemas y Dinámica Organizacional | $(1.0, 0.0)$ | $(0.0, 0.0, 1.0)$ | `IS: 1.00` | *Teoría General de Sistemas*, *Pensamiento Sistémico*, *Dinámica de Sistemas*, *Métodos Cuantitativos para la Toma de Decisiones*. |
| **`R14_IS_GOV_BPM`** | Arquitectura Empresarial, Gobierno de TI y Procesos de Negocio (BPM) | $(0.0, 1.0)$ | $(0.0, 0.0, 1.0)$ | `IS: 1.00` | Se evalúa antes de Hardware y Software para proteger *Modelado y Automatización de Procesos Empresariales* (`D032`) y *Planificación Estratégica y Sistemas de Calidad Empresarial* (`D037`), además de *Arquitectura Empresarial* y *Gobierno de TI*. |
| **`R15_IS_PM`** | Formulación, Evaluación y Gestión de Proyectos de TI/Software | $(0.0, 1.0)$ | $(0.0, 0.0, 1.0)$ | `IS: 0.70, SE: 0.30` | *Formulación y Evaluación de Proyectos*, *Gestión de Proyectos de TI*, *Administración de Proyectos de Software*. |
| **`R16_IS_HCI`** | Factores Humanos e Interacción Humano-Computador (HCI / UX) | $(0.0, 1.0)$ | $(0.0, 0.0, 1.0)$ | `IS: 0.50, SE: 0.50` | *Interacción Humano-Computador*, *Diseño de Interfaces*, *Diseño de Experiencia de Usuario*. |
| **`R17_IS_INFO_SYS`** | Sistemas de Información Empresariales e Inteligencia de Negocios | $(0.0, 1.0)$ | $(0.0, 0.0, 1.0)$ | `IS: 1.00` | Exige inicio o calificador explícito para no capturar *Física de los Sistemas de Información* (`D041`). Incluye *Sistemas de Información*, *Inteligencia de Negocios*, *Negocios Electrónicos*. |
| **`R18_IS_BIZ_LAW`** | Economía, Finanzas, Administración, Auditoría y Legislación Informática | $(0.0, 1.0)$ | $(0.0, 0.0, 1.0)$ | `IS: 1.00` | *Ingeniería Económica*, *Contabilidad y Costos*, *Administración*, *Emprendimiento*, *Auditoría de Sistemas*, *Legislación Informática*. |
| **`R19_CS_DISCRETE_LOGIC`** | Matemáticas Discretas, Lógica Formal y Pensamiento Computacional | $(1.0, 0.0)$ | $(0.0, 1.0, 0.0)$ | `CS: 1.00` | Usa `\blogica\b` con delimitador de palabra para impedir que coincida con `tecnologica` (`D039`). Incluye *Matemáticas Discretas*, *Estructuras Discretas*, *Lógica Computacional*. |
| **`R20_CS_ALGO_THEORY`** | Algoritmos, Estructuras de Datos, Teoría de la Computación y Compiladores | $(1.0, 0.0)$ | $(0.0, 1.0, 0.0)$ | `CS: 1.00` | *Estructuras de Datos*, *Diseño y Análisis de Algoritmos*, *Teoría de la Computación*, *Lenguajes Formales y Autómatas*, *Compiladores*, *Paradigmas de Programación*. |
| **`R21_CS_AI_DS_GFX`** | Inteligencia Artificial, Ciencia de Datos y Computación Gráfica/Científica | $(1.0, 0.0)$ | $(0.0, 1.0, 0.0)$ | `CS: 1.00` | *Inteligencia Artificial*, *Aprendizaje Automático*, *Ciencia de Datos*, *Minería de Datos*, *Computación Gráfica*, *Computación Científica*. |
| **`R22_SE_INTRO_PROG`** | Algoritmos y Programación Inicial / Metodología de la Programación | $(0.5, 0.5)$ | $(0.0, 1.0, 0.0)$ | `CS: 0.50, SE: 0.50` | Híbrida en $X$ ($0.5\,T + 0.5\,A$): combina formulación algorítmica e implementación inicial (*Algoritmos y Programación*, *Metodología de la Programación*). |
| **`R23_SE_PROG_LANG`** | Programación, Orientación a Objetos y Lenguajes de Programación | $(0.0, 1.0)$ | $(0.0, 1.0, 0.0)$ | `SE: 0.70, CS: 0.30` | *Fundamentos de Programación*, *Programación Orientada a Objetos*, *Lenguajes de Programación*, *Programación Concurrente*, *Aplicación Práctica de Programación* (`D050`). |
| **`R24_SE_CORE`** | Ingeniería de Software, Requisitos, Arquitectura, Calidad y Proyectos de Software | $(0.0, 1.0)$ | $(0.0, 1.0, 0.0)$ | `SE: 1.00` | *Ingeniería de Software I/II*, *Ingeniería de Requisitos*, *Arquitectura y Diseño de Software*, *Calidad y Pruebas de Software*, *Análisis y Diseño de Sistemas*. |
| **`R25_IT_SEC`** | Seguridad de la Información y Ciberseguridad | $(0.0, 1.0)$ | $(0.0, 1.0, 0.0)$ | `IT: 1.00` | *Seguridad Informática*, *Seguridad de la Información*, *Seguridad en Redes*, *Ciberseguridad*, *Criptografía y Seguridad*. |
| **`R26_IT_OS_DB_NET`** | Sistemas Operativos, Bases de Datos, Redes, Nube y Desarrollo Web/Móvil/Integración | $(0.0, 1.0)$ | $(0.0, 1.0, 0.0)$ | `IT: 0.75, SE: 0.25` | *Sistemas Operativos*, *Bases de Datos*, *Redes de Computadoras*, *Computación en la Nube*, *Desarrollo Web/Móvil*, *Fundamentos de Infraestructura Tecnológica* (`D039`). Acota `^comunicaciones$|redes (y|de) comunicaciones` para no capturar *Modelos Estocásticos y Simulación en Computación y Comunicaciones* (`D020`). |
| **`R27_STEM_BASIC`** | Ciencias Básicas Generales: Matemáticas, Estadística, Física, Química y Biología | $(1.0, 0.0)$ | $(0.0, 0.0, 0.0)$ | `STEM: 1.00` | *Cálculo*, *Álgebra Lineal*, *Ecuaciones Diferenciales*, *Probabilidad y Estadística*, *Modelos Estocásticos*, *Investigación de Operaciones*, *Simulación*, *Física*, *Química*, *Biología*. |

---

## 4. Verificación de Cobertura y Concordancia Inter-Evaluador Ciega (`n = 120`)

1. **Cobertura del 100% de las asignaturas del corpus:** Al aplicar `COMPILED_CODEBOOK` sobre las **2,109 asignaturas** de los Bloques 2 a 5, **exactamente 0 asignaturas** caen en `R00_UNMATCHED`.
2. **Invarianza entre bloques:** A diferencia de los scripts originales (donde 132 asignaturas cambiaban de categoría según el bloque), el libro de códigos unificado aplica exactamente la misma función determinista a los 60 planes de estudio.
3. **Validación ciega independiente ($\kappa$ de Cohen):** Bajo el protocolo externo [`PROTOCOLO_REVISION_EXTERNA.md`](PROTOCOLO_REVISION_EXTERNA.md), un evaluador independiente ciego codificó la muestra estratificada de **120 asignaturas** ([`evaluacion_ciega_resultados_120.json`](evaluacion_ciega_resultados_120.json)), alcanzando una concordancia sustancial a casi perfecta con `S1`:
   - **Polo $X$:** Acuerdo bruto $= 80.83\%$, $\kappa = 0.7198$ (IC 95% $[0.6199, 0.8124]$), $\kappa_w = 0.7350$, con solo $1/120$ inversión polar estricta (`T` $\leftrightarrow$ `A`).
   - **Polo $Y$:** Acuerdo bruto $= 82.50\%$, $\kappa = 0.7751$ (IC 95% $[0.6896, 0.8581]$), $\kappa_w = 0.8560$, con $0/120$ inversiones polares (`H` $\leftrightarrow$ `O`).
   - **Dominio CC2020:** Acuerdo bruto $= 80.83\%$, $\kappa = 0.7699$ (IC 95% $[0.6823, 0.8485]$).
4. **Verificación automatizada:** La suite [`tests/test_pipeline.py`](tests/test_pipeline.py) comprueba mediante pruebas unitarias todos los casos de borde, colisiones léxicas y umbrales de concordancia inter-evaluador.
