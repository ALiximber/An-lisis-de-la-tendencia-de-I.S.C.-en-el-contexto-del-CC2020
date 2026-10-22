"""Bloque 5 (D061-D075): clasificación auditable de asignaturas y cálculo de coordenadas CC2020.

Entrada : bloque_05_transcripcion.json (asignaturas con peso en créditos u horas)
Salida  : bloque_05_datos.json            (mismo esquema que bloques 1 a 4)
          bloque_05_resultados.csv        (12 columnas solicitadas)
          bloque_05_clasificacion.csv     (auditoría materia por materia)
"""
from pathlib import Path
import csv, json, math, re, unicodedata

B = Path(__file__).resolve().parent
raw = json.loads((B / "bloque_05_transcripcion.json").read_text(encoding="utf-8"))

RULES = [
    # 1. Exclusiones: formación transversal, optativas sin contenido definido, capstones/prácticas
    (r"optativa|eletiva|electiv|libre elecci|campo de profundizaci|"
     r"temas selectos|topicos de vanguardia|perspectivas disciplinares|profundizacion|itinerario|"
     r"idioma|ingles|lengua extranjera|beginner|comunicacion (oral|\d|efectiva|escrita|y expresion)|competencias comunicativas|"
     r"procesos comunicativos|^comunicacion$|comprension lectora|redaccion|escritura|habilidades|"
     r"argumentacion|expresion oral|expresion escrita|humanidades|teologia|constitucion|democracia|catedra|cultura|"
     r"sociologia|psicologia|filosofia|antropologia|historia|sociohumanistica|etica|etico|moral|"
     r"desarrollo sustentable|sustentabilidad|emprend|liderazgo|actividades|empleabilidad|"
     r"metodologia (universitaria|de (la )?investigacion|del trabajo academico)|tecnicas de estudio|"
     r"seminario de investigacion|taller de investigacion|fundamentos de investigacion|recursos y necesidades|desafios|"
     r"modulo interdisciplinario|ingenieria y sociedad|ciencias, tecnologia y desarrollo|informatica y sociedad|"
     r"proyecto social|servicio social|practica|practicum|residencia profesional|estancia|pasantia|"
     r"trabajo terminal|trabajo de grado|trabajo especial|trabajo de conclusao|trabalho de conclusao|"
     r"trabajo final|trabajo de titulo|trabajo profesional|proyecto terminal|proyecto integrador|proyecto final|"
     r"projeto final|proyecto modular|proyecto de (grado|ingenieria|sistemas|software|fin de carrera|graduacion|innovacion|diseno|tesis)|"
     r"proyectos computacionales|capstone|tesis|tesina|memoria de titulo|taller de tesina|taller de grado|taller de tesis|taller de titulacion|"
     r"titulacion e integracion|unidad de integracion|articulo cientifico|taller de proyecto|taller de evaluacion|"
     r"taller interdisciplinario|taller de desarrollo de proyectos|introduccion a (la|los) (ingenieria|sistemas|ciencias|sistemas computacionales)|"
     r"fundamentacion en ingenieria|herramientas (computacionales|informaticas)|sistemas de representacion|"
     r"realidad nacional|asignaturas de especialidad|tecnologias emergentes|sociedad y el estado|"
     r"pensamiento cientifico|espanol general|intro\.?\s*a la ing|seminario de orientacion|seminario de sistemas|"
     r"actividades artisticas|taller de lenguaje|quimica y sociedad|vida y cultura|cultura de paz|"
     r"igualdad de genero|responsabilidad social|jesucristo y la persona|contextos e interculturalidad|"
     r"filosofia de la ingenieria|ciencias sociales|social humanistica|experiencia recepcional|cultura maya|"
     r"cursos complementarios|habilidades del pensamiento",
     None, None),
    # 2. Pensamiento / Ciencias de sistemas aplicadas a organizaciones
    (r"teoria (general )?de sistemas|pensamiento sistemico|dinamica de sistemas|metodos cuantitativos", "T", "O"),
    # 3. Hardware y circuitos
    (r"fundamentos fisicos|circuitos electricos|circuitos eletricos|electronica|eletronica|sistemas electricos|senales|"
     r"sistemas de comunicaciones|telecomunicaciones|conmutacion y enrutamiento|fundamentos de hardware|"
     r"electricidad y electronica|dispositivos semiconductores|procesamiento de senales|"
     r"fundamentos de organizacion de computadoras|organizacao basica de computadores|circuitos digitais", "T", "H"),
    (r"sistemas digitales|sistemas digitais|diseno digital|logica digital|circuitos logicos|maquinas digitales|diseno logico|"
     r"circuitos digitais|circuitos digitales|microcontroladores|microprocesadores|microprocessadores|microcomputadoras|"
     r"microelectronica|dispositivos electronicos|instalaciones electricas|instrumentacion|"
     r"programacion de bajo nivel|assembly|ensamblador|lenguajes de interfaz|sistemas embebidos|sistemas embarcados|robotica|automatizacion|"
     r"sistemas electronicos digitales|sistemas computacionales y arquitectura",
     "A", "H"),
    # 4. Arquitecturas
    (r"arquitectura (empresarial|de infraestructura)|gobierno|gobernanza", "A", "O"),
    (r"arquitectura de software|diseno y arquitectura de software", "A", "S"),
    (r"arquitectura (del|de|dos) comput|organizacion (y arquitectura|del computador|de computadoras)|organizacao de computadores|"
     r"fundamentos de arquitectura|taller de arquitectura|arquitectura de sistemas y computadores|"
     r"organizacion computacional",
     "T", "H"),
    (r"modelacion de datos|modelado de datos", "A", "S"),
    # 5. Gestión de proyectos / TI
    (r"formulacion|gestion de proyectos|gerencia|administracion de proyectos|evaluacion y administracion|"
     r"elaboracion de proyectos|gestion de ti|gestion de procesos|proyectos de ti|ejecucion de proyectos|"
     r"proyectos de tecnologias|gestion y calidad de proyectos|gestion informatica|direccion empresarial|"
     r"gestion y direccion de proyectos|gestion y evaluacion de proyectos|administracion de tecnologias|"
     r"gestion y gobernanza|planeamiento estrategico empresarial|planeamiento estrategico de ti|gestion estrategica",
     "A", "O"),
    # 6. Factores humanos / HCI
    (r"interaccion (humano|persona)|interfaz|interfaces|experiencia (de )?usuari[oa]", "A", "O"),
    # 7. Seguridad
    (r"seguridad|security|ciberseguridad|criptografia", "A", "S"),
    # 8. Teoría de la computación, algoritmos y fundamentos computacionales
    (r"pensamiento logico|pensamiento computacional|pensamiento algoritmico", "T", None),
    (r"algoritmos y programacion|algoritmia y programacion|metodologia de la programacion|metodos de programacion|"
     r"algoritmos e programacao|principios de desenvolvimento de algoritmos|resolucion de problemas y algoritmos", "A", "S"),
    (r"matematicas? discreta|estructuras discretas|estruturas discretas|logica|teoria de la computacion|teoria da computacao|"
     r"computabilidad|automatas|automatos|lenguajes formales|linguagens formais|algoritm|teoria de (la informacion|lenguajes)|"
     r"sintaxis y semantica|lenguajes y paradigmas|paradigmas|^lenguajes$|lenguajes de programacion|compiladores|compiladores e interpretes|"
     r"programacion (logica|funcional|concurrente|paralela)|arboles y grafos|teoria dos grafos|estructuras? de datos|estruturas de dados|"
     r"principios de computacion|introduccion a la teoria|desarrollo formal|inteligencia artificial|inteligencia artificial|"
     r"aprendizaje|sistemas inteligentes|vision artificial|ciencia de datos|mineria de datos|"
     r"computacion (grafica|cientifica|visual|ubicua)|computacao grafica|graficacion|lenguajes y maquinas|"
     r"introduccion a la (computacion|informatica)|introducao a computacao|"
     r"informatica teorica|analisis de algoritmos|analise de algoritmos|algoritmica", "T", "S"),
    # 9. Sistemas de información / negocio
    (r"sistemas? de informacion|sistemas y (procesos|organizaciones)|inteligencia de negocios|"
     r"negocios electronicos|computacion y sociedad|industria de ti|organizaciones y sistemas|"
     r"relaciones humanas en empresas|modelos de negocio|sistemas de informacion empresariales|"
     r"auditoria de sistemas", "A", "O"),
    # 10. Software, datos, redes y desarrollo aplicado
    (r"bases? de datos|bancos? de dados|sistemas operativos|sistemas operacionais|sistemas operacionales|software|\bred(es)?\b|"
     r"programacion|programacao|desarrollo|aplicaciones|\bweb\b|movil|moviles|nube|distribuid|paralel|videojuegos|devops|conectividad|"
     r"analisis (y diseno )?de sistemas|implantacion|integracion de sistemas|servidores|"
     r"informacion y comunicaciones|comunicacion de datos|comunicaciones|computacion aplicada|requerimientos|requisitos|calidad|"
     r"pruebas y aseguramiento|construccion y mantenimiento|ingenieria de software|engenharia de software|"
     r"ingenieria del software|ingenieria de requisitos|taller de lenguaje|taller de bases de datos|taller de programacion|"
     r"sistemas de tiempo real|fundamentos de tecnologias de la informacion|"
     r"modelado de sistemas|implementacion de metodos computacionales|manejo e implementacion de archivos|"
     r"verificacion y validacion|computo integrado|desarrollo basado en plataformas|transmision y comunicacion|"
     r"interfaces graficas|tecnologia orientada a objetos|tecnologia[s]? de (la )?informacion|analisis de datos y toma de decisiones",
     "A", "S"),
    # 11. Organización y negocio
    (r"economi|finanz|contab|costos|presupuesto|empresa|negocio|administracion|administrativ|gestion|legislacion|"
     r"deontologia|auditoria|organizacion|reingenieria|capital humano|planeamiento estrategico|planificacion estrategica|"
     r"aspectos legales|principios de administracion",
     "A", "O"),
    # 12. Ciencias básicas y métodos cuantitativos (sin capa Y)
    (r"calculo|algebra|matematic|probabili|estadistic|ecuaciones|analisis (vectorial|matematico|numerico)|"
     r"metodos numericos|geometria|fisica|mecanica|termodinamica|ondas|electricidad|electromagnet|eletromagnetismo|estatica|"
     r"cinematica|biologia|quimica|optimizacion|investigacion (de operaciones|operativa)|investigacao operacional|modelos?|modelacion|"
     r"simulacion|procesos estocasticos|dinamica|sistemas complejos|vectores|vetores|precalculo|"
     r"experimentacion numerica|metodos experimentales|electrostatica|estructura de la materia|"
     r"series de fourier|dibujo",
     "T", None),
]
COMPILED = [(re.compile(p), x, y) for p, x, y in RULES]

def norm(s):
    s = unicodedata.normalize("NFKD", s.lower())
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"\(\*\)", "", s)
    return re.sub(r"\s+", " ", s).strip()

def classify(name):
    n = norm(name)
    for i, (rx, x, y) in enumerate(COMPILED, 1):
        if rx.search(n):
            return x, y, i
    return None, None, 0

META = {
    "D061": ("Bacharelado em Ciência da Computação — matriz BCC", "Universidade de São Paulo (USP - IME)", "Brasil", "2023", "Plan de Estudios Oficial", "créditos"),
    "D062": ("Engenharia de Computação — catálogo DAC 34", "Universidade Estadual de Campinas (UNICAMP)", "Brasil", "2022", "Plan de Estudios Oficial", "créditos"),
    "D063": ("Ingeniería de Sistemas — versión 5", "Universidad de Antioquia (UdeA)", "Colombia", "2018", "Plan de Estudios Oficial", "créditos"),
    "D064": ("Licenciatura en Ciencias de la Computación — plan oficial", "Universidad Nacional de Córdoba (UNC - FAMAF)", "Argentina", "2021", "Plan de Estudios Oficial", "créditos"),
    "D065": ("Ingeniería Informática y de Sistemas — plan de estudios", "Universidad Nacional de San Antonio Abad del Cusco (UNSAAC)", "Perú", "2020", "Plan de Estudios Oficial", "créditos"),
    "D066": ("Bachillerato en Ingeniería en Computación — plan 412", "Instituto Tecnológico de Costa Rica (TEC)", "Costa Rica", "2020", "Plan de Estudios Oficial", "créditos"),
    "D067": ("Ingeniería en Ciencias de la Computación — pénsum 2020", "Escuela Politécnica Nacional (EPN)", "Ecuador", "2020", "Plan de Estudios Oficial", "créditos"),
    "D068": ("Ingeniería de Sistemas — plan de estudios", "Universidad Católica Boliviana (UCB San Pablo)", "Bolivia", "2020", "Plan de Estudios Oficial", "créditos"),
    "D069": ("Ingeniería de Sistemas — plan ABET", "Universidad del Norte (Uninorte)", "Colombia", "2020", "Plan de Estudios Oficial", "créditos"),
    "D070": ("Licenciatura en Ingeniería en Sistemas Computacionales", "Universidad Veracruzana (UV)", "México", "2020", "Plan de Estudios Oficial", "créditos"),
    "D071": ("Licenciatura en Ciencias de la Computación — plan oficial", "Universidad Nacional del Sur (UNS)", "Argentina", "2020", "Plan de Estudios Oficial", "horas"),
    "D072": ("Ingeniería Civil en Informática — plan SCT", "Universidad Austral de Chile (UACh)", "Chile", "2021", "Plan de Estudios Oficial", "créditos SCT"),
    "D073": ("Licenciatura en Ingeniería de Software — plan LIS", "Universidad Autónoma de Yucatán (UADY - FMAT)", "México", "2020", "Plan de Estudios Oficial", "créditos"),
    "D074": ("Ingeniería de Sistemas — plan de estudios", "Universidad Nacional de Trujillo (UNT)", "Perú", "2020", "Plan de Estudios Oficial", "créditos"),
    "D075": ("Bachillerato en Informática Empresarial — plan de estudios", "Universidad de Costa Rica (UCR - Sedes Regionales)", "Costa Rica", "2020", "Plan de Estudios Oficial", "créditos"),
}
URLS = {d: u for d, u in json.loads((B / "bloque_05_fuentes.json").read_text(encoding="utf-8"))}

def afinidad(pt, pa, ch, cs, co):
    nx, ny = pt + pa, ch + cs + co
    if co / ny >= 0.30: return "IS"
    if ch / ny >= 0.25: return "CE"
    if pt / nx >= 0.45: return "CS"
    if cs / ny >= 0.55: return "SE"
    return "IT"

rows, audit, unmatched = [], [], {}
for doc in sorted(raw):
    pt = pa = ch = cs = co = 0.0
    total = cx = cy = 0.0
    for r in raw[doc]:
        w = float(r["Peso"]); total += w
        x, y, rule = classify(r["Asignatura"])
        if x == "T": pt += w
        elif x == "A": pa += w
        if y == "H": ch += w
        elif y == "S": cs += w
        elif y == "O": co += w
        if x: cx += w
        if y: cy += w
        if rule == 0:
            unmatched.setdefault(doc, []).append(r["Asignatura"])
        audit.append(dict(ID=doc, Asignatura=r["Asignatura"], Peso=w, Condicion=r["Condicion"],
                          Regla=rule, X=x or "", Y=y or ""))
    nx, ny = pt + pa, ch + cs + co
    assert nx > 0 and ny > 0, doc
    X = 5 * (pa - pt) / nx
    Y = 5 * (co - ch) / ny
    dx = math.sqrt(max(0, 25 - X ** 2))
    dy = math.sqrt(max(0, 25 * (ch + co) / ny - Y ** 2))
    title, inst, pais, anio, tipo, unidad = META[doc]
    rows.append({
        "ID": doc, "Titulo_Documento": title, "Institucion_Fuente": inst, "Pais": pais, "Anio": anio,
        "Tipo_Fuente": tipo,
        "Coordenada_X": round(X, 2), "Coordenada_Y": round(Y, 2),
        "Desviacion_Radio": round(math.hypot(dx, dy), 2),
        "Proximidad_Disciplina_CC2020": afinidad(pt, pa, ch, cs, co),
        "Resumen_Evidencia_X": f"Pt={pt:g}; Pa={pa:g} {unidad}; cobertura X={nx/total:.0%} del total ({total:g})",
        "Resumen_Evidencia_Y": f"Ch={ch:g}; Cs={cs:g}; Co={co:g} {unidad}; cobertura Y={ny/total:.0%} del total",
        "Pt": pt, "Pa": pa, "Ch": ch, "Cs": cs, "Co": co, "Total_Peso": total,
        "Delta_X": dx, "Delta_Y": dy, "URL": URLS[doc], "Unidad_Peso": unidad,
    })

(B / "bloque_05_datos.json").write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
cols = ["ID", "Titulo_Documento", "Institucion_Fuente", "Pais", "Anio", "Tipo_Fuente", "Coordenada_X",
        "Coordenada_Y", "Desviacion_Radio", "Proximidad_Disciplina_CC2020", "Resumen_Evidencia_X",
        "Resumen_Evidencia_Y"]

def escribir_csv(nombre, campos, filas, **kw):
    for destino in (B / nombre, B / nombre.replace(".csv", "_nuevo.csv")):
        try:
            with destino.open("w", newline="", encoding="utf-8-sig") as f:
                w = csv.DictWriter(f, fieldnames=campos, **kw); w.writeheader(); w.writerows(filas)
            return destino
        except PermissionError:
            print(f"AVISO: {destino.name} está bloqueado")
    raise PermissionError(f"No se pudo escribir {nombre}")

escribir_csv("bloque_05_resultados.csv", cols, rows, extrasaction="ignore")
escribir_csv("bloque_05_clasificacion.csv", list(audit[0]), audit)

if __name__ == "__main__":
    for r in rows:
        print(r["ID"], f'X={r["Coordenada_X"]:6.2f} Y={r["Coordenada_Y"]:6.2f} R={r["Desviacion_Radio"]:5.2f}',
              r["Proximidad_Disciplina_CC2020"], "|", r["Resumen_Evidencia_X"].split(";")[-1].strip(),
              "|", r["Resumen_Evidencia_Y"].split(";")[-1].strip())
    print("\nSin coincidencia con regla (excluidas):")
    for d, names in unmatched.items():
        print(d, names)
