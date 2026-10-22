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

