"""Script de consolidación y visualización del Corpus CC2020 completo (75 documentos).
Genera la visualización global con delimitación de la mancha de densidad (KDE 2D) y curva de regresión no lineal."""
from pathlib import Path
import json
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BASE = Path(__file__).resolve().parent

# 1. Cargar todos los bloques D001 - D075
all_records = []
for b in range(1, 6):
    fpath = BASE / f"bloque_{b:02d}_datos.json"
    data = json.loads(fpath.read_text(encoding="utf-8"))
    for row in data:
        row["Bloque_Num"] = b
        row["Tipo_Agrupado"] = "Perfil de Egreso (Bloque 1)" if b == 1 else "Plan de Estudios Oficial (Bloques 2-5)"
    all_records.extend(data)

df = pd.DataFrame(all_records)
assert len(df) == 75, f"Esperados 75 registros, encontrados {len(df)}"

# Guardar dataset maestro consolidado
df.to_csv(BASE / "corpus_CC2020_completo_75.csv", index=False, encoding="utf-8-sig")
(BASE / "corpus_CC2020_completo_75.json").write_text(json.dumps(all_records, ensure_ascii=False, indent=2), encoding="utf-8")

X = df["Coordenada_X"].values
Y = df["Coordenada_Y"].values

# 2. Estimación de Densidad Bivariada 2D (KDE Gaussiano Vectorizado en NumPy)
gx = np.linspace(-5.2, 5.2, 350)
gy = np.linspace(-5.2, 5.2, 350)
GX, GY = np.meshgrid(gx, gy)

hx = 1.06 * np.std(X) * (len(X) ** -0.2) * 0.95
hy = 1.06 * np.std(Y) * (len(X) ** -0.2) * 0.95

d2 = ((GX[:, :, None] - X[None, None, :]) / hx) ** 2 + ((GY[:, :, None] - Y[None, None, :]) / hy) ** 2
Z = np.mean(np.exp(-0.5 * d2) / (2 * np.pi * hx * hy), axis=2)

# 3. Regresión No Lineal (Nadaraya-Watson Kernel Regression)
x_curve = np.linspace(X.min(), X.max(), 300)
bw_reg = 0.90
weights = np.exp(-0.5 * ((x_curve[:, None] - X[None, :]) / bw_reg) ** 2)
y_kernel = np.sum(weights * Y[None, :], axis=1) / np.sum(weights, axis=1)

# Banda de dispersión local (±1 desviación estándar condicional)
y_local_var = np.sum(weights * ((Y[None, :] - y_kernel[:, None]) ** 2), axis=1) / np.sum(weights, axis=1)
y_local_std = np.sqrt(y_local_var)

# 4. Creación de la Figura
fig, ax = plt.subplots(figsize=(14.5, 11.5), dpi=220)
ax.set(xlim=(-5.15, 5.15), ylim=(-5.15, 5.15), xticks=range(-5, 6), yticks=range(-5, 6))
ax.set_aspect("equal", adjustable="box")

# Cuadrantes y marcas guía
ax.axhline(0, color="#64748b", ls="--", lw=1.1, zorder=2)
ax.axvline(0, color="#64748b", ls="--", lw=1.1, zorder=2)
ax.grid(alpha=0.16, color="#94a3b8", ls=":")

# Nombres de cuadrantes en esquinas
ax.text(4.95, 4.90, "Cuadrante I: Aplicación & Sistemas Organizacionales\n(IS / SE / IT)", 
        ha="right", va="top", fontsize=9, color="#64748b", style="italic", fontweight="bold")
ax.text(-4.95, 4.90, "Cuadrante II: Teoría & Sistemas Organizacionales\n(Fundamentos Sistémicos)", 
        ha="left", va="top", fontsize=9, color="#64748b", style="italic", fontweight="bold")
ax.text(-4.95, -4.90, "Cuadrante III: Teoría & Arquitectura / Hardware\n(CS / CE)", 
        ha="left", va="bottom", fontsize=9, color="#64748b", style="italic", fontweight="bold")
ax.text(4.95, -4.90, "Cuadrante IV: Aplicación & Tecnologías Embebidas\n(Despliegue Físico)", 
        ha="right", va="bottom", fontsize=9, color="#64748b", style="italic", fontweight="bold")

# 5. Capa de la Mancha de Densidad (KDE 2D)
levels = np.linspace(Z.max() * 0.04, Z.max() * 0.95, 15)
cf = ax.contourf(GX, GY, Z, levels=levels, cmap="Blues", alpha=0.42, zorder=1)

# Delimitación de la mancha (Isolíneas de densidad envolvente)
cs_outer = ax.contour(GX, GY, Z, levels=[Z.max() * 0.07, Z.max() * 0.28, Z.max() * 0.60],
                      colors=["#0284c7", "#0369a1", "#075985"], linewidths=[1.5, 2.0, 2.4],
                      linestyles=["-.", "--", "-"], zorder=2)

# 6. Banda y Curva de Regresión No Lineal
ax.fill_between(x_curve, y_kernel - y_local_std, y_kernel + y_local_std,
                color="#f43f5e", alpha=0.15, label="Banda de soporte no lineal (±1σ condicional)", zorder=3)

line_reg, = ax.plot(x_curve, y_kernel, color="#e11d48", lw=3.2, zorder=4,
                    label="Regresión no lineal Nadaraya-Watson (Curva de tendencia)")

# 7. Dispersión de los 75 Puntos por Disciplina
colors = {"CS": "#2563eb", "CE": "#92400e", "SE": "#16a34a",
          "IT": "#d97706", "IS": "#7c3aed", "DS": "#db2777"}

# Bloques 2-5: Planes de estudio oficiales (Círculos sólidos)
df_planes = df[df["Bloque_Num"] > 1]
for disc, grp in df_planes.groupby("Proximidad_Disciplina_CC2020"):
    ax.scatter(grp["Coordenada_X"], grp["Coordenada_Y"],
               color=colors.get(disc, "#475569"), label=f"{disc} — Planes de estudio oficiales (n={len(grp)})",
               s=78, alpha=0.90, edgecolors="white", linewidths=1.1, zorder=6)

# Bloque 1: Perfiles de egreso (Diamantes ámbar)
df_perfiles = df[df["Bloque_Num"] == 1]
ax.scatter(df_perfiles["Coordenada_X"], df_perfiles["Coordenada_Y"],
           color="#f59e0b", marker="D", s=88, alpha=0.94, edgecolors="#78350f", linewidths=1.2,
           label=f"Perfiles de egreso D001–D015 (n={len(df_perfiles)})", zorder=7)

# 8. Anotaciones de Instituciones Emblemáticas con offsets no superpuestos
ANOTACIONES = {
    "D001": ("IPN ESCOM", (32, -22)),
    "D031": ("UNAM", (-46, -38)),
    "D032": ("PUCP", (36, -24)),
    "D033": ("U. de Chile", (-52, 24)),
    "D034": ("TecNM", (-44, -18)),
    "D041": ("UBA", (-46, 26)),
    "D042": ("PUC Chile", (-54, 8)),
    "D045": ("ITESM", (36, -32)),
    "D046": ("UdelaR", (32, -20)),
    "D047": ("UNSA", (34, 20)),
    "D049": ("UIS", (34, 18)),
    "D050": ("UANL", (-52, 14)),
    "D054": ("UNMSM", (32, 24)),
    "D056": ("UNR", (-48, -4)),
    "D057": ("UTFSM", (-48, 28)),
    "D058": ("UASLP", (-44, -34)),
    "D061": ("USP", (-54, -22)),
    "D062": ("UNICAMP", (-46, -26)),
    "D063": ("UdeA", (-44, 22)),
    "D064": ("UNC FAMAF", (-52, -2)),
    "D066": ("TEC Costa Rica", (34, 14)),
    "D073": ("UADY", (34, -22)),
    "D075": ("UCR Empresarial", (36, 22)),
}

for doc_id, (label_txt, offset) in ANOTACIONES.items():
    match = df[df["ID"] == doc_id]
    if not match.empty:
        row = match.iloc[0]
        ax.annotate(f"{row['ID']}: {label_txt}", xy=(row["Coordenada_X"], row["Coordenada_Y"]),
                    xytext=offset, textcoords="offset points", ha="center", va="center", fontsize=8.2,
                    fontweight="bold", color="#0f172a",
                    arrowprops=dict(arrowstyle="-", color="#475569", lw=0.7),
                    bbox=dict(facecolor="white", edgecolor="#cbd5e1", alpha=0.94, pad=1.6, boxstyle="round,pad=0.22"),
                    zorder=8)

# 9. Ubicación de la leyenda en Cuadrante IV (inferior derecho, sin colisiones)
handles, labels = ax.get_legend_handles_labels()
# Reordenar leyenda para colocar regresión y mancha primero, luego disciplinas
leg = ax.legend(loc="lower right", bbox_to_anchor=(0.98, 0.04), frameon=True,
                facecolor="white", edgecolor="#94a3b8", framealpha=0.95,
                fontsize=8.5, title="Componentes y Disciplinas CC2020", title_fontsize=9.5)
leg.get_title().set_fontweight("bold")

# 10. Ejes, Títulos y Subtítulos
ax.set_xlabel("Theory, Principles, Innovation  <-  X  ->  Application, Deployment, Configuration",
              fontsize=11, fontweight="bold", labelpad=16, color="#0f172a")
ax.set_ylabel("Computer Hardware and Architecture  <-  Y  ->  Organizational Issues and Information Systems",
              fontsize=11, fontweight="bold", labelpad=16, color="#0f172a")
ax.set_title("Corpus CC2020 Completo (75 Documentos, D001–D075)\n"
             "Delimitación de la Mancha Curricular (KDE 2D) y Regresión No Lineal",
             fontsize=13, fontweight="bold", pad=20, color="#0f172a")

fig.text(0.5, 0.025,
         "Mancha sombreada: densidad multivariada bivariada 2D (KDE). Isolíneas azules: niveles de delimitación de la mancha (0.07, 0.28, 0.60).\n"
         "Línea roja continua: regresión no lineal no paramétrica Nadaraya-Watson con banda de dispersión local (±1σ condicional).\n"
         "Los perfiles de egreso (Bloque 1) declaran competencias profesionales orientadas a la aplicación (X ≈ +5), mientras que los planes de estudio oficiales (Bloques 2-5)\n"
         "reflejan la distribución de créditos reales concentrados en ciencias básicas, algoritmia y sistemas de software.",
         ha="center", fontsize=8.5, color="#334155")

fig.subplots_adjust(bottom=0.15, left=0.12, right=0.96, top=0.90)
output_img = BASE / "corpus_CC2020_master_mancha_regresion.png"
fig.savefig(str(output_img), dpi=220)
plt.close(fig)
print("Gráfico maestro refinado guardado exitosamente:", output_img)
