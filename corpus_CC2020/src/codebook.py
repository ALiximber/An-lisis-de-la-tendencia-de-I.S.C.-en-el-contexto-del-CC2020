"""Catálogo unificado y auditable de clasificación curricular CC2020 (Codebook v2.0).

Resuelve:
1. Las 132 inconsistencias entre los scripts originales calcular_bloque_02.py a 05.py.
2. Errores de precedencia y falsos positivos por subcadenas (p. ej. 'tecnológica' -> 'lógica',
   'Cálculo Avanzado y Aplicaciones' -> 'aplicaciones', 'Física de los Sistemas de Información' -> 'sistemas de información',
   'Arquitectura y Organización de Computadores' -> 'organización', 'Aplicación Práctica de Programación' -> 'práctica',
   'Modelado y Automatización de Procesos Empresariales' -> 'automatización').
3. Separación explícita entre asignaturas obligatorias y optativas/electivas de catálogo (evitando el triple conteo en D023).
4. Asignaciones múltiples (pesos fraccionarios 0.5/0.5) para asignaturas genuinamente híbridas entre ejes o capas.
5. Mapeo simultáneo a las coordenadas (X, Y) y a los 6 dominios curriculares de referencia (STEM, CE, CS, SE, IT, IS).
"""
import re
import unicodedata


def norm_text(s: str) -> str:
    """Normaliza texto a minúsculas sin diacríticos ni marcas de nota (*)."""
    s = unicodedata.normalize("NFKD", (s or "").lower())
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"\(\*\)", "", s)
    return re.sub(r"\s+", " ", s).strip()


def normalize_condition(asignatura: str, condicion_raw: str) -> str:
    """Estandariza la condición curricular distinguendo obligatorias, elección cerrada de ciencias básicas y optativas abiertas."""
    n = norm_text(asignatura)
    c = norm_text(condicion_raw)
    # Casos de elección cerrada entre dos cursos obligatorios de ciencias básicas (ej. D021 Javeriana Cali)
    if n.startswith("optativa: calculo") or n.startswith("optativa: electricidad"):
        return "Obligatoria_Eleccion_Cerrada"
    if "optativ" in c or "electiv" in c or "eletiv" in c:
        # En D023 las 12 materias 'Electivo' tienen nombre específico de catálogo
        if re.search(r"\b(optativa|optativas|electiva|electivas|electivo|electivos|eletivas|libre eleccion|campo de profundizacion|asignaturas de especialidad)\b", n):
            return "Optativa_Generica"
        return "Optativa_Catalogo"
    if re.search(r"\b(optativa|optativas|electiva|electivas|electivo|electivos|eletivas|libre eleccion|campo de profundizacion|asignaturas de especialidad|cursos complementarios)\b", n):
        return "Optativa_Generica"
    return "Obligatoria"


# Estructura de cada regla en CODEBOOK_RULES:
# (rule_id, nombre_categoria, patron_regex, pes_X=(wT, wA), pes_Y=(wH, wS, wO), dom_weights={dom: w}, es_hibrida, criterio_nota)
CODEBOOK_RULES = [
    # -------------------------------------------------------------------------
    # BLOQUE A: EXCLUSIONES TRANSVERSALES, OPTATIVAS ABIERTAS Y TRABAJOS DE GRADO GENÉRICOS
    # -------------------------------------------------------------------------
    (
        "R01_EXCL_OPT",
        "Optativas y electivas sin contenido fijo desagregado",
        r"^(optativa(?!:)|optativas|electiva|electivas|electivo|electivos|disciplinas optativas|disciplinas eletivas|"
        r"materias optativas|asignaturas optativas|asignaturas electivas|cursos electivos|cursos complementarios|"
        r"libre eleccion|asignaturas de especialidad|asignaturas del campo de profundizacion|"
        r"curso (i+|1|2|3) profundizacion|temas selectos$|topicos de vanguardia|perspectivas disciplinares)",
        (0.0, 0.0), (0.0, 0.0, 0.0), {}, False,
        "Espacios de elección abierta sin asignatura obligatoria fija."
    ),
    (
        "R02_EXCL_CAPSTONE",
        "Prácticas profesionales, servicio social y trabajos terminales de titulación",
        r"practica(s)? (profesional|preprofesional|supervisada|comunitaria|en la profesion|inicial)|"
        r"^practica profesional|\bpracticum\b|pasantia|residencia profesional|estancia profesional|servicio social|"
        r"trabajo (terminal|de grado|final de grado|de titulo|profesional|especial de grado|de conclusao)|"
        r"trabalho de conclusao|projeto final de graduacao|proyecto (terminal|modular|final|de graduacion|de grado|de fin de carrera|de tesis|de ingenieria|de sistemas|social|de innovacion)|"
        r"taller de (tesis|tesina|grado|titulacion|proyecto|evaluacion formativa|investigacion)|"
        r"taller interdisciplinario de investigacion|preparacion de proyectos de investigacion|"
        r"seminario de (investigacion|orientacion|sistemas|realidad nacional)|"
        r"\btesis\b|\btesina\b|memoria de titulo|titulacion e integracion|unidad de integracion curricular|"
        r"articulo cientifico|formulacion de proyecto de fin de carrera|capstone project sistemas|"
        r"proyecto integrador (\d|de tecnologias|y practica)",
        (0.0, 0.0), (0.0, 0.0, 0.0), {}, False,
        "Espacios integradores de graduación, tesis o prácticas preprofesionales."
    ),
    (
        "R03_EXCL_TRANSV",
        "Formación humanística, idiomas, comunicación, ética y habilidades blandas",
        r"\bidioma(s)?\b|\bingles\b|lengua extranjera|beginner|espanol general|"
        r"comunicacion (oral|escrita|efectiva|y redaccion|y expresion|\d)|^comunicacion$|habilidades de comunicacion|"
        r"competencias comunicativas|procesos comunicativos|comprension lectora|redaccion|escritura academica|"
        r"argumentacion|expresion (oral|escrita)|taller de lenguaje$|"
        r"humanidades|humanismo|teologia|constitucion|democracia|catedra|cultura (digital|maya|de paz|y comunicacion)|"
        r"actividades (culturales|artisticas)|sociologia|psicologia|filosofia|antropologia|historia de honduras|"
        r"sociohumanistica|ciencias sociales|area social humanistica|"
        r"\betica\b|aspectos eticos|responsabilidad social|desarrollo sustentable|sustentabilidad|"
        r"liderazgo personal|desarrollo de habilidades sociales|taller de habilidades interpersonales|"
        r"desarrollo del talento|empleabilidad|habilidades del pensamiento|estructura del pensamiento complejo|"
        r"metodologia (universitaria|de la investigacion|de investigacion|del trabajo academico)|"
        r"metodos y tecnicas de investigacion|tecnicas de estudio|fundamentos (y generalidades )?de investigacion|"
        r"introduccion al pensamiento cientifico|introduccion al conocimiento de la sociedad|"
        r"ingenieria, etica y sociedad|ingenieria y sociedad|informatica y sociedad|computacion y sociedad|"
        r"ciencias, tecnologia y desarrollo|quimica y sociedad|contexto geopolitico|realidad nacional|"
        r"recursos y necesidades de mexico|seguridad, higiene y gestion ambiental|experiencia formativa|"
        r"desafios de (la ingenieria|innovacion)|modulo interdisciplinario",
        (0.0, 0.0), (0.0, 0.0, 0.0), {}, False,
        "Formación general transversal, sociohumanística, ética, idiomas y metodología general."
    ),
    (
        "R04_EXCL_INTRO_GEN",
        "Introducciones generales a la carrera y herramientas ofimáticas",
        r"introduccion a (la|los) (ingenieria|sistemas|informatica|computacion)|"
        r"intro\.?\s*a la ing|introducao a computacao|fundamentacion en ingenieria|"
        r"herramientas (computacionales|informaticas|digitales para la gestion)|"
        r"tecnologias (emergentes|avanzadas)$|sistemas de representacion",
        (0.0, 0.0), (0.0, 0.0, 0.0), {}, False,
        "Cursos introductorios panorámicos o de nivelación en herramientas generales."
    ),

    # -------------------------------------------------------------------------
    # BLOQUE B: ASIGNATURAS HÍBRIDAS CON ASIGNACIÓN FRACCIONARIA JUSTIFICADA (0.5 / 0.5)
    # -------------------------------------------------------------------------
    (
        "R05_HYB_ARCH_OS",
        "Híbrida: Arquitectura de Computadoras + Sistemas Operativos / Bajo Nivel",
        r"arquitectura (del computador|de computadores) y sistemas operativos|"
        r"lenguajes ensambladores y sistemas operativos",
        (0.5, 0.5), (0.5, 0.5, 0.0), {"CE": 0.5, "IT": 0.5}, True,
        "Integra explícitamente arquitectura/bajo nivel (H) y sistemas operativos (S)."
    ),
    (
        "R06_HYB_GFX_HCI",
        "Híbrida: Computación Gráfica + Interacción Humano-Computadora",
        r"computacion grafica e interaccion humano-computadora",
        (0.5, 0.5), (0.0, 0.5, 0.5), {"CS": 0.5, "IS": 0.5}, True,
        "Integra algoritmos de graficación por computadora (T,S) y factores humanos/HCI (A,O)."
    ),
    (
        "R07_HYB_SEC_AUD",
        "Híbrida: Ciberseguridad Técnica + Auditoría Organizacional de Sistemas",
        r"(seguridad|ciberseguridad) y auditoria de sistemas",
        (0.0, 1.0), (0.0, 0.5, 0.5), {"IT": 0.5, "IS": 0.5}, True,
        "Integra seguridad informática técnica (A,S) y auditoría organizacional de TI (A,O)."
    ),
    (
        "R08_HYB_ELEC_DIG",
        "Híbrida: Principios Físicos/Arquitectura + Diseño Digital/Assembly",
        r"principios electricos y aplicaciones digitales|organizacao basica de computadores e assembly|"
        r"sistemas computacionales y arquitectura de computadores",
        (0.5, 0.5), (1.0, 0.0, 0.0), {"CE": 1.0}, True,
        "Combina fundamentos físicos/arquitectura teórica (T,H) y aplicación digital/bajo nivel (A,H)."
    ),
    (
        "R09_HYB_TELECOM",
        "Híbrida: Fundamentos de Telecomunicaciones y Transmisión de Datos",
        r"fundamentos de (redes y )?telecomunicaciones|transmision y comunicacion de datos|"
        r"informacion y comunicaciones",
        (0.5, 0.5), (0.5, 0.5, 0.0), {"CE": 0.5, "IT": 0.5}, True,
        "Combina teoría de transmisión/señales físicas (T,H) y protocolos de comunicación de redes (A,S)."
    ),

    # -------------------------------------------------------------------------
    # BLOQUE C: HARDWARE, ELECTRÓNICA Y ARQUITECTURA DE COMPUTADORAS (CE)
    # -------------------------------------------------------------------------
    (
        "R10_HW_THEORY",
        "Hardware Teórico: Circuitos, Electrónica, Señales y Sistemas de Comunicaciones",
        r"fundamentos fisicos de la informatica|circuitos (electricos|eletricos)|"
        r"analisis de sistemas electricos|sistemas electricos lineales|"
        r"electricidad y electronica|electrotecnia y electronica|fundamentos de electronica|"
        r"^electronica$|electronica analogica|eletronica basica|dispositivos semiconductores|"
        r"microelectronica|procesamiento (digital )?de senales|introduccion al procesamiento de senales|"
        r"sistemas de comunicaciones|fundamentos de hardware",
        (1.0, 0.0), (1.0, 0.0, 0.0), {"CE": 1.0}, False,
        "Fundamentos físicos, electrónica analógica, análisis de circuitos y teoría de señales (T,H)."
    ),
    (
        "R11_HW_ARCH",
        "Arquitectura y Organización de Computadoras",
        r"arquitectura (del|de|dos) comput|arquitectura y organizacion de (la computadora|computadores|computadoras)|"
        r"organizacion (y arquitectura|del computador|de computadoras|computacional|basica de computadores)|"
        r"organizacao de computadores|fundamentos de (organizacion de computadoras|arquitectura)|"
        r"taller de arquitectura|arquitectura de sistemas y computadores",
        (1.0, 0.0), (1.0, 0.0, 0.0), {"CE": 1.0}, False,
        "Estructura interna del procesador, jerarquía de memoria y organización de computadores (T,H)."
    ),
    (
        "R12_HW_APPLIED",
        "Hardware Aplicado: Sistemas Digitales, Microprocesadores, Embebidos y Robótica",
        r"sistemas (digitales|digitais|electronicos digitales|en chip|embebidos|embarcados)|"
        r"introducao aos sistemas digitais|diseno (digital|logico|de sistemas digitales)|"
        r"fundamentos de diseno digital|introduccion al diseno logico|logica digital|"
        r"circuitos (digitales|digitais|logicos)|maquinas digitales|elementos de computadores|"
        r"tecnologia de computadores|dispositivos electronicos|microcomputadoras|"
        r"microprocesadores|microprocessadores|microcontroladores|instrumentacion y control|"
        r"programacion de bajo nivel|lenguajes de interfaz|instalaciones electricas para centros de datos|"
        r"taller de robotica|robotica y automatizacion|tecnologias para la automatizacion|computo integrado|"
        r"electronica digital",
        (0.0, 1.0), (1.0, 0.0, 0.0), {"CE": 1.0}, False,
        "Diseño lógico digital, síntesis VLSI, microcontroladores, ensamblador y sistemas embebidos (A,H)."
    ),

    # -------------------------------------------------------------------------
    # BLOQUE D: SISTEMAS ORGANIZACIONALES, GESTIÓN DE TI Y SISTEMAS DE INFORMACIÓN (IS)
    # -------------------------------------------------------------------------
    (
        "R13_IS_SYS_THEORY",
        "Teoría de Sistemas y Dinámica Organizacional",
        r"teoria (general )?de sistemas|pensamiento sistemico|dinamica de sistemas|"
        r"metodos cuantitativos (para la toma de decisiones|de gestion)|"
        r"analisis de datos y toma de decisiones",
        (1.0, 0.0), (0.0, 0.0, 1.0), {"IS": 1.0}, False,
        "Fundamentos sistémicos y modelos formales de toma de decisiones organizacionales (T,O)."
    ),
    (
        "R14_IS_GOV_BPM",
        "Arquitectura Empresarial, Gobierno de TI y Procesos de Negocio (BPM)",
        r"arquitectura (empresarial|de infraestructura y gobierno)|gobierno y gestion de tecnologias|"
        r"gobernanza de tecnologias|gestion y gobernanza de ti|gestion estrategica de ti|"
        r"planeamiento estrategico (de ti|empresarial|de sistemas)|planificacion estrategica y sistemas de calidad|"
        r"estrategia y gestion de sistemas de informacion|modelado y automatizacion de procesos empresariales|"
        r"diseno y gestion de procesos organizacionales|modelo de procesos organizacionales|"
        r"taller de procesos organizacionales|gestion de procesos (de negocio|bpm|tecnologicos)|"
        r"reingenieria de procesos|organizacion y administracion de infraestructura de tecnologias",
        (0.0, 1.0), (0.0, 0.0, 1.0), {"IS": 1.0}, False,
        "Alineación estratégica de TI, gobernanza, arquitectura empresarial y procesos de negocio (A,O)."
    ),
    (
        "R15_IS_PM",
        "Formulación, Evaluación y Gestión de Proyectos de TI/Software",
        r"formulacion( y evaluacion|, evaluacion y gestion| y gestion)? de proyectos|"
        r"(gestion|administracion|gerencia y gestion|evaluacion y administracion|gestion y direccion|gestion y calidad|gestion y evaluacion) de proyectos|"
        r"administracion de proyectos (de software|tecnologicos)|proyectos de (ti|tecnologias de la informacion)|"
        r"ejecucion de proyectos de ti|elaboracion de proyectos|innovacion y gestion de proyectos|"
        r"gestion (de ti|informatica|gerencial)|administracion de tecnologias de informacion",
        (0.0, 1.0), (0.0, 0.0, 1.0), {"IS": 0.7, "SE": 0.3}, False,
        "Dirección, planificación económica y gestión de proyectos tecnológicos e informáticos (A,O)."
    ),
    (
        "R16_IS_HCI",
        "Factores Humanos e Interacción Humano-Computador (HCI / UX)",
        r"interaccion (humano|persona)|diseno de (interfaz|interfaces|experiencia)|"
        r"fundamentos de interaccion humano",
        (0.0, 1.0), (0.0, 0.0, 1.0), {"IS": 0.5, "SE": 0.5}, False,
        "Diseño centrado en el usuario, ergonomía cognitiva y experiencia de usuario (A,O)."
    ),
    (
        "R17_IS_INFO_SYS",
        "Sistemas de Información Empresariales e Inteligencia de Negocios",
        r"(analisis|diseno|administracion|implantacion|fundamentos) de sistemas de informacion|"
        r"^sistemas de informacion( para los negocios| empresariales| organizacionales)?$|"
        r"organizaciones y sistemas de informacion|sistemas y (procesos de negocio|organizaciones)|"
        r"sistemas (empresariales|de gestion)|inteligencia de negocios|negocios electronicos|"
        r"modelos de negocio y tecnologias|industria de ti|relaciones humanas en empresas|"
        r"gestion del conocimiento|diseno y gestion de sistemas",
        (0.0, 1.0), (0.0, 0.0, 1.0), {"IS": 1.0}, False,
        "Sistemas de información organizacionales, ERP, BI y comercio electrónico (A,O)."
    ),
    (
        "R18_IS_BIZ_LAW",
        "Economía, Finanzas, Administración, Auditoría y Legislación Informática",
        r"economi|finanz|contab|costos y presupuesto|analisis de costos|empresa y su entorno|"
        r"fundamentos de la empresa|cultura empresarial|gestion empresarial|^administracion$|administracion financiera|"
        r"taller de administracion|principios de administracion|teoria administrativa|direccion empresarial|"
        r"organizacion y (gestion empresarial|metodos)|nucleo gestion para ingenieros|analisis de capital humano|"
        r"fundamentos en gestion integral|emprend|auditoria (informatica|de sistemas)|"
        r"sistema de gestion de calidad|gestion de calidad y auditoria|"
        r"legislacion|deontologia|aspectos legales|etica y legislacion",
        (0.0, 1.0), (0.0, 0.0, 1.0), {"IS": 1.0}, False,
        "Gestión empresarial, ingeniería económica, finanzas, auditoría y marco legal de TI (A,O)."
    ),

    # -------------------------------------------------------------------------
    # BLOQUE E: CIENCIAS DE LA COMPUTACIÓN — TEORÍA, ALGORITMIA E INTELIGENCIA ARTIFICIAL (CS)
    # -------------------------------------------------------------------------
    (
        "R19_CS_DISCRETE_LOGIC",
        "Matemáticas Discretas, Lógica Formal y Pensamiento Computacional",
        r"matematicas? (computacionales y )?discreta|estructuras discretas|estruturas discretas|"
        r"algebra y matematica discreta|\blogica\b|pensamiento (logico|computacional|algoritmico)|"
        r"desarrollo del pensamiento logico",
        (1.0, 0.0), (0.0, 1.0, 0.0), {"CS": 1.0}, False,
        "Estructuras discretas, lógica matemática/computacional y pensamiento algorítmico (T,S)."
    ),
    (
        "R20_CS_ALGO_THEORY",
        "Algoritmos, Estructuras de Datos, Teoría de la Computación y Compiladores",
        r"estructura(s)? de datos|estruturas de dados|arboles y grafos|teoria dos grafos|"
        r"(analisis|analise|diseno|diseno avanzado|teoria|fundamentos) (y diseno |de )?algoritm|algoritmia y (complejidad|estructura)|"
        r"algoritmos (avanzados|y complejidad)|^algoritmos$|algoritmica|"
        r"teoria de (la computacion|autom|lenguajes|la informacion)|teoria da computacao|"
        r"matematica(s)? computacional(es)? y teoria|computabilidad|automatas|automatos|"
        r"lenguajes formales|linguagens formais|lenguajes y (automatas|maquinas|compiladores|paradigmas)|"
        r"sintaxis y semantica|compiladores|organizacion de lenguajes|informatica teorica|"
        r"desarrollo formal de sistemas|principios de computacion|teoria de base de datos|"
        r"analisis de lenguajes de programacion|paradigmas de programacion|programacion (logica|funcional)",
        (1.0, 0.0), (0.0, 1.0, 0.0), {"CS": 1.0}, False,
        "Núcleo teórico de CS: estructuras de datos, complejidad algorítmica, autómatas y compiladores (T,S)."
    ),
    (
        "R21_CS_AI_DS_GFX",
        "Inteligencia Artificial, Ciencia de Datos y Computación Gráfica/Científica",
        r"inteligencia artificial|inteligencia artificial|sistemas (inteligentes|basados en conocimiento)|"
        r"aprendizaje (automatico|estadistico|de maquina)|modelos de aprendizaje|vision artificial|"
        r"ciencia de datos|mineria de datos|computacion (grafica|cientifica|visual|ubicua)|"
        r"computacao grafica|graficacion|herramientas de computacion grafica",
        (1.0, 0.0), (0.0, 1.0, 0.0), {"CS": 1.0}, False,
        "Modelos de inteligencia artificial, aprendizaje automático, ciencia de datos y graficación (T,S)."
    ),

    # -------------------------------------------------------------------------
    # BLOQUE F: INGENIERÍA DE SOFTWARE Y PROGRAMACIÓN (SE)
    # -------------------------------------------------------------------------
    (
        "R22_SE_INTRO_PROG",
        "Algoritmos y Programación Inicial / Metodología de la Programación",
        r"algoritmos y (programacion|pseudocodigo|resolucion de problemas)|"
        r"algoritmia y programacion|algoritmos e programacao|desarrollo logico y algoritmos|"
        r"introduccion a los algoritmos|resolucion de problemas y algoritmos|"
        r"principios de desenvolvimento de algoritmos|metodologia(s)? de (la |diseno y )?programacion|"
        r"metodos de programacion",
        (0.5, 0.5), (0.0, 1.0, 0.0), {"CS": 0.5, "SE": 0.5}, True,
        "Cursos iniciales de resolución algorítmica e implementación en lenguajes de programación (0.5T/0.5A, S)."
    ),
    (
        "R23_SE_PROG_LANG",
        "Programación, Orientación a Objetos y Lenguajes de Programación",
        r"fundamentos de programacion|introduccion a la programacion|^programacion$|programacion (\d|i+|estructurada|avanzada|procedural|interactiva)|"
        r"programacion orientada a objetos|desarrollo (orientado al objeto|de software orientado a objetos)|"
        r"tecnologia orientada a objetos|tecnicas (y practicas )?de programacion|aplicacion practica de programacion|"
        r"taller de programacion|laboratorio de programacao|topicos (avanzados )?de programacion|"
        r"^lenguajes? de programacion|^lenguajes$|taller de lenguajes? (\d|i+)|"
        r"programacion (paralela|concurrente)|concurrencia y paralelismo|"
        r"implementacion de metodos computacionales|programacion de software de sistemas|"
        r"manejo e implementacion de archivos|interfaces graficas con aplicaciones",
        (0.0, 1.0), (0.0, 1.0, 0.0), {"SE": 0.7, "CS": 0.3}, False,
        "Construcción de programas, programación orientada a objetos, concurrente y uso de lenguajes (A,S)."
    ),
    (
        "R24_SE_CORE",
        "Ingeniería de Software, Requisitos, Arquitectura, Calidad y Proyectos de Software",
        r"ingenieria (de|del|y calidad de) software|engenharia de software|fundamentos de ingenieria de software|"
        r"introduccion a la ingenieria de software|desarrollo de software|introduccion al desarrollo de software|"
        r"software avanzado|metodologias de desarrollo|ingenieria de requisitos|analisis (de requerimientos|y especificacion de requerimientos)|"
        r"requerimientos y diseno|requisitos de software|arquitectura (de|del|y diseno de) software|"
        r"diseno (de|y arquitectura de) software|procesos y diseno de software|modelamiento y analisis de software|"
        r"analisis y diseno de (sistemas|software)|analisis de sistemas$|modelado de sistemas|"
        r"calidad (de|y pruebas de) software|gestion de la calidad de software|pruebas y aseguramiento|"
        r"verificacion y validacion de software|construccion (de software|y mantenimiento)|"
        r"evaluacion de procesos de software|herramientas de software|"
        r"proyecto de (software|diseno y desarrollo de software|implementacion de software)|"
        r"taller de desarrollo de proyectos de informatica|proyectos computacionales",
        (0.0, 1.0), (0.0, 1.0, 0.0), {"SE": 1.0}, False,
        "Ciclo de vida de ingeniería de software, requisitos, diseño, pruebas, calidad y construcción (A,S)."
    ),

    # -------------------------------------------------------------------------
    # BLOQUE G: TECNOLOGÍAS DE LA INFORMACIÓN — INFRAESTRUCTURA, REDES, BD, SO, SEGURIDAD Y WEB (IT)
    # -------------------------------------------------------------------------
    (
        "R25_IT_SEC",
        "Seguridad de la Información y Ciberseguridad",
        r"seguridad (informatica|de la informacion|de informacion|en sistemas|en los sistemas|en redes|de redes|en computo|en software|en la web)|"
        r"introduccion a la seguridad|fundamentos y aplicacion de seguridad|evaluacion de la seguridad|"
        r"administracion y seguridad de redes|gestion de servidores y seguridad|information security|"
        r"ciberseguridad|codificacion, criptografia y seguridad|desarrollo seguro de software",
        (0.0, 1.0), (0.0, 1.0, 0.0), {"IT": 1.0}, False,
        "Seguridad informática, criptografía aplicada, seguridad en redes e infraestructura (A,S / IT)."
    ),
    (
        "R26_IT_OS_DB_NET",
        "Sistemas Operativos, Bases de Datos, Redes, Nube y Desarrollo Web/Móvil/Integración",
        r"sistemas (operativos|operacionais|operacionales|distribuidos|de tiempo real)|"
        r"principios de sistemas operativos|conceptos de sistemas operativos|taller de sistemas operativos|"
        r"administracion de (sistemas operativos|servidores|servicios en red|redes|bases de datos)|"
        r"programacion para la administracion de sistemas|"
        r"base(s)? de datos|bancos? de dados|conceptos de bases de datos|fundamentos de base(s)? de datos|"
        r"diseno de bases de datos|taller de base(s)? de datos|sistemas de bases de datos|modelacion de datos|gestion y modelacion de datos|"
        r"\bred(es)?\b|conectividad|comunicacion de datos|comunicaciones|conmutacion y enrutamiento|"
        r"telecomunicaciones y redes|computacion (en la nube|distribuida|paralela y distribuida|aplicada)|"
        r"computo en la nube|desarrollo (web|basado en plataformas|de aplicaciones|y operaciones)|"
        r"introduccion al desarrollo web|programacion (web|orientada a la web|en la web|movil)|"
        r"tecnologias (web|para el desarrollo de aplicaciones web|de la informacion)|"
        r"tecnologia de informacion y comunicacion|fundamentos de tecnologias de la informacion|"
        r"fundamentos de infraestructura tecnologica|"
        r"aplicaciones (moviles|para comunicaciones en red|y herramientas de sistemas)|"
        r"soluciones web|videojuegos|realidad virtual|implantacion de sistemas|integracion de sistemas",
        (0.0, 1.0), (0.0, 1.0, 0.0), {"IT": 0.75, "SE": 0.25}, False,
        "Infraestructura de software, sistemas operativos, bases de datos, redes, nube y despliegue web/móvil (A,S)."
    ),

    # -------------------------------------------------------------------------
    # BLOQUE H: CIENCIAS BÁSICAS Y MÉTODOS MATEMÁTICOS GENERALES (STEM)
    # -------------------------------------------------------------------------
    (
        "R27_STEM_BASIC",
        "Ciencias Básicas Generales: Matemáticas, Estadística, Física, Química y Biología",
        r"calculo|precalculo|analisis (matematico|vectorial|numerico)|metodos (numericos|estadisticos|experimentales)|"
        r"experimentacion numerica|ecuaciones diferenciales|series de fourier|"
        r"algebra|geometria|vectores|vetores|matematica(s)?|fundamentos matematicos|complemento(s)? (matematico|de matematica)|"
        r"preliminares de matematica|temas selectos de matematicas|"
        r"probabilidad(es)?|estadistica|modelos de probabiliad|procesos estocasticos|"
        r"modelos estocasticos|investigacion (de operaciones|operativa)|optimizacion|"
        r"modelos y (simulacion|optimizacion)|modelacion (y simulacion|y optimizacion|matematica|computacional del movimiento)|"
        r"modelado( y simulacion|, simulacion y optimizacion)|simulacion|sistemas complejos|"
        r"fisica|mecanica|cinematica|dinamica del cuerpo|estatica|termodinamica|ondas|"
        r"electricidad|electromagnetismo|eletromagnetismo|electrostatica|estructura de la materia|"
        r"modelos fisicos|quimica|biologia|dibujo",
        (1.0, 0.0), (0.0, 0.0, 0.0), {"STEM": 1.0}, False,
        "Tronco de ciencias básicas e ingeniería matemática (puntúa en Teoría X, sin capa específica en Y)."
    ),
]

COMPILED_CODEBOOK = [
    (rule_id, cat_name, re.compile(pat), wx, wy, doms, is_hyb, note)
    for (rule_id, cat_name, pat, wx, wy, doms, is_hyb, note) in CODEBOOK_RULES
]


def classify_course(asignatura: str, condicion_raw: str = "Obligatoria", modo: str = "estandar"):
    """Clasifica una asignatura devolviendo un diccionario auditable completo.

    Parámetros:
    - modo="estandar": excluye optativas abiertas y electivas de catálogo (evita doble/triple conteo en D023).
    - modo="con_electivas_catalogo": evalúa también electivas con nombre técnico de catálogo (análisis de sensibilidad).
    """
    cond_norm = normalize_condition(asignatura, condicion_raw)
    n = norm_text(asignatura)

    if modo == "estandar" and cond_norm in ("Optativa_Generica", "Optativa_Catalogo"):
        return {
            "Condicion_Normalizada": cond_norm,
            "Regla_ID": "R01_EXCL_OPT",
            "Categoria": "Optativa/Electiva excluida del núcleo obligatorio",
            "wT": 0.0, "wA": 0.0,
            "wH": 0.0, "wS": 0.0, "wO": 0.0,
            "Pole_X": "", "Pole_Y": "",
            "Dominios": {},
            "Dominio_Principal": "EXCL",
            "Es_Hibrida": False,
            "Criterio": f"Excluida por condición curricular ({cond_norm})."
        }

    for rule_id, cat_name, rx, (wT, wA), (wH, wS, wO), doms, is_hyb, note in COMPILED_CODEBOOK:
        if rx.search(n):
            if wT > 0 and wA > 0:
                px = "T/A"
            elif wT > 0:
                px = "T"
            elif wA > 0:
                px = "A"
            else:
                px = ""

            if (wH > 0 and wS > 0) or (wS > 0 and wO > 0) or (wH > 0 and wO > 0):
                py = "/".join([k for k, v in [("H", wH), ("S", wS), ("O", wO)] if v > 0])
            elif wH > 0:
                py = "H"
            elif wS > 0:
                py = "S"
            elif wO > 0:
                py = "O"
            else:
                py = ""

            dom_princ = max(doms.items(), key=lambda kv: kv[1])[0] if doms else "EXCL"
            return {
                "Condicion_Normalizada": cond_norm,
                "Regla_ID": rule_id,
                "Categoria": cat_name,
                "wT": wT, "wA": wA,
                "wH": wH, "wS": wS, "wO": wO,
                "Pole_X": px, "Pole_Y": py,
                "Dominios": doms,
                "Dominio_Principal": dom_princ,
                "Es_Hibrida": is_hyb,
                "Criterio": note
            }

    return {
        "Condicion_Normalizada": cond_norm,
        "Regla_ID": "R00_UNMATCHED",
        "Categoria": "Sin coincidencia (Evidencia insuficiente)",
        "wT": 0.0, "wA": 0.0,
        "wH": 0.0, "wS": 0.0, "wO": 0.0,
        "Pole_X": "", "Pole_Y": "",
        "Dominios": {},
        "Dominio_Principal": "UNMATCHED",
        "Es_Hibrida": False,
        "Criterio": "Título insuficiente para asignar categoría sin descripción oficial."
    }
