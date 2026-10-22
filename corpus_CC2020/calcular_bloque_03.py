"""Bloque 3 (D031-D045): clasificación auditable de asignaturas y cálculo de coordenadas CC2020.

Entrada : bloque_03_transcripcion.json (asignaturas con peso en créditos u horas)
Salida  : bloque_03_datos.json            (mismo esquema que bloque_01_datos.json)
          bloque_03_resultados.csv        (12 columnas solicitadas)
          bloque_03_clasificacion.csv     (auditoría materia por materia)
"""
from pathlib import Path
import csv, json, math, re, unicodedata

B = Path(__file__).resolve().parent
raw = json.loads((B / "bloque_03_transcripcion.json").read_text(encoding="utf-8"))

RULES = [
    # 1. Exclusiones: formación transversal, optativas sin contenido definido, capstones/prácticas
    (r"optativa|electiv|libre elecci|campo de profundizaci|"
     r"temas selectos|topicos de vanguardia|perspectivas disciplinares|profundizacion|itinerario|"
     r"idioma|ingles|lengua extranjera|beginner|comunicacion (oral|\d)|competencias comunicativas|"
     r"procesos comunicativos|^comunicacion$|comprension lectora|redaccion|escritura|habilidades|"
     r"argumentacion|expresion oral|humanidades|teologia|constitucion|democracia|catedra|cultura|"
     r"sociologia|psicologia|filosofia|antropologia|historia|sociohumanistica|etica|etico|moral|"
     r"desarrollo sustentable|sustentabilidad|emprend|liderazgo|actividades|empleabilidad|"
     r"metodologia (universitaria|de (la )?investigacion)|tecnicas de estudio|seminario de investigacion|"
     r"taller de investigacion|fundamentos de investigacion|recursos y necesidades|desafios|"
     r"modulo interdisciplinario|ingenieria y sociedad|ciencias, tecnologia y desarrollo|"
     r"proyecto social|servicio social|practica|practicum|residencia profesional|estancia|"
     r"trabajo terminal|trabajo de grado|trabajo de titulo|trabajo profesional|proyecto terminal|"
     r"proyecto modular|proyecto de (grado|ingenieria|sistemas|software|fin de carrera|graduacion|innovacion)|"
     r"proyecto integrador|capstone|tesis|articulo cientifico|taller de proyecto|taller de evaluacion|"
     r"taller interdisciplinario|introduccion a (la|los) (ingenieria|sistemas|ciencias)|fundamentacion en ingenieria|"
     r"herramientas (computacionales|informaticas)|sistemas de representacion|"
     r"realidad nacional|asignaturas de especialidad|tecnologias emergentes|sociedad y el estado|"
     r"pensamiento cientifico|espanol general|intro\.?\s*a la ing",
     None, None),
    # 2. Pensamiento / Ciencias de sistemas aplicadas a organizaciones
    (r"teoria de sistemas|pensamiento sistemico|metodos cuantitativos", "T", "O"),
    # 3. Hardware y circuitos
    (r"fundamentos fisicos|circuitos electricos|electronica|sistemas electricos|senales|"
     r"sistemas de comunicaciones|telecomunicaciones|conmutacion y enrutamiento|fundamentos de hardware", "T", "H"),
    (r"sistemas digitales|diseno digital|logica digital|maquinas digitales|diseno logico|"
     r"circuitos logicos|circuitos digitales|microcontroladores|microprocesadores|microcomputadoras|"
     r"microelectronica|dispositivos electronicos|instalaciones electricas|instrumentacion|"
     r"programacion de bajo nivel|ensamblador|lenguajes de interfaz|sistemas embebidos|robotica|automatizacion",
     "A", "H"),
    # 4. Arquitecturas
    (r"arquitectura (empresarial|de infraestructura)|gobierno|gobernanza", "A", "O"),
    (r"arquitectura de software", "A", "S"),
    (r"arquitectura (del|de) comput|organizacion (y arquitectura|del computador)|organizacion de computadoras|"
     r"fundamentos de arquitectura|taller de arquitectura|arquitectura de sistemas y computadores",
     "T", "H"),
    (r"modelacion de datos|modelado de datos", "A", "S"),
    # 5. Gestión de proyectos / TI
    (r"formulacion|gestion de proyectos|gerencia|administracion de proyectos|evaluacion y administracion|"
     r"elaboracion de proyectos|gestion de ti|gestion de procesos|proyectos de ti|ejecucion de proyectos|"
     r"proyectos de tecnologias",
     "A", "O"),
    # 6. Factores humanos / HCI
    (r"interaccion (humano|persona)|interfaz|interfaces|experiencia de usuario", "A", "O"),
    # 7. Seguridad
    (r"seguridad|security|ciberseguridad|criptografia", "A", "S"),
    # 8. Teoría de la computación, algoritmos y fundamentos computacionales
    (r"pensamiento logico|pensamiento computacional", "T", None),
    (r"algoritmos y programacion|algoritmia y programacion", "A", "S"),
    (r"matematicas? discreta|estructuras discretas|logica|teoria de la computacion|computabilidad|automatas|"
     r"lenguajes formales|algoritm|teoria de (la informacion|lenguajes)|sintaxis y semantica|"
     r"lenguajes y paradigmas|paradigmas|^lenguajes$|lenguajes de programacion|compiladores|"
     r"programacion (logica|funcional|concurrente|paralela)|arboles y grafos|estructuras? de datos|"
     r"principios de computacion|introduccion a la teoria|desarrollo formal|inteligencia artificial|"
     r"aprendizaje|sistemas inteligentes|vision artificial|ciencia de datos|mineria de datos|"
     r"computacion (grafica|cientifica|visual|ubicua)|graficacion|lenguajes y maquinas|introduccion a la computacion", "T", "S"),
    # 9. Sistemas de información / negocio
    (r"sistemas? de informacion|sistemas y (procesos|organizaciones)|inteligencia de negocios|"
     r"negocios electronicos|computacion y sociedad|industria de ti", "A", "O"),
    # 10. Software, datos, redes y desarrollo aplicado
    (r"bases? de datos|sistemas operativos|software|\bred(es)?\b|programacion|desarrollo|"
     r"aplicaciones|\bweb\b|movil|moviles|nube|distribuid|paralel|videojuegos|devops|conectividad|"
     r"analisis (y diseno )?de sistemas|implantacion|integracion de sistemas|servidores|"
     r"informacion y comunicaciones|comunicacion de datos|computacion aplicada|requerimientos|calidad|"
     r"ingenieria de requisitos|taller de lenguaje|sistemas de tiempo real|fundamentos de tecnologias de la informacion|"
     r"modelado de sistemas|implementacion de metodos computacionales",
     "A", "S"),
    # 11. Organización y negocio
    (r"economi|finanz|contab|costos|presupuesto|empresa|negocio|administracion|administrativ|gestion|legislacion|"
     r"deontologia|auditoria|organizacion|reingenieria|capital humano|planeamiento estrategico|planificacion estrategica|"
     r"aspectos legales",
     "A", "O"),
    # 12. Ciencias básicas y métodos cuantitativos (sin capa Y)
    (r"calculo|algebra|matematic|probabili|estadistic|ecuaciones|analisis (vectorial|matematico|numerico)|"
     r"metodos numericos|geometria|fisica|mecanica|termodinamica|ondas|electricidad|electromagnet|estatica|"
     r"cinematica|biologia|quimica|optimizacion|investigacion (de operaciones|operativa)|modelos?|modelacion|"
     r"simulacion|procesos estocasticos|dinamica|sistemas complejos|vectores|precalculo|"
     r"experimentacion numerica|metodos experimentales|electrostatica|estructura de la materia",
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
    "D031": ("Ingeniería en Computación — plan 2016/2023", "UNAM — Facultad de Ingeniería", "México", "2016", "Plan de Estudios Oficial", "créditos"),
    "D032": ("Ingeniería Informática — plan 2026-2", "Pontificia Universidad Católica del Perú (PUCP)", "Perú", "2026", "Plan de Estudios Oficial", "créditos"),
    "D033": ("Ingeniería Civil en Computación — plan 2019", "Universidad de Chile (FCFM-DCC)", "Chile", "2019", "Plan de Estudios Oficial", "créditos"),
    "D034": ("Ingeniería en Sistemas Computacionales — retícula ISIC-2010-224", "Tecnológico Nacional de México (TecNM)", "México", "2010", "Retícula Curricular", "créditos"),
    "D035": ("Ingeniería en Computación — plan 2024", "Universidad Nacional de La Plata (UNLP)", "Argentina", "2024", "Plan de Estudios Oficial", "horas/créditos"),
    "D036": ("Bachillerato en Computación con Varios Énfasis — plan 420705", "Universidad de Costa Rica (UCR-ECCI)", "Costa Rica", "2016", "Plan de Estudios Oficial", "créditos"),
    "D037": ("Ingeniería en Tecnologías de la Información — plan 135 créditos", "Universidad Técnica Particular de Loja (UTPL)", "Ecuador", "2020", "Plan de Estudios Oficial", "créditos"),
    "D038": ("Ingeniería en Sistemas Computacionales — nuevo plan", "Universidad Nacional Autónoma de Honduras (UNAH)", "Honduras", "2021", "Plan de Estudios Oficial", "unidades valorativas"),
    "D039": ("Ingeniería de Sistemas y Computación — plan ISIS 134", "Universidad de los Andes (UniAndes)", "Colombia", "2018", "Plan de Estudios Oficial", "créditos"),
    "D040": ("Ingeniería de Sistemas — plan de estudios", "Universidad EAFIT", "Colombia", "2020", "Plan de Estudios Oficial", "créditos"),
    "D041": ("Ingeniería en Informática — plan 2020", "Universidad de Buenos Aires (UBA - FIUBA)", "Argentina", "2020", "Plan de Estudios Oficial", "créditos"),
    "D042": ("Licenciatura en Ciencias de la Ingeniería / Civil Computación", "Pontificia Universidad Católica de Chile (PUC Chile)", "Chile", "2020", "Plan de Estudios Oficial", "créditos"),
    "D043": ("Licenciatura en Ingeniería en Computación — plan UEA", "Universidad Autónoma Metropolitana (UAM Azcapotzalco)", "México", "s. f.", "Plan de Estudios Oficial", "créditos UEA"),
    "D044": ("Ingeniería en Computación — plan ICOM", "Universidad de Guadalajara (UdeG - CUCEI)", "México", "2017", "Plan de Estudios Oficial", "créditos"),
    "D045": ("Ingeniería en Tecnologías Computacionales — modelo Tec21", "Tecnológico de Monterrey (ITESM)", "México", "2019", "Plan de Estudios Oficial", "créditos"),
}
URLS = {d: u for d, u in json.loads((B / "bloque_03_fuentes.json").read_text(encoding="utf-8"))}

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

(B / "bloque_03_datos.json").write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
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

escribir_csv("bloque_03_resultados.csv", cols, rows, extrasaction="ignore")
escribir_csv("bloque_03_clasificacion.csv", list(audit[0]), audit)

if __name__ == "__main__":
    for r in rows:
        print(r["ID"], f'X={r["Coordenada_X"]:6.2f} Y={r["Coordenada_Y"]:6.2f} R={r["Desviacion_Radio"]:5.2f}',
              r["Proximidad_Disciplina_CC2020"], "|", r["Resumen_Evidencia_X"].split(";")[-1].strip(),
              "|", r["Resumen_Evidencia_Y"].split(";")[-1].strip())
    print("\nSin coincidencia con regla (excluidas):")
    for d, names in unmatched.items():
        print(d, names)
