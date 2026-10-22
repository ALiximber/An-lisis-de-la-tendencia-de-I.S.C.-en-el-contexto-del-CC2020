"""Módulo de generación de visualizaciones científicas de calidad de publicación (Fase 11).

Genera tanto las actualizaciones de las gráficas existentes (Bloques 1-5 y gráfica maestra)
como las nuevas figuras analíticas separadas por población, disciplina, país/denominación
y sensibilidad metodológica.
"""
from __future__ import annotations
from pathlib import Path
from typing import Dict, List, Any
import math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse
from matplotlib.lines import Line2D
from matplotlib.colors import LinearSegmentedColormap

from .estadistica import kde_2d_hdr, nadaraya_watson_fit

PALETTE = {
    "CE": "#1f77b4",
    "CS": "#d62728",
    "SE": "#2ca02c",
    "IT": "#ff7f0e",
    "IS": "#9467bd",
    "IS/IT": "#8c564b",
    "SE/IT": "#17becf",
    "SE/IS": "#bcbd22",
    "CS/SE": "#e377c2",
}


def _color_for(af: str) -> str:
    if af in PALETTE:
        return PALETTE[af]
    base = af.split("/")[0].strip()
    return PALETTE.get(base, "#555555")


def _setup_cc2020_axes(ax: plt.Axes, title: str, subtitle: str = "") -> None:
    ax.set_xlim(-5.5, 5.5)
    ax.set_ylim(-5.5, 5.5)
    ax.set_xticks(range(-5, 6))
    ax.set_yticks(range(-5, 6))
    ax.grid(True, linestyle=":", linewidth=0.6, alpha=0.55, color="#888888", zorder=1)
    ax.axhline(0, color="#222222", linewidth=1.2, zorder=2)
    ax.axvline(0, color="#222222", linewidth=1.2, zorder=2)

    quad_kw = dict(fontsize=8.2, color="#555555", alpha=0.80, style="italic")
    ax.text(-5.25, 5.15, "C-II: Teoría + Organizacional\n(Sistemas de Información formales)", va="top", ha="left", **quad_kw)
    ax.text(5.25, 5.15, "C-I: Aplicación + Organizacional\n(IS / Gestión de TI / Procesos)", va="top", ha="right", **quad_kw)
    ax.text(-5.25, -5.15, "C-III: Teoría + Hardware/Sistemas\n(CS / CE / Fundamentos STEM)", va="bottom", ha="left", **quad_kw)
    ax.text(5.25, -5.15, "C-IV: Aplicación + Hardware\n(Sistemas Embebidos / Redes Físicas)", va="bottom", ha="right", **quad_kw)

    ax.set_xlabel(
        "Eje X (Operacionalización): Teoría, Principios y Ciencias Básicas (−5)  ⟷  Aplicación, Despliegue y Práctica (+5)",
        fontsize=9.8,
        fontweight="bold",
        labelpad=7,
    )
    ax.set_ylabel(
        "Eje Y (Operacionalización): Hardware y Arquitectura Física (−5)  ⟷  Organizacional y Sistemas de Información (+5)",
        fontsize=9.8,
        fontweight="bold",
        labelpad=7,
    )
    if subtitle:
        ax.set_title(f"{title}\n{subtitle}", fontsize=11.2, fontweight="bold", pad=10)
    else:
        ax.set_title(title, fontsize=11.5, fontweight="bold", pad=10)
    ax.set_aspect("equal", adjustable="box")


def plot_block_individual(
    base_dir: Path,
    block_num: int,
    rows: List[Dict[str, Any]],
    block_title: str,
) -> Path:
    """Genera la visualización individual de cada bloque (bloque_01..05_distribucion_cc2020.png)
    con coordenadas corregidas y elipses/círculos de dispersión."""
    fig, ax = plt.subplots(figsize=(11, 10), dpi=300)
    is_profile = block_num == 1
    sub = (
        "Población: Perfiles de Egreso Declarativos (n = 15) — Radio = incertidumbre declarativa"
        if is_profile
        else f"Población: Planes de Estudio Oficiales — Bloque {block_num} (n = {len(rows)}) — Círculo = Radio de dispersión interna R"
    )
    _setup_cc2020_axes(ax, block_title, sub)

    xs = np.array([r["Coordenada_X"] for r in rows], dtype=float)
    ys = np.array([r["Coordenada_Y"] for r in rows], dtype=float)

    for r in rows:
        x = r["Coordenada_X"]
        y = r["Coordenada_Y"]
        rad = r["Desviacion_Radio"]
        af = r["Afinidad_CC2020"]
        col = _color_for(af)
        circ_alpha = 0.13 if is_profile else 0.08
        circ_scale = 1.0 if is_profile else 0.25  # Escala visual documentada para legibilidad cuando R~4.8
        circle = Circle(
            (x, y),
            radius=rad * circ_scale,
            facecolor=col,
            edgecolor=col,
            alpha=circ_alpha,
            linewidth=1.0,
            linestyle="--" if not is_profile else "-",
            zorder=3,
        )
        ax.add_patch(circle)
        marker = "^" if is_profile else "o"
        ax.scatter(x, y, s=68, color=col, edgecolor="white", linewidth=0.9, marker=marker, zorder=5)
        ax.annotate(
            f"{r['ID']} ({af})",
            (x, y),
            xytext=(5, 4),
            textcoords="offset points",
            fontsize=7.6,
            fontweight="bold",
            color="#222222",
            zorder=6,
        )

    # Centroide del bloque
    cx, cy = float(xs.mean()), float(ys.mean())
    ax.scatter(cx, cy, s=150, color="#111111", marker="P", edgecolor="gold", linewidth=1.3, zorder=7)
    ax.annotate(
        f"Centroide B{block_num}\n({cx:+.2f}, {cy:+.2f})",
        (cx, cy),
        xytext=(8, -14),
        textcoords="offset points",
        fontsize=8.3,
        fontweight="bold",
        bbox=dict(boxstyle="round,pad=0.25", facecolor="#fff9db", edgecolor="#333333", alpha=0.9),
        zorder=8,
    )

    note_txt = (
        "Nota metodológica: Coordenadas propias inspiradas en el marco conceptual ACM/IEEE-CS CC2020 (no escalas numéricas oficiales de ACM)."
        if is_profile
        else "Nota metodológica: En planes de estudio, R ≈ 4.9 refleja la dispersión intrínseca de asignaturas entre polos (−5 y +5); "
             "los círculos se dibujan a escala 0.25×R para preservar legibilidad."
    )
    fig.text(0.5, 0.012, note_txt, ha="center", fontsize=8.2, color="#444444", style="italic")
    fig.tight_layout(rect=[0.0, 0.03, 1.0, 1.0])

    out_path = base_dir / f"bloque_0{block_num}_distribucion_cc2020.png"
    fig.savefig(out_path, dpi=300)
    plt.close(fig)
    return out_path


def plot_master_corrected(
    base_dir: Path,
    corpus_data: Dict[str, Any],
    stats_data: Dict[str, Any],
) -> Path:
    """Genera la versión corregida y científicamente defendible de `corpus_CC2020_master_mancha_regresion.png`:
    - Separa visual y estadísticamente los 60 Planes de Estudio (KDE HDR 50%, 80%, 95% + Regresión Nadaraya-Watson
      restringida exclusivamente al soporte empírico de planes con N_eff >= 3.0 + IC 95% bootstrap)
      de los 15 Perfiles de Egreso Declarativos (representados con su propio contorno y marcadores distintos).
    """
    plan_docs = corpus_data["plan_docs"]
    profile_docs = corpus_data["profile_docs"]

    x_p = np.array([r["Coordenada_X"] for r in plan_docs], dtype=float)
    y_p = np.array([r["Coordenada_Y"] for r in plan_docs], dtype=float)
    x_prof = np.array([r["Coordenada_X"] for r in profile_docs], dtype=float)
    y_prof = np.array([r["Coordenada_Y"] for r in profile_docs], dtype=float)

    kde_p = stats_data["kde"]["_objects"]["kde_60_scott"]
    nw_p = stats_data["nadaraya_watson"]["fit_60_opt"]
    corr_p60 = stats_data["correlaciones"]["Planes_60_Global"]
    corr_p59 = stats_data["correlaciones"]["Planes_59_Sin_D032_Global"]

    fig, ax = plt.subplots(figsize=(12.5, 11.2), dpi=300)
    _setup_cc2020_axes(
        ax,
        "Mapa Consolidado CC2020 (Auditado): Planes de Estudio (n = 60) vs. Perfiles de Egreso (n = 15)",
        f"KDE 2D (Regla de Scott: hx={kde_p['hx']:.2f}, hy={kde_p['hy']:.2f}) con Regiones HDR (50%, 80%, 95%) y Regresión Kernel LOOCV (h={nw_p['h']:.2f})",
    )

    # 1. Mancha de densidad KDE exclusiva de los 60 planes de estudio
    XX, YY, Z = kde_p["XX"], kde_p["YY"], kde_p["Z"]
    hdr = kde_p["hdr_thresholds"]
    levels_hdr = sorted([hdr[0.95], hdr[0.80], hdr[0.50], kde_p["z_max"] * 1.01])

    cmap_kde = LinearSegmentedColormap.from_list(
        "cc2020_hdr",
        ["#ffffff00", "#d0ebff", "#74c0fc", "#339af0", "#1864ab"],
    )
    Z_masked = np.ma.masked_less(Z, hdr[0.95])
    ax.contourf(
        XX,
        YY,
        Z_masked,
        levels=np.linspace(hdr[0.95], kde_p["z_max"], 24),
        cmap=cmap_kde,
        alpha=0.55,
        zorder=2,
    )
    cs = ax.contour(
        XX,
        YY,
        Z,
        levels=[hdr[0.95], hdr[0.80], hdr[0.50]],
        colors=["#4dabf7", "#1971c2", "#0b4f6c"],
        linewidths=[1.0, 1.35, 1.8],
        linestyles=["--", "-.", "-"],
        zorder=3,
    )
    ax.clabel(
        cs,
        fmt={hdr[0.95]: "HDR 95%", hdr[0.80]: "HDR 80%", hdr[0.50]: "HDR 50%"},
        fontsize=7.8,
        inline=True,
    )

    # 2. Contorno de los 15 perfiles de egreso (en tono ámbar/naranja discontinuo, sin mezclarlo con planes)
    kde_prof = stats_data["kde"]["_objects"]["kde_15_scott"]
    hdr_prof = kde_prof["hdr_thresholds"]
    ax.contour(
        kde_prof["XX"],
        kde_prof["YY"],
        kde_prof["Z"],
        levels=[hdr_prof[0.80]],
        colors=["#d9480f"],
        linewidths=[1.4],
        linestyles=[":"],
        zorder=3,
    )

    # 3. Curva Nadaraya-Watson restringida al soporte válido de los 60 planes (N_eff >= 2.5)
    mask = nw_p["valid_mask"]
    xv = nw_p["x_eval"][mask]
    mv = nw_p["m_hat"][mask]
    cil = nw_p["ci_low"][mask]
    cih = nw_p["ci_high"][mask]
    sdv = nw_p["sd_hat"][mask]

    ax.fill_between(
        xv,
        mv - sdv,
        mv + sdv,
        color="#ffe066",
        alpha=0.22,
        zorder=4,
        label="Dispersión condicional Planes ±1σ(x)",
    )
    ax.fill_between(
        xv,
        cil,
        cih,
        color="#f03e3e",
        alpha=0.25,
        zorder=4,
        label="IC 95% Bootstrap media condicional m̂(x)",
    )
    ax.plot(
        xv,
        mv,
        color="#c92a2a",
        linewidth=2.8,
        zorder=6,
        label=f"Nadaraya–Watson Planes (h={nw_p['h']:.2f}, R²={nw_p['r2_in_sample']:.2f})",
    )

    # Recta OLS de referencia sobre los 60 planes
    x_line = np.linspace(float(x_p.min()), float(x_p.max()), 100)
    y_ols = corr_p60["ols_intercept"] + corr_p60["ols_slope"] * x_line
    ax.plot(
        x_line,
        y_ols,
        color="#2b8a3e",
        linestyle="--",
        linewidth=1.8,
        zorder=5,
        label=f"Tendencia lineal OLS Planes (r={corr_p60['pearson_r']:+.2f}, p={corr_p60['pearson_p_perm']:.4f})",
    )

    # 4. Puntos de los 60 planes de estudio (círculos coloreados por afinidad corregida)
    for r in plan_docs:
        col = _color_for(r["Afinidad_CC2020"])
        is_d032 = r["ID"] == "D032"
        ax.scatter(
            r["Coordenada_X"],
            r["Coordenada_Y"],
            s=65 if not is_d032 else 95,
            color=col,
            edgecolor="#111111" if is_d032 else "white",
            linewidth=1.5 if is_d032 else 0.8,
            marker="o",
            zorder=7,
        )
        if is_d032 or r["ID"] in ("D017", "D031", "D033", "D034", "D025", "D050", "D041", "D075"):
            lbl = f"{r['ID']}*" if is_d032 else r["ID"]
            ax.annotate(
                lbl,
                (r["Coordenada_X"], r["Coordenada_Y"]),
                xytext=(4, 4),
                textcoords="offset points",
                fontsize=7.3,
                fontweight="bold",
                color="#111111",
                zorder=8,
            )

    # 5. Puntos de los 15 perfiles de egreso (triángulos con borde oscuro)
    for r in profile_docs:
        col = _color_for(r["Afinidad_CC2020"])
        ax.scatter(
            r["Coordenada_X"],
            r["Coordenada_Y"],
            s=72,
            color=col,
            edgecolor="#222222",
            linewidth=1.1,
            marker="^",
            alpha=0.88,
            zorder=7,
        )
        if r["ID"] in ("D001", "D003", "D002", "D008"):
            ax.annotate(
                r["ID"],
                (r["Coordenada_X"], r["Coordenada_Y"]),
                xytext=(4, 4),
                textcoords="offset points",
                fontsize=7.3,
                color="#5c2b09",
                fontweight="bold",
                zorder=8,
            )

    # Centroides separados de ambas poblaciones
    ax.scatter(x_p.mean(), y_p.mean(), s=175, color="#0b4f6c", marker="P", edgecolor="white", linewidth=1.4, zorder=9)
    ax.scatter(x_prof.mean(), y_prof.mean(), s=175, color="#d9480f", marker="X", edgecolor="white", linewidth=1.4, zorder=9)

    # Leyenda integrada
    legend_handles = [
        Line2D([0], [0], marker="o", color="w", label="Planes de Estudio (D016–D075, n=60)", markerfacecolor="#555", markersize=8),
        Line2D([0], [0], marker="^", color="w", label="Perfiles de Egreso (D001–D015, n=15, discurso)", markerfacecolor="#888", markeredgecolor="#222", markersize=8),
        Line2D([0], [0], color="#1f77b4", marker="o", linestyle="None", label="Afinidad CE (Computer Engineering)"),
        Line2D([0], [0], color="#d62728", marker="o", linestyle="None", label="Afinidad CS (Computer Science)"),
        Line2D([0], [0], color="#2ca02c", marker="o", linestyle="None", label="Afinidad SE (Software Engineering)"),
        Line2D([0], [0], color="#ff7f0e", marker="o", linestyle="None", label="Afinidad IT (Information Technology)"),
        Line2D([0], [0], color="#9467bd", marker="o", linestyle="None", label="Afinidad IS (Information Systems)"),
        Line2D([0], [0], color="#c92a2a", lw=2.6, label=f"Regresión NW Planes (h={nw_p['h']:.2f}, soporte N_eff ≥ 2.5)"),
        Line2D([0], [0], color="#2b8a3e", lw=1.8, ls="--", label=f"OLS Planes (r={corr_p60['pearson_r']:+.2f}; sin D032*: r={corr_p59['pearson_r']:+.2f})"),
    ]
    ax.legend(handles=legend_handles, loc="lower left", fontsize=7.8, framealpha=0.93, ncol=2)

    foot = (
        "*Nota: D032 (PUCP) refleja ciclos 5–10 de especialidad (sin Estudios Generales Ciencias ciclos 1–4). "
        "La regresión no se extrapola a X > +2.6 porque en [2.6, 5.0] solo existen Perfiles de Egreso declarativos (D001–D015)."
    )
    fig.text(0.5, 0.01, foot, ha="center", fontsize=8.0, color="#333333", style="italic")
    fig.tight_layout(rect=[0.0, 0.028, 1.0, 1.0])

    out_path = base_dir / "corpus_CC2020_master_mancha_regresion.png"
    fig.savefig(out_path, dpi=300)
    plt.close(fig)
    return out_path


def plot_60_planes_global_vs_comp(
    base_dir: Path,
    corpus_data: Dict[str, Any],
    stats_data: Dict[str, Any],
) -> Path:
    """Figura 2: Análisis exclusivo de los 60 Planes de Estudio comparando:
    Panel A: Coordenada X Global (con ciencias básicas STEM) vs Y.
    Panel B: Coordenada X solo de Computación (excluyendo STEM general) vs Y."""
    plan_docs = corpus_data["plan_docs"]
    xg = np.array([r["Coordenada_X"] for r in plan_docs], dtype=float)
    xc = np.array([r["X_Computacion"] for r in plan_docs], dtype=float)
    y = np.array([r["Coordenada_Y"] for r in plan_docs], dtype=float)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8.6), dpi=300)

    # Panel A: Global (con STEM)
    _setup_cc2020_axes(
        ax1,
        "A. Planes de Estudio (n = 60) — Coordenada X Global (incluye tronco STEM)",
        f"Media X_glob = {xg.mean():+.2f} (DE={xg.std(ddof=1):.2f}), Media Y = {y.mean():+.2f} (DE={y.std(ddof=1):.2f})",
    )
    kde_g = kde_2d_hdr(xg, y, bandwidth="scott")
    hdr_g = kde_g["hdr_thresholds"]
    ax1.contourf(
        kde_g["XX"], kde_g["YY"],
        np.ma.masked_less(kde_g["Z"], hdr_g[0.95]),
        levels=18, cmap="Blues", alpha=0.45, zorder=2
    )
    ax1.contour(
        kde_g["XX"], kde_g["YY"], kde_g["Z"],
        levels=[hdr_g[0.95], hdr_g[0.80], hdr_g[0.50]],
        colors=["#74c0fc", "#228be6", "#1864ab"], linewidths=[0.9, 1.3, 1.7], zorder=3
    )
    nw_g = nadaraya_watson_fit(xg, y, h=stats_data["nadaraya_watson"]["loocv_60"]["h_opt"])
    m_g = nw_g["valid_mask"]
    ax1.fill_between(nw_g["x_eval"][m_g], nw_g["ci_low"][m_g], nw_g["ci_high"][m_g], color="#fa5252", alpha=0.25, zorder=4)
    ax1.plot(nw_g["x_eval"][m_g], nw_g["m_hat"][m_g], color="#c92a2a", lw=2.4, zorder=5, label="Nadaraya–Watson + IC 95%")

    for r in plan_docs:
        ax1.scatter(r["Coordenada_X"], r["Coordenada_Y"], s=58, color=_color_for(r["Afinidad_CC2020"]), edgecolor="white", lw=0.7, zorder=6)
    ax1.scatter(xg.mean(), y.mean(), s=160, color="#111", marker="P", edgecolor="gold", lw=1.3, zorder=8, label=f"Centroide ({xg.mean():+.2f}, {y.mean():+.2f})")
    ax1.legend(loc="lower left", fontsize=8.2)

    # Panel B: Solo Computación (sin STEM básico)
    _setup_cc2020_axes(
        ax2,
        "B. Planes de Estudio (n = 60) — Coordenada X_comp (Núcleo de Computación sin STEM)",
        f"Media X_comp = {xc.mean():+.2f} (DE={xc.std(ddof=1):.2f}) → Desplazamiento medio ΔX_STEM = {(xc - xg).mean():+.2f} hacia Aplicación",
    )
    kde_c = kde_2d_hdr(xc, y, bandwidth="scott")
    hdr_c = kde_c["hdr_thresholds"]
    ax2.contourf(
        kde_c["XX"], kde_c["YY"],
        np.ma.masked_less(kde_c["Z"], hdr_c[0.95]),
        levels=18, cmap="Greens", alpha=0.45, zorder=2
    )
    ax2.contour(
        kde_c["XX"], kde_c["YY"], kde_c["Z"],
        levels=[hdr_c[0.95], hdr_c[0.80], hdr_c[0.50]],
        colors=["#8ce99a", "#40c057", "#2b8a3e"], linewidths=[0.9, 1.3, 1.7], zorder=3
    )
    nw_c = nadaraya_watson_fit(xc, y, h=0.85)
    m_c = nw_c["valid_mask"]
    ax2.fill_between(nw_c["x_eval"][m_c], nw_c["ci_low"][m_c], nw_c["ci_high"][m_c], color="#fa5252", alpha=0.25, zorder=4)
    ax2.plot(nw_c["x_eval"][m_c], nw_c["m_hat"][m_c], color="#c92a2a", lw=2.4, zorder=5, label="Nadaraya–Watson + IC 95%")

    for r in plan_docs:
        ax2.scatter(r["X_Computacion"], r["Coordenada_Y"], s=58, color=_color_for(r["Afinidad_CC2020"]), edgecolor="white", lw=0.7, zorder=6)
    ax2.scatter(xc.mean(), y.mean(), s=160, color="#111", marker="P", edgecolor="gold", lw=1.3, zorder=8, label=f"Centroide ({xc.mean():+.2f}, {y.mean():+.2f})")
    ax2.legend(loc="lower left", fontsize=8.2)

    fig.suptitle(
        "Efecto del Tronco Latinoamericano de Ciencias Básicas (STEM) sobre el Posicionamiento Teórico-Aplicado (Eje X)",
        fontsize=13,
        fontweight="bold",
        y=0.98,
    )
    fig.tight_layout(rect=[0.0, 0.0, 1.0, 0.95])
    out_path = base_dir / "distribucion_60_planes.png"
    fig.savefig(out_path, dpi=300)
    plt.close(fig)
    return out_path


def plot_15_perfiles_vs_pares(
    base_dir: Path,
    corpus_data: Dict[str, Any],
    stats_data: Dict[str, Any],
) -> Path:
    """Figura 3: Separación de poblaciones documentales (Fase 7).
    Contrasta los 15 perfiles de egreso declarativos con los 60 planes de estudio y traza los
    vectores de emparejamiento exacto para IPN-ESCOM (D001 ↔ D017) y TecNM (D003 ↔ D034)."""
    profile_docs = corpus_data["profile_docs"]
    plan_docs = corpus_data["plan_docs"]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8.5), dpi=300)

    # Panel A: Mapa de los 15 perfiles y los 2 pares institucionales exactos
    _setup_cc2020_axes(
        ax1,
        "A. Perfiles de Egreso (D001–D015) y Pares Institucionales Exactos",
        "Comparación directa Perfil Declarativo (▲) vs. Malla Curricular Global (●) y Solo Computación (◆)",
    )
    for r in plan_docs:
        ax1.scatter(r["Coordenada_X"], r["Coordenada_Y"], s=32, color="#ced4da", alpha=0.65, zorder=2)

    for r in profile_docs:
        col = _color_for(r["Afinidad_CC2020"])
        ax1.scatter(r["Coordenada_X"], r["Coordenada_Y"], s=78, color=col, edgecolor="#222", marker="^", lw=1.0, zorder=5)
        ax1.annotate(r["ID"], (r["Coordenada_X"], r["Coordenada_Y"]), xytext=(4, 3), textcoords="offset points", fontsize=7.5, fontweight="bold")

    # Trazar los 2 pares institucionales exactos: D001->D017 (IPN-ESCOM) y D003->D034 (TecNM)
    pairs = [
        ("D001", "D017", "IPN-ESCOM (ISC 2020)", "#d9480f"),
        ("D003", "D034", "TecNM (ISIC-2010-224)", "#1864ab"),
    ]
    plan_map = {r["ID"]: r for r in plan_docs}
    prof_map = {r["ID"]: r for r in profile_docs}

    for id_prof, id_plan, label_p, col_p in pairs:
        pr = prof_map[id_prof]
        pl = plan_map[id_plan]
        # Flecha desde malla global hasta perfil declarativo
        ax1.annotate(
            "",
            xy=(pr["Coordenada_X"], pr["Coordenada_Y"]),
            xytext=(pl["Coordenada_X"], pl["Coordenada_Y"]),
            arrowprops=dict(arrowstyle="->", color=col_p, lw=2.2, ls="-"),
            zorder=7,
        )
        # Punto de malla solo computación
        ax1.scatter(pl["X_Computacion"], pl["Coordenada_Y"], s=95, color=col_p, marker="D", edgecolor="white", lw=1.2, zorder=8)
        ax1.annotate(
            "",
            xy=(pr["Coordenada_X"], pr["Coordenada_Y"]),
            xytext=(pl["X_Computacion"], pl["Coordenada_Y"]),
            arrowprops=dict(arrowstyle="->", color=col_p, lw=1.6, ls="--"),
            zorder=7,
        )
        ax1.scatter(pl["Coordenada_X"], pl["Coordenada_Y"], s=95, color=col_p, marker="o", edgecolor="black", lw=1.3, zorder=8)
        ax1.annotate(
            f"{id_plan} (Global)\n({pl['Coordenada_X']:+.2f}, {pl['Coordenada_Y']:+.2f})",
            (pl["Coordenada_X"], pl["Coordenada_Y"]),
            xytext=(-15, -24),
            textcoords="offset points",
            fontsize=7.6,
            fontweight="bold",
            color=col_p,
            bbox=dict(boxstyle="round,pad=0.2", fc="white", ec=col_p, alpha=0.9),
            zorder=9,
        )
        ax1.annotate(
            f"{id_plan} (Sin STEM)\n({pl['X_Computacion']:+.2f}, {pl['Coordenada_Y']:+.2f})",
            (pl["X_Computacion"], pl["Coordenada_Y"]),
            xytext=(6, -18),
            textcoords="offset points",
            fontsize=7.4,
            color=col_p,
            zorder=9,
        )

    # Panel B: Comparación de distribuciones en X e Y entre las 3 mediciones
    xg_all = [r["Coordenada_X"] for r in plan_docs]
    xc_all = [r["X_Computacion"] for r in plan_docs]
    xp_all = [r["Coordenada_X"] for r in profile_docs]
    yg_all = [r["Coordenada_Y"] for r in plan_docs]
    yp_all = [r["Coordenada_Y"] for r in profile_docs]

    data_box = [xg_all, xc_all, xp_all, yg_all, yp_all]
    labels_box = [
        "Eje X: Planes\n(Global c/ STEM)\n[n=60]",
        "Eje X: Planes\n(Solo Computación)\n[n=60]",
        "Eje X: Perfiles\n(Declarativos)\n[n=15]",
        "Eje Y: Planes\n(Hardware↔Org)\n[n=60]",
        "Eje Y: Perfiles\n(Declarativos)\n[n=15]",
    ]
    colors_box = ["#4dabf7", "#69db7c", "#ffa94d", "#748ffc", "#ff8787"]
    bp = ax2.boxplot(data_box, tick_labels=labels_box, patch_artist=True, widths=0.52, showmeans=True)
    for patch, c in zip(bp["boxes"], colors_box):
        patch.set_facecolor(c)
        patch.set_alpha(0.75)
    ax2.axhline(0, color="#222", lw=1.1, ls="--")
    ax2.set_ylim(-5.2, 5.2)
    ax2.grid(True, axis="y", ls=":", alpha=0.6)
    ax2.set_ylabel("Valor de Coordenada en escala [−5, +5]", fontsize=10, fontweight="bold")
    ax2.set_title(
        "B. Descomposición de la Diferencia entre Perfiles Declarativos y Mallas Curriculares\n"
        "El 44% de la brecha aparente en X se explica por el tronco obligatorio de Ciencias Básicas (STEM)",
        fontsize=10.8,
        fontweight="bold",
    )

    fig.tight_layout()
    out_path = base_dir / "distribucion_15_perfiles_vs_pares.png"
    fig.savefig(out_path, dpi=300)
    plt.close(fig)
    return out_path


def plot_disciplinas_y_pca(
    base_dir: Path,
    corpus_data: Dict[str, Any],
) -> Path:
    """Figura 4: Vectores de competencias en los 6 dominios curriculares (STEM, CE, CS, SE, IT, IS),
    comparación de afinidades (Original vs Regla Corregida vs Similitud Vectorial) y Biplot PCA."""
    plan_docs = corpus_data["plan_docs"]
    pca_info = corpus_data["pca_info"]

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(20, 6.8), dpi=300)

    # Panel A: Cambio en la distribución de afinidades CC2020 (n = 60 planes)
    cats = ["CS", "SE", "IS", "CE", "IT"]
    cnt_orig = [sum(1 for r in plan_docs if r["Afinidad_Original"] == c) for c in cats]
    cnt_regla = [sum(1 for r in plan_docs if r["Afinidad_Regla_Corregida"] == c) for c in cats]
    cnt_vec = [sum(1 for r in plan_docs if r["Afinidad_Vectorial_Principal"] == c) for c in cats]

    x_pos = np.arange(len(cats))
    w = 0.26
    b1 = ax1.bar(x_pos - w, cnt_orig, width=w, label="Original (sesgo STEM + bloqueo IT)", color="#adb5bd", edgecolor="#333")
    b2 = ax1.bar(x_pos, cnt_regla, width=w, label="Regla Corregida (sin sesgo STEM)", color="#339af0", edgecolor="#111")
    b3 = ax1.bar(x_pos + w, cnt_vec, width=w, label="Similitud Coseno Arquetipos CC2020", color="#51cf66", edgecolor="#111")

    for bars in (b1, b2, b3):
        for bar in bars:
            h = bar.get_height()
            ax1.annotate(f"{int(h)}", (bar.get_x() + bar.get_width() / 2, h), xytext=(0, 3), textcoords="offset points", ha="center", fontsize=8.2, fontweight="bold")

    ax1.set_xticks(x_pos)
    ax1.set_xticklabels(cats, fontsize=10, fontweight="bold")
    ax1.set_ylim(0, 46)
    ax1.set_ylabel("Número de Planes de Estudio (de n = 60)", fontsize=9.5, fontweight="bold")
    ax1.set_title("A. Distribución de Afinidad Disciplinaria\nCorrección del sesgo CS y desbloqueo de IT", fontsize=10.5, fontweight="bold")
    ax1.grid(True, axis="y", ls=":", alpha=0.6)
    ax1.legend(fontsize=8.0, loc="upper right")

    # Panel B: Composición curricular promedio por afinidad corregida (6 dominios)
    dom_cols = ["pct_STEM", "pct_CE", "pct_CS", "pct_SE", "pct_IT", "pct_IS"]
    dom_labels = ["STEM Básico", "CE (Hardware)", "CS (Teoría/IA)", "SE (Software)", "IT (Infra/Redes)", "IS (Org/Sistemas)"]
    dom_colors = ["#868e96", "#1f77b4", "#d62728", "#2ca02c", "#ff7f0e", "#9467bd"]

    bottom = np.zeros(len(cats))
    for d_col, d_lbl, d_colr in zip(dom_cols, dom_labels, dom_colors):
        means = []
        for c in cats:
            sub = [r[d_col] for r in plan_docs if r["Afinidad_Regla_Corregida"] == c]
            means.append(float(np.mean(sub)) if sub else 0.0)
        vals = np.array(means)
        ax2.bar(cats, vals, bottom=bottom, label=d_lbl, color=d_colr, edgecolor="white", width=0.58)
        bottom += vals

    ax2.set_ylim(0, 105)
    ax2.set_ylabel("Porcentaje del Peso Curricular Clasificado (%)", fontsize=9.5, fontweight="bold")
    ax2.set_title("B. Perfil Vectorial Medio (6 Dominios)\nsegún Afinidad Disciplinaria Corregida", fontsize=10.5, fontweight="bold")
    ax2.legend(fontsize=7.8, loc="upper right", ncol=2)
    ax2.grid(True, axis="y", ls=":", alpha=0.6)

    # Panel C: Biplot PCA de los 6 dominios curriculares
    var1, var2 = pca_info["Explained_Variance_Ratio"][0], pca_info["Explained_Variance_Ratio"][1]
    for r in plan_docs:
        col = _color_for(r["Afinidad_Regla_Corregida"])
        ax3.scatter(r["PC1"], r["PC2"], s=52, color=col, edgecolor="white", lw=0.7, alpha=0.9, zorder=4)

    loadings = pca_info["Loadings"]
    scale_vec = 3.2
    for d_col, d_lbl in zip(dom_cols, ["STEM", "CE", "CS", "SE", "IT", "IS"]):
        lx = loadings[d_col]["PC1"] * scale_vec
        ly = loadings[d_col]["PC2"] * scale_vec
        ax3.annotate(
            "", xy=(lx, ly), xytext=(0, 0),
            arrowprops=dict(arrowstyle="->", color="#111111", lw=1.6), zorder=6
        )
        ax3.text(lx * 1.12, ly * 1.12, d_lbl, fontsize=8.8, fontweight="bold", ha="center", va="center",
                 bbox=dict(boxstyle="round,pad=0.15", fc="#fff9db", ec="#555", alpha=0.88), zorder=7)

    ax3.axhline(0, color="#444", lw=0.9, ls="--")
    ax3.axvline(0, color="#444", lw=0.9, ls="--")
    ax3.grid(True, ls=":", alpha=0.6)
    ax3.set_xlabel(f"PC1 ({var1:.1f}% var.) — Correlación con Eje X: r = {pca_info['Corr_PC1_X']:+.2f}", fontsize=9.5, fontweight="bold")
    ax3.set_ylabel(f"PC2 ({var2:.1f}% var.) — Correlación con Eje Y: r = {pca_info['Corr_PC2_Y']:+.2f}", fontsize=9.5, fontweight="bold")
    ax3.set_title(
        f"C. Biplot PCA de 6 Dominios ({pca_info['Cumulative_PC1_PC2_Pct']:.1f}% varianza)\n"
        "Valida la fidelidad geométrica del plano bidimensional (X, Y)",
        fontsize=10.5,
        fontweight="bold",
    )

    fig.tight_layout()
    out_path = base_dir / "distribucion_disciplinas_y_vectores.png"
    fig.savefig(out_path, dpi=300)
    plt.close(fig)
    return out_path


def plot_paises_y_denominaciones(
    base_dir: Path,
    corpus_data: Dict[str, Any],
    stats_data: Dict[str, Any],
) -> Path:
    """Figura 5: Distribución por Familia de Denominación del Programa y por País (en los 60 planes)."""
    plan_docs = corpus_data["plan_docs"]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8.2), dpi=300)

    # Panel A: Centroides y elipses DE por Familia de Denominación
    _setup_cc2020_axes(
        ax1,
        "A. Posicionamiento por Familia de Denominación del Programa (n = 60)",
        f"Kruskal–Wallis Eje X: H={stats_data['kruskal_familia_X']['H']:.2f} (p={stats_data['kruskal_familia_X']['p_perm']:.4f}) | "
        f"Eje Y: H={stats_data['kruskal_familia_Y']['H']:.2f} (p={stats_data['kruskal_familia_Y']['p_perm']:.4f})",
    )
    fam_Styles = {
        "ISC_Sistemas_Computacionales": ("Ing. en Sistemas Computacionales (ISC)", "#1f77b4", "o"),
        "IS_Ingenieria_Sistemas": ("Ing. de Sistemas / Sistemas e Info. (IS)", "#9467bd", "s"),
        "IC_Ciencias_Ingenieria_Computacion": ("Ing. en Computación / Ciencias Comp. (IC/CC)", "#d62728", "D"),
        "II_Ingenieria_Informatica": ("Ing. en Informática / Lic. Informática (II)", "#2ca02c", "^"),
        "ISW_TI_Software_Tecnologias": ("Ing. de Software / Tecnologías Info. (ISW/TI)", "#ff7f0e", "P"),
    }

    for fam_key, (fam_label, col, mk) in fam_Styles.items():
        sub = [r for r in plan_docs if r["Familia_Denominacion"] == fam_key]
        if not sub:
            continue
        xs = np.array([r["Coordenada_X"] for r in sub], dtype=float)
        ys = np.array([r["Coordenada_Y"] for r in sub], dtype=float)
        ax1.scatter(xs, ys, s=46, color=col, marker=mk, alpha=0.65, edgecolor="white", lw=0.6, zorder=4)
        mx, my = float(xs.mean()), float(ys.mean())
        sx = float(xs.std(ddof=1)) if len(xs) > 1 else 0.4
        sy = float(ys.std(ddof=1)) if len(ys) > 1 else 0.4
        ell = Ellipse((mx, my), width=2 * sx, height=2 * sy, facecolor=col, edgecolor=col, alpha=0.14, lw=1.4, ls="--", zorder=3)
        ax1.add_patch(ell)
        ax1.scatter(mx, my, s=150, color=col, marker=mk, edgecolor="#111", lw=1.5, zorder=7, label=f"{fam_label} (n={len(sub)}: {mx:+.2f}, {my:+.2f})")

    ax1.legend(loc="lower left", fontsize=7.8, framealpha=0.92)

    # Panel B: Comparación por País (países representados en los 60 planes, ordenados por mediana en Y)
    by_country: Dict[str, List[Dict[str, Any]]] = {}
    for r in plan_docs:
        by_country.setdefault(r["Pais"], []).append(r)

    countries_sorted = sorted(by_country.keys(), key=lambda k: (-len(by_country[k]), k))
    y_pos = np.arange(len(countries_sorted))
    means_x = [float(np.mean([r["Coordenada_X"] for r in by_country[c]])) for c in countries_sorted]
    means_y = [float(np.mean([r["Coordenada_Y"] for r in by_country[c]])) for c in countries_sorted]
    counts = [len(by_country[c]) for c in countries_sorted]

    h_bar = 0.36
    ax2.barh(y_pos - h_bar / 2, means_x, height=h_bar, color="#339af0", edgecolor="#111", label="Media Coordenada X (Teoría − ↔ + Aplicación)")
    ax2.barh(y_pos + h_bar / 2, means_y, height=h_bar, color="#845ef7", edgecolor="#111", label="Media Coordenada Y (Hardware − ↔ + Organizacional)")
    ax2.axvline(0, color="#222", lw=1.1)
    ax2.set_yticks(y_pos)
    ax2.set_yticklabels([f"{c} (n={n})" for c, n in zip(countries_sorted, counts)], fontsize=9.0, fontweight="bold")
    ax2.invert_yaxis()
    ax2.set_xlim(-3.2, 3.2)
    ax2.grid(True, axis="x", ls=":", alpha=0.6)
    ax2.set_xlabel("Coordenada Promedio en escala [−5, +5]", fontsize=9.8, fontweight="bold")
    ax2.set_title(
        f"B. Posicionamiento Medio por País en Planes de Estudio (15 Países, n = 60)\n"
        f"Kruskal–Wallis (países con n≥3): Eje X p={stats_data['kruskal_pais_X']['p_perm']:.3f} | Eje Y p={stats_data['kruskal_pais_Y']['p_perm']:.3f}",
        fontsize=10.5,
        fontweight="bold",
    )
    ax2.legend(loc="lower right", fontsize=8.5)

    fig.tight_layout()
    out_path = base_dir / "distribucion_paises_y_denominaciones.png"
    fig.savefig(out_path, dpi=300)
    plt.close(fig)
    return out_path


def plot_comparacion_original_vs_corregido(
    base_dir: Path,
    corpus_data: Dict[str, Any],
    sens_data: Dict[str, Any],
) -> Path:
    """Figura 6: Vectores de desplazamiento entre el modelo original (S0) y el modelo corregido (S1)
    sobre los 60 planes de estudio, más resumen de estabilidad ante los 6 escenarios de sensibilidad."""
    plan_docs = corpus_data["plan_docs"]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8.4), dpi=300)

    _setup_cc2020_axes(
        ax1,
        "A. Vectores de Corrección Curricular: Original (S0) → Auditado (S1) en Planes (n = 60)",
        "Se etiquetan los programas con desplazamiento > 0.45 unidades por corrección de colisiones léxicas o electivas",
    )
    for r in plan_docs:
        x0, y0 = r["X_Original"], r["Y_Original"]
        x1, y1 = r["Coordenada_X"], r["Coordenada_Y"]
        dist = r["Shift_Distancia"]
        col = _color_for(r["Afinidad_CC2020"])
        ax1.scatter(x0, y0, s=30, color="#adb5bd", edgecolor="#666", lw=0.6, zorder=3)
        ax1.scatter(x1, y1, s=55, color=col, edgecolor="white", lw=0.7, zorder=5)
        if dist >= 0.08:
            ax1.annotate(
                "", xy=(x1, y1), xytext=(x0, y0),
                arrowprops=dict(arrowstyle="->", color="#e03131" if dist >= 0.45 else "#495057", lw=1.5 if dist >= 0.45 else 0.9),
                zorder=4,
            )
        if dist >= 0.45:
            ax1.annotate(
                f"{r['ID']} (Δ={dist:.2f})",
                (x1, y1),
                xytext=(5, 4),
                textcoords="offset points",
                fontsize=7.6,
                fontweight="bold",
                color="#c92a2a",
                zorder=7,
            )

    # Panel B: Comparación de desviación absoluta media (MAE en X, MAE en Y y Distancia 2D) en análisis de sensibilidad
    comps = sens_data["comparisons"]
    labels_c = [
        "S0 Original vs.\nS1 Corregido\n(Errores regex/electivas)",
        "S1 Ponderado vs.\nS2 Pesos Uniformes\n(Créditos vs. w=1)",
        "S1 Estándar vs.\nS3 Con Electivas\n(Efecto catálogo D023)",
        "S1 Híbrido (0.5) vs.\nS4 Discreto Puro\n(Sin pesos 0.5/0.5)",
        "S1 Global vs.\nS5 Solo Computación\n(Excluyendo STEM)",
    ]
    mae_x = [c["MAE_X"] for c in comps]
    mae_y = [c["MAE_Y"] for c in comps]
    dist_2d = [c["Mean_Dist_2D"] for c in comps]

    x_idx = np.arange(len(comps))
    w = 0.25
    b_x = ax2.bar(x_idx - w, mae_x, width=w, label="MAE Eje X", color="#339af0", edgecolor="#111")
    b_y = ax2.bar(x_idx, mae_y, width=w, label="MAE Eje Y", color="#845ef7", edgecolor="#111")
    b_d = ax2.bar(x_idx + w, dist_2d, width=w, label="Distancia Euclidiana Media 2D", color="#ff922b", edgecolor="#111")

    for bars in (b_x, b_y, b_d):
        for bar in bars:
            val = bar.get_height()
            ax2.annotate(f"{val:.2f}", (bar.get_x() + bar.get_width() / 2, val), xytext=(0, 3), textcoords="offset points", ha="center", fontsize=8.0, fontweight="bold")

    ax2.set_xticks(x_idx)
    ax2.set_xticklabels(labels_c, fontsize=8.6, fontweight="bold")
    ax2.set_ylim(0, max(dist_2d) * 1.18)
    ax2.grid(True, axis="y", ls=":", alpha=0.6)
    ax2.set_ylabel("Cambio Absoluto Promedio en unidades de escala [−5, +5]", fontsize=9.6, fontweight="bold")
    ax2.set_title(
        "B. Análisis de Sensibilidad Multiescenario (S0 a S5 sobre n = 60 Planes)\n"
        f"Estabilidad de Afinidad entre Ponderado (S1) y Uniforme (S2): {sens_data['afinidad_stability_S1_vs_S2_pct']:.1f}%",
        fontsize=10.5,
        fontweight="bold",
    )
    ax2.legend(loc="upper left", fontsize=8.5)

    fig.tight_layout()
    out_path = base_dir / "comparacion_original_vs_corregido_sensibilidad.png"
    fig.savefig(out_path, dpi=300)
    plt.close(fig)
    return out_path


def generate_all_visualizations(
    base_dir: Path,
    corpus_data: Dict[str, Any],
    stats_data: Dict[str, Any],
    sens_data: Dict[str, Any],
) -> List[str]:
    """Genera todas las visualizaciones del proyecto y devuelve la lista de rutas creadas."""
    generated: List[str] = []

    block_titles = {
        1: "Mapa de Coordenadas CC2020 — Bloque 1 (D001–D015: Perfiles de Egreso)",
        2: "Mapa de Coordenadas CC2020 — Bloque 2 (D016–D030: Planes de Estudio Oficiales)",
        3: "Mapa de Coordenadas CC2020 — Bloque 3 (D031–D045: Planes de Estudio Oficiales)",
        4: "Mapa de Coordenadas CC2020 — Bloque 4 (D046–D060: Planes de Estudio Oficiales)",
        5: "Mapa de Coordenadas CC2020 — Bloque 5 (D061–D075: Planes de Estudio Oficiales)",
    }

    for b in range(1, 6):
        b_rows = [r for r in corpus_data["all_docs"] if r["Bloque"] == b]
        p = plot_block_individual(base_dir, b, b_rows, block_titles[b])
        generated.append(str(p))

    generated.append(str(plot_master_corrected(base_dir, corpus_data, stats_data)))
    generated.append(str(plot_60_planes_global_vs_comp(base_dir, corpus_data, stats_data)))
    generated.append(str(plot_15_perfiles_vs_pares(base_dir, corpus_data, stats_data)))
    generated.append(str(plot_disciplinas_y_pca(base_dir, corpus_data)))
    generated.append(str(plot_paises_y_denominaciones(base_dir, corpus_data, stats_data)))
    generated.append(str(plot_comparacion_original_vs_corregido(base_dir, corpus_data, sens_data)))

    return generated

