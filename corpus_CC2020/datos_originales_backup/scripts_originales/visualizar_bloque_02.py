"""Diagrama de dispersión del bloque 2 (D016–D030). Lee bloque_02_datos.json y verifica las fórmulas."""
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
df = pd.DataFrame(json.loads((BASE / "bloque_02_datos.json").read_text(encoding="utf-8")))
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
    assert np.allclose(df[col], values, atol=0.006), f"Inconsistencia en {col}"
assert x.between(-5, 5).all() and y.between(-5, 5).all()
df["X"], df["Y"], df["DX"], df["DY"] = x, y, dx, dy
colors = {"CS": "#3366cc", "CE": "#8c564b", "SE": "#238b45",
          "IT": "#d97706", "IS": "#8b5cf6", "DS": "#d43f72"}

fig, ax = plt.subplots(figsize=(12, 9))
ax.set(xlim=(-5, 5), ylim=(-5, 5), xticks=range(-5, 6), yticks=range(-5, 6))
ax.set_aspect("equal", adjustable="box")
ax.axhline(0, color="#777777", ls="--", lw=0.8)
ax.axvline(0, color="#777777", ls="--", lw=0.8)
ax.grid(alpha=0.12)
for disc, group in df.groupby("Proximidad_Disciplina_CC2020"):
    ax.scatter(group.X, group.Y, color=colors[disc], label=disc,
               s=65, alpha=0.85, clip_on=False, zorder=4)

# Opcional: dispersión entre categorías (no es intervalo de confianza).
MOSTRAR_DISPERSION = False
if MOSTRAR_DISPERSION:
    for _, r in df.iterrows():
        if r.DX > 0 and r.DY > 0:
            ax.add_patch(Ellipse((r.X, r.Y), 2 * r.DX, 2 * r.DY, fill=False, alpha=0.18,
                                 edgecolor=colors[r.Proximidad_Disciplina_CC2020]))

# Etiquetas con líneas guía cortas, desplazadas hacia afuera del centroide de la nube.
cx, cy = df.X.mean(), df.Y.mean()
AJUSTES = {"D021": (-58, -18), "D028": (-70, -34), "D027": (0, -48), "D016": (46, -34)}  # solo etiquetas
for i, (_, r) in enumerate(df.sort_values(["X", "Y"]).iterrows()):
    vx, vy = r.X - cx, r.Y - cy
    ang = np.arctan2(vy, vx) + (0.35 if i % 2 else -0.35)   # alterna para separar puntos vecinos
    dist = 26 + 10 * (i % 3)
    off = AJUSTES.get(r.ID, (dist * np.cos(ang), dist * np.sin(ang)))
    ax.annotate(r.ID, xy=(r.X, r.Y), xytext=off,
                textcoords="offset points", ha="center", va="center", fontsize=9,
                arrowprops=dict(arrowstyle="-", color="#777", lw=0.6),
                bbox=dict(facecolor="white", edgecolor="none", alpha=0.85, pad=1.5))

ax.set_xlabel("Theory, Principles, Innovation  <-  X  ->  Application, Deployment, Configuration",
              fontsize=10, labelpad=14)
ax.set_ylabel("Computer Hardware and Architecture  <-  Y  ->  Organizational Issues and Information Systems",
              fontsize=10, labelpad=14)
ax.set_title("Bloque 2/5: planes de estudio D016–D030 (ponderados por créditos u horas)\n"
             "Codificación por reglas explícitas; no son mediciones oficiales de CC2020", pad=18)
ax.legend(title="Afinidad provisional", loc="upper left")
fig.text(0.5, 0.035,
         "Se excluyen optativas sin contenido, idiomas, humanidades, prácticas y trabajos de grado (ver cobertura).\n"
         "Etiquetas unidas por líneas: la posición del texto no es la posición del dato.",
         ha="center", fontsize=9)
fig.subplots_adjust(bottom=0.16, left=0.13, right=0.96, top=0.88)
fig.savefig(BASE / "bloque_02_dispersion.png", dpi=180)
plt.close(fig)
print("Verificados 15 registros, fórmulas, rangos e identificadores.")
