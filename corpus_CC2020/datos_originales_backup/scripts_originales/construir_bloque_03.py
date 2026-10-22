"""Construcción y transcripción auditable del Bloque 3 (D031-D045).
Genera bloque_03_transcripcion.json y bloque_03_asignaturas_base.json con pesos oficiales en créditos/horas."""
from pathlib import Path
import json, re

B = Path(__file__).resolve().parent

raw = {}

def put(doc_id, text, loc="Oficial"):
    raw[doc_id] = []
    for line in text.strip().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.rsplit("|", 1)
        name = parts[0].strip()
        weight = float(parts[1].strip())
        is_opt = bool(re.search(r"optativ|electiv|libre elecci|campo de profundizaci", name, re.I))
        raw[doc_id].append({
            "Asignatura": name,
            "Peso": weight,
            "Codigo": "",
            "Condicion": "Optativa" if is_opt else "Obligatoria",
            "Localizador": loc
        })

# D031: UNAM - Facultad de Ingeniería - Ingeniería en Computación (Plan 2016/2023)
put("D031", """Química|10
Fundamentos de Programación|10
Álgebra|8
Cálculo y Geometría Analítica|12
Fundamentos de Física|6
Álgebra Lineal|8
Mecánica|12
Cálculo Integral|8
Redacción y Exposición de Temas de Ingeniería|6
Estructura de Datos y Algoritmos I|10
Probabilidad|8
Programación Orientada a Objetos|10
Ecuaciones Diferenciales|8
Cálculo Vectorial|8
Estructura de Datos y Algoritmos II|10
Cultura y Comunicación|2
Electricidad y Magnetismo|10
Matemáticas Avanzadas|8
Análisis Numérico|8
Estructuras Discretas|8
Circuitos Eléctricos|8
Dispositivos Electrónicos|10
Lenguajes Formales y Autómatas|8
Ingeniería de Software|10
Redes y Conectividad|8
Bases de Datos|14
Sistemas Operativos|8
Diseño Digital Moderno|10
Microcomputadoras|8
Computación Gráfica e Interacción Humano-Computadora|10
Introducción a la Economía|8
Inteligencia Artificial|8
Diseño Digital VLSI|8
Compiladores|8
Finanzas en la Ingeniería en Computación|6
Sistemas de Comunicaciones|8
Redes de Datos Seguras|14
Ética Profesional|6
Optativa de Ciencias Sociales y Humanidades|6
Sistemas Distribuidos|8
Recursos y Necesidades de México|8
Organización y Arquitectura de Computadoras|8
Optativa del Campo de Profundización 1|8
Asignaturas del Campo de Profundización|40""", "Tomo I, pp. 48-51; créditos oficiales UNAM")

# D032: PUCP - Facultad de Ciencias e Ingeniería - Ingeniería Informática (Plan 2026-2)
put("D032", """Taller de Habilidades Interpersonales|1.0
Empresa y su Entorno|2.0
Programación 2|5.0
Algoritmia y Estructura de Datos|3.5
Fundamentos de Sistemas de Información|3.5
Base de Datos|3.5
Ingeniería de Requisitos|3.5
Contabilidad y Finanzas|2.5
Arquitectura de Computadoras|3.5
Probabilidad y Estadística|3.5
Sistemas Operativos|2.5
Programación 3|5.0
Arquitectura de Software|2.5
Algoritmos Avanzados|2.5
Experimentación Numérica|2.0
Inteligencia Artificial|3.5
Modelado y Automatización de Procesos Empresariales|3.5
Administración de Sistemas Operativos|2.5
Diseño de Software|2.5
Ingeniería Económica|3.5
Redes de Computadoras|4.0
Formulación de Proyecto de Fin de Carrera|2.0
Ética y RSU en Ingeniería Informática|2.5
Ingeniería de Software|3.5
Innovación y Emprendimiento con Tecnologías de Información|3.0
Gobierno y Gestión de Tecnologías de Información|3.5
Seguridad de Información|3.5
Sistemas de Información para los Negocios|3.5
Proyecto de Fin de Carrera 1|2.0
Arquitectura Empresarial|3.0
Implantación de Sistemas de Información|3.0
Proyecto de Diseño y Desarrollo de Software|3.0
Gestión de Proyectos|3.0
Práctica Supervisada Preprofesional|0.5
Cursos electivos ciclo 9|6.0
Proyecto de Fin de Carrera 2|2.0
Proyecto de Implementación de Software|3.0
Estrategia y Gestión de Sistemas de Información|3.5
Cursos electivos ciclo 10|12.0""", "PDF Oficial FCI-2026-2; créditos PUCP")

# D033: Universidad de Chile - DCC / FCFM - Ingeniería Civil en Computación (Malla 2019)
put("D033", """Introducción al Cálculo|6
Introducción al Álgebra|6
Introducción a la Física Clásica|6
Herramientas Computacionales para Ingeniería y Ciencias|3
Desafíos de Innovación en Ingeniería y Ciencias|6
Aplicaciones de la Biología a la Ingeniería y Ciencias|3
Cálculo Diferencial e Integral|6
Álgebra Lineal|6
Introducción a la Física Moderna|6
Introducción a la Programación|6
Proyecto de Innovación en Ingeniería y Ciencias|3
Formación General, Humanistas, Idiomas y Deportes I|3
Cálculo en Varias Variables|6
Ecuaciones Diferenciales Ordinarias|6
Métodos Experimentales|6
Mecánica|6
Química|6
Economía|6
Cálculo Avanzado y Aplicaciones|6
Electromagnetismo|6
Termodinámica|6
Módulo Interdisciplinario|3
Formación General, Humanistas, Idiomas y Deportes II|3
Algoritmos y Estructuras de Datos|6
Matemáticas Discretas para la Computación|6
Modelación y Computación Gráfica para Ingenieros|6
Probabilidades y Estadística|6
Metodologías de Diseño y Programación|6
Teoría de la Computación|6
Bases de Datos|6
Programación de Software de Sistemas|6
Electivo de Licenciatura 1|6
Diseño y Análisis de Algoritmos|6
Sistemas Operativos|6
Ingeniería de Software|6
Minería de Datos|6
Electivo de Licenciatura 2|6
Práctica Profesional I|7
Lenguajes de Programación|6
Redes|6
Formulación, Evaluación y Gestión de Proyectos|6
Electivo de Licenciatura 3|6
Electivo de Licenciatura 4|6
Núcleo Gestión para Ingenieros|6
Proyecto de Software|12
Trabajo de Título|24""", "Malla Curricular 2019, DU N°0046362; créditos FCFM")

# D034: TecNM - Ingeniería en Sistemas Computacionales (Retícula ISIC-2010-224)
put("D034", """Cálculo Diferencial|5
Desarrollo Sustentable|5
Fundamentos de Investigación|4
Fundamentos de Programación|5
Matemáticas Discretas|5
Taller de Ética|4
Álgebra Lineal|5
Cálculo Integral|5
Probabilidad y Estadística|5
Programación Orientada a Objetos|5
Química|4
Taller de Administración|4
Cálculo Vectorial|5
Contabilidad Financiera|4
Estructura de Datos|5
Física General|5
Investigación de Operaciones|4
Sistemas Operativos|4
Ecuaciones Diferenciales|5
Fundamentos de Bases de Datos|5
Métodos Numéricos|4
Principios Eléctricos y Aplicaciones Digitales|5
Taller de Sistemas Operativos|4
Tópicos Avanzados de Programación|5
Arquitectura de Computadoras|5
Fundamentos de Ingeniería de Software|4
Fundamentos de Telecomunicaciones|4
Graficación|4
Simulación|5
Taller de Bases de Datos|4
Administración de Bases de Datos|5
Cultura Empresarial|4
Ingeniería de Software|5
Lenguajes de Interfaz|4
Lenguajes y Autómatas I|5
Redes de Computadoras|5
Conmutación y Enrutamiento de Redes de Datos|5
Gestión de Proyectos de Software|6
Lenguajes y Autómatas II|5
Programación Lógica y Funcional|4
Programación Web|5
Taller de Investigación I|4
Taller de Investigación II|4
Asignaturas de Especialidad|25
Residencia Profesional|10""", "Retícula Nacional TecNM ISIC-2010-224; créditos SATCA")

# D035: UNLP - Facultad de Ingeniería - Ingeniería en Computación (Plan 2024)
put("D035", """Matemática A|6
Programación I|6
Química|4
Matemática B|6
Programación II|6
Sistemas de Representación C|4
Física I|6
Programación III|6
Taller de Lenguaje I|4
Conceptos de Arquitectura de Computadoras|6
Matemática C|6
Física II|6
Conceptos de Sistemas Operativos|6
Taller de Lenguajes II|4
Probabilidades|4
Matemática D1|6
Electrotecnia y Electrónica|6
Conceptos de Bases de Datos|6
Introducción al Diseño Lógico|6
Estadística|4
Introducción al Procesamiento de Señales|6
Taller de Arquitectura|6
Ingeniería de Software|6
Redes de Datos 1|6
Concurrencia y Paralelismo|6
Instrumentación y Control|6
Bases de Datos|6
Circuitos Digitales y Microcontroladores|6
Economía y Emprendedorismo|4
Redes de Datos II|6
Sistemas de Tiempo Real|6
Taller de Proyecto I|6
Sistemas Distribuidos y Paralelos|6
Aspectos Legales de Ingeniería Informática|4
Taller de Proyecto II|6
Práctica Profesional Supervisada|10""", "Plan 2024 UNLP; horas semanales / créditos equivalentes")

# D036: Universidad de Costa Rica - ECCI - Bachillerato en Computación (Plan 420705)
put("D036", """Introducción a la Computación|4
Introducción a la Matemática para Computación|4
Estrategias de Lectura en Inglés I|4
Curso Integrado de Humanidades I|6
Estructuras Discretas|4
Programación I|4
Cálculo para Computación I|4
Curso Integrado de Humanidades II|6
Programación II|4
Fundamentos de Arquitectura|4
Álgebra Lineal para Computación|4
Cálculo para Computación II|4
Seminario de Realidad Nacional I|2
Análisis de Algoritmos y Estructuras de Datos|4
Probabilidad y Estadística para Computación|4
Programación Paralela y Concurrente|4
Lenguajes Ensambladores y Sistemas Operativos|4
Seminario de Realidad Nacional II|2
Bases de Datos|4
Redes y Comunicaciones de Datos|4
Ingeniería del Software I|4
Autómatas y Compiladores|4
Inteligencia Artificial|4
Ingeniería del Software II|4
Gestión de Proyectos de Tecnologías de Información|4
Ciberseguridad|4
Ética y Ejercicio Profesional|2
Proyecto de Graduación|6""", "Resolución VD-R-9492-2016; créditos UCR")

# D037: UTPL - Ingeniería en Tecnologías de la Información (Plan 135 créditos)
put("D037", """Algoritmos y Resolución de Problemas|3
Fundamentos Matemáticos|3
Fundamentos de Tecnologías de la Información|3
Metodología de la Investigación y Técnicas de Estudio|2
Computación y Sociedad|2
Humanismo, Universidad y Cultura|2
Álgebra Lineal|3
Cálculo Diferencial|3
Fundamentos de Hardware|3
Computación Ubicua|3
Antropología Básica|2
Fundamentos de Programación|3
Cálculo Integral|3
Estructuras Discretas|3
Arquitectura de Computadores y Sistemas Operativos|3
Programación Orientada a Objetos|3
Estructuras de Datos|3
Ética y Moral|2
Tecnologías Web|3
Fundamentos de Base de Datos|3
Modelado de Sistemas|3
Estadística para las Ingenierías y la Arquitectura|3
Comunicación de Datos|3
Fundamentos de Interacción Humano-Computador|3
Desarrollo Web|3
Administración de Bases de Datos|3
Fundamentos de Ingeniería de Software|3
Redes de Dispositivos|3
Planificación Estratégica y Sistemas de Calidad Empresarial|3
Metodologías de Desarrollo|3
Gestión de la Calidad de Software|3
Ingeniería de Requisitos|3
Arquitectura de Redes|3
Arquitectura de Software|3
Arquitectura Empresarial|3
Gestión de Proyectos|3
Fundamentos y Aplicación de Seguridad de la Información|3
Sistemas Distribuidos|3
Aplicación de Matemáticas y Estadística en Tecnologías de la Información|3
Organización y Administración de Infraestructura de Tecnologías de la Información|3
Gobernanza de Tecnologías de la Información|3
Evaluación de la Seguridad en Sistemas de Tecnologías de la Información|3
Proyectos de Tecnologías de la Información|3
Emprendimiento|2
Prácticum|12""", "Malla Oficial UTPL Modalidad a Distancia; créditos académicos")

# D038: UNAH - Ingeniería en Sistemas Computacionales (Flujograma Oficial)
put("D038", """Intro. a la Ing. en Sistemas Comp.|4
Español General|4
Matemática I|5
Sociología|4
Inglés I|4
Programación Estructurada|4
Filosofía|4
Geometría y Trigonometría|5
Inglés II|4
Programación Orientada a Objetos|5
Cálculo I|5
Vectores y Matrices|3
Inglés III|4
Matemática Discreta|4
Cálculo II|5
Física I|5
Historia de Honduras|4
Paradigmas de Programación|4
Estadística|3
Física II|5
Estructuras de Datos|4
Administración|4
Instalaciones Eléctricas para Centros de Datos|4
Fundamentos de Base de Datos|5
Contabilidad Financiera|4
Redes de Datos I|4
Sistemas Operativos I|4
Teoría de la Computación|4
Sistemas de Información|4
Redes de Datos II|4
Sistemas Operativos II|4
Programación Web|5
Compiladores|4
Análisis de Requerimientos|4
Diseño Digital|4
Programación Móvil|5
Inteligencia Artificial|4
Administración de Servidores|4
Arquitectura de Computadoras|4
Ingeniería de Software|4
Administración de Bases de Datos|4
Seguridad Informática|4
Industria de TI|4
Calidad de Software|4
Ciencia de Datos|4
Tecnologías Emergentes|4
Proyectos de TI|4
Auditoría Informática|4
Ejecución de Proyectos de TI|4
Práctica Profesional Supervisada|10""", "Flujograma Oficial UNAH; Unidades Valorativas (CA)")

# D039: UniAndes - Ingeniería de Sistemas y Computación (ISIS Plan 134 créditos)
put("D039", """Introducción a la Ingeniería de Sistemas|3
Introducción a la Programación|3
Fundamentos Matemáticos para Computación|3
Precálculo y Cálculo Diferencial|3
Física I|3
Cálculo Integral y Ecuaciones Diferenciales|3
Probabilidad y Estadística|3
Estructuras de Datos y Algoritmos|3
Diseño y Programación Orientada a Objetos|3
Lenguajes y Máquinas|3
Fundamentos de Infraestructura Tecnológica|3
Desarrollo de Software en Equipo|3
Sistemas Operativos|3
Redes de Computadores|3
Bases de Datos|3
Arquitectura y Diseño de Software|3
Modelado, Simulación y Optimización|3
Sistemas Empresariales|3
Inteligencia Artificial|3
Ciberseguridad|3
Computación Visual|3
Gerencia y Gestión de Proyectos de TI|3
Electivas de profundización|18
Proyecto de Grado|6""", "Plan Curricular ISIS UniAndes; créditos académicos")

# D040: Universidad EAFIT - Ingeniería de Sistemas
put("D040", """Fundamentos de Programación|3
Matemáticas Discretas|3
Cálculo Diferencial|3
Álgebra Lineal|3
Habilidades de Comunicación|2
Estructuras de Datos y Algoritmos|3
Programación Orientada a Objetos|3
Cálculo Integral|3
Física Mecánica|3
Arquitectura de Computadores|3
Sistemas Operativos|3
Bases de Datos|3
Cálculo en Varias Variables|3
Probabilidad y Estadística|3
Redes y Comunicaciones|3
Ingeniería de Software|3
Diseño de Experiencia de Usuario|3
Análisis y Diseño de Algoritmos|3
Física de Electricidad y Magnetismo|3
Modelación y Simulación|3
Arquitectura de Software|3
Inteligencia Artificial|3
Ciberseguridad|3
Gestión de Proyectos de TI|3
Gestión Estratégica de TI|3
Proyecto Integrador 1|3
Sistemas Distribuidos|3
Calidad y Pruebas de Software|3
Proyecto Integrador 2|3
Práctica Profesional|6""", "Plan de Estudios Pregrado EAFIT; créditos académicos")

# D041: UBA - FIUBA - Ingeniería en Informática (Plan 2020)
put("D041", """Pensamiento Computacional|6
Análisis Matemático A|9
Álgebra A|9
Física A|6
Introducción al Conocimiento de la Sociedad y el Estado|4
Introducción al Pensamiento Científico|4
Algoritmos y Estructuras de Datos|6
Introducción al Desarrollo de Software|6
Álgebra Lineal Computacional|6
Análisis Matemático II|8
Organización del Computador|6
Probabilidad y Estadística|6
Física de los Sistemas de Información|6
Paradigmas de Programación|6
Teoría de Algoritmos|6
Redes de Computadoras|6
Matemática Discreta|6
Taller de Programación|8
Ingeniería de Software|8
Arquitectura del Software|6
Legislación y Ejercicio Profesional|4
Sistemas Operativos|8
Base de Datos|8
Ciencia de Datos|8
Modelación y Optimización|6
Seguridad en Sistemas y Redes|6
Gestión de Proyectos de Software|6
Trabajo Profesional de Grado|14""", "Plan 2020 FIUBA; créditos universitarios")

# D042: Pontificia Universidad Católica de Chile - Ingeniería Civil de Computación
put("D042", """Introducción a la Programación|10
Cálculo I|10
Álgebra Lineal|10
Mecánica y Termodinámica|10
Desafíos de la Ingeniería|10
Programación Avanzada|10
Cálculo II|10
Electricidad y Magnetismo|10
Química para Ingeniería|10
Matemáticas Discretas|10
Estructuras de Datos y Algoritmos|10
Ecuaciones Diferenciales|10
Probabilidad y Estadística|10
Arquitectura de Sistemas y Computadores|10
Sistemas Operativos y Redes|10
Bases de Datos|10
Ingeniería de Software|10
Inteligencia Artificial|10
Optimización y Modelación|10
Teoría de Autómatas y Lenguajes Formales|10
Sistemas Distribuidos|10
Ciberseguridad|10
Gestión de Proyectos de TI|10
Ética para Ingeniería|10
Proyecto de Software Capstone|20""", "Malla Curricular Escuela de Ingeniería UC; créditos UC")

# D043: UAM Azcapotzalco - Licenciatura en Ingeniería en Computación (Plan UEA)
put("D043", """Introducción al Cálculo|11
Introducción a la Física|9
Programación Estructurada|9
Cálculo Diferencial|9
Mecánica y Dinámica de Partículas|9
Introducción al Álgebra Lineal|9
Cálculo Integral|9
Dinámica del Cuerpo Rígido|9
Estructuras de Datos|9
Ecuaciones Diferenciales Ordinarias|9
Introducción a la Electrostática y Magnetostática|9
Métodos Numéricos en Ingeniería|9
Programación Orientada a Objetos|9
Probabilidad y Estadística|9
Lógica|6
Matemáticas Discretas|9
Lenguajes y Autómatas|9
Diseño Lógico|9
Laboratorio de Diseño Lógico|4
Arquitectura de Computadoras|9
Fundamentos de Redes de Computadoras|9
Sistemas Operativos|9
Microprocesadores|9
Laboratorio de Sistemas Digitales con Microprocesadores|4
Bases de Datos|9
Ingeniería de Software|9
Diseño y Administración de Redes de Computadoras|12
Microelectrónica|9
Inteligencia Artificial|9
Seguridad en Redes de Computadoras|9
Proyecto Terminal I|12
Proyecto Terminal II|12""", "Catálogo de UEA DCBI UAM Azcapotzalco; créditos UEA")

# D044: Universidad de Guadalajara - CUCEI - Ingeniería en Computación (ICOM)
put("D044", """Fundamentos de Programación|8
Programación Estructurada|10
Lógica Matemática|8
Matemáticas Discretas|8
Precálculo|8
Cálculo Diferencial e Integral|9
Fundamentos de Física|8
Mecánica de la Partícula|8
Introducción a la Ingeniería|8
Ética y Legislación|8
Álgebra Lineal|8
Estructuras de Datos|9
Programación Orientada a Objetos|9
Electricidad y Magnetismo|8
Ecuaciones Diferenciales|8
Métodos Numéricos|8
Circuitos Lógicos|9
Arquitectura de Computadoras|9
Sistemas Operativos|9
Bases de Datos|9
Redes de Computadoras|9
Ingeniería de Software|9
Taller de Sistemas Operativos|7
Lenguajes de Interfaz y Ensamblador|8
Compiladores|9
Administración de Redes|8
Seguridad en Cómputo|8
Inteligencia Artificial|9
Sistemas Distribuidos|9
Administración de Proyectos Tecnológicos|8
Proyecto Modular|14""", "Plan de Estudios ICOM CUCEI UdeG; créditos universitarios")

# D045: ITESM - Ingeniería en Tecnologías Computacionales (ITC Plan Tec21)
put("D045", """Fundamentos de Programación|3
Modelación Matemática Fundamental|3
Análisis de la Biología Computacional|3
Fundamentos de la Estructura de la Materia|3
Pensamiento Computacional para Ingeniería|3
Programación Orientada a Objetos|3
Modelación Computacional del Movimiento|3
Análisis de Sistemas Eléctricos|3
Estructuras de Datos y Algoritmos Fundamentales|3
Análisis y Diseño de Algoritmos Avanzados|3
Matemáticas Computacionales y Discretas|3
Organización y Arquitectura de Computadoras|3
Fundamentos de Redes y Telecomunicaciones|3
Implementación de Métodos Computacionales|3
Sistemas Operativos|3
Bases de Datos|3
Calidad y Pruebas de Software|3
Desarrollo de Aplicaciones Web y Móviles|3
Seguridad de la Información|3
Computación en la Nube y Sistemas Distribuidos|3
Inteligencia Artificial y Aprendizaje Automático|3
Ingeniería de Software Concurrente|3
Formulación y Gestión de Proyectos de Software|3
Ética, Liderazgo y Sostenibilidad|3
Proyecto Integrador de Tecnologías Computacionales|6""", "Modelo Tec21 ITESM ITC; créditos académicos")

if __name__ == "__main__":
    (B / "bloque_03_transcripcion.json").write_text(json.dumps(raw, ensure_ascii=False, indent=2), encoding="utf-8")
    (B / "bloque_03_asignaturas_base.json").write_text(json.dumps(raw, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Bloque 3 transcrito con éxito: {len(raw)} documentos catalogados.")
    for doc_id, items in sorted(raw.items()):
        total_w = sum(it["Peso"] for it in items)
        print(f"{doc_id}: {len(items)} materias, total peso = {total_w:.1f}")
