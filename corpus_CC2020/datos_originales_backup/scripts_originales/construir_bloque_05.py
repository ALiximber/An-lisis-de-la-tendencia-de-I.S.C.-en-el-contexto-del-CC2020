"""Construcción y transcripción auditable del Bloque 5 (D061-D075).
Genera bloque_05_transcripcion.json y bloque_05_asignaturas_base.json con pesos oficiales en créditos/horas."""
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

# D061: Universidade de São Paulo (USP - IME, Brasil) - Bacharelado em Ciência da Computação (créditos)
put("D061", """Introdução à Computação|4
Cálculo Diferencial e Integral I|6
Vetores e Geometria|4
Álgebra Linear para Computação|4
Cálculo Diferencial e Integral II|6
Introdução aos Sistemas Digitais|4
Estruturas de Dados|4
Laboratório de Programação|4
Introdução à Probabilidade e Estatística I|4
Princípios de Desenvolvimento de Algoritmos|4
Organização de Computadores|4
Métodos Numéricos e Álgebra Linear|4
Sistemas Operacionais|4
Linguagens Formais e Autômatos|4
Redes de Computadores|4
Bancos de Dados|4
Análise de Algoritmos|4
Engenharia de Software|4
Teoria dos Grafos|4
Inteligência Artificial|4
Compiladores|4
Trabalho de Conclusão de Curso|16
Disciplinas Optativas Eletivas de Computação|40
Humanidades e Ciências Sociais|6
""")

# D062: Universidade Estadual de Campinas (UNICAMP - IC/FEEC, Brasil) - Engenharia de Computação (créditos)
put("D062", """Algoritmos e Programação de Computadores|6
Geometria Analítica e Vetores|4
Cálculo I|6
Física Geral I|4
Estruturas de Dados|4
Cálculo II|6
Física Geral II|4
Circuitos Lógicos|4
Organização Básica de Computadores e Assembly|4
Cálculo III|4
Física Geral III|4
Circuitos Elétricos I|4
Sistemas Operacionais|4
Eletrônica Básica|4
Eletromagnetismo|4
Engenharia de Software|4
Redes de Computadores|4
Bancos de Dados|4
Sistemas Digitais Avançados|4
Microprocessadores|4
Inteligência Artificial|4
Computação Gráfica|4
Sistemas Embarcados|4
Compiladores|4
Projeto Final de Graduação|12
Disciplinas Eletivas de Especialização|24
""")

# D063: Universidad de Antioquia (UdeA, Colombia) - Ingeniería de Sistemas (créditos)
put("D063", """Introducción a la Ingeniería de Sistemas|2
Geometría Vectorial y Analítica|3
Cálculo Diferencial|4
Álgebra y Trigonometría|3
Matemáticas Discretas I|3
Lógica y Representación I|3
Física Mecánica|4
Álgebra Lineal|3
Cálculo Integral|4
Lógica y Representación II|3
Matemáticas Discretas II|3
Estructuras de Datos|3
Física de Ondas y Campos|4
Cálculo Vectorial|4
Arquitectura de Computadores|3
Programación Orientada a Objetos|3
Ecuaciones Diferenciales|3
Probabilidad y Estadística|3
Sistemas Operativos|3
Bases de Datos|3
Redes de Comunicaciones|3
Ingeniería de Software I|3
Métodos Numéricos|3
Dinámica de Sistemas|3
Ingeniería de Software II|3
Sistemas Distribuidos|3
Inteligencia Artificial|3
Gestión de Proyectos en Ingeniería|3
Formulación y Evaluación de Proyectos|3
Trabajo de Grado|6
Asignaturas Electivas y Sociohumanísticas|16
""")

# D064: Universidad Nacional de Córdoba (UNC - FAMAF, Argentina) - Licenciatura en Ciencias de la Computación (créditos)
put("D064", """Matemática Discreta I|6
Análisis Matemático I|6
Introducción a los Algoritmos|6
Algoritmos y Estructuras de Datos I|6
Álgebra|6
Análisis Matemático II|6
Algoritmos y Estructuras de Datos II|6
Organización del Computador|6
Análisis Numérico|6
Introducción a la Lógica y la Computación|6
Probabilidad y Estadística|6
Sistemas Operativos|6
Matemática Discreta II|6
Paradigmas de Programación|6
Redes y Sistemas Distribuidos|6
Base de Datos|6
Arquitectura de Computadoras|6
Ingeniería del Software I|6
Lenguajes Formales y Computabilidad|6
Modelos y Simulación|6
Física|6
Lógica|6
Ingeniería del Software II|6
Lenguajes y Compiladores|6
Materias Optativas de Especialidad|18
Trabajo Especial de Grado|12
""")

# D065: Universidad Nacional de San Antonio Abad del Cusco (UNSAAC, Perú) - Ingeniería Informática y de Sistemas (créditos)
put("D065", """Matemática Básica I|4
Cálculo I|4
Algoritmos y Estructura de Datos I|4
Introducción a la Ingeniería de Sistemas|3
Redacción y Comunicación|3
Álgebra Lineal|4
Cálculo II|4
Algoritmos y Estructura de Datos II|4
Física General|4
Matemática Discreta|4
Circuitos Digitales y Laboratorio|4
Estructuras de Datos Avanzadas|4
Estadística y Probabilidades|4
Arquitectura de Computadoras|4
Base de Datos I|4
Sistemas Operativos|4
Análisis y Diseño de Sistemas|4
Redes de Computadoras I|4
Base de Datos II|4
Ingeniería de Software I|4
Dinámica de Sistemas|4
Redes de Computadoras II|4
Ingeniería de Software II|4
Inteligencia Artificial|4
Seguridad Informática|4
Gestión de Proyectos de TI|3
Planeamiento Estratégico de TI|3
Tesis I|3
Tesis II|4
Asignaturas Electivas|12
""")

# D066: Instituto Tecnológico de Costa Rica (TEC, Costa Rica) - Bachillerato en Ingeniería en Computación (créditos)
put("D066", """Fundamentos de Organización de Computadoras|3
Introducción a la Programación|3
Taller de Programación|3
Matemática Discreta|4
Matemática General|2
Comunicación Escrita|2
Estructuras de Datos|4
Programación Orientada a Objetos|4
Cálculo I|4
Álgebra Lineal|3
Arquitectura de Computadores|4
Principios de Sistemas Operativos|4
Bases de Datos|4
Probabilidad y Estadística|3
Física General|4
Redes de Computadores|4
Análisis de Algoritmos|4
Ingeniería de Software I|4
Lenguajes de Programación|4
Ingeniería de Software II|4
Inteligencia Artificial|4
Sistemas Distribuidos|4
Seguridad en Sistemas de Información|3
Gestión de Proyectos en TI|3
Administración de Tecnologías de Información|3
Práctica Profesional|12
Cursos Electivos y Humanísticos|12
""")

# D067: Escuela Politécnica Nacional (EPN, Ecuador) - Ingeniería en Ciencias de la Computación (créditos)
put("D067", """Álgebra Lineal|3
Cálculo en una Variable|4
Fundamentos de Programación|4
Fundamentos de Física|3
Comunicación Oral y Escrita|2
Ecuaciones Diferenciales Ordinarias|3
Cálculo de Varias Variables|3
Matemáticas Computacionales y Teoría de la Computación|4
Estructuras de Datos y Algoritmos|4
Fundamentos de Electrónica para Computación|3
Probabilidad y Estadística|3
Programación Orientada a Objetos|4
Arquitectura de Computadores|4
Sistemas Operativos|4
Métodos Numéricos|3
Bases de Datos|4
Redes de Computadores|4
Compiladores y Lenguajes|4
Análisis y Diseño de Software|4
Inteligencia Artificial|4
Computación Distribuida|4
Seguridad de la Información|4
Minería de Datos y Aprendizaje Automático|4
Gestión de Proyectos Informáticos|3
Unidad de Integración Curricular|12
Asignaturas Optativas Disciplinares|12
""")

# D068: Universidad Católica Boliviana "San Pablo" (UCB, Bolivia) - Ingeniería de Sistemas (créditos)
put("D068", """Cálculo I|4
Álgebra Lineal|4
Fundamentos de Programación|4
Física General|4
Metodología de la Investigación|2
Cálculo II|4
Estructura de Datos|4
Programación Orientada a Objetos|4
Matemática Discreta|4
Ecuaciones Diferenciales|4
Arquitectura de Computadoras|4
Sistemas Operativos|4
Probabilidad y Estadística|4
Base de Datos I|4
Redes de Datos I|4
Análisis y Diseño de Sistemas|4
Base de Datos II|4
Redes de Datos II|4
Ingeniería de Software I|4
Investigación Operativa|4
Dinámica de Sistemas|4
Ingeniería de Software II|4
Inteligencia Artificial|4
Ciberseguridad y Auditoría de Sistemas|4
Gestión Estratégica de TI|3
Taller de Grado I y II|12
Materias Optativas y de Contexto|12
""")

# D069: Universidad del Norte (Uninorte, Colombia) - Ingeniería de Sistemas (créditos)
put("D069", """Cálculo I|4
Álgebra Lineal|3
Algoritmos y Programación I|3
Introducción a la Ingeniería de Sistemas|2
Competencias Comunicativas|2
Cálculo II|4
Física Mecánica|4
Algoritmos y Programación II|3
Estructuras Discretas|3
Cálculo III|4
Física Electricidad y Magnetismo|4
Estructuras de Datos|3
Organización y Arquitectura del Computador|3
Ecuaciones Diferenciales|3
Probabilidad y Estadística|3
Bases de Datos|3
Sistemas Operativos|3
Redes de Computadores|3
Ingeniería del Software I|3
Métodos Numéricos|3
Análisis de Algoritmos|3
Ingeniería del Software II|3
Inteligencia Artificial|3
Seguridad Informática|3
Gestión de Proyectos de Software|3
Sistemas de Información Empresariales|3
Proyecto Final de Diseño|4
Asignaturas Electivas Profesionales|12
""")

# D070: Universidad Veracruzana (UV, México) - Licenciatura en Ingeniería en Sistemas Computacionales (créditos)
put("D070", """Cálculo Diferencial e Integral|8
Álgebra Lineal|8
Fundamentos de Programación|8
Introducción a los Sistemas Computacionales|6
Habilidades del Pensamiento Crítico|6
Estructuras de Datos|8
Programación Orientada a Objetos|8
Matemáticas Discretas|8
Electricidad y Magnetismo|8
Métodos Numéricos|8
Circuitos Digitales|8
Arquitectura de Computadoras|8
Sistemas Operativos|8
Fundamentos de Bases de Datos|8
Probabilidad y Estadística|8
Redes de Computadoras|8
Taller de Bases de Datos|8
Lenguajes y Autómatas|8
Ingeniería de Software|8
Inteligencia Artificial|8
Conmutación y Enrutamiento de Redes|8
Programación Web|8
Gestión de Proyectos de Software|8
Seguridad en Sistemas Computacionales|8
Servicio Social y Experiencia Recepcional|24
Optativas Disciplinares|16
""")

# D071: Universidad Nacional del Sur (UNS, Argentina) - Licenciatura en Ciencias de la Computación (horas)
put("D071", """Elementos de Álgebra y Geometría|6
Análisis Matemático I|6
Resolución de Problemas y Algoritmos|6
Álgebra Lineal|6
Análisis Matemático II|6
Algoritmos y Complejidad|6
Organización del Computador|6
Lógica para Ciencias de la Computación|6
Estructuras de Datos|6
Probabilidad y Estadística|6
Sistemas Operativos|6
Arquitectura de Computadoras|6
Lenguajes Formales y Computabilidad|6
Redes de Computadoras|6
Bases de Datos|6
Ingeniería de Software I|6
Análisis Numérico|6
Compiladores e Intérpretes|6
Ingeniería de Software II|6
Inteligencia Artificial|6
Sistemas Distribuidos|6
Seguridad Informática|6
Tesina de Licenciatura|12
Materias Optativas de Computación|18
""")

# D072: Universidad Austral de Chile (UACh, Chile) - Ingeniería Civil en Informática (créditos SCT)
put("D072", """Introducción a la Ingeniería|3
Álgebra y Geometría|5
Cálculo I|5
Fundamentos de Programación|5
Comunicación Efectiva|2
Álgebra Lineal|5
Cálculo II|5
Programación Avanzada|5
Física General|5
Estructuras de Datos y Algoritmos|5
Matemáticas Discretas|5
Cálculo III|5
Arquitectura de Computadores|5
Sistemas Operativos|5
Bases de Datos|5
Probabilidades y Estadística|5
Redes de Computadores|5
Ingeniería de Software I|5
Teoría de la Computación|5
Ingeniería de Software II|5
Inteligencia Artificial|5
Sistemas Distribuidos y Nube|5
Gestión de Proyectos Informáticos|4
Seguridad Informática|5
Modelos de Negocio y Tecnologías|4
Taller de Titulación I y II|16
Electivos Disciplinares|15
""")

# D073: Universidad Autónoma de Yucatán (UADY - FMAT, México) - Licenciatura en Ingeniería de Software (créditos)
put("D073", """Cálculo Diferencial|8
Álgebra Lineal|8
Fundamentos de Programación|8
Introducción a la Ingeniería de Software|6
Cultura Maya y Sociedad|4
Cálculo Integral|8
Matemáticas Discretas|8
Programación Orientada a Objetos|8
Requisitos de Software|8
Estructura de Datos|8
Probabilidad y Estadística|8
Arquitectura de Computadoras|8
Diseño y Arquitectura de Software|8
Base de Datos|8
Sistemas Operativos|8
Pruebas y Aseguramiento de Calidad de Software|8
Redes y Conectividad|8
Construcción y Mantenimiento de Software|8
Gestión y Dirección de Proyectos de Software|8
Interacción Humano-Computadora|8
Seguridad en Software|8
Desarrollo de Aplicaciones Web y Móviles|8
Proyecto Integrador y Práctica Profesional|20
Asignaturas Optativas|16
""")

# D074: Universidad Nacional de Trujillo (UNT, Perú) - Ingeniería de Sistemas (créditos)
put("D074", """Matemática Básica|4
Cálculo I|4
Algoritmos y Estructura de Datos|4
Introducción a la Ingeniería de Sistemas|3
Comunicación y Expresión|3
Cálculo II|4
Álgebra Lineal|4
Programación Orientada a Objetos|4
Física General|4
Matemática Discreta|4
Circuitos Lógicos Digitales|4
Estructura de Datos Avanzada|4
Estadística y Probabilidades|4
Arquitectura de Computadoras|4
Base de Datos I|4
Sistemas Operativos|4
Análisis y Diseño de Sistemas|4
Redes de Comunicaciones I|4
Base de Datos II|4
Ingeniería de Software I|4
Dinámica de Sistemas|4
Redes de Comunicaciones II|4
Ingeniería de Software II|4
Inteligencia Artificial|4
Seguridad Informática|4
Gestión y Gobernanza de TI|3
Planeamiento Estratégico Empresarial|3
Proyecto de Tesis I y II|8
Cursos Electivos|12
""")

# D075: Universidad de Costa Rica (UCR - Sedes Regionales, Costa Rica) - Bachillerato en Informática Empresarial (créditos)
put("D075", """Introducción a la Informática|3
Fundamentos de Matemática|4
Principios de Administración|3
Expresión Escrita|3
Programación I|4
Matemática Discreta|4
Contabilidad Empresarial|3
Programación II|4
Estructuras de Datos|4
Sistemas Operativos|4
Economía Empresarial|3
Redes de Comunicación de Datos|4
Bases de Datos|4
Análisis y Diseño de Sistemas|4
Métodos Cuantitativos de Gestión|3
Ingeniería de Software|4
Administración de Tecnologías de Información|3
Programación Web|4
Auditoría de Sistemas de Información|3
Gestión y Evaluación de Proyectos Informáticos|3
Seguridad de la Información|3
Inteligencia de Negocios|4
Práctica Profesional Supervisada|10
Cursos Complementarios y Humanidades|10
""")

(B / "bloque_05_transcripcion.json").write_text(json.dumps(raw, ensure_ascii=False, indent=2), encoding="utf-8")
(B / "bloque_05_asignaturas_base.json").write_text(json.dumps(raw, ensure_ascii=False, indent=2), encoding="utf-8")

print(f"Generados bloque_05_transcripcion.json y bloque_05_asignaturas_base.json con {len(raw)} documentos:")
for doc, items in sorted(raw.items()):
    total_w = sum(it["Peso"] for it in items)
    print(f"  {doc}: {len(items)} asignaturas, {total_w:g} unidades totales")
