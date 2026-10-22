"""Transcripción y codificación auditable del bloque 2. No asigna coordenadas a mano."""
from pathlib import Path
import json, re, unicodedata, math
B=Path(__file__).resolve().parent
raw=json.loads((B/'bloque_02_asignaturas_base.json').read_text(encoding='utf-8'))
raw['D016']=[r for r in raw['D016'] if re.fullmatch(r'Semestre[1-8]',r['Localizador'] or '')]
raw.pop('D026',None)
def put(id, text, loc='p. 1'):
    raw[id]=[]
    for line in text.strip().splitlines():
        name,w=line.strip().rsplit('|',1)
        raw[id].append(dict(Asignatura=name,Peso=float(w),Codigo='',Condicion='Optativa' if re.search('Optativ|Electiv|Libre elección',name,re.I) else 'Obligatoria',Localizador=loc))
put('D017','''Cálculo|7.5
Análisis Vectorial|7.5
Matemáticas Discretas|10.5
Comunicación Oral y Escrita|7.5
Fundamentos de Programación|7.5
Álgebra Lineal|9
Cálculo Aplicado|7.5
Mecánica y Electromagnetismo|10.5
Ingeniería, Ética y Sociedad|9
Fundamentos Económicos|7.5
Algoritmos y Estructuras de Datos|7.5
Ecuaciones Diferenciales|9
Circuitos Eléctricos|7.5
Fundamentos de Diseño Digital|7.5
Bases de Datos|7.5
Finanzas Empresariales|7.5
Paradigmas de Programación|7.5
Análisis y Diseño de Algoritmos|7.5
Probabilidad y Estadística|9
Matemáticas Avanzadas para la Ingeniería|9
Electrónica Analógica|7.5
Diseño de Sistemas Digitales|7.5
Tecnologías para el Desarrollo de Aplicaciones Web|7.5
Sistemas Operativos|7.5
Teoría de la Computación|7.5
Procesamiento Digital de Señales|7.5
Instrumentación y Control|7.5
Arquitectura de Computadoras|7.5
Análisis y Diseño de Sistemas|7.5
Formulación y Evaluación de Proyectos Informáticos|6
Compiladores|7.5
Redes de Computadoras|7.5
Sistemas en Chip|7.5
Optativa A1|7.5
Optativa B1|7.5
Métodos Cuantitativos para la Toma de Decisiones|7.5
Ingeniería de Software|7.5
Inteligencia Artificial|7.5
Aplicaciones para Comunicaciones en Red|7.5
Desarrollo de Aplicaciones Móviles Nativas|7.5
Optativa A2|7.5
Optativa B2|7.5
Trabajo Terminal I|12
Sistemas Distribuidos|7.5
Administración de Servicios en Red|7.5
Estancia Profesional|3
Desarrollo de Habilidades Sociales para la Alta Dirección|3
Trabajo Terminal II|12
Gestión Empresarial|7.5
Liderazgo Personal|7.5''')
put('D018','''Introducción a los Sistemas Computacionales|6
Diseño de Interfaz de Usuario|9
Programación Estructurada|8
Comprensión Lectora y Redacción Indirecta|5
Inglés para Tecnologías de la Información I|5
Álgebra Superior|7
Probabilidad y Estadística|7
Arquitectura de Computadoras|7
Programación Orientada a Objetos I|8
Contabilidad|6
Inglés para Tecnologías de la Información II|5
Cálculo Diferencial|7
Reingeniería de Procesos|6
Sistemas Operativos|4
Programación Orientada a Objetos II|6
Análisis de Costos|6
Administración|6
Cálculo Integral|7
Requerimientos y Diseño de Software|10
Redes de Computadoras|6
Algoritmos y Estructuras de Datos|6
Bases de Datos|8
Ingeniería Económica|6
Matemáticas Discretas|6
Desarrollo de Software|9
Conectividad|8
Aplicaciones Móviles|6
Tópicos de Programación|5
Emprendimiento y Liderazgo|4
Inteligencia Artificial|6
Administración de Proyectos de Software|6
Cómputo en la Nube|6
Desarrollo Web|8
Administración de Bases de Datos|6
Metodología de la Investigación|4
Modelos de Aprendizaje Computacional|7
Evaluación y Administración de Proyectos|7
Administración y Seguridad de Redes|7
Análisis de Capital Humano|6
Bases de Datos Avanzadas|6
Ética y Desarrollo Profesional|4
Aplicaciones y Herramientas de Sistemas Innovadores|4
Auditoría Informática|4
Evaluación de Procesos de Software|6
Taller de Evaluación Formativa|2
Optativas de etapa básica|12
Optativas de etapa disciplinaria|18
Optativas de etapa terminal|32
Prácticas Profesionales|10''','PDF: etapas y mapa; tabla oficial CGFP de unidades obligatorias')
put('D020','''Cálculo Diferencial|4
Introducción a la Ingeniería de Sistemas y Computación|3
Programación|3
Pensamiento Sistémico|3
Cátedra nacional de inducción y preparación para la vida universitaria|2
Fundamentos de Mecánica|4
Cálculo Integral|4
Álgebra Lineal|4
Programación Orientada a Objetos|3
Fundamentos de Electricidad y Magnetismo|4
Cálculo en Varias Variables|4
Matemáticas Discretas I|4
Bases de Datos|3
Elementos de Computadores|3
Probabilidad y Estadística|3
Ingeniería Económica|3
Matemáticas Discretas II|4
Estructuras de Datos|3
Arquitectura de Computadores|3
Modelos y Simulación|3
Gerencia y Gestión de Proyectos|3
Redes de Computadores|3
Ingeniería de Software I|3
Introducción a la Teoría de la Computación|4
Optimización|3
Sistemas de Información|3
Métodos Numéricos|3
Ingeniería de Software II|3
Algoritmos|3
Sistemas Operativos|3
Modelos estocásticos y simulación en computación y comunicaciones|3
Arquitectura de Infraestructura y Gobierno de TICs|3
Información y Comunicaciones|3
Arquitectura de Software|3
Sistemas Inteligentes|3
Lenguajes|3
Taller Interdisciplinario de Investigación y Gestión|3
Codificación, Criptografía y Seguridad de la Información|3
Computación Paralela y Distribuida|4
Computación Aplicada|3
Libre elección VIII-a|3
Libre elección VIII-b|2
Libre elección IX-a|4
Libre elección IX-b|4
Libre elección IX-c|4
Libre elección IX-d|4
Libre elección X-a|4
Libre elección X-b|4
Libre elección X-c|4
Trabajo de Grado|6''','p. 1; recorrido sugerido, sin nivelación')
put('D021','''Introducción al Modelado de Sistemas|3
Herramientas Computacionales|1
Introducción a la Ingeniería de Sistemas y Computación|2
Introducción a la Programación|3
Cálculo Diferencial|3
Expresión Oral y Escrita|2
Constitución Política y Democracia Colombiana|2
Humanidades I|2
Experiencia Formativa Vida Universitaria|0
Técnicas y Prácticas de Programación|2
Estructuras de Datos|3
Álgebra Lineal|3
Cálculo Integral|3
Teología I|2
Humanidades II|2
Programación Orientada a Objetos|3
Lógica Digital y Lenguaje de Máquina|3
Optativa: Cálculo Multivariable o Ecuaciones Diferenciales|3
Teología II|2
Programación Funcional|4
Lógica para Ciencias de la Computación|3
Árboles y Grafos|3
Arquitectura del Computador|3
Cinemática y Dinámica|4
Diseño de Interfaces Humano-Computador|3
Computabilidad y Complejidad|3
Computación Gráfica|3
Comunicación de Datos|3
Probabilidad y Estadística|3
Optativa: Electricidad y Magnetismo o Física Térmica y Ondulatoria|3
Desarrollo Formal de Sistemas|3
Análisis y Diseño de Algoritmos|3
Gestión de Proyectos de Tecnología|3
Gestión y Modelación de Datos|3
Sistemas Operativos|3
Computación Científica|3
Procesos y Diseño de Software|3
Programación Paralela|3
Aspectos Éticos, Sociales y Profesionales de la Computación|2
Introducción a la Seguridad Informática|2
Construcción de Software y Pruebas|3
Sistemas Inteligentes|3
Proyecto Social|2
Ética|2
Tecnologías Emergentes|2
Ingeniería Económica|3
Práctica Profesional|6
Seminario de Investigación|1
Preparación de Proyectos de Investigación e Innovación|2
Trabajo de Grado|6
Optativas de énfasis: tres asignaturas|9
Electivas Generales|12
Optativa de Opción Complementaria|12''','p. 1; alternativas rosadas contadas una vez; énfasis variable excluido')
put('D022','''Matemática I|4
Álgebra de Vectores y Matrices|4
Introducción a la Ingeniería|3
Principios de Computación|4
Dibujo y Geometría Descriptiva|3
Matemática II|4
Física I|4
Sociología General|3
Programación I|4
Psicología Aplicada a la Empresa|3
Matemática III|4
Física II|4
Estática|4
Programación II|4
Inglés|3
Matemática IV|4
Física III|4
Redes de Computadoras I|3
Programación III|4
Inglés Técnico|3
Probabilidades y Estadística|4
Sistemas Eléctricos Lineales I|4
Redes de Computadoras II|3
Programación Web|4
Bases de Datos I|4
Investigación de Operaciones I|3
Electrónica|4
Legislación Aplicada a la Empresa|3
Desarrollo de Software I|4
Bases de Datos II|4
Ingeniería Económica|3
Teoría Administrativa|3
Análisis de Sistemas|4
Desarrollo de Software II|4
Contabilidad|3
Desarrollo de Aplicaciones para Dispositivos Móviles|4
Arquitectura de Computadoras|4
Implantación de Sistemas|4
Seguridad Informática|4
Métodos y Técnicas de Investigación|3
Ingeniería del Software|4
Programación de Bajo Nivel|4
Organización y Métodos|3
Emprendedurismo|3
Auditoría de Sistemas|3
Formulación y Evaluación de Proyectos|3
Sistemas Operativos|4
Compiladores|4
Ética Profesional|3
Desarrollo de Software III|4''','p. 14 del PDF; no se duplican los cursos extraordinarios')
put('D024','''Introducción a la Ingeniería de Sistemas|2
Cálculo Diferencial|3
Álgebra Lineal|3
Cálculo Integral|3
Sistemas Operativos|3
Redes y Comunicaciones|3
Arquitectura Empresarial|3
Gestión de TI|3
Proyecto de Grado|3
Matemáticas Discretas|3
Arquitectura de Computadores|3
Física General|3
Bases de Datos|3
Diseño de Bases de Datos|3
Administración de Bases de Datos|3
Information Security|3
Teoría de Sistemas en las Organizaciones|2
Estadística Descriptiva|3
Análisis y Especificación de Requerimientos|3
Diseño de Software|3
Verificación y Validación de Software|3
Calidad de Software|3
Emprendimiento de Base Tecnológica|3
Fundamentos de Programación|3
Programación|3
Probabilidad|2
Estructura de Datos|3
Formulación y Evaluación de Proyectos de Ingeniería|2
Proyecto de Ingeniería II|3
Proyecto de Ingeniería I|3
Electivos Disciplinares Específicos I-IV|12
Electivos Disciplinares Comunes I-II|6
Cátedra Unadista|3
Pensamiento Lógico Matemático|3
Competencias Comunicativas|3
Fundamentos en Gestión Integral|3
Fundamentos y Generalidades de Investigación|3
Herramientas Digitales para la Gestión del Conocimiento|3
Inglés A1|3
Inglés A2|3
Inglés B1|3
Inglés B2|3
Ética y Ciudadanía|3
Electivos Interdisciplinares Básicos Comunes I-II|6
Electivos Formación Complementaria I-III|6''','p. 1; mapa con pesos individuales; no se cuentan catálogos de electivas')
put('D025','''Análisis Matemático I|120
Álgebra y Geometría Analítica|120
Física I|120
Inglés I|48
Lógica y Estructuras Discretas|72
Algoritmos y Estructuras de Datos|120
Arquitectura de Computadoras|96
Sistemas y Procesos de Negocio|72
Análisis Matemático II|120
Física II|120
Ingeniería y Sociedad|48
Inglés II|48
Sintaxis y Semántica de los Lenguajes|96
Paradigmas de Programación|96
Sistemas Operativos|96
Análisis de Sistemas de Información|144
Probabilidad y Estadística|72
Economía|72
Bases de Datos|96
Desarrollo de Software|96
Comunicación de Datos|96
Análisis Numérico|72
Diseño de Sistemas de Información|144
Electivas de tercer nivel|96
Legislación|48
Ingeniería y Calidad de Software|72
Redes de Datos|96
Investigación Operativa|96
Simulación|72
Tecnologías para la Automatización|72
Administración de Sistemas de Información|144
Electivas de cuarto nivel|144
Inteligencia Artificial|72
Ciencia de Datos|72
Sistemas de Gestión|96
Gestión Gerencial|72
Seguridad en los Sistemas de Información|72
Proyecto Final|144
Electivas de quinto nivel|240
Práctica Profesional Supervisada|200''','Ordenanza 1877, pp. 36–38; horas reloj')
put('D026','''Preliminares de Matemática|60
Álgebra|112
Análisis Matemático I-a|80
Introducción a la Informática|96
Análisis Matemático I-b|64
Geometría Analítica|96
Matemática Discreta|88
Programación Procedural|120
Cálculo Avanzado|96
Estructuras de Datos y Algoritmos|96
Física General|72
Sistemas y Organizaciones|120
Análisis y Diseño de Sistemas I|96
Arquitectura de Computadoras|96
Autómatas y Lenguajes|72
Métodos Numéricos|56
Probabilidad y Estadística|88
Base de Datos I|96
Programación Orientada a Objetos|88
Redes y Comunicaciones I|96
Sistemas Operativos|112
Análisis y Diseño de Sistemas II|96
Laboratorio de Redes y Comunicaciones|96
Programación Lógica y Funcional|80
Programación Orientada a la Web|104
Economía y Gestión de Empresas|120
Ingeniería de Software I|96
Redes y Comunicaciones II|96
Seguridad, Higiene y Gestión Ambiental|64
Legislación Informática|64
Gestión de Calidad y Auditoría|96
Modelos y Simulación|80
Sistemas Distribuidos I|88
Ingeniería de Software II|64
Seguridad Informática|80
Sistemas Distribuidos II|96
Base de Datos II|80
Sistemas Inteligentes|80
Proyecto Final|200
Práctica Profesional Supervisada|200
Práctica Comunitaria|40''','Resolución 032/2023, pp. PDF 19–20 (impresas 18–19)')
put('D027','''Introducción a la Programación I|90
Introducción al Álgebra|90
Introducción a los Sistemas Informáticos|75
Inglés|90
Diseño Lógico|60
Introducción a la Programación II|90
Lenguajes Formales y Autómatas|75
Cálculo I|90
Arquitectura de Computadoras I|90
Análisis y Diseño de Algoritmos I|90
Programación Orientada a Objetos|75
Álgebra Lineal|90
Redes de Computadoras I|90
Metodologías de Desarrollo de Software|90
Análisis y Diseño de Algoritmos II|90
Cálculo II|90
Sistemas Operativos|90
Bases de Datos I|90
Física I|90
Lenguajes y Paradigmas|75
Programación Web|90
Bases de Datos II|90
Probabilidad y Estadística|90
Ingeniería de Software I|90
Organización y Gestión Empresarial|90
Teoría de la Información|90
Redes de Computadoras II|90
Física II|90
Calidad de Software|90
Arquitectura de Computadoras II|60
Fundamentos de Ciencia de Datos|90
Compiladores e Intérpretes|75
Ingeniería de Software II|90
Ciberseguridad|60
Inteligencia Artificial|75
Formulación y Evaluación de Proyectos TIC|90
Ética y Legislación de la Práctica Profesional|75
Práctica Profesional Supervisada y Proyecto Integrador|225
Optativas|180
Libre elección|60''','Plan 2023, tablas pp. 14–18; horas')
put('D029','''Cálculo Diferencial|4
Biología General|4
Química General|4
Fundamentación en Ingeniería|3
Pensamiento Lógico Matemático|3
Cálculo Integral|3
Física Mecánica|4
Algoritmos y Programación|3
Álgebra Lineal|3
Constitución Política Colombiana y Sostenibilidad|3
Sociohumanística y Cultura I|2
Cálculo Multivariado|3
Física Electromagnetismo|4
Programación Orientada a Objetos|4
Competencias Comunicativas|4
Idioma I|3
Ecuaciones Diferenciales|3
Arquitectura del Computador y Sistemas Operativos|4
Estructura de Datos|3
Cultura del Emprendimiento I|2
Estadística Descriptiva|3
Idioma II|3
Métodos Numéricos|3
Matemáticas Discretas|3
Ingeniería de Software|3
Cultura del Emprendimiento II|3
Estructura del Pensamiento Complejo|3
Idioma III|3
Gestión de Proyectos|3
Redes I|3
Bases de Datos|3
Probabilidad y Estadística Inferencial|3
Electiva I|3
Idioma IV|3
Desarrollo Web y Móvil|4
Redes II|3
Sistemas de Información|3
Cultura del Emprendimiento III|3
Electiva II|3
Seminario de Investigación|2
Práctica Profesional|3
Sociohumanística y Cultura II|2
Contexto Geopolítico|4
Electiva III|3
Electiva IV|3
Proyecto de Grado|3''')
put('D030','''Álgebra y Matemática Discreta|9
Fundamentos Físicos de la Informática|9
Fundamentos de Programación|9
Fundamentos de la Empresa|9
Cálculo y Métodos Numéricos|9
Sistemas Operativos|9
Tecnología de Computadores|9
Lógica Computacional|9
Estadística|9
Interacción persona - ordenador|9
Algoritmia y Complejidad|9
Estructura de Datos|9
Redes de Ordenadores|9
Ingeniería de Software|9
Programación Avanzada|9
Programación Orientada a Objetos (OO)|9
Modelos de Probabiliad|9
Bases de Datos|9
Desarrollo de Aplicaciones Distributivas|9
Diseño Avanzado de Algoritmos|9
Programación para la Administración de Sistemas|9
Seguridad en los Sistemas de Información|9
Aprendizaje Estadístico|9
Sistemas Operativos Avanzados|9
Gestión de Proyectos|9
Bases de Datos Avanzadas|9
Inteligencia Artificial e Ingeniería del Conocimiento|9
Deontología y Legislación Informática|9
Integración de Sistemas|9
Desarrollo Seguro de Software|9
Tecnologías Emergentes|9
Minería de Datos Masivos|9
Seguridad en la Web|9
Sistemas Distribuidos de Gran Escala|9
Aprendizaje Automático y Minería de Datos|9
Técnicas para la Elaboración de Proyectos|9''','tabla web: 9 créditos por unidad; se conservan dos erratas del sitio')

if __name__=='__main__':
    (B/'bloque_02_transcripcion.json').write_text(json.dumps(raw,ensure_ascii=False,indent=2),encoding='utf-8')
    for id,rows in sorted(raw.items()): print(id,len(rows),sum(r['Peso'] for r in rows))
