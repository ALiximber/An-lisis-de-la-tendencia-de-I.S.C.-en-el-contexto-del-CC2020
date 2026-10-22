# VALIDACIÓN ESTADÍSTICA, ANÁLISIS DE SENSIBILIDAD Y AUDITORÍA EMPÍRICA (`VALIDACION_ESTADISTICA.md`)

## 1. Separación Estadística de Poblaciones Documentales (Fase 7 y 8)

El primer requisito de validez estadística es no mezclar poblaciones cuyas unidades de observación miden constructos distintos:
- **Población A (`D001`–`D015`, $n = 15$ Perfiles de Egreso):** Basada en proposiciones competenciales declarativas ($\bar{X} = +3.90, s_X = 0.85$; $\bar{Y} = +0.82, s_Y = 1.44$). Dentro de esta población no existe asociación entre $X$ e $Y$ ($r = -0.0214, p_{\text{perm}} = 0.9396$; $\rho_S = -0.0218, p_{\text{perm}} = 0.9283$).
- **Población B (`D016`–`D075`, $n = 60$ Planes de Estudio):** Basada en mallas curriculares ponderadas por créditos u horas ($\bar{X}_{\text{global}} = -0.19, s_X = 1.24$; $\bar{Y} = +0.10, s_Y = 0.80$).

En el script original (`visualizar_corpus_completo.py`), mezclar ambas poblaciones ($N = 75$) producía dos distorsiones:
1. Extendía la curva de regresión Nadaraya–Watson hasta $X = +5.00$, pese a que en el intervalo $[+3.16, +5.00]$ hay **cero planes de estudio** ($N_{\text{eff}}(x) = 0$ para planes).
2. Alteraba la pendiente y la forma funcional de la relación entre $X$ e $Y$ al unir un conglomerado de planes centrado en $(-0.19, +0.10)$ con un conglomerado de perfiles declarativos centrado en $(+3.90, +0.82)$.

En el código corregido ([`src/estadistica.py`](file:///c:/Users/Aliximber/Desktop/DOCUMENTOS/corpus_CC2020/src/estadistica.py) y [`src/visualizaciones.py`](file:///c:/Users/Aliximber/Desktop/DOCUMENTOS/corpus_CC2020/src/visualizaciones.py)), todos los modelos inferenciales (KDE, Nadaraya–Watson, OLS, PCA y Kruskal–Wallis) se estiman estrictamente por separado para la población de planes de estudio ($n = 60$ y $n = 59$ sin `D032`).

---

## 2. Auditoría de la Estimación de Densidad Kernel 2D (KDE) y Regiones HDR

Se evaluó el estimador de densidad kernel gaussiano bidimensional:
$$\hat{f}(x, y) = \frac{1}{n \cdot 2\pi h_X h_Y} \sum_{i=1}^{n} \exp\!\left[-\frac{1}{2}\left(\frac{x - X_i}{h_X}\right)^2 - \frac{1}{2}\left(\frac{y - Y_i}{h_Y}\right)^2\right]$$

### 2.1. Sensibilidad al ancho de banda y efectos de borde
Se compararon tres criterios de selección de ancho de banda sobre los 60 planes de estudio:

| Criterio de Ancho de Banda | $h_X$ | $h_Y$ | Pico de Densidad $\hat{f}_{\max}$ | Umbral HDR 50% | Umbral HDR 80% | Umbral HDR 95% | Masa dentro de $[-5, +5]^2$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Regla de Scott** ($n^{-1/6} s_j$) | $0.6149$ | $0.3979$ | $0.19784$ | $0.07514$ | $0.02614$ | $0.00866$ | $100.00\%$ ($1.0000$) |
| **Regla de Silverman** (robusta por IQR) | $0.5226$ | $0.3500$ | $0.22375$ | $0.08067$ | $0.02818$ | $0.00993$ | $100.00\%$ ($1.0000$) |
| **Ancho Fijo Original** (`1.05, 1.05`) | $1.0500$ | $1.0500$ | $0.08417$ | $0.03966$ | $0.01511$ | $0.00406$ | $99.82\%$ ($0.9982$) |

**Hallazgos sobre KDE:**
1. **Ausencia de sesgo de truncamiento en bordes para planes de estudio:** Debido a que los 60 planes se concentran en $X \in [-2.92, +3.15]$ e $Y \in [-1.81, +1.80]$, el $100.0\%$ de la masa de probabilidad bajo las reglas de Scott y Silverman queda contenida en el interior del dominio $[-5, +5]^2$. En cambio, en los 15 perfiles de egreso (donde 6 documentos colapsan en $X = +5.00$), el kernel gaussiano no acotado derrama masa más allá de $X > +5.00$.
2. **Sustitución de fracciones arbitrarias del pico por Regiones de Alta Densidad (HDR):** El script original trazaba isolíneas a alturas fijas `0.07, 0.28, 0.60 * Z.max()`. Dichas alturas son relativas al máximo puntual y no informan qué proporción de programas queda encerrada. En [`src/estadistica.py`](file:///c:/Users/Aliximber/Desktop/DOCUMENTOS/corpus_CC2020/src/estadistica.py), `kde_2d_hdr()` integra numéricamente la grilla ordenada para obtener exactamente las **Regiones de Alta Densidad (HDR) que contienen el 50%, 80% y 95% de la masa de probabilidad acumulada**.

---

## 3. Auditoría de la Regresión Nadaraya–Watson y Comparación con Modelos Paramétricos

### 3.1. Pruebas de correlación y modelos paramétricos (OLS lineal vs. Cuadrático)
Se ejecutaron pruebas exactas por permutación Monte Carlo ($10,000$ permutaciones con semilla fija `2020`) e intervalos de confianza bootstrap al 95% ($2,000$ réplicas) en cinco subconjuntos:

| Subconjunto Analizado | $n$ | Pearson $r$ | IC 95% Bootstrap ($r$) | $p$-valor (Perm.) | Spearman $\rho_S$ | $p$-valor ($\rho_S$) | Pendiente OLS $\beta_1$ | $R^2$ OLS | MSE LOOCV (OLS) | MSE LOOCV (Cuadrático) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Planes de Estudio (Global con STEM)** | $60$ | **$+0.5345$** | $[+0.280, +0.718]$ | **$0.0001$** | **$+0.4479$** | **$0.0003$** | $+0.3459$ | $0.2857$ | $0.4659$ | $0.4584$ |
| **Planes de Estudio (Solo Computación, sin STEM)** | $60$ | **$+0.5117$** | $[+0.295, +0.685]$ | **$0.0002$** | **$+0.5070$** | **$0.0001$** | $+0.3768$ | $0.2619$ | $0.4861$ | $0.4784$ |
| **Planes sin `D032` PUCP (Global con STEM)** | $59$ | **$+0.4841$** | $[+0.224, +0.681]$ | **$0.0002$** | **$+0.4194$** | **$0.0018$** | $+0.3217$ | $0.2343$ | $0.4688$ | $0.4690$ |
| **Planes sin `D032` PUCP (Solo Computación)** | $59$ | **$+0.4780$** | $[+0.250, +0.663]$ | **$0.0001$** | **$+0.4817$** | **$0.0001$** | $+0.3472$ | $0.2285$ | $0.4751$ | $0.4769$ |
| **Submuestra Mallas Completas (`D016`–`D038` sin `D032`)** | $22$ | $+0.3385$ | $[-0.090, +0.730]$ | $0.1209$ | $+0.3461$ | $0.1114$ | $+0.2412$ | $0.1146$ | $0.5633$ | $0.5483$ |
| **Perfiles de Egreso (`D001`–`D015`)** | $15$ | $-0.0214$ | $[-0.481, +0.354]$ | $0.9396$ | $-0.0218$ | $0.9283$ | $-0.0364$ | $0.0005$ | $1.7002$ | $16.9550$ |

### 3.2. Selección de ancho de banda por LOOCV para Nadaraya–Watson
Al evaluar el error cuadrático medio de validación cruzada dejando uno fuera ($\text{MSE}_{\text{LOOCV}}$) sobre una grilla $h \in [0.40, 2.00]$:
- En los **60 planes de estudio**, el óptimo es **$h_{\text{LOOCV}}^* = 0.65$** con $\text{MSE}_{\text{LOOCV}} = 0.4665$ y $R^2_{\text{in-sample}} = 0.3123$ (frente a $\text{MSE}_{\text{LOOCV}} = 0.4803$ para el valor arbitrario original $h = 0.95$).
- En los **59 planes (excluyendo `D032` PUCP)**, el óptimo es **$h_{\text{LOOCV}}^* = 0.60$** con $\text{MSE}_{\text{LOOCV}} = 0.4790$ y $R^2_{\text{in-sample}} = 0.2560$.
- **Comparación crítica de modelos (OLS vs. Nadaraya–Watson):** El error de predicción fuera de muestra del modelo lineal simple ($\text{MSE}_{\text{LOOCV, OLS}} = 0.4659$ en $n=60$ y $0.4688$ en $n=59$) es virtualmente idéntico (e incluso ligeramente inferior en $n=59$) al de Nadaraya–Watson ($0.4665$ y $0.4790$). Esto demuestra que **la tendencia principal dentro de los planes de estudio es predominantemente monótona y cuasi-lineal** ($\hat{Y} \approx 0.16 + 0.35 X$), sin evidencia estadística de inflexiones no lineales complejas. La utilidad de Nadaraya–Watson es descriptiva (visualizar la estabilización local en el centroide), siempre que se acompañe de su banda de confianza bootstrap al 95% y se restrinja al dominio donde el tamaño muestral efectivo cumple $N_{\text{eff}}(x) = \frac{(\sum K_h)^2}{\sum K_h^2} \ge 2.5$ ($X \in [-2.35, +2.50]$).

### 3.3. Origen estructural y empírico de la correlación positiva entre $X$ e $Y$
La correlación positiva observada en los planes de estudio ($r = +0.5345$, o $r = +0.4841$ sin `D032`) responde a dos factores combinados que deben transparentarse científicamente:
1. **Acoplamiento en la matriz de codificación:** En el diseño curricular y en el libro de códigos, la mayoría de las asignaturas de Hardware (`R07`, `R09`: Circuitos, Física de Semiconductores, Arquitectura de Computadores) poseen naturaleza teórica ($X = -5, Y = -5$), mientras que casi todas las asignaturas Organizacionales (`R17`, `R18`, `R26`: Sistemas de Información, Gestión de Proyectos, Administración y Finanzas) poseen naturaleza aplicada ($X = +5, Y = +5$).
2. **Asimetría empírica de la oferta universitaria latinoamericana:** Existen numerosos programas en el Cuadrante III ($X < 0, Y < 0$: Ingeniería en Computación con fuerte carga de ciencias básicas y hardware) y en el Cuadrante I ($X > 0, Y > 0$: Ingeniería de Sistemas / Informática Empresarial orientada a gestión y software aplicado), pero **casi ningún programa universitario de grado se ubica en el Cuadrante IV profundo ($X > +1.5, Y < -1.0$: hardware puramente aplicado sin base matemática/física)** ni en el Cuadrante II profundo ($X < -1.5, Y > +1.0$: teoría organizacional pura).

---

## 4. Diferencias por Familia de Denominación y por País (Pruebas de Kruskal–Wallis)

### 4.1. Por familia de denominación del título ($n = 60$ planes)
La prueba no paramétrica de Kruskal–Wallis con $5,000$ permutaciones confirma **diferencias altamente significativas tanto en el Eje $X$ ($H = 13.2876, p = 0.0070$) como en el Eje $Y$ ($H = 19.3066, p = 0.0004$)**:

| Familia de Denominación | $n$ | Media $X$ (DE) | Mediana $X$ (IQR) | Media $Y$ (DE) | Mediana $Y$ (IQR) | Perfil Curricular Dominante |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Ing. de Software / Tecnologías de la Información (`ISW/TI`)** | $6$ | $+1.15$ ($1.61$) | $+1.53$ ($1.88$) | $+0.54$ ($1.07$) | $+0.61$ ($1.53$) | Fuertemente aplicado (`SE`/`IT`/`IS`), menor tronco físico-matemático. |
| **Ing. en Sistemas Computacionales (`ISC`)** | $8$ | $+0.66$ ($0.93$) | $+0.34$ ($0.88$) | $+0.21$ ($0.59$) | $+0.04$ ($0.62$) | Equilibrado-aplicado en $X$ y neutro en $Y$ (combina hardware, software y gestión). |
| **Ing. / Lic. en Informática (`II`)** | $8$ | $-0.23$ ($1.41$) | $-0.59$ ($0.72$) | $+0.29$ ($0.70$) | $+0.16$ ($0.35$) | Ligera inclinación teórico-software con orientación organizacional moderada. |
| **Ing. de Sistemas (`IS`)** | $23$ | $-0.35$ ($0.93$) | $-0.33$ ($1.08$) | $+0.39$ ($0.53$) | $+0.37$ ($0.48$) | Tronco `STEM` robusto en $X$, pero claramente desplazado hacia Organización (`+0.39`) en $Y$. |
| **Ciencias de la Computación / Ing. en Computación (`IC/CC`)** | $15$ | $-0.79$ ($0.96$) | $-0.87$ ($1.25$) | $-0.65$ ($0.70$) | $-0.52$ ($0.84$) | Ubicado en el Cuadrante III: alta carga teórica/algorítmica y de arquitectura de hardware. |

### 4.2. Por país (para los 7 países con $n \ge 3$ planes de estudio, $N = 50$)
Se observan diferencias estadísticamente significativas entre sistemas universitarios nacionales en el **Eje $X$ ($H = 13.2329, p = 0.0262$)** y en el **Eje $Y$ ($H = 14.0287, p = 0.0184$)**:
- **Chile ($n=5$: $\bar{X} = -0.88$, mediana $-0.83$), Argentina ($n=8$: $\bar{X} = -0.67$, mediana $-0.55$) y Colombia ($n=11$: $\bar{X} = -0.59$, mediana $-0.75$)** presentan los planes de estudio con mayor peso relativo de ciencias básicas y fundamentos teóricos (debido a los ciclos de *Plan Común de Ingeniería* en Chile y de *Ciencias Básicas* en Argentina y Colombia).
- **México ($n=13$: $\bar{X} = +0.10, \bar{Y} = -0.33$)** destaca por ser el único país grande con media negativa en el Eje $Y$ ($\bar{Y} = -0.33$, mediana $-0.39$), reflejando la fuerte tradición de electrónica, sistemas digitales, arquitectura de computadoras e interfaces en los programas mexicanos de *Ingeniería en Computación* e *Ingeniería en Sistemas Computacionales* (UNAM, IPN-ESCOM, UAM, UASLP, UdeG, TecNM).
- **Perú ($n=7$: $\bar{X} = +0.70, \bar{Y} = +0.74$) y Colombia ($n=11$: $\bar{Y} = +0.49$)** muestran la mayor orientación hacia el polo organizacional y de sistemas de información empresarial en el Eje $Y$.

---

## 5. Validación Empírica (`n = 120`) y Análisis de Sensibilidad (`S0`–`S5`)

### 5.1. Auditoría sobre el universo de 2,109 asignaturas y muestra estratificada (`n = 120`)
- Al contrastar la clasificación original contra el libro de códigos corregido ([`CODEBOOK_CC2020.md`](file:///c:/Users/Aliximber/Desktop/DOCUMENTOS/CODEBOOK_CC2020.md)) sobre las **2,109 asignaturas** de los Bloques 2 a 5:
  - **2,007 asignaturas ($95.16\%$)** mantienen su asignación polar intacta.
  - **102 asignaturas ($4.84\%$)** cambiaron de codificación: **72 asignaturas ($3.41\%$)** correspondían a errores de colisión léxica o exclusión/inclusión indebida en los scripts originales (p. ej., `Fundamentos de Infraestructura Tecnológica`, `Física de los Sistemas de Información`, `Cálculo Avanzado y Aplicaciones`, `Arquitectura y Organización de Computadores`, `Modelado y Automatización de Procesos Empresariales`, y las 12 electivas de catálogo de `D023`), y **30 asignaturas ($1.42\%$)** corresponden al refinamiento híbrido ($0.5/0.5$).
- La muestra estratificada de **120 asignaturas** exportada en [`corpus_CC2020/auditoria_muestra_estratificada.csv`](file:///c:/Users/Aliximber/Desktop/DOCUMENTOS/corpus_CC2020/auditoria_muestra_estratificada.csv) documenta línea por línea el diagnóstico de auditoría de cada caso.

### 5.2. Estabilidad ante los 6 escenarios del Análisis de Sensibilidad
El archivo [`corpus_CC2020/analisis_sensibilidad.csv`](file:///c:/Users/Aliximber/Desktop/DOCUMENTOS/corpus_CC2020/analisis_sensibilidad.csv) evalúa las coordenadas de los 60 planes de estudio bajo 6 configuraciones metodológicas:

| Comparación de Escenarios | $\text{MAE}_X$ | $\text{MAE}_Y$ | Distancia 2D Media | Distancia 2D Máxima | Correlación $r(X_a, X_b)$ | Correlación $r(Y_a, Y_b)$ | Correlación Interna $r(X_b, Y_b)$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **S0 (Original) vs. S1 (Corregido Estándar)** | $0.195$ | $0.108$ | $0.249$ | $1.132$ (`D029`) | $0.9769$ | $0.9639$ | $+0.5345$ |
| **S1 (Ponderado por Créditos/Horas) vs. S2 (Pesos Uniformes $w_i=1$)** | $0.113$ | $0.074$ | $0.154$ | $0.491$ | $0.9923$ | $0.9934$ | $+0.5579$ |
| **S1 (Estándar) vs. S3 (Incluyendo Electivas de Catálogo)** | $0.006$ | $0.002$ | $0.006$ | $0.345$ (`D023`) | $0.9994$ | $0.9999$ | $+0.5404$ |
| **S1 (Con Híbridos $0.5/0.5$) vs. S4 (Discreto Puro $\pm 5$)** | $0.084$ | $0.025$ | $0.092$ | $0.490$ | $0.9947$ | $0.9971$ | $+0.5127$ |
| **S1 (Global con STEM) vs. S5 (Solo Computación sin STEM)** | $1.880$ | $0.000$ | $1.880$ | $3.610$ | $0.8428$ | $1.0000$ | $+0.5117$ |

**Conclusiones del análisis de sensibilidad:**
1. Las coordenadas son **extraordinariamente robustas al sistema de créditos/horas** ($r > 0.992$ entre S1 ponderado y S2 sin ponderar, con una estabilidad del **$93.33\%$** en la clasificación de afinidad disciplinaria) y **robustas a la discretización de asignaturas híbridas** ($r > 0.994$ entre S1 y S4).
2. La variable estructural de mayor impacto sobre el eje horizontal es la **inclusión o exclusión del tronco general de ciencias básicas `STEM`** (Escenario S5 vs. S1: desplazamiento medio de $+1.88$ unidades hacia el polo aplicado), razón por la cual esta investigación reporta ambas métricas ($X_{\text{global}}$ y $X_{\text{comp}}$) de manera conjunta.
