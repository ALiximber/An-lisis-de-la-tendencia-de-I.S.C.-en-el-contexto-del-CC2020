"""Diagrama de dispersión del bloque 4 (D046–D060). Lee bloque_04_datos.json y verifica las fórmulas."""
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
df = pd.DataFrame(json.loads((BASE / "bloque_04_datos.json").read_text(encoding="utf-8")))
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
    "D046": (35, -25),   # UdelaR (-0.41, -0.36)
    "D047": (35, 25),    # UNSA (1.00, 1.00)
    "D048": (-45, -15),  # UdeC (-0.96, 0.00)
    "D049": (35, 15),    # UIS (-0.91, 0.12)
    "D050": (-50, -30),  # UANL (-1.55, -0.48)
    "D051": (-50, 15),   # UNA (-1.12, -0.14)
    "D052": (40, 30),    # UTP (-0.83, 0.13)
    "D053": (-45, -35),  # USAC (-1.44, -0.84)
    "D054": (35, 30),    # UNMSM (-0.16, 1.13)
    "D055": (-35, 35),   # Univalle (-0.92, 0.35)
    "D056": (-55, 0),    # UNR (-1.60, -0.24)
    "D057": (-45, 35),   # USM (-1.36, 1.25)
    "D058": (-45, -35),  # UASLP (-1.43, -1.39)
    "D059": (40, -25),   # PUCE (1.21, -0.58)
    "D060": (30, -35),   # UMSA (-1.09, -0.67)
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
ax.set_title("Bloque 4/5: planes de estudio D046–D060 (ponderados por créditos u horas)\n"
             "Codificación por reglas explícitas; no son mediciones oficiales de CC2020", pad=18)
ax.legend(title="Afinidad provisional", loc="upper left")
fig.text(0.5, 0.035,
         "Se excluyen optativas sin contenido, idiomas, humanidades, prácticas y trabajos de grado (ver cobertura en informe).\n"
         "Etiquetas unidas por líneas: la posición del texto no es la posición del dato.",
         ha="center", fontsize=9)
fig.subplots_adjust(bottom=0.16, left=0.13, right=0.96, top=0.88)
fig.savefig(BASE / "bloque_04_dispersion.png", dpi=180)
plt.close(fig)
print("Verificados 15 registros de Bloque 4, fórmulas, rangos e identificadores. Imagen guardada.")
