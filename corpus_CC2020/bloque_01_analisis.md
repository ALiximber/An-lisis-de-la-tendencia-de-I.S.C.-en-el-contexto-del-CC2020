# Corpus CC2020 — Bloque 1 de 5
Fecha de consulta: 22 de octubre de 2026. Objetivo total: 75 documentos. Este bloque: D001–D015; pendientes: D016–D075.

## Alcance
Primera codificación exploratoria de 15 perfiles de egreso institucionales: 13 de México, uno de Ecuador y uno de Honduras. No es una muestra representativa ni una auditoría de créditos. El predominio de fuentes sin fecha impide verificar el criterio temporal 2015–presente para la mayoría. Se conservan como excepciones explícitas y no se les asigna la fecha de consulta como año de publicación. El siguiente bloque debe priorizar planes fechados y ponderación por créditos. No mezclar medias de perfiles y planes.

La figura 2.2 adjunta de CC2020 es conceptual: no proporciona coordenadas, centroides ni límites numéricos. El plano pedido es una adaptación del usuario. La figura incluye CSEC y EE, además de las seis etiquetas solicitadas. El campo de afinidad usa únicamente CS/CE/SE/IT/IS/DS por requerimiento; puede ocultar ciberseguridad. No implica equivalencia, acreditación ni distancia euclidiana validada.

## Reglas de codificación
1. Se toma exclusivamente el apartado de perfil/atributos de egreso señalado en cada ficha, no el perfil de ingreso, campo laboral ni el nombre de las materias.
2. Cada viñeta técnica cuenta una unidad. En prosa se separan predicados con objetos diferentes; los verbos asociados al mismo objeto permanecen juntos. Las decisiones concretas se enumeran abajo.
3. T identifica fundamentos o modelación matemática explícitos; A identifica construcción, aplicación, operación, evaluación profesional o gestión. Una unidad que hace explícitos ambos recibe 0.5 en cada categoría. Estas fracciones son supuestos analíticos, no pesos publicados por la institución. Investigación sin orientación definida no se presume básica.
4. Ch identifica hardware e interfaces físicas. Cs incluye software, datos, sistemas operativos, redes operativas e infraestructura. Co identifica gestión de proyectos/equipos, negocio, procesos organizacionales y gobernanza. La sola mención de empresas como usuarios no cambia software a Co. Si una unidad trata dos capas se reparte por igual. Usar hardware como herramienta no equivale a diseñarlo.
5. Se excluyen declaraciones genéricas de ética, idiomas, valores y trabajo en equipo sin gestión de proyectos. No se considera que carezcan de valor educativo; quedan fuera de estos dos ejes.
6. Pt/Pa y Ch/Cs/Co son conteos ponderados, no créditos. Los porcentajes se obtienen dividiendo cada conteo entre su denominador. No representan la totalidad curricular.
7. La afinidad disciplinar es una interpretación temática provisional del objeto profesional: SE (construcción de software), IT (operación/integración), IS (procesos y gestión organizacional). No se deduce automáticamente de X/Y. No se asignan CS, CE o DS sin predominio documental suficiente.
8. La codificación de un solo evaluador no elimina el juicio interpretativo. Los números son reproducibles dados los códigos; no son mediciones objetivas independientes de estos. Falta validación por segundo evaluador.

## Cálculos
X = 5(Pa-Pt)/(Pa+Pt).
Y = 5(Co-Ch)/(Ch+Cs+Co).
Delta_X = sqrt(25-X²).
Delta_Y = sqrt(25(Ch+Co)/(Ch+Cs+Co)-Y²).
Desviacion_Radio = sqrt(Delta_X²+Delta_Y²).

Las desviaciones describen la masa repartida entre categorías extremas, incluyendo fracciones mixtas. No son errores de estimación ni intervalos de confianza. Radio cero solo indica que las unidades codificadas cayeron en la misma categoría; no demuestra especialización. El radio no está restringido a 5. Los centros sí están en [-5,5]. La visualización omite por defecto elipses para evitar confundir dispersión con incertidumbre.

## Tabla completa
|ID|Titulo_Documento|Institucion_Fuente|Pais|Anio|Tipo_Fuente|Coordenada_X|Coordenada_Y|Desviacion_Radio|Proximidad_Disciplina_CC2020|Resumen_Evidencia_X|Resumen_Evidencia_Y|URL|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|D001|Ingeniería en Sistemas Computacionales (2020)|IPN — ESCOM|México|2020|Perfil de egreso|2.50|1.25|4.84|SE|Pt=1; Pa=3; conteo ponderado de competencias|Ch=0; Cs=3; Co=1; conteo ponderado de competencias|https://www.escom.ipn.mx/htmls/oferta/isc2020.php|
|D002|Ing. en Sistemas Computacionales — Plan 2016 — Perfil de egreso|Universidad Juárez Autónoma de Tabasco|México|2016|Perfil de egreso|5.00|1.00|2.00|SE|Pt=0; Pa=5; conteo ponderado de competencias|Ch=0; Cs=4; Co=1; conteo ponderado de competencias|https://archivos.ujat.mx/2018/DAIS/PE%20DAIS/ISC%202016/5.ISC_2016_PEGRESO.pdf|
|D003|Ingeniería en Sistemas Computacionales|TecNM — Instituto Tecnológico de Tláhuac II|México|2010|Perfil de egreso|4.44|0.00|4.04|IT|Pt=0.5; Pa=8.5; conteo ponderado de competencias|Ch=2; Cs=5; Co=2; conteo ponderado de competencias|https://tlahuac2.tecnm.mx/oferta-educativa/sistemas-computacionales|
|D004|INGENIERÍA EN SISTEMAS COMPUTACIONALES|Universidad Politécnica Metropolitana de Puebla|México|s. f.|Perfil de egreso|5.00|0.00|0.00|IT|Pt=0; Pa=2; conteo ponderado de competencias|Ch=0; Cs=2; Co=0; conteo ponderado de competencias|https://metropoli.edu.mx/ingenieria-en-sistemas-computacionales/|
|D005|Licenciatura en Ingeniería en Sistemas Computacionales|Universidad IEU|México|2025|Perfil de egreso|5.00|-0.42|1.38|IT|Pt=0; Pa=6; conteo ponderado de competencias|Ch=0.5; Cs=5.5; Co=0; conteo ponderado de competencias|https://ieu.edu.mx/oferta-academica/licenciaturas/ingenieria-en-sistemas-computacionales/|
|D006|Ingenieria en Sistemas Computacionales|Universidad Internacional de América|México|s. f.|Perfil de egreso|4.00|1.00|3.61|IT|Pt=0.5; Pa=4.5; conteo ponderado de competencias|Ch=0; Cs=4; Co=1; conteo ponderado de competencias|https://www.unida.edu.mx/portal/oferta-educativa/ingenieria-en-sistemas-computacionales/|
|D007|Ingeniería en Sistemas Computacionales|Universidad del Valle de Cuernavaca|México|s. f.|Perfil de egreso|5.00|0.00|0.00|IT|Pt=0; Pa=3; conteo ponderado de competencias|Ch=0; Cs=3; Co=0; conteo ponderado de competencias|https://www.univac.edu.mx/ingenieria-en-sistemas-computacionales/|
|D008|Ingeniería en Sistemas Computacionales #ISC|UNISA Centro Universitario|México|s. f.|Perfil de egreso|4.17|0.00|2.76|SE|Pt=0.5; Pa=5.5; conteo ponderado de competencias|Ch=0; Cs=6; Co=0; conteo ponderado de competencias|https://www.unisa.edu.mx/ingenieria-en-sistemas-computacionales/|
|D009|Ingeniería en Sistemas Computacionales|Universidad CUGS|México|s. f.|Perfil de egreso|5.00|0.00|0.00|IT|Pt=0; Pa=3; conteo ponderado de competencias|Ch=0; Cs=3; Co=0; conteo ponderado de competencias|https://www.ucugs.edu.mx/ing-en-sistemas-computacionales|
|D010|Sistemas Computacionales|Universidad UGES|México|s. f.|Perfil de egreso|5.00|2.00|2.45|IT|Pt=0; Pa=5; conteo ponderado de competencias|Ch=0; Cs=3; Co=2; conteo ponderado de competencias|https://www.gesacademico.edu.mx/ingenieria-sistemas.html|
|D011|Ingeniería en Sistemas Computacionales|Universidad del Valle de Atemajac — Guadalajara|México|s. f.|Perfil de egreso|5.00|0.00|0.00|SE|Pt=0; Pa=1; conteo ponderado de competencias|Ch=0; Cs=1; Co=0; conteo ponderado de competencias|https://www.univa.mx/guadalajara/programas-educativos/licenciaturas-impulso-profesional/ingenieria-en-sistemas-computacionales/|
|D012|Ingeniería en Sistemas Computacionales|Universidad INSUCO|México|s. f.|Perfil de egreso|5.00|1.25|2.17|SE|Pt=0; Pa=4; conteo ponderado de competencias|Ch=0; Cs=3; Co=1; conteo ponderado de competencias|https://www.insuco.edu.mx/ingenieria-en-sistemas-computacionales|
|D013|37. Ingeniería en Sistemas Computacionales|Universidad Católica de Santiago de Guayaquil|Ecuador|s. f.|Perfil de egreso|5.00|4.00|2.00|IS|Pt=0; Pa=5; conteo ponderado de competencias|Ch=0; Cs=1; Co=4; conteo ponderado de competencias|https://www.ucsg.edu.ec/wp-content/uploads/acreditacion/documentos-acreditacionUCSG/SE-2.1.4%20Perfiles%20de%20Ingreso%20y%20Egreso%20Carreras%20UCSG.pdf|
|D014|Perfil de ingreso y egreso — Licenciatura en Sistemas Computacionales|Universidad Autónoma de Chiapas — FCA|México|s. f.|Perfil de egreso|5.00|0.00|0.00|IT|Pt=0; Pa=3; conteo ponderado de competencias|Ch=0; Cs=3; Co=0; conteo ponderado de competencias|https://www.fca.unach.mx/23-programas-academicos/licenciatura/licenciatura-en-sistemas-computacionales/187-perfil-de-ingreso-egreso-lsc|
|D015|Ingeniería en Sistemas Computacionales — PERFIL PROFESIONAL|Universidad Jesús de Nazareth|Honduras|s. f.|Perfil de egreso|5.00|1.83|3.29|IS|Pt=0; Pa=15; conteo ponderado de competencias|Ch=1.5; Cs=6.5; Co=7; conteo ponderado de competencias|https://www.ujn.edu.hn/carreras/sistemas.html|

## Registro de decisiones y exclusiones
### D001 — IPN — ESCOM
Atributos 1–4; se excluye 5 (ética y actualización). T: modelación con ciencias básicas (1). A: resolución, desarrollo y planificación (2–4). Cs: 1–3; Co: 4. La capa del atributo 1 se aproxima por su objeto computacional genérico.

Fuente: [Ingeniería en Sistemas Computacionales (2020)](https://www.escom.ipn.mx/htmls/oferta/isc2020.php).

### D002 — Universidad Juárez Autónoma de Tabasco
Cinco viñetas de las páginas 1–2. Todas A. Cs: software, bases de datos, sistemas distribuidos y ejecución de proyectos de software (1,2,3,5). Co: coordinación de equipos y recursos (4).

Fuente: [Ing. en Sistemas Computacionales — Plan 2016 — Perfil de egreso](https://archivos.ujat.mx/2018/DAIS/PE%20DAIS/ISC%202016/5.ISC_2016_PEGRESO.pdf).

### D003 — TecNM — Instituto Tecnológico de Tláhuac II
Nueve viñetas. La 2 combina herramientas matemáticas y aplicación de modelos: T/A=0.5/0.5. Las demás A. Ch: interfaces y evaluación de hardware (3,7). Cs: 1,2,5,6,9. Co: coordinación y oportunidades empresariales (4,8). Año del plan ISIC-2010-224; fecha del perfil no declarada.

Fuente: [Ingeniería en Sistemas Computacionales](https://tlahuac2.tecnm.mx/oferta-educativa/sistemas-computacionales).

### D004 — Universidad Politécnica Metropolitana de Puebla
Perfil segmentado en dos objetos: desarrollo de software y despliegue/administración de redes. Ambos A/Cs. Bilingüismo excluido. Texto recuperado del índice del buscador; la apertura directa devolvió error 500.

Fuente: [INGENIERÍA EN SISTEMAS COMPUTACIONALES](https://metropoli.edu.mx/ingenieria-en-sistemas-computacionales/).

### D005 — Universidad IEU
Seis viñetas, todas A. Cs: 1–5. La sexta integra arquitectura tecnológica con hardware, software y redes: mitad Ch y mitad Cs. 2025 corresponde al inicio anunciado del programa en rediseño; no prueba fecha de actualización de cada viñeta.

Fuente: [Licenciatura en Ingeniería en Sistemas Computacionales](https://ieu.edu.mx/oferta-academica/licenciaturas/ingenieria-en-sistemas-computacionales/).

### D006 — Universidad Internacional de América
Cinco viñetas. La quinta combina modelación matemática/estadística y simulación aplicada: T/A=0.5/0.5. Las otras A. Cs: 1,2,3,5; Co: factibilidad técnico-económica (4). Gestión de centros de cómputo se considera operación de infraestructura. RVOE de 2004 no usado como fecha del perfil.

Fuente: [Ingenieria en Sistemas Computacionales](https://www.unida.edu.mx/portal/oferta-educativa/ingenieria-en-sistemas-computacionales/).

### D007 — Universidad del Valle de Cuernavaca
Tres cláusulas: aplicaciones web/multimedia, soluciones con TI y soporte de sistemas/bases/redes. Todas A/Cs. Se agrupan los verbos que comparten objeto; no se cuentan nuevamente la presentación del perfil ni los objetivos.

Fuente: [Ingeniería en Sistemas Computacionales](https://www.univac.edu.mx/ingenieria-en-sistemas-computacionales/).

### D008 — UNISA Centro Universitario
Seis unidades: resolución matemática/computacional (mixta T/A); infraestructura de datos/redes; métodos y lenguajes; aplicaciones; estándares de calidad; seguridad. Las últimas cinco A; todas Cs por objeto principal. Se excluyen trabajo en equipo genérico y ética. RVOE 2022 no equivale a fecha del perfil.

Fuente: [Ingeniería en Sistemas Computacionales #ISC](https://www.unisa.edu.mx/ingenieria-en-sistemas-computacionales/).

### D009 — Universidad CUGS
Tres viñetas sustantivas: soluciones de información, diagnóstico/solución de fallas y desarrollo/evaluación de programas. Todas A/Cs. Se excluye la cuarta viñeta por ser una frase introductoria sin competencia adicional. Perfil explícitamente no exhaustivo.

Fuente: [Ingeniería en Sistemas Computacionales](https://www.ucugs.edu.mx/ing-en-sistemas-computacionales).

### D010 — Universidad UGES
Cinco viñetas, todas A. Cs: software, datos/redes y nube (1,2,5). Co: transformación empresarial y ciberseguridad organizacional (3,4). El ciclo de admisión 2026 no se trata como año del perfil. La clasificación de ciberseguridad organizacional requiere validación de contenidos.

Fuente: [Sistemas Computacionales](https://www.gesacademico.edu.mx/ingenieria-sistemas.html).

### D011 — Universidad del Valle de Atemajac — Guadalajara
Una unidad técnica: desarrollar/actualizar/evaluar software para información organizacional, A/Cs. Valores éticos y ecológicos excluidos. La finalidad empresarial del software no se convierte automáticamente en formación en gestión.

Fuente: [Ingeniería en Sistemas Computacionales](https://www.univa.mx/guadalajara/programas-educativos/licenciaturas-impulso-profesional/ingenieria-en-sistemas-computacionales/).

### D012 — Universidad INSUCO
Cuatro grupos de acción: desarrollar/mantener productos; gestionar datos y tecnologías de realidad aumentada; resolver problemas tecnológicos; emprender. Todos A. Primeros tres Cs; emprendimiento Co. La redacción del segundo grupo es ambigua y requiere revisión institucional.

Fuente: [Ingeniería en Sistemas Computacionales](https://www.insuco.edu.mx/ingenieria-en-sistemas-computacionales).

### D013 — Universidad Católica de Santiago de Guayaquil
Página 46, viñetas 1–5, todas A. Cs: construcción de sistemas usando herramientas (1); Co: gerencia, proyectos, auditoría y consultoría (2–5). Inglés (6) excluido. Hardware citado como herramienta, sin competencia de diseño de hardware. Auditoría/consultoría clasificadas organizacionalmente de forma provisional.

Fuente: [37. Ingeniería en Sistemas Computacionales](https://www.ucsg.edu.ec/wp-content/uploads/acreditacion/documentos-acreditacionUCSG/SE-2.1.4%20Perfiles%20de%20Ingreso%20y%20Egreso%20Carreras%20UCSG.pdf).

### D014 — Universidad Autónoma de Chiapas — FCA
Primeras tres capacidades: sistemas de información, bases de datos y redes; todas A/Cs. Cuarta capacidad ética y lista de valores excluidas. Programa de licenciatura afín; no se renombra como ingeniería.

Fuente: [Perfil de ingreso y egreso — Licenciatura en Sistemas Computacionales](https://www.fca.unach.mx/23-programas-academicos/licenciatura/licenciatura-en-sistemas-computacionales/187-perfil-de-ingreso-egreso-lsc).

### D015 — Universidad Jesús de Nazareth
Se analiza únicamente la lista de 16 competencias específicas. Se excluye 6: investigación sin orientación ni capa suficientemente determinadas. Las otras 15 son A. Ch: 12 y mitad de 11. Cs: 2,3,5,9,13,14 y mitad de 11. Co: 1,4,7,8,10,15,16. No se suman las listas posteriores para evitar solapamiento.

Fuente: [Ingeniería en Sistemas Computacionales — PERFIL PROFESIONAL](https://www.ujn.edu.hn/carreras/sistemas.html).


## Límites e interpretación
- D001, D002: año explícito del programa/plan; D003: plan 2010, excepción histórica; D005: inicio anunciado 2025 del rediseño. Las fechas no certifican la revisión del perfil textual.
- D004: corroboración mediante texto indexado; la apertura directa falló. Verificación documental parcial.
- D008: RVOE 2022; no se usa como fecha del perfil. D010: ciclo de admisión 2026; tampoco equivale a fecha de publicación.
- D014: licenciatura afín, no ingeniería.
- D015: se limita a la lista de competencias específicas para no duplicar contenidos en listados posteriores.
- D001, D003, D006 y D008 contienen referencias matemáticas que afectan X. En el resto, X=5 significa ausencia de unidades teóricas explícitas en el fragmento codificado, no ausencia de teoría en la carrera.
- D013 y D015 muestran mayor énfasis organizacional bajo esta codificación. D005 incorpora la integración de hardware. Estos hallazgos requieren contraste con retículas y programas de asignatura.
- No se ha demostrado representatividad geográfica, temporal ni curricular. Este bloque por perfiles necesita complementarse con planes fechados, modelos y artículos en los siguientes bloques.

## Reproducibilidad
El archivo JSON contiene las doce columnas solicitadas, URL, fecha de consulta, pesos, desviaciones por eje y decisiones. El script usa pandas, numpy y matplotlib y verifica fórmulas antes de dibujar. Guardar ambos en la misma carpeta y ejecutar visualizar_bloque_01.py.

## Referencia del marco
ACM/IEEE-CS, Computing Curricula 2020: Paradigms for Global Computing Education (2020): https://doi.org/10.1145/3467967
La adaptación cartesiana y las fórmulas provienen de la solicitud del usuario, no se atribuyen como instrumento oficial validado de CC2020.

## Código
```python
from pathlib import Path
import json
import sys
sys.path.append(str(Path(__file__).resolve().parent / ".deps"))
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

BASE = Path(__file__).resolve().parent
df = pd.DataFrame(json.loads((BASE / "bloque_01_datos.json").read_text(encoding="utf-8")))
assert len(df) == 15 and df["ID"].is_unique
nx = df.Pt + df.Pa
ny = df.Ch + df.Cs + df.Co
assert (nx > 0).all() and (ny > 0).all()
x = 5 * (df.Pa - df.Pt) / nx
y = 5 * (df.Co - df.Ch) / ny
dx = np.sqrt(np.maximum(0, 25 - x**2))
dy = np.sqrt(np.maximum(0, 25 * (df.Ch + df.Co) / ny - y**2))
for col, values in [("Coordenada_X", x), ("Coordenada_Y", y),
                    ("Desviacion_Radio", np.hypot(dx, dy))]:
    assert np.allclose(df[col], values), f"Inconsistencia en {col}"
assert x.between(-5, 5).all() and y.between(-5, 5).all()
df["X"], df["Y"], df["DX"], df["DY"] = x, y, dx, dy
colors = {"CS":"#3366cc", "CE":"#8c564b", "SE":"#238b45",
          "IT":"#d97706", "IS":"#8b5cf6", "DS":"#d43f72"}

# No se inventan centros ni fronteras disciplinares oficiales.
fig, ax = plt.subplots(figsize=(12, 9))
ax.set(xlim=(-5, 5), ylim=(-5, 5), xticks=range(-5, 6), yticks=range(-5, 6))
ax.set_aspect("equal", adjustable="box")
ax.axhline(0, color="#777777", ls="--", lw=0.8)
ax.axvline(0, color="#777777", ls="--", lw=0.8)
ax.grid(alpha=0.12)
for disc, group in df.groupby("Proximidad_Disciplina_CC2020"):
    ax.scatter(group.X, group.Y, color=colors[disc], label=disc,
               s=65, alpha=0.85, clip_on=False, zorder=4)

# Opcional: dispersion de categorias, no intervalos de confianza.
MOSTRAR_DISPERSION = False
if MOSTRAR_DISPERSION:
    for _, r in df.iterrows():
        if r.DX > 0 and r.DY > 0:
            ax.add_patch(Ellipse((r.X, r.Y), 2*r.DX, 2*r.DY,
                                fill=False, alpha=0.18,
                                edgecolor=colors[r.Proximidad_Disciplina_CC2020]))
        elif r.DY > 0:
            ax.vlines(r.X, r.Y-r.DY, r.Y+r.DY, alpha=0.18)
        elif r.DX > 0:
            ax.hlines(r.Y, r.X-r.DX, r.X+r.DX, alpha=0.18)

# Etiquetas agrupadas: los documentos coincidentes conservan su coordenada.
groups = list(df.groupby(["X", "Y"], sort=True))
right = [(xy, g) for xy, g in groups if np.isclose(xy[0], 5)]
positions = np.linspace(-2.0, 4.1, len(right))
for (xy, group), label_y in zip(right, positions):
    ax.annotate(", ".join(group.ID), xy=xy, xytext=(3.05, label_y),
                ha="right", va="center", fontsize=9,
                arrowprops=dict(arrowstyle="-", color="#777", lw=0.7),
                bbox=dict(facecolor="white", edgecolor="none", alpha=0.8))
for xy, group in groups:
    if not np.isclose(xy[0], 5):
        offset = (-12, -24) if "D008" in group.ID.values else (-12, 15)
        ax.annotate(", ".join(group.ID), xy=xy, xytext=offset,
                    textcoords="offset points", ha="right", fontsize=9,
                    arrowprops=dict(arrowstyle="-", color="#777", lw=0.7))
ax.set_xlabel("Theory, Principles, Innovation  <-  X  ->  Application, Deployment, Configuration",
              fontsize=10, labelpad=14)
ax.set_ylabel("Computer Hardware and Architecture  <-  Y  ->  Organizational Issues and Information Systems",
              fontsize=10, labelpad=14)
ax.set_title("Bloque 1/5: perfiles de egreso D001–D015\n"
             "Adaptación analítica; coordenadas condicionadas a la codificación", pad=18)
ax.legend(title="Afinidad temática provisional", loc="upper left")
fig.text(0.5, 0.035,
         "Pesos iguales por competencia; no son porcentajes de créditos.\n"
         "Etiquetas unidas por líneas: posición del texto distinta de la posición del dato.",
         ha="center", fontsize=9)
fig.subplots_adjust(bottom=0.16, left=0.13, right=0.96, top=0.88)
fig.savefig(BASE / "bloque_01_dispersion.png", dpi=180)
plt.close(fig)
print("Verificados 15 registros, fórmulas, rangos e identificadores.")

```

