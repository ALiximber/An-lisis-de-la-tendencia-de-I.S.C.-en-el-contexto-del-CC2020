# PROTOCOLO EXTERNO DE CODIFICACIÓN CIEGA DE ASIGNATURAS (`PROTOCOLO_REVISION_EXTERNA.md`)

## 1. Propósito del Protocolo

Este documento define las instrucciones estandarizadas para que un **evaluador independiente** (investigador externo, par académico o auditor ciego sin acceso al código fuente de `src/codebook.py` ni a las etiquetas precalculadas) clasifique las 120 asignaturas de la muestra estratificada contenida en `plantilla_evaluacion_ciega_120.csv` (o `evaluacion_ciega_entrada_120.json`).

---

## 2. Reglas de Codificación Ciega por Asignatura

Para cada asignatura, el evaluador recibe únicamente:
- `Muestra_N`: Número correlativo ($1$ a $120$).
- `ID`, `Institucion`, `Programa`, `Periodo`: Contexto institucional de la asignatura.
- `Asignatura`: Nombre oficial de la materia en el plan de estudios.
- `Condicion`: Condición curricular normalizada (`Obligatoria`, `Obligatoria_Eleccion_Cerrada`, `Optativa_Generica`, `Optativa_Catalogo`).

El evaluador debe completar tres campos basándose estrictamente en el marco conceptual **ACM/IEEE-CS Computing Curricula 2020 (CC2020)**:

### Campo 1: `Eval_Polo_X` (Eje Horizontal: Teoría/Principios vs. Aplicación/Despliegue)
- **`""` (Vacío / Excluida):** Si la materia es una optativa genérica (`Optativa_Generica`), una electiva de catálogo abierto (`Optativa_Catalogo`), una práctica profesional, servicio social, proyecto de graduación/tesis, idioma extranjero, comunicación oral/escrita, ética general, humanidades, deportes o introducción vocacional general a la carrera.
- **`"T"` (Teoría, Principios y Fundamentos):** Asignaturas cuyo núcleo es la demostración matemática, las ciencias naturales básicas (Cálculo, Álgebra, Ecuaciones Diferenciales, Probabilidad y Estadística, Métodos Numéricos, Física, Química, Biología), la matemática discreta, la lógica formal, el análisis y diseño teórico de algoritmos, las estructuras de datos fundamentales, la teoría de la computación (autómatas y lenguajes formales), los compiladores, la inteligencia artificial / aprendizaje automático, la investigación de operaciones / teoría de sistemas, la física de circuitos/señales o la arquitectura y organización teórica de computadoras.
- **`"A"` (Aplicación, Construcción, Despliegue y Gestión):** Asignaturas cuyo núcleo es la programación práctica, el desarrollo web o móvil, la ingeniería de software (requisitos, arquitectura de software, pruebas, calidad, mantenimiento), las bases de datos y gestión de datos, los sistemas operativos y plataformas en la nube, las redes de computadoras y telecomunicaciones operativas, la ciberseguridad práctica, los sistemas digitales aplicados / microcontroladores / sistemas embebidos / robótica, la interacción humano-computador (HCI/UX), los sistemas de información empresarial, la gestión de proyectos de TI o la administración, economía, contabilidad y finanzas.
- **`"T/A"` (Híbrida Teórico-Aplicada):** Asignaturas que articulan en proporciones equivalentes teoría formal e implementación práctica, tales como cursos generales de *Lenguajes / Paradigmas de Programación*, *Ciencia de Datos / Minería de Datos* o *Computación Gráfica / Visualización*.

### Campo 2: `Eval_Polo_Y` (Eje Vertical: Hardware vs. Software/Sistemas vs. Organización)
- **`""` (Vacío / Sin Estrato $Y$):** Si la asignatura fue excluida en $X$ (`Eval_Polo_X == ""`) **o** si es una asignatura de Ciencias Básicas y Matemáticas Generales de Ingeniería (`STEM`: Cálculo, Álgebra, Física general, Química, Biología, Estadística, Métodos Numéricos).
- **`"H"` (Hardware y Sistemas Físicos):** Circuitos eléctricos, electrónica analógica/digital, diseño lógico/digital, arquitectura y organización de computadoras, microprocesadores/microcontroladores, lenguaje ensamblador/interfaz, sistemas embebidos, robótica e instrumentación física.
- **`"H/S"` (Híbrida Hardware-Software):** Redes de computadoras, conectividad, conmutación/enrutamiento y telecomunicaciones (que combinan capa física de transmisión y protocolos lógicos de red).
- **`"S"` (Software, Datos, Algoritmos y Plataformas):** Matemática discreta, lógica para computación, estructuras de datos, algoritmos, teoría de la computación, compiladores, lenguajes de programación, programación aplicada, ingeniería de software, bases de datos, sistemas operativos, computación paralela/distribuida/nube, ciberseguridad, inteligencia artificial, ciencia de datos y computación gráfica.
- **`"S/O"` (Híbrida Software-Organización):** Interacción humano-computador (HCI/UX), análisis y diseño de sistemas organizacionales, e investigación de operaciones / teoría general de sistemas / simulación de sistemas.
- **`"O"` (Organización, Procesos de Negocio y Gestión):** Sistemas de información gerencial/empresarial, inteligencia de negocios (BI), modelado y automatización de procesos de negocio (BPM), arquitectura empresarial, gobierno de TI, formulación y gestión de proyectos de TI, auditoría/legislación informática, administración de empresas, contabilidad, costos, economía, finanzas y planeación estratégica.

### Campo 3: `Eval_Dominio_CC2020` (Dominio Principal de Referencia)
Seleccionar exactamente uno de los siguientes 7 códigos:
- **`EXCL`:** Excluida (optativa abierta/catálogo, práctica/tesis, humanidades/idiomas/ética o introducción general).
- **`STEM`:** Ciencias Básicas y Matemáticas Generales de Ingeniería.
- **`CE`:** *Computer Engineering* (Hardware, electrónica, sistemas digitales, arquitectura de computadores, embebidos, robótica).
- **`CS`:** *Computer Science* (Matemática discreta, lógica, estructuras de datos, algoritmos, teoría de la computación, compiladores, lenguajes de programación, IA/ML, ciencia de datos, computación gráfica/científica).
- **`SE`:** *Software Engineering* (Programación y desarrollo de software, ingeniería de software, arquitectura de software, requisitos, pruebas, calidad de software, análisis y diseño de sistemas).
- **`IT`:** *Information Technology* (Redes y telecomunicaciones, sistemas operativos, servidores, nube, ciberseguridad, bases de datos operativas, infraestructura de TI, HCI/UX).
- **`IS`:** *Information Systems* (Sistemas de información, procesos empresariales, BI, gestión de proyectos y gobierno de TI, investigación de operaciones/sistemas, administración, economía y finanzas).
