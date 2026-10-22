"""Diagrama de dispersión del bloque 5 (D061–D075). Lee bloque_05_datos.json y verifica las fórmulas."""
from pathlib import Path
import json
import sys
sys.path.append(str(Path(__file__).resolve().parent / ".deps"))
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BASE = Path(__file__).resolve().parent
df = pd.DataFrame(json.loads((BASE / "bloque_05_datos.json").read_text(encoding="utf-8")))
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
               s=70, alpha=0.9, clip_on=False, zorder=4)

# Posicionamiento calibrado de etiquetas para evitar superposiciones
AJUSTES = {
    "D061": (-45, -25),  # USP (-1.82, -0.67)
    "D062": (-45, -30),  # UNICAMP (-1.27, -2.12)
    "D063": (-45, 25),   # UdeA (-1.97, 0.59)
    "D064": (-50, 0),    # UNC (-2.92, -0.59)
    "D065": (-45, 20),   # UNSAAC (-0.31, 0.14)
    "D066": (-35, -25),  # TEC (0.00, -0.07)
    "D067": (-40, -35),  # EPN (-0.83, -0.32)
    "D068": (25, 35),    # UCB (-0.05, 0.22)
    "D069": (-45, 35),   # Uninorte (-1.10, 0.33)
    "D070": (35, -30),   # UV (0.00, -0.59)
    "D071": (-40, -15),  # UNS (-1.36, -0.62)
    "D072": (-20, 45),   # UACh (-0.31, 0.19)
    "D073": (35, 25),    # UADY (1.50, 0.31)
    "D074": (45, 10),    # UNT (0.10, 0.14)
    "D075": (40, 25),    # UCR Empresarial (2.60, 1.76)
}

for _, r in df.iterrows():
    off = AJUSTES.get(r.ID, (25, 20))
    ax.annotate(r.ID, xy=(r.X, r.Y), xytext=off,
                textcoords="offset points", ha="center", va="center", fontsize=9,
                arrowprops=dict(arrowstyle="-", color="#666666", lw=0.7),
                bbox=dict(facecolor="white", edgecolor="#cccccc", alpha=0.9, pad=1.5, boxstyle="round,pad=0.2"))

ax.set_xlabel("Theory, Principles, Innovation  <-  X  ->  Application, Deployment, Configuration",
              fontsize=10, labelpad=14)
ax.set_ylabel("Computer Hardware and Architecture  <-  Y  ->  Organizational Issues and Information Systems",
              fontsize=10, labelpad=14)
ax.set_title("Bloque 5/5: planes de estudio D061–D075 (ponderados por créditos u horas)\n"
             "Codificación por reglas explícitas; no son mediciones oficiales de CC2020", pad=18)
ax.legend(title="Afinidad provisional", loc="upper left")
fig.text(0.5, 0.035,
         "Se excluyen optativas sin contenido, idiomas, humanidades, prácticas y trabajos de grado (ver cobertura en informe).\n"
         "Etiquetas unidas por líneas: la posición del texto no es la posición del dato.",
         ha="center", fontsize=9)
fig.subplots_adjust(bottom=0.16, left=0.13, right=0.96, top=0.88)
fig.savefig(BASE / "bloque_05_dispersion.png", dpi=180)
plt.close(fig)
print("Verificados 15 registros de Bloque 5, fórmulas, rangos e identificadores. Imagen guardada.")
