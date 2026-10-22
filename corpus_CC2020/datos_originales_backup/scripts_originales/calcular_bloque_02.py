"""Bloque 2 (D016-D030): clasificación auditable de asignaturas y cálculo de coordenadas.

Entrada : bloque_02_transcripcion.json (asignaturas con peso en créditos u horas)
Salida  : bloque_02_datos.json            (mismo esquema que bloque_01_datos.json)
          bloque_02_resultados.csv        (12 columnas solicitadas)
          bloque_02_clasificacion.csv     (auditoría materia por materia)

Las coordenadas NO se asignan a mano: salen de REGLAS (lista ordenada de expresiones
regulares; gana la primera que coincide). Lo que no coincide queda 'no clasificado' y se
excluye del cálculo, registrando su peso para reportar la cobertura.
"""
from pathlib import Path
import csv, json, math, re, unicodedata

B = Path(__file__).resolve().parent
raw = json.loads((B / "bloque_02_transcripcion.json").read_text(encoding="utf-8"))

# (patrón, X, Y)  X: T=teoría/principios, A=aplicación/despliegue, None=excluido en X
#                 Y: H=hardware, S=software/sistemas, O=organizacional, None=excluido en Y
RULES = [
    # 1. Exclusiones: formación transversal, optativas sin contenido, capstones/prácticas
    (r"optativa [ab]\d|optativa de estudio general|optativas|electiv|libre eleccion|optativa de opcion|"
     r"temas selectos|topicos de vanguardia|perspectivas disciplinares|profundizacion|enfasis|"
     r"idioma|ingles|lengua extranjera|beginner|comunicacion (oral|\d)|competencias comunicativas|"
     r"procesos comunicativos|^comunicacion$|comprension lectora|redaccion indirecta|escritura academica|"
     r"argumentacion|expresion oral|humanidades|teologia|constitucion|democracia|catedra|cultura|"
     r"sociologia|psicologia|sociohumanistica|etica|etico|emprend|liderazgo|actividades culturales|empleabilidad|"
     r"metodos y tecnicas de investigacion|pensamiento complejo|"
     r"desarrollo del (talento|pensamiento)|desarrollo de habilidades|responsabilidad social|"
     r"proyecto social|practica comunitaria|practicas? (profesional|preprofesional|en la profesion)|estancia|trabajo terminal|trabajo de grado|"
     r"proyecto de (grado|ingenieria|sistemas)|proyecto (final|integrador)|capstone|tesis|"
     r"articulo cientifico|seminario de investigacion|preparacion de proyectos de investigacion|"
     r"taller interdisciplinario|taller de evaluacion|metodologia (universitaria|de (la )?investigacion)|"
     r"fundamentos y generalidades de investigacion|herramientas digitales para|ingenieria y sociedad|"
     r"ciencias, tecnologia y desarrollo|contexto geopolitico|seguridad, higiene|"
     r"tecnologias (emergentes|avanzadas)|fundamentos en gestion integral|"
     r"introduccion a (la|los) (ingenieria|sistemas|informatica)|fundamentacion en ingenieria|"
     r"herramientas (computacionales|informaticas)|cuenca|experiencia formativa|orinoquia",
     None, None),
    # 2. Pensamiento/ciencias de sistemas orientadas a organización
    (r"teoria de sistemas|pensamiento sistemico|metodos cuantitativos", "T", "O"),
    # 3. Hardware
    (r"fundamentos fisicos de la informatica|circuitos|electronica|sistemas electricos|senales|"
     r"sistemas de comunicaciones", "T", "H"),
    (r"sistemas digitales|diseno digital|logica digital|maquinas digitales|diseno logico|"
     r"tecnologia de computadores|elementos de computadores|sistemas en chip|instrumentacion|"
     r"programacion de bajo nivel|sistemas embebidos|robotica|automatizacion", "A", "H"),
    # 4. Arquitecturas
    (r"arquitectura (empresarial|de infraestructura)|gobierno", "A", "O"),
    (r"arquitectura de software", "A", "S"),
    (r"arquitectura (del|de) comput|arquitectura y organizacion|organizacion de computadoras", "T", "H"),
    (r"modelacion de datos|modelado de datos", "A", "S"),
    # 5. Gestión de proyectos / TI
    (r"formulacion|gestion de proyectos|gerencia|administracion de proyectos|evaluacion y administracion|"
     r"elaboracion de proyectos|gestion de ti|gestion de procesos", "A", "O"),
    # 6. Factores humanos
    (r"interaccion (humano|persona)|interfaz|interfaces", "A", "O"),
    # 7. Seguridad
    (r"seguridad|security|ciberseguridad|criptografia", "A", "S"),
    # 8. Teoría de la computación y fundamentos algorítmicos
    (r"pensamiento logico", "T", None),
    (r"algoritmos y programacion|algoritmia y programacion", "A", "S"),
    (r"matematicas? discreta|estructuras discretas|logica|teoria de la computacion|computabilidad|automatas|"
     r"lenguajes formales|algoritm|teoria de (la informacion|lenguajes)|sintaxis y semantica|"
     r"lenguajes y paradigmas|paradigmas|^lenguajes$|lenguajes de programacion|compiladores|"
     r"programacion (logica|funcional)|arboles y grafos|estructuras? de datos|principios de computacion|"
     r"introduccion a la teoria|desarrollo formal|inteligencia artificial|sistemas inteligentes|aprendizaje|"
     r"vision artificial|ciencia de datos|sistemas basados en conocimiento|computacion (grafica|cientifica)|"
     r"codificacion", "T", "S"),
    # 9. Sistemas de información / negocio antes que la capa de software genérica
    (r"sistemas? de informacion|sistemas y (procesos|organizaciones)|inteligencia de negocios|"
     r"negocios electronicos", "A", "O"),
    # 10. Software, datos, redes y sistemas
    (r"bases? de datos|sistemas operativos|software|\bred(es)?\b|telecomunicaciones|programacion|desarrollo|"
     r"aplicaciones|\bweb\b|moviles|nube|distribuid|paralela|videojuegos|devops|conectividad|"
     r"analisis (y diseno )?de sistemas|implantacion|integracion de sistemas|informacion y comunicaciones|"
     r"comunicacion de datos|computacion aplicada|realidad virtual|requerimientos|mineria de datos",
     "A", "S"),
    # 11. Organización y negocio
    (r"economi|finanz|contab|costos|presupuesto|empresa|negocio|administracion|administrativ|gestion|legislacion|"
     r"deontologia|auditoria|organizacion|reingenieria|capital humano|planeamiento estrategico", "A", "O"),
    # 12. Ciencias básicas y métodos cuantitativos (sin capa Y)
    (r"calculo|algebra|matematic|probabili|estadistic|ecuaciones|analisis (vectorial|matematico|numerico)|"
     r"metodos numericos|geometria|fisica|mecanica|oscilacion|ondas|electricidad|electromagnet|estatica|"
     r"cinematica|biologia|quimica|optimizacion|investigacion (de operaciones|operativa)|modelos?|"
     r"simulacion|procesos estocasticos|modelado|dinamica|sistemas complejos|dibujo|preliminares|"
     r"complemento matematico", "T", None),
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
    return None, None, 0   # regla 0 = sin coincidencia

META = {  # (título, institución, país, año, tipo, unidad, URL-nota)
    "D016": ("Ingeniería en Sistemas Computacionales — plan de estudios", "Universidad de las Américas Puebla (UDLAP)", "México", "s. f.", "Plan de Estudios Oficial", "créditos"),
    "D017": ("Ingeniería en Sistemas Computacionales — mapa curricular 2020", "IPN — ESCOM", "México", "2020", "Retícula Curricular", "créditos"),
    "D018": ("Licenciatura en Sistemas Computacionales — plan 2023-2", "Universidad Autónoma de Baja California (Mexicali)", "México", "2023", "Plan de Estudios Oficial", "créditos"),
    "D019": ("Ingeniería de Sistemas Computacionales — plan de estudios", "Universidad Privada del Norte (UPN)", "Perú", "2021 (fecha en la URL)", "Plan de Estudios Oficial", "créditos"),
    "D020": ("Ingeniería de Sistemas y Computación — plan flexible 2023", "Universidad Nacional de Colombia (Bogotá)", "Colombia", "2023", "Retícula Curricular", "créditos"),
    "D021": ("Ingeniería de Sistemas y Computación — plan de estudios", "Pontificia Universidad Javeriana Cali", "Colombia", "s. f.", "Plan de Estudios Oficial", "créditos"),
    "D022": ("Ingeniería en Sistemas — pensum", "Universidad de Sonsonate", "El Salvador", "s. f.", "Plan de Estudios Oficial", "unidades valorativas"),
    "D023": ("Ingeniería de Sistemas — plan académico", "Universidad Nacional del Callao (FIIS)", "Perú", "2024 (fecha de impresión)", "Plan de Estudios Oficial", "créditos"),
    "D024": ("Ingeniería de Sistemas — plan de estudios", "Universidad Nacional Abierta y a Distancia (UNAD)", "Colombia", "2025 (ruta de la URL)", "Retícula Curricular", "créditos"),
    "D025": ("Ingeniería en Sistemas de Información — plan 2023", "UTN — Facultad Regional Buenos Aires", "Argentina", "2023", "Plan de Estudios Oficial", "horas"),
    "D026": ("Ingeniería en Sistemas — plan de estudios", "Universidad Nacional de La Pampa (UNLPam)", "Argentina", "2023", "Plan de Estudios Oficial", "horas"),
    "D027": ("Ingeniería de Sistemas — plan 2023", "UNICEN — Facultad de Ciencias Exactas", "Argentina", "2023", "Plan de Estudios Oficial", "horas"),
    "D028": ("Ingeniería de Sistemas — plan PIS 603", "Universidad de los Llanos (Unillanos)", "Colombia", "2018", "Plan de Estudios Oficial", "créditos"),
    "D029": ("Ingeniería de Sistemas (presencial) — plan de estudios", "Universidad EAN", "Colombia", "s. f.", "Plan de Estudios Oficial", "créditos"),
    "D030": ("Licenciatura en Ingeniería de Sistemas Computacionales", "UNIR México", "México", "s. f.", "Plan de Estudios Oficial", "créditos"),
}
URLS = {d: u for d, u in json.loads((B / "bloque_02_fuentes.json").read_text(encoding="utf-8"))}

def afinidad(pt, pa, ch, cs, co):
    """Afinidad PROVISIONAL (reglas del script, no centroides oficiales de CC2020)."""
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

(B / "bloque_02_datos.json").write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
cols = ["ID", "Titulo_Documento", "Institucion_Fuente", "Pais", "Anio", "Tipo_Fuente", "Coordenada_X",
        "Coordenada_Y", "Desviacion_Radio", "Proximidad_Disciplina_CC2020", "Resumen_Evidencia_X",
        "Resumen_Evidencia_Y"]
def escribir_csv(nombre, campos, filas, **kw):
    """Escribe el CSV; si Excel lo tiene abierto, lo guarda como <nombre>_nuevo.csv."""
    for destino in (B / nombre, B / nombre.replace(".csv", "_nuevo.csv")):
        try:
            with destino.open("w", newline="", encoding="utf-8-sig") as f:
                w = csv.DictWriter(f, fieldnames=campos, **kw); w.writeheader(); w.writerows(filas)
            return destino
        except PermissionError:
            print(f"AVISO: {destino.name} está bloqueado (¿abierto en Excel?)")
    raise PermissionError(f"No se pudo escribir {nombre}")

escribir_csv("bloque_02_resultados.csv", cols, rows, extrasaction="ignore")
escribir_csv("bloque_02_clasificacion.csv", list(audit[0]), audit)

if __name__ == "__main__":
    for r in rows:
        print(r["ID"], f'X={r["Coordenada_X"]:6.2f} Y={r["Coordenada_Y"]:6.2f} R={r["Desviacion_Radio"]:5.2f}',
              r["Proximidad_Disciplina_CC2020"], "|", r["Resumen_Evidencia_X"].split(";")[-1].strip(),
              "|", r["Resumen_Evidencia_Y"].split(";")[-1].strip())
    print("\nSin coincidencia con regla (excluidas):")
    for d, names in unmatched.items():
        print(d, names)
