# LIBRO DE CÓDIGOS UNIFICADO CC2020 (`CODEBOOK_CC2020.md`)

## 1. Propósito y Fundamento Conceptual

Este libro de códigos establece el sistema formal, determinista y auditable para clasificar las **2,109 asignaturas** de los 60 planes de estudio (`D016`–`D075`) del corpus latinoamericano de programas de computación, implementado computacionalmente en [`corpus_CC2020/src/codebook.py`](file:///c:/Users/Aliximber/Desktop/DOCUMENTOS/corpus_CC2020/src/codebook.py).

Siguiendo el marco **Computing Curricula 2020 (CC2020)** de ACM e IEEE-CS (2020, Capítulos 2 y 4), cada asignatura obligatoria o de elección cerrada se proyecta simultáneamente sobre:

1. **Dos ejes bidimensionales de operacionalización propia $(X, Y)$:**
   - **Eje $X$ (Naturaleza epistemológica):**
     - **Polo Teórico ($T$, valor $-5$):** Principios matemáticos, fundamentos físicos, teoría de la computación, algoritmia formal, arquitectura teórica de computadores y modelos matemáticos/estadísticos.
     - **Polo Aplicado ($A$, valor $+5$):** Construcción, implementación, ingeniería de software, despliegue de infraestructura, administración de datos/redes y gestión organizacional de TI.
     - **Asignación Híbrida ($T/A$, pesos $w_T = 0.5, w_A = 0.5$, valor $0$):** Asignaturas cuya estructura epistémica combina de manera indisociable formalización matemática/algorítmica y desarrollo/implementación práctica (p. ej., *Lenguajes de Programación*, *Ciencia y Minería de Datos*, *Computación Gráfica y Visual*).
   - **Eje $Y$ (Estrato del sistema sociotécnico):**
     - **Polo Hardware ($H$, valor $-5$):** Electrónica, circuitos, sistemas digitales, arquitectura física de procesadores, sistemas embebidos y capa física de comunicaciones.
     - **Estrato Central de Software y Sistemas ($S$, valor $0$):** Algoritmos, estructuras de datos, desarrollo de software, bases de datos, sistemas operativos, redes de computadoras, ciberseguridad e inteligencia artificial.
     - **Polo Organizacional ($O$, valor $+5$):** Sistemas de información empresarial, procesos de negocio, gobierno y gestión de proyectos de TI, economía/finanzas, auditoría/legislación informática y factores humanos (HCI/UX).
     - **Exclusión de Eje $Y$ ($\text{None}$):** Ciencias básicas generales (`STEM`: Cálculo, Álgebra Lineal, Física General, Química, Biología), las cuales aportan fundamento teórico general en $X$ ($w_T = 1.0$) pero son transversales al espectro Hardware–Software–Organización.

2. **Seis dominios curriculares de referencia (`DOMAINS_6`):**
   - `STEM`: Ciencias Básicas y Matemáticas Generales de Ingeniería.
   - `CE`: *Computer Engineering* (Hardware, Electrónica, Sistemas Digitales, Arquitectura de Computadores, Sistemas Embebidos/IoT).
   - `CS`: *Computer Science* (Matemática Discreta, Lógica, Algoritmos y Estructuras de Datos, Teoría de la Computación, Compiladores, Inteligencia Artificial, Computación Científica/Gráfica).
   - `SE`: *Software Engineering* (Programación Aplicada, Ingeniería de Requisitos, Diseño y Arquitectura de Software, Pruebas, Calidad, DevOps y Gestión de Proyectos de Software).
   - `IT`: *Information Technology* (Administración de Sistemas Operativos y Servidores, Redes e Infraestructura, Ciberseguridad Operativa, Computación en la Nube, Desarrollo Web/Móvil e Integración de Plataformas).
   - `IS`: *Information Systems* (Sistemas de Información Empresarial, Inteligencia de Negocios, Procesos Organizacionales, Gobierno y Auditoría de TI, Economía y Administración).

---

## 2. Tratamiento de la Condición Curricular (Obligatorias vs. Optativas)

La función `normalize_condition(asignatura, condicion_raw)` en [`src/codebook.py`](file:///c:/Users/Aliximber/Desktop/DOCUMENTOS/corpus_CC2020/src/codebook.py) clasifica cada registro en una de tres categorías antes de evaluar las reglas temáticas:

1. **`Obligatoria`:** Asignatura troncal fija del plan de estudios (se incluye íntegramente en el cálculo).
2. **`Obligatoria_Eleccion_Cerrada`:** Asignatura obligatoria donde el estudiante elige entre dos cursos equivalentes del mismo dominio científico (p. ej., en `D021` PUJ Cali: *«Optativa: Cálculo Multivariable o Ecuaciones Diferenciales»* y *«Optativa: Electricidad y Magnetismo o Física Térmica y Ondulatoria»*). Se conserva en el cálculo porque el crédito es obligatorio dentro del área de Ciencias Básicas (`R27_STEM_BASIC`).
3. **`Optativa_Generica` / `Optativa_Catalogo`:**
   - `Optativa_Generica`: Espacios abiertos sin temática fija (*«Optativa I»*, *«Electiva Profesional»*, *«Libre Elección»*).
   - `Optativa_Catalogo`: Asignaturas listadas con nombre específico pero marcadas con `Condicion = "Electivo"` dentro de un catálogo de múltiples líneas donde el alumno solo cursa una fracción (caso de las 12 electivas de `D023` UNAC Callao). En el modo estándar (`modo="estandar"`), se excluyen del denominador obligatorio para impedir el triple conteo de líneas electivas; en el análisis de sensibilidad (`modo="con_electivas_catalogo"`, Escenario S3), se evalúan temáticamente para medir su impacto.

---

## 3. Catálogo de las 27 Reglas Jerárquicas (`R01` a `R27`)

Las reglas se evalúan en orden estricto de especificidad semántica (de `R01` a `R27`) para evitar que términos genéricos (*«aplicaciones»*, *«sistemas»*, *«organización»*, *«calidad»*) capturen asignaturas de ciencias básicas, hardware o gestión empresarial.

| ID Regla | Categoría Curricular | Pesos $X$ $(w_T, w_A)$ | Pesos $Y$ $(w_H, w_S, w_O)$ | Reparto en Dominios (`DOMAINS_6`) | Criterio de Decisión y Ejemplos del Corpus |
| :--- | :--- | :---: | :---: | :--- | :--- |
| **`R01_EXCL_OPT`** | Optativas y electivas abiertas | $(0, 0)$ | $(0, 0, 0)$ | Excluida | Espacios de elección abierta (*Optativa I*, *Electiva de Profundización*, *Temas Selectos* sin área). |
| **`R02_EXCL_CAPSTONE`** | Prácticas profesionales, servicio social y trabajo de grado | $(0, 0)$ | $(0, 0, 0)$ | Excluida | Espacios integradores o administrativos (*Práctica Profesional*, *Servicio Social*, *Tesis*, *Proyecto Final de Carrera*). Usa delimitadores para no excluir *Aplicación Práctica de Programación* (`D050`). |
| **`R03_EXCL_TRANSV`** | Formación humanística, idiomas, comunicación, ética y habilidades blandas | $(0, 0)$ | $(0, 0, 0)$ | Excluida | *Inglés*, *Comunicación Oral y Escrita*, *Ética Profesional*, *Metodología de la Investigación*, *Ingeniería y Sociedad*. |
| **`R04_EXCL_INTRO_GEN`** | Introducciones generales a la carrera y ofimática básica | $(0, 0)$ | $(0, 0, 0)$ | Excluida | Cursos de ambientación vocacional (*Introducción a la Ingeniería en Sistemas*, *Herramientas Informáticas*). |
| **`R05_BUS_PROC_AUTO`** | Automatización de procesos de negocio y calidad empresarial | $(0.0, 1.0)$ | $(0.0, 0.0, 1.0)$ | `IS: 0.85, IT: 0.15` | Se evalúa antes de Hardware y Software para evitar que `automatizacion` o `calidad` capturen *Modelado y Automatización de Procesos Empresariales* (`D032`) o *Planificación Estratégica y Sistemas de Calidad Empresarial* (`D037`). |
| **`R06_STEM_APPL_MATH_PHYS`** | Ciencias básicas con vocabulario de sistemas o aplicaciones | $(1.0, 0.0)$ | $(0.0, 0.0, 0.0)$ | `STEM: 1.0` | Se evalúa antes de IS y Software para proteger cursos como *Física de los Sistemas de Información* (`D041`), *Cálculo Avanzado y Aplicaciones* (`D033`) y *Temas Selectos de Matemáticas* (`D058`). |
| **`R07_HW_ELECTR_SIGNALS`** | Electrónica, circuitos eléctricos, electromagnetismo aplicado y señales | $(1.0, 0.0)$ | $(1.0, 0.0, 0.0)$ | `CE: 1.0` | *Circuitos Eléctricos*, *Electrónica Analógica*, *Procesamiento Digital de Señales*, *Sistemas de Comunicaciones*. |
| **`R08_HW_DIGITAL_EMBEDDED`** | Sistemas digitales, microprocesadores, robótica y sistemas embebidos | $(0.0, 1.0)$ | $(1.0, 0.0, 0.0)$ | `CE: 1.0` | *Diseño Digital*, *Microcontroladores*, *Sistemas Embebidos*, *Robótica*, *Principios Eléctricos y Aplicaciones Digitales* (`D034`), *Lenguajes de Interfaz*. |
| **`R09_HW_COMP_ARCH`** | Arquitectura y organización de computadoras | $(1.0, 0.0)$ | $(1.0, 0.0, 0.0)$ | `CE: 0.75, CS: 0.25` | Captura tanto *Organización y Arquitectura de Computadores* como *Arquitectura y Organización de Computadores* (`D047`, `D057`), evitando que `organizacion` caiga en Administración. |
| **`R10_SECURITY`** | Ciberseguridad, seguridad de la información y criptografía | $(0.0, 1.0)$ | $(0.0, 1.0, 0.0)$ | `IT: 0.60, CS: 0.20, SE: 0.20` | *Seguridad Informática*, *Ciberseguridad*, *Seguridad en Redes*, *Criptografía*. |
| **`R11_HCI_UX`** | Interacción humano-computador y experiencia de usuario (HCI/UX) | $(0.0, 1.0)$ | $(0.0, 0.5, 0.5)$ | `IT: 0.40, SE: 0.40, IS: 0.20` | Híbrida en $Y$ ($0.5\,S + 0.5\,O$) por articular diseño de interfaces de software y factores humanos/organizacionales (*Interacción Humano-Computador*, *Diseño de Interfaces*). |
| **`R12_SYS_THINKING_OR`** | Teoría general de sistemas, investigación de operaciones y simulación | $(1.0, 0.0)$ | $(0.0, 0.5, 0.5)$ | `IS: 0.50, CS: 0.50` | *Teoría General de Sistemas*, *Investigación de Operaciones*, *Modelos y Simulación*, *Dinámica de Sistemas*. |
| **`R13_CS_DISCRETE_LOGIC`** | Matemática discreta, lógica formal, teoría de la computación y autómatas | $(1.0, 0.0)$ | $(0.0, 1.0, 0.0)$ | `CS: 1.0` | Usa `\blogica\b` con delimitador de palabra para impedir que coincida con `tecnologica`. Incluye *Matemáticas Discretas*, *Teoría de la Computación*, *Lenguajes Formales y Autómatas*, *Compiladores*. |
| **`R14_CS_ALGO_DS`** | Estructuras de datos, diseño y análisis de algoritmos | $(1.0, 0.0)$ | $(0.0, 1.0, 0.0)$ | `CS: 0.85, SE: 0.15` | *Estructuras de Datos*, *Diseño y Análisis de Algoritmos*, *Complejidad Algorítmica*, *Árboles y Grafos*. |
| **`R15_CS_AI_DS_GRAPHICS`** | Inteligencia artificial, aprendizaje automático y computación científica | $(1.0, 0.0)$ | $(0.0, 1.0, 0.0)$ | `CS: 1.0` | *Inteligencia Artificial*, *Aprendizaje Automático / Machine Learning*, *Visión por Computador*, *Computación Científica*. |
| **`R16_CS_HYBRID_LANG_DM`** | Lenguajes de programación, minería/ciencia de datos y computación gráfica | $(0.5, 0.5)$ | $(0.0, 1.0, 0.0)$ | `CS: 0.65, SE: 0.20, IT: 0.15` | Híbrida en $X$ ($0.5\,T + 0.5\,A$). Unifica singular y plural (*Lenguaje(s) de Programación I/II*, *Paradigmas de Programación*, *Minería de Datos*, *Ciencia de Datos*, *Computación Gráfica*). |
| **`R17_IS_ENTERPRISE`** | Sistemas de información empresarial, inteligencia de negocios y ERP | $(0.0, 1.0)$ | $(0.0, 0.0, 1.0)$ | `IS: 0.85, IT: 0.15` | *Sistemas de Información*, *Inteligencia de Negocios (BI)*, *Arquitectura Empresarial*, *Comercio Electrónico*. |
| **`R18_IT_PROJECT_GOV`** | Gestión de proyectos de TI, gobierno de TI y auditoría informática | $(0.0, 1.0)$ | $(0.0, 0.0, 1.0)$ | `IS: 0.55, SE: 0.25, IT: 0.20` | *Gestión de Proyectos de TI*, *Gobierno de TI*, *Auditoría de Sistemas*, *Legislación Informática*. |
| **`R19_SE_CORE`** | Ingeniería de software, arquitectura, requisitos, pruebas y calidad | $(0.0, 1.0)$ | $(0.0, 1.0, 0.0)$ | `SE: 0.90, IT: 0.10` | *Ingeniería de Software I/II*, *Arquitectura de Software*, *Ingeniería de Requisitos*, *Pruebas y Calidad de Software*, *DevOps*. |
| **`R20_SE_PROG_DEV`** | Programación aplicada, POO y desarrollo web/móvil | $(0.0, 1.0)$ | $(0.0, 1.0, 0.0)$ | `SE: 0.70, CS: 0.15, IT: 0.15` | *Fundamentos de Programación*, *Programación Orientada a Objetos*, *Algoritmos y Programación*, *Desarrollo Web*, *Desarrollo de Aplicaciones Móviles*. |
| **`R21_DB_DATA`** | Bases de datos y administración/modelado de datos | $(0.0, 1.0)$ | $(0.0, 1.0, 0.0)$ | `IT: 0.45, SE: 0.35, IS: 0.20` | *Bases de Datos I/II*, *Administración de Bases de Datos*, *Modelado de Datos*, *Sistemas Gestores de Bases de Datos*. |
| **`R22_OS_DIST_CLOUD`** | Sistemas operativos, sistemas distribuidos y computación en la nube | $(0.0, 1.0)$ | $(0.0, 1.0, 0.0)$ | `IT: 0.45, CS: 0.30, SE: 0.25` | *Sistemas Operativos*, *Sistemas Distribuidos*, *Computación Paralela*, *Computación en la Nube / Cloud Computing*. |
| **`R23_NET_TELECOM`** | Redes de computadoras, conectividad y telecomunicaciones | $(0.0, 1.0)$ | $(0.25, 0.75, 0.0)$ | `IT: 0.65, CE: 0.25, CS: 0.10` | Unifica la discrepancia entre el Bloque 2 y los Bloques 3–5 reconociendo que las redes combinan protocolos de software ($0.75\,S$) e infraestructura física de transmisión ($0.25\,H$). |
| **`R24_IT_INFRA_SERV`** | Infraestructura tecnológica, administración de servidores y soporte de TI | $(0.0, 1.0)$ | $(0.0, 1.0, 0.0)$ | `IT: 0.85, SE: 0.15` | *Fundamentos de Infraestructura Tecnológica* (`D039`), *Administración de Servidores*, *Integración de Sistemas*, *Tecnologías de la Información*. |
| **`R25_SE_SYS_AD`** | Análisis y diseño de sistemas | $(0.0, 1.0)$ | $(0.0, 0.75, 0.25)$ | `SE: 0.55, IS: 0.30, IT: 0.15` | Híbrida en $Y$ ($0.75\,S + 0.25\,O$) por integrar diseño técnico de software y levantamiento organizacional (*Análisis y Diseño de Sistemas*). |
| **`R26_ORG_BUS_ECON`** | Administración, economía, contabilidad, finanzas y emprendimiento tecnológico | $(0.0, 1.0)$ | $(0.0, 0.0, 1.0)$ | `IS: 1.0` | *Contabilidad*, *Ingeniería Económica*, *Finanzas*, *Administración General*, *Emprendimiento Tecnológico*. |
| **`R27_STEM_BASIC`** | Ciencias básicas generales y matemáticas de ingeniería | $(1.0, 0.0)$ | $(0.0, 0.0, 0.0)$ | `STEM: 1.0` | *Cálculo Diferencial/Integral/Vectorial*, *Álgebra Lineal*, *Ecuaciones Diferenciales*, *Probabilidad y Estadística*, *Métodos Numéricos*, *Física*, *Química*, *Biología*. |

---

## 4. Verificación de Cobertura y Pruebas de Consistencia

1. **Cobertura del 100% de las asignaturas del corpus:** Al aplicar `COMPILED_CODEBOOK` sobre las **2,109 asignaturas** de los Bloques 2 a 5, **exactamente 0 asignaturas** caen en `R00_UNMATCHED`.
2. **Invarianza entre bloques:** A diferencia de los scripts originales (donde 132 asignaturas cambiaban de categoría según el bloque), el libro de códigos unificado aplica exactamente la misma función determinista a los 60 planes de estudio.
3. **Verificación automatizada:** La suite [`corpus_CC2020/tests/test_pipeline.py`](file:///c:/Users/Aliximber/Desktop/DOCUMENTOS/corpus_CC2020/tests/test_pipeline.py) comprueba mediante pruebas unitarias todos los casos de borde y colisiones léxicas documentadas.
