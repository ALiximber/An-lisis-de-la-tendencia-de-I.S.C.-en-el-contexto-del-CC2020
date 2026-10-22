"""Módulo de auditoría y modelado estadístico (Fase 8):
- KDE bidimensional con regiones de alta densidad acumulada (HDR 50%, 80%, 95%) y reglas de Scott/Silverman.
- Regresión kernel de Nadaraya-Watson con validación cruzada LOOCV, tamaño muestral efectivo N_eff(x)
  e intervalos de confianza bootstrap al 95% para la media condicional.
- Pruebas paramétricas y no paramétricas (permutación exacta/Monte Carlo para Pearson r, Spearman rho,
  comparación OLS vs cuadrática vs NW, y diferencias por familia de denominación y país).
"""
from __future__ import annotations
import math
from typing import Dict, List, Any, Tuple
import numpy as np


def kde_2d_hdr(
    xs: np.ndarray,
    ys: np.ndarray,
    grid_lim: Tuple[float, float] = (-5.0, 5.0),
    grid_size: int = 200,
    bandwidth: Tuple[float, float] | str = "scott",
    probs: Tuple[float, ...] = (0.50, 0.80, 0.95),
) -> Dict[str, Any]:
    """Calcula KDE 2D gaussiano y obtiene tanto los umbrales de probabilidad acumulada
    (Highest Density Regions, HDR) como las alturas relativas al pico máximo."""
    n = len(xs)
    sx = float(np.std(xs, ddof=1)) if n > 1 else 1.0
    sy = float(np.std(ys, ddof=1)) if n > 1 else 1.0

    if bandwidth == "scott":
        factor = n ** (-1.0 / 6.0)
        hx, hy = max(0.35, sx * factor), max(0.35, sy * factor)
    elif bandwidth == "silverman":
        iqr_x = float(np.percentile(xs, 75) - np.percentile(xs, 25)) / 1.349
        iqr_y = float(np.percentile(ys, 75) - np.percentile(ys, 25)) / 1.349
        sig_x = min(sx, iqr_x) if iqr_x > 0 else sx
        sig_y = min(sy, iqr_y) if iqr_y > 0 else sy
        factor = n ** (-1.0 / 6.0)
        hx, hy = max(0.35, sig_x * factor), max(0.35, sig_y * factor)
    elif isinstance(bandwidth, tuple):
        hx, hy = float(bandwidth[0]), float(bandwidth[1])
    else:
        raise ValueError(f"Bandwidth desconocido: {bandwidth}")

    gx = np.linspace(grid_lim[0], grid_lim[1], grid_size)
    gy = np.linspace(grid_lim[0], grid_lim[1], grid_size)
    XX, YY = np.meshgrid(gx, gy)

    dx = (XX[:, :, None] - xs[None, None, :]) / hx
    dy = (YY[:, :, None] - ys[None, None, :]) / hy
    Z = np.exp(-0.5 * (dx * dx + dy * dy)).sum(axis=2) / (
        n * 2.0 * math.pi * hx * hy
    )

    # Cálculo de umbrales HDR que encierran exactamente el p% de la masa de probabilidad en la grilla
    flat_z = np.sort(Z.ravel())[::-1]
    cum_mass = np.cumsum(flat_z)
    total_mass = float(cum_mass[-1]) if len(cum_mass) > 0 else 1.0
    cum_prob = cum_mass / total_mass

    hdr_thresholds: Dict[float, float] = {}
    for p in probs:
        idx = int(np.searchsorted(cum_prob, p))
        idx = min(idx, len(flat_z) - 1)
        hdr_thresholds[p] = float(flat_z[idx])

    # Fracción de masa de probabilidad que realmente queda dentro del cuadrado [-5, 5]^2
    cell_area = ((grid_lim[1] - grid_lim[0]) / (grid_size - 1)) ** 2
    mass_inside_box = float(Z.sum() * cell_area)

    return {
        "XX": XX,
        "YY": YY,
        "Z": Z,
        "hx": round(hx, 4),
        "hy": round(hy, 4),
        "z_max": float(Z.max()),
        "hdr_thresholds": hdr_thresholds,
        "mass_inside_box": round(min(1.0, mass_inside_box), 4),
    }


def nadaraya_watson_loocv(
    xs: np.ndarray,
    ys: np.ndarray,
    h_grid: np.ndarray | None = None,
) -> Dict[str, Any]:
    """Selecciona el ancho de banda óptimo h para Nadaraya-Watson mediante Leave-One-Out
    Cross-Validation (LOOCV) y reporta la curva de error cuadrático medio."""
    if h_grid is None:
        h_grid = np.linspace(0.40, 2.00, 33)

    n = len(xs)
    diff_mat = xs[:, None] - xs[None, :]
    loocv_mse: List[float] = []

    for h in h_grid:
        W = np.exp(-0.5 * (diff_mat / h) ** 2)
        np.fill_diagonal(W, 0.0)
        row_sums = W.sum(axis=1)
        # Si un punto extremo queda con peso casi nulo, usar el vecino más cercano
        preds = np.zeros(n, dtype=float)
        for i in range(n):
            if row_sums[i] > 1e-12:
                preds[i] = float(np.dot(W[i], ys) / row_sums[i])
            else:
                dists = np.abs(diff_mat[i]).copy()
                dists[i] = np.inf
                preds[i] = float(ys[int(np.argmin(dists))])
        mse = float(np.mean((ys - preds) ** 2))
        loocv_mse.append(mse)

    best_idx = int(np.argmin(loocv_mse))
    return {
        "h_opt": round(float(h_grid[best_idx]), 4),
        "min_loocv_mse": round(float(loocv_mse[best_idx]), 4),
        "h_grid": [round(float(h), 2) for h in h_grid],
        "loocv_mse": [round(float(m), 4) for m in loocv_mse],
    }


def nadaraya_watson_fit(
    xs: np.ndarray,
    ys: np.ndarray,
    h: float,
    x_eval: np.ndarray | None = None,
    n_boot: int = 1000,
    seed: int = 2020,
    min_neff: float = 2.5,
) -> Dict[str, Any]:
    """Ajusta la regresión kernel de Nadaraya-Watson con ancho de banda h, calcula:
    - Media condicional m(x)
    - Desviación estándar condicional sigma(x)
    - Tamaño de muestra efectivo N_eff(x) = (sum w_i)^2 / sum(w_i^2)
    - Banda de confianza bootstrap al 95% [ci_low(x), ci_high(x)] para m(x)."""
    if x_eval is None:
        x_eval = np.linspace(float(xs.min()), float(xs.max()), 200)

    u = (x_eval[:, None] - xs[None, :]) / h
    K = np.exp(-0.5 * u * u)
    sum_K = K.sum(axis=1)
    sum_K2 = (K * K).sum(axis=1)
    neff = np.where(sum_K2 > 1e-12, (sum_K * sum_K) / sum_K2, 0.0)

    W = K / np.where(sum_K[:, None] > 1e-12, sum_K[:, None], 1.0)
    m_hat = W @ ys
    var_hat = (W * ((ys[None, :] - m_hat[:, None]) ** 2)).sum(axis=1)
    sd_hat = np.sqrt(np.maximum(0.0, var_hat))

    # Bootstrap no paramétrico para el intervalo de confianza al 95% de m(x)
    rng = np.random.default_rng(seed)
    n = len(xs)
    boot_curves = np.zeros((n_boot, len(x_eval)), dtype=float)
    for b in range(n_boot):
        idx = rng.integers(0, n, size=n)
        xb = xs[idx]
        yb = ys[idx]
        ub = (x_eval[:, None] - xb[None, :]) / h
        Kb = np.exp(-0.5 * ub * ub)
        sKb = Kb.sum(axis=1)
        Wb = Kb / np.where(sKb[:, None] > 1e-12, sKb[:, None], 1.0)
        boot_curves[b] = Wb @ yb

    ci_low = np.percentile(boot_curves, 2.5, axis=0)
    ci_high = np.percentile(boot_curves, 97.5, axis=0)
    valid_mask = neff >= min_neff

    # R^2 in-sample
    u_in = (xs[:, None] - xs[None, :]) / h
    K_in = np.exp(-0.5 * u_in * u_in)
    W_in = K_in / K_in.sum(axis=1, keepdims=True)
    y_pred_in = W_in @ ys
    ss_res = float(np.sum((ys - y_pred_in) ** 2))
    ss_tot = float(np.sum((ys - np.mean(ys)) ** 2))
    r2_in = 1.0 - ss_res / ss_tot if ss_tot > 0 else 0.0

    return {
        "x_eval": x_eval,
        "m_hat": m_hat,
        "sd_hat": sd_hat,
        "neff": neff,
        "ci_low": ci_low,
        "ci_high": ci_high,
        "valid_mask": valid_mask,
        "h": round(float(h), 4),
        "r2_in_sample": round(r2_in, 4),
    }


def _rankdata(a: np.ndarray) -> np.ndarray:
    """Calcula rangos promedio para empates (equivalente a scipy.stats.rankdata)."""
    n = len(a)
    order = np.argsort(a)
    ranks = np.empty(n, dtype=float)
    i = 0
    while i < n:
        j = i
        while j + 1 < n and a[order[j + 1]] == a[order[i]]:
            j += 1
        avg_rank = 0.5 * (i + j) + 1.0
        for k in range(i, j + 1):
            ranks[order[k]] = avg_rank
        i = j + 1
    return ranks


def correlation_and_regression_tests(
    xs: np.ndarray,
    ys: np.ndarray,
    n_perm: int = 10000,
    seed: int = 2020,
) -> Dict[str, Any]:
    """Ejecuta pruebas de correlación de Pearson y Spearman (con p-valor exacto por permutación
    e IC 95% bootstrap), regresión lineal OLS y regresión cuadrática."""
    n = len(xs)
    rng = np.random.default_rng(seed)

    r_pearson = float(np.corrcoef(xs, ys)[0, 1]) if n > 2 else 0.0
    rx = _rankdata(xs)
    ry = _rankdata(ys)
    r_spearman = float(np.corrcoef(rx, ry)[0, 1]) if n > 2 else 0.0

    # Permutaciones para p-valor bilateral
    perm_r = np.zeros(n_perm, dtype=float)
    perm_rho = np.zeros(n_perm, dtype=float)
    xs_c = xs - xs.mean()
    ys_c = ys - ys.mean()
    denom_r = float(np.sqrt(np.sum(xs_c ** 2) * np.sum(ys_c ** 2)))
    rx_c = rx - rx.mean()
    ry_c = ry - ry.mean()
    denom_rho = float(np.sqrt(np.sum(rx_c ** 2) * np.sum(ry_c ** 2)))

    for i in range(n_perm):
        p_idx = rng.permutation(n)
        perm_r[i] = float(np.dot(xs_c, ys_c[p_idx]) / denom_r) if denom_r > 0 else 0.0
        perm_rho[i] = float(np.dot(rx_c, ry_c[p_idx]) / denom_rho) if denom_rho > 0 else 0.0

    p_pearson = float((np.sum(np.abs(perm_r) >= abs(r_pearson)) + 1) / (n_perm + 1))
    p_spearman = float((np.sum(np.abs(perm_rho) >= abs(r_spearman)) + 1) / (n_perm + 1))

    # Bootstrap IC 95% para Pearson r
    boot_r = np.zeros(2000, dtype=float)
    for b in range(2000):
        b_idx = rng.integers(0, n, size=n)
        if np.std(xs[b_idx]) > 1e-12 and np.std(ys[b_idx]) > 1e-12:
            boot_r[b] = float(np.corrcoef(xs[b_idx], ys[b_idx])[0, 1])
    r_ci_low, r_ci_high = np.percentile(boot_r, [2.5, 97.5])

    # OLS lineal: Y = b0 + b1 * X
    b1, b0 = np.polyfit(xs, ys, 1)
    y_ols = b0 + b1 * xs
    ss_tot = float(np.sum((ys - ys.mean()) ** 2))
    ss_res_ols = float(np.sum((ys - y_ols) ** 2))
    r2_ols = 1.0 - ss_res_ols / ss_tot if ss_tot > 0 else 0.0

    # LOOCV MSE para OLS lineal y para modelo cuadrático
    loocv_ols = []
    loocv_quad = []
    for i in range(n):
        mask = np.ones(n, dtype=bool)
        mask[i] = False
        c1 = np.polyfit(xs[mask], ys[mask], 1)
        loocv_ols.append((ys[i] - np.polyval(c1, xs[i])) ** 2)
        c2 = np.polyfit(xs[mask], ys[mask], 2)
        loocv_quad.append((ys[i] - np.polyval(c2, xs[i])) ** 2)

    q2, q1, q0 = np.polyfit(xs, ys, 2)
    y_quad = q0 + q1 * xs + q2 * (xs ** 2)
    ss_res_quad = float(np.sum((ys - y_quad) ** 2))
    r2_quad = 1.0 - ss_res_quad / ss_tot if ss_tot > 0 else 0.0

    return {
        "n": n,
        "pearson_r": round(r_pearson, 4),
        "pearson_p_perm": round(p_pearson, 5),
        "pearson_ci95": [round(float(r_ci_low), 4), round(float(r_ci_high), 4)],
        "spearman_rho": round(r_spearman, 4),
        "spearman_p_perm": round(p_spearman, 5),
        "ols_intercept": round(float(b0), 4),
        "ols_slope": round(float(b1), 4),
        "ols_r2": round(r2_ols, 4),
        "ols_loocv_mse": round(float(np.mean(loocv_ols)), 4),
        "quad_coeffs": [round(float(q0), 4), round(float(q1), 4), round(float(q2), 4)],
        "quad_r2": round(r2_quad, 4),
        "quad_loocv_mse": round(float(np.mean(loocv_quad)), 4),
    }


def kruskal_wallis_permutation(
    groups: Dict[str, np.ndarray],
    n_perm: int = 5000,
    seed: int = 2020,
) -> Dict[str, Any]:
    """Ejecuta la prueba no paramétrica de Kruskal-Wallis H con p-valor exacto por permutación
    para evaluar diferencias entre grupos (ej. países o familias de denominación)."""
    valid_groups = {k: v for k, v in groups.items() if len(v) >= 2}
    if len(valid_groups) < 2:
        return {"H": 0.0, "p_perm": 1.0, "k_groups": len(valid_groups)}

    all_vals = np.concatenate(list(valid_groups.values()))
    sizes = [len(v) for v in valid_groups.values()]
    N = len(all_vals)
    ranks = _rankdata(all_vals)

    def _calc_H(r_vec: np.ndarray) -> float:
        idx = 0
        sum_sq = 0.0
        for sz in sizes:
            r_g = r_vec[idx : idx + sz]
            sum_sq += (np.sum(r_g) ** 2) / sz
            idx += sz
        return float((12.0 / (N * (N + 1.0))) * sum_sq - 3.0 * (N + 1.0))

    H_obs = _calc_H(ranks)
    rng = np.random.default_rng(seed)
    count_ge = 0
    for _ in range(n_perm):
        r_perm = rng.permutation(ranks)
        if _calc_H(r_perm) >= H_obs:
            count_ge += 1
    p_val = float((count_ge + 1) / (n_perm + 1))

    summary_groups = {
        k: {
            "n": len(v),
            "mean": round(float(np.mean(v)), 2),
            "sd": round(float(np.std(v, ddof=1)) if len(v) > 1 else 0.0, 2),
            "median": round(float(np.median(v)), 2),
            "iqr": round(float(np.percentile(v, 75) - np.percentile(v, 25)), 2),
        }
        for k, v in valid_groups.items()
    }

    return {
        "H": round(H_obs, 4),
        "p_perm": round(p_val, 5),
        "k_groups": len(valid_groups),
        "N_total": N,
        "groups": summary_groups,
    }


def run_complete_statistical_audit(corpus_data: Dict[str, Any]) -> Dict[str, Any]:
    """Ejecuta toda la batería de pruebas estadísticas requeridas en las Fases 7, 8 y 12."""
    all_docs = corpus_data["all_docs"]
    profile_docs = corpus_data["profile_docs"]
    plan_docs = corpus_data["plan_docs"]
    plan_docs_59 = [r for r in plan_docs if r["ID"] != "D032"]
    plan_docs_completos_22 = [
        r for r in plan_docs if r["Granularidad_Curricular"] == "Malla_Curricular_Completa"
    ]

    # Vectores de coordenadas
    x_all = np.array([r["Coordenada_X"] for r in all_docs], dtype=float)
    y_all = np.array([r["Coordenada_Y"] for r in all_docs], dtype=float)

    x_prof = np.array([r["Coordenada_X"] for r in profile_docs], dtype=float)
    y_prof = np.array([r["Coordenada_Y"] for r in profile_docs], dtype=float)

    x_plan60 = np.array([r["Coordenada_X"] for r in plan_docs], dtype=float)
    y_plan60 = np.array([r["Coordenada_Y"] for r in plan_docs], dtype=float)
    xc_plan60 = np.array([r["X_Computacion"] for r in plan_docs], dtype=float)

    x_plan59 = np.array([r["Coordenada_X"] for r in plan_docs_59], dtype=float)
    y_plan59 = np.array([r["Coordenada_Y"] for r in plan_docs_59], dtype=float)
    xc_plan59 = np.array([r["X_Computacion"] for r in plan_docs_59], dtype=float)

    x_plan22 = np.array([r["Coordenada_X"] for r in plan_docs_completos_22], dtype=float)
    y_plan22 = np.array([r["Coordenada_Y"] for r in plan_docs_completos_22], dtype=float)

    # 1. Correlaciones y modelos paramétricos
    tests_all75 = correlation_and_regression_tests(x_all, y_all)
    tests_prof15 = correlation_and_regression_tests(x_prof, y_prof)
    tests_plan60_glob = correlation_and_regression_tests(x_plan60, y_plan60)
    tests_plan60_comp = correlation_and_regression_tests(xc_plan60, y_plan60)
    tests_plan59_glob = correlation_and_regression_tests(x_plan59, y_plan59)
    tests_plan59_comp = correlation_and_regression_tests(xc_plan59, y_plan59)
    tests_plan22_glob = correlation_and_regression_tests(x_plan22, y_plan22)

    # 2. Selección LOOCV para Nadaraya-Watson en planes (n=60 y n=59)
    nw_loocv_60 = nadaraya_watson_loocv(x_plan60, y_plan60)
    nw_loocv_59 = nadaraya_watson_loocv(x_plan59, y_plan59)
    nw_fit_60_opt = nadaraya_watson_fit(x_plan60, y_plan60, h=nw_loocv_60["h_opt"])
    nw_fit_60_h095 = nadaraya_watson_fit(x_plan60, y_plan60, h=0.95)
    nw_fit_59_opt = nadaraya_watson_fit(x_plan59, y_plan59, h=nw_loocv_59["h_opt"])

    # 3. KDE 2D con Scott, Silverman y ancho fijo original (1.05, 1.05)
    kde_60_scott = kde_2d_hdr(x_plan60, y_plan60, bandwidth="scott")
    kde_60_silverman = kde_2d_hdr(x_plan60, y_plan60, bandwidth="silverman")
    kde_60_fixed = kde_2d_hdr(x_plan60, y_plan60, bandwidth=(1.05, 1.05))
    kde_15_scott = kde_2d_hdr(x_prof, y_prof, bandwidth="scott")

    # 4. Comparación de las dos poblaciones documentales (Perfiles D001-D015 vs Planes D016-D075)
    # y los dos pares institucionales exactos
    d001 = next(r for r in profile_docs if r["ID"] == "D001")
    d017 = next(r for r in plan_docs if r["ID"] == "D017")
    d003 = next(r for r in profile_docs if r["ID"] == "D003")
    d034 = next(r for r in plan_docs if r["ID"] == "D034")

    pares_exactos = [
        {
            "Institucion": "IPN — ESCOM (México)",
            "Programa": "Ingeniería en Sistemas Computacionales (Plan 2020)",
            "ID_Perfil": "D001",
            "ID_Plan": "D017",
            "X_Perfil": d001["Coordenada_X"],
            "Y_Perfil": d001["Coordenada_Y"],
            "X_Plan_Global": d017["Coordenada_X"],
            "X_Plan_Comp": d017["X_Computacion"],
            "Y_Plan": d017["Coordenada_Y"],
            "Delta_X_Perfil_vs_PlanGlobal": round(d001["Coordenada_X"] - d017["Coordenada_X"], 2),
            "Delta_X_Perfil_vs_PlanComp": round(d001["Coordenada_X"] - d017["X_Computacion"], 2),
            "Delta_Y_Perfil_vs_Plan": round(d001["Coordenada_Y"] - d017["Coordenada_Y"], 2),
            "Distancia_Euclidiana_Global": round(
                math.hypot(d001["Coordenada_X"] - d017["Coordenada_X"], d001["Coordenada_Y"] - d017["Coordenada_Y"]), 2
            ),
        },
        {
            "Institucion": "Tecnológico Nacional de México (TecNM)",
            "Programa": "Ingeniería en Sistemas Computacionales (ISIC-2010-224)",
            "ID_Perfil": "D003",
            "ID_Plan": "D034",
            "X_Perfil": d003["Coordenada_X"],
            "Y_Perfil": d003["Coordenada_Y"],
            "X_Plan_Global": d034["Coordenada_X"],
            "X_Plan_Comp": d034["X_Computacion"],
            "Y_Plan": d034["Coordenada_Y"],
            "Delta_X_Perfil_vs_PlanGlobal": round(d003["Coordenada_X"] - d034["Coordenada_X"], 2),
            "Delta_X_Perfil_vs_PlanComp": round(d003["Coordenada_X"] - d034["X_Computacion"], 2),
            "Delta_Y_Perfil_vs_Plan": round(d003["Coordenada_Y"] - d034["Coordenada_Y"], 2),
            "Distancia_Euclidiana_Global": round(
                math.hypot(d003["Coordenada_X"] - d034["Coordenada_X"], d003["Coordenada_Y"] - d034["Coordenada_Y"]), 2
            ),
        },
    ]

    # 5. Pruebas por familia de denominación del programa (en los 60 planes)
    fam_groups_x: Dict[str, List[float]] = {}
    fam_groups_y: Dict[str, List[float]] = {}
    for r in plan_docs:
        fam = r["Familia_Denominacion"]
        fam_groups_x.setdefault(fam, []).append(r["Coordenada_X"])
        fam_groups_y.setdefault(fam, []).append(r["Coordenada_Y"])

    kw_familia_x = kruskal_wallis_permutation({k: np.array(v) for k, v in fam_groups_x.items()})
    kw_familia_y = kruskal_wallis_permutation({k: np.array(v) for k, v in fam_groups_y.items()})

    # 6. Pruebas por país (para países con >= 3 planes de estudio)
    country_groups_x: Dict[str, List[float]] = {}
    country_groups_y: Dict[str, List[float]] = {}
    for r in plan_docs:
        pais = r["Pais"]
        country_groups_x.setdefault(pais, []).append(r["Coordenada_X"])
        country_groups_y.setdefault(pais, []).append(r["Coordenada_Y"])

    kw_pais_x = kruskal_wallis_permutation(
        {k: np.array(v) for k, v in country_groups_x.items() if len(v) >= 3}
    )
    kw_pais_y = kruskal_wallis_permutation(
        {k: np.array(v) for k, v in country_groups_y.items() if len(v) >= 3}
    )

    return {
        "correlaciones": {
            "Mixto_75_Invalido": tests_all75,
            "Perfiles_15": tests_prof15,
            "Planes_60_Global": tests_plan60_glob,
            "Planes_60_Solo_Computacion": tests_plan60_comp,
            "Planes_59_Sin_D032_Global": tests_plan59_glob,
            "Planes_59_Sin_D032_Solo_Computacion": tests_plan59_comp,
            "Planes_22_Malla_Completa": tests_plan22_glob,
        },
        "nadaraya_watson": {
            "loocv_60": nw_loocv_60,
            "loocv_59": nw_loocv_59,
            "fit_60_opt": nw_fit_60_opt,
            "fit_60_h095": nw_fit_60_h095,
            "fit_59_opt": nw_fit_59_opt,
        },
        "kde": {
            "planes_60_scott": {
                "hx": kde_60_scott["hx"],
                "hy": kde_60_scott["hy"],
                "z_max": round(kde_60_scott["z_max"], 5),
                "hdr_thresholds": {str(k): round(v, 5) for k, v in kde_60_scott["hdr_thresholds"].items()},
                "mass_inside_box": kde_60_scott["mass_inside_box"],
            },
            "planes_60_silverman": {
                "hx": kde_60_silverman["hx"],
                "hy": kde_60_silverman["hy"],
                "z_max": round(kde_60_silverman["z_max"], 5),
                "hdr_thresholds": {str(k): round(v, 5) for k, v in kde_60_silverman["hdr_thresholds"].items()},
                "mass_inside_box": kde_60_silverman["mass_inside_box"],
            },
            "planes_60_fixed_105": {
                "hx": kde_60_fixed["hx"],
                "hy": kde_60_fixed["hy"],
                "z_max": round(kde_60_fixed["z_max"], 5),
                "hdr_thresholds": {str(k): round(v, 5) for k, v in kde_60_fixed["hdr_thresholds"].items()},
                "mass_inside_box": kde_60_fixed["mass_inside_box"],
            },
            "_objects": {
                "kde_60_scott": kde_60_scott,
                "kde_60_fixed": kde_60_fixed,
                "kde_15_scott": kde_15_scott,
            },
        },
        "pares_exactos": pares_exactos,
        "kruskal_familia_X": kw_familia_x,
        "kruskal_familia_Y": kw_familia_y,
        "kruskal_pais_X": kw_pais_x,
        "kruskal_pais_Y": kw_pais_y,
    }

