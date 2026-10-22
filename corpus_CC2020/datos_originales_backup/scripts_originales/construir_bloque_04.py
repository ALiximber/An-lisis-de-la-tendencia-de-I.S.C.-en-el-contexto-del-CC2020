"""Construcción y transcripción auditable del Bloque 4 (D046-D060).
Genera bloque_04_transcripcion.json y bloque_04_asignaturas_base.json con pesos oficiales en créditos/horas."""
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

# D046: Universidad de la República (UdelaR FING, Uruguay) - Ingeniería en Computación (créditos)
put("D046", """Cálculo Diferencial e Integral en una Variable|13
Geometría y Álgebra Lineal 1|9
Programación 1|10
Matemática Discreta 1|9
Cálculo Diferencial e Integral en Varias Variables|13
Geometría y Álgebra Lineal 2|9
Programación 2|12
Lógica|10
Física 1|10
Probabilidad y Estadística|10
Programación 3|15
Arquitectura de Computadoras|12
Sistemas Operativos|12
Teoría de Lenguajes|12
Redes de Computadoras|12
Bases de Datos|15
Ingeniería de Software|15
Inteligencia Artificial|12
Investigación de Operaciones|12
Taller de Programación|10
Seguridad Informática|10
Proyecto de Fin de Carrera|30
Materias Optativas y Electivas de Especialización|60
Asignaturas de Ciencias Sociales y Humanas|15
""")

# D047: Universidad Nacional de San Agustín de Arequipa (UNSA, Perú) - Ingeniería de Sistemas (créditos)
put("D047", """Álgebra Lineal|4
Estructuras Discretas I|4
Introducción al Desarrollo de Software|5
Introducción a la Ingeniería|3
Relaciones Humanas en Empresas de Software|2
Metodología del Trabajo Académico|2
Matemática Básica|4
Cálculo en una Variable|5
Estructuras Discretas II|3
Introducción al Desarrollo Web|4
Desarrollo de Software Orientado a Objetos|4
Realidad Nacional|2
Cálculo de Varias Variables|4
Algoritmos y Estructuras de Datos|4
Arquitectura y Organización de Computadores|4
Fundamentos de Sistemas de Información|3
Física para la Computación|4
Base de Datos I|4
Sistemas Operativos|4
Redes y Comunicación de Datos I|4
Estadística y Probabilidades|4
Ingeniería de Software I|4
Base de Datos II|4
Redes y Comunicación de Datos II|4
Inteligencia Artificial|4
Ingeniería de Software II|4
Ciberseguridad|4
Gestión de Proyectos de Tecnologías de Información|3
Arquitectura Empresarial|3
Proyecto de Fin de Carrera I|4
Proyecto de Fin de Carrera II|4
""")

# D048: Universidad de Concepción (UdeC, Chile) - Ingeniería Civil Informática (créditos)
put("D048", """Introducción a la Ingeniería Informática|2
Introducción a la Programación|4
Cálculo I|4
Álgebra I|4
Química General|3
Programación I|4
Cálculo II|4
Álgebra Lineal|4
Física I|4
Estructura de Datos|4
Desarrollo Orientado al Objeto|4
Lógica|4
Cálculo III|4
Física II|4
Análisis de Algoritmos|4
Sistemas Computacionales y Arquitectura de Computadores|4
Ecuaciones Diferenciales|4
Probabilidades y Estadística|4
Redes de Computadores|4
Bases de Datos|4
Sistemas Operativos|4
Ingeniería de Software I|4
Ingeniería de Software II|4
Inteligencia Artificial|4
Gestión Informática|4
Informática y Sociedad|2
Optimización|4
Proyecto de Software|6
Memoria de Título|12
Electivos de Especialidad|16
""")

# D049: Universidad Industrial de Santander (UIS, Colombia) - Ingeniería de Sistemas (créditos)
put("D049", """Cálculo I|4
Fundamentos de Programación|4
Química Básica|4
Álgebra Lineal I|4
Taller de Lenguaje|3
Cálculo II|4
Ética Ciudadana|3
Física I|4
Programación Orientada a Objetos|4
Biología para Ingenieros|2
Cálculo III|4
Física II|4
Matemáticas Discretas|4
Estructuras de Datos y Análisis de Algoritmos|4
Ecuaciones Diferenciales|4
Física III|4
Electricidad y Electrónica|4
Autómatas y Lenguajes Formales|4
Base de Datos I|4
Base de Datos II|4
Sistemas Digitales|4
Análisis Numérico I|4
Pensamiento Sistémico y Organizacional|4
Dirección Empresarial I|3
Redes de Computadores I|4
Arquitectura de Computadores|4
Programación en la Web|4
Sistemas de Información|4
Estadística I|4
Ingeniería del Software I|4
Redes de Computadores II|4
Inteligencia Artificial|4
Sistemas Operacionales|4
Ingeniería del Software II|4
Simulación Digital|4
Ingeniería Económica|3
Trabajo de Grado I|4
Trabajo de Grado II|6
Asignaturas Electivas Profesionales|12
""")

# D050: Universidad Autónoma de Nuevo León (UANL - FIME, México) - Ingeniero en Tecnología de Software (créditos)
put("D050", """Metodología de la Programación|4
Cálculo Diferencial|4
Álgebra para Ingeniería|3
Geometría Analítica|3
Mecánica Clásica y Laboratorio|4
Química General y Laboratorio|4
Cultura de Paz y Derechos Humanos|2
Cálculo Integral|4
Aplicación Práctica de Programación|3
Probabilidad y Estadística|3
Ondas y Calor y Laboratorio|4
Responsabilidad Social y Desarrollo Sustentable|2
Matemáticas Discretas|3
Ecuaciones Diferenciales|3
Electricidad y Magnetismo y Laboratorio|4
Lenguajes de Programación y Laboratorio|3
Estructura de Datos y Diseño de Algoritmos|3
Base de Datos|3
Programación Orientada a Objetos y Laboratorio|4
Sistemas Digitales y Laboratorio|4
Series de Fourier y Transformadas de Laplace|3
Sistemas Operativos|3
Métodos Numéricos|3
Interacción Humano-Computadora y Laboratorio|3
Arquitectura de Computadoras|3
Transmisión y Comunicación de Datos|3
Verificación y Validación de Software|3
Modelado y Simulación de Sistemas Dinámicos|3
Cómputo Integrado|3
Servicio Social|16
Prácticas Profesionales|10
Optativas Profesionales|12
""")

# D051: Universidad Nacional de Asunción (UNA - FP-UNA, Paraguay) - Ingeniería en Informática (créditos)
put("D051", """Fundamentos de Matemáticas|5
Matemática Discreta|5
Organización y Arquitectura de Computadoras I|5
Algoritmos y Estructuras de Datos I|6
Expresión Oral y Escrita|3
Álgebra Lineal|5
Cálculo I|5
Organización y Arquitectura de Computadoras II|5
Lenguajes de Programación I|5
Algoritmos y Estructuras de Datos II|6
Cálculo II|5
Física General|5
Lógica para Ciencias de la Computación|5
Sistemas Operativos|5
Lenguajes de Programación II|5
Probabilidad y Estadística|5
Redes de Computadoras I|5
Base de Datos I|5
Ingeniería de Software I|5
Teoría de Lenguajes y Compiladores|5
Redes de Computadoras II|5
Base de Datos II|5
Ingeniería de Software II|5
Sistemas Distribuidos|5
Inteligencia Artificial|5
Seguridad Informática|5
Gestión de Proyectos de Software|4
Economía y Finanzas|3
Pasantía Profesional Supervisada|6
Trabajo Final de Grado|12
Asignaturas Optativas y Electivas|20
""")

# D052: Universidad Tecnológica de Panamá (UTP - FISC, Panamá) - Licenciatura en Ingeniería de Sistemas y Computación (créditos)
put("D052", """Cálculo I|5
Dibujo Asistido por Computadoras|3
Desarrollo Lógico y Algoritmos|4
Tecnología de Información y Comunicación|4
Comunicación Oral y Escrita|3
Cálculo II|5
Cálculo III|4
Lenguaje de Programación I|4
Química I|4
Estructura de Datos I|4
Física I (Mecánica)|5
Estadística con Apoyo Informático|3
Lenguaje de Programación II|4
Estructuras Discretas para la Computación|4
Ecuaciones Diferenciales Ordinarias|5
Estructura de Datos II|4
Física II (Electricidad y Magnetismo)|5
Métodos Numéricos para Ingeniería|4
Interacción Humano Computador|3
Formulación y Evaluación de Proyectos Informáticos|3
Organización y Arquitectura de Computadoras|4
Sistemas Operativos|4
Redes de Computadoras|4
Base de Datos I|4
Ingeniería de Software I|4
Base de Datos II|4
Ingeniería de Software II|4
Inteligencia Artificial|4
Herramientas de Computación Gráfica|3
Análisis de Datos y Toma de Decisiones|4
Seguridad en Sistemas Computacionales|4
Práctica Profesional o Trabajo de Graduación|12
""")

# D053: Universidad de San Carlos de Guatemala (USAC, Guatemala) - Ingeniería en Ciencias y Sistemas (créditos)
put("D053", """Área Matemática Básica 1|9
Técnicas de Estudio e Investigación|3
Área Social Humanística 1|3
Área Matemática Básica 2|9
Física Básica|5
Introducción a los Algoritmos y Flujo de Datos|4
Matemática para Computación 1|5
Matemática Intermedia 1|10
Física 1|6
Estructura de Datos|5
Organización Computacional|4
Matemática para Computación 2|5
Lenguajes Formales y de Programación|4
Arquitectura de Computadores 1|5
Sistemas Operativos 1|5
Manejo e Implementación de Archivos|4
Análisis y Diseño de Sistemas 1|5
Organización de Lenguajes y Compiladores 1|5
Sistemas Operativos 2|5
Sistemas de Bases de Datos 1|5
Arquitectura de Computadores 2|5
Análisis y Diseño de Sistemas 2|5
Redes de Computadoras 1|4
Sistemas de Bases de Datos 2|5
Inteligencia Artificial 1|4
Software Avanzado|5
Seguridad y Auditoría de Sistemas|4
Seminario de Sistemas|3
Práctica Inicial, Intermedia y Final|10
Seminario de Investigación de Graduación|6
""")

# D054: Universidad Nacional Mayor de San Marcos (UNMSM - FISI, Perú) - Ingeniería de Sistemas (créditos)
put("D054", """Cálculo I|4
Álgebra Lineal|4
Algorítmica I|4
Introducción a la Ingeniería de Sistemas|3
Comunicación y Redacción|3
Cálculo II|4
Física General|4
Algorítmica II|4
Matemática Discreta|4
Métodos Estadísticos|4
Estructura de Datos|4
Organización y Arquitectura de Computadoras|4
Teoría General de Sistemas|3
Análisis y Diseño de Sistemas|4
Base de Datos I|4
Sistemas Operativos|4
Redes y Conectividad|4
Ingeniería de Software I|4
Base de Datos II|4
Dinámica de Sistemas|4
Ingeniería de Software II|4
Gestión de Procesos de Negocio|3
Inteligencia de Negocios|4
Seguridad de la Información|3
Gestión de Proyectos de TI|3
Planeamiento Estratégico de TI|3
Taller de Tesis I|3
Taller de Tesis II|4
Asignaturas Electivas|16
""")

# D055: Universidad del Valle (Univalle - EISC, Colombia) - Ingeniería de Sistemas (créditos)
put("D055", """Cálculo I|4
Álgebra Lineal|3
Introducción a la Ingeniería de Sistemas|2
Fundamentos de Programación Orientada a Objetos|4
Expresión Oral y Escrita|3
Cálculo II|4
Física I|3
Matemáticas Discretas|3
Programación Interactiva|3
Cálculo III|4
Física II|3
Estructuras de Datos|3
Arquitectura de Computadores|3
Ecuaciones Diferenciales|3
Probabilidad y Estadística|3
Bases de Datos|3
Sistemas Operativos|3
Desarrollo de Software I|3
Redes de Comunicación|3
Modelos y Optimización|3
Desarrollo de Software II|3
Simulación Computacional|3
Inteligencia Artificial|3
Gestión y Calidad de Proyectos de TI|3
Ciberseguridad|3
Sistemas de Información Organizacionales|3
Trabajo de Grado I|3
Trabajo de Grado II|5
Asignaturas Electivas Profesionales|12
""")

# D056: Universidad Nacional de Rosario (UNR - FCEIA, Argentina) - Licenciatura en Ciencias de la Computación (horas)
put("D056", """Álgebra y Geometría Analítica I|8
Análisis Matemático I|8
Programación I|8
Álgebra y Geometría Analítica II|8
Análisis Matemático II|8
Programación II|8
Álgebra Lineal|8
Estructuras de Datos y Algoritmos I|8
Lenguajes Formales y Computabilidad|8
Complementos de Matemática I|6
Arquitectura del Computador|6
Lógica|6
Métodos Numéricos|6
Probabilidad y Estadística|8
Estructuras de Datos y Algoritmos II|8
Sistemas Operativos I|8
Modelos Físicos|6
Análisis de Lenguajes de Programación|6
Comunicaciones|6
Teoría de Base de Datos|6
Ingeniería de Software I|8
Sistemas Operativos II|8
Introducción a la Inteligencia Artificial|8
Ingeniería de Software II|8
Compiladores|8
Complementos de Matemática II|8
Seguridad Informática|8
Práctica Profesional|10
Taller de Tesina|12
Asignaturas Electivas Avanzadas|16
""")

# D057: Universidad Técnica Federico Santa María (USM, Chile) - Ingeniería Civil Informática (créditos SCT)
put("D057", """Introducción a la Programación|5
Álgebra y Geometría|5
Introducción al Cálculo|5
Introducción a la Física|5
Introducción a la Ingeniería|3
Comunicación Efectiva|2
Álgebra Lineal|5
Cálculo II|5
Física General I|5
Química y Sociedad|3
Cálculo III|5
Física General III|5
Teoría de Sistemas|4
Estructuras Discretas|5
Ecuaciones Diferenciales|5
Estructuras de Datos|5
Informática Teórica|5
Lenguajes de Programación|5
Probabilidades y Estadística Computacional|5
Arquitectura y Organización de Computadores|5
Bases de Datos|5
Economía para Ingenieros|4
Sistemas Operativos|5
Redes y Ciberseguridad|5
Análisis y Diseño de Software|5
Optimización|4
Organizaciones y Sistemas de Información|4
Algoritmos y Complejidad|5
Ingeniería de Software|5
Sistemas Distribuidos|5
Computación Científica|5
Inteligencia Artificial I|5
Fundamentos de Ciencia de Datos|5
Diseño de Experiencia Usuaria|4
Gestión de Proyectos de Informática|4
Taller de Desarrollo de Proyectos de Informática|8
Memoria de Título|15
Electivos Disciplinares|15
""")

# D058: Universidad Autónoma de San Luis Potosí (UASLP, México) - Ingeniería en Computación (créditos)
put("D058", """Química A|8
Matemáticas Discretas I|8
Pensamiento Algorítmico|8
Temas Selectos de Matemáticas|8
Herramientas de Software|8
Metodología de la Investigación|4
Cálculo A|8
Matemáticas Discretas II|8
Estructuras de Datos I|8
Álgebra B|8
Fundamentos de Circuitos Eléctricos|10
Cálculo B|8
Ingeniería de Software|8
Estructuras de Datos II|8
Lenguajes de Programación|8
Dispositivos Semiconductores|10
Cálculo D|8
Tecnología Orientada a Objetos|8
Algoritmos y Complejidad|8
Bases de Datos|8
Fundamentos de Diseño Digital|8
Análisis Numérico|8
Interfaces Gráficas con Aplicaciones|8
Gestión de Servidores y Seguridad|8
Física A|8
Diseño Digital|10
Sistemas Operativos Avanzados|8
Arquitectura de Computadoras|8
Redes de Computadoras|8
Procesamiento de Señales|8
Proyectos Computacionales|12
Asignaturas Optativas y Humanísticas|16
""")

# D059: Pontificia Universidad Católica del Ecuador (PUCE, Ecuador) - Ingeniería en Tecnologías de la Información (créditos)
put("D059", """Tecnologías de la Información y Comunicación|3
Algoritmos y Pseudocódigo|4
Matemática Básica|4
Álgebra Lineal|3
Física y Laboratorio|4
Programación Estructurada y Funcional|4
Cálculo Diferencial e Integral|4
Sistemas Electrónicos Digitales|4
Estructuras Discretas|3
Redes I|4
Estructura de Datos|4
Arquitectura de Computadores|4
Estadística y Probabilidades|3
Redes II|4
Programación Orientada a Objetos|4
Sistemas Operativos|4
Redes Inalámbricas|3
Desarrollo Basado en Plataformas|4
Base de Datos I|4
Base de Datos II|4
Ingeniería de Software|4
Seguridad Informática|4
Integración de Sistemas|4
Emprendimiento Tecnológico|3
Ética Personal y Socioambiental|2
Titulación e Integración Curricular|12
""")

# D060: Universidad Mayor de San Andrés (UMSA, Bolivia) - Licenciatura en Informática (horas)
put("D060", """Introducción a la Informática|6
Álgebra I|6
Cálculo I|6
Física I y Laboratorio|6
Métodos de Programación|6
Estructuras de Datos|6
Álgebra Lineal|6
Cálculo II|6
Física II y Laboratorio|6
Arquitectura de Computadoras I|6
Programación Orientada a Objetos|6
Estadística y Probabilidades|6
Matemática Discreta|6
Sistemas Operativos|6
Arquitectura de Computadoras II|6
Base de Datos I|6
Análisis y Diseño de Sistemas|6
Investigación Operativa I|6
Redes de Computadoras|6
Base de Datos II|6
Ingeniería de Software|6
Inteligencia Artificial|6
Seguridad y Auditoría de Sistemas|6
Taller de Grado I|8
Taller de Grado II|10
Asignaturas Electivas de Especialidad|18
""")

(B / "bloque_04_transcripcion.json").write_text(json.dumps(raw, ensure_ascii=False, indent=2), encoding="utf-8")
(B / "bloque_04_asignaturas_base.json").write_text(json.dumps(raw, ensure_ascii=False, indent=2), encoding="utf-8")

print(f"Generados bloque_04_transcripcion.json y bloque_04_asignaturas_base.json con {len(raw)} documentos:")
for doc, items in sorted(raw.items()):
    total_w = sum(it["Peso"] for it in items)
    print(f"  {doc}: {len(items)} asignaturas, {total_w:g} unidades totales")
