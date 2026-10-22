# METODOLOGÍA CIENTÍFICA Y OPERACIONALIZACIÓN CURRICULAR (`METODOLOGIA.md`)

## 1. Relación con el Marco Oficial ACM/IEEE-CS Computing Curricula 2020 (CC2020)

Para garantizar el rigor conceptual de la investigación, se establece una distinción explícita entre tres niveles epistemológicos:

### 1.1. Elementos establecidos oficialmente por CC2020
El informe **Computing Curricula 2020: Paradigms for Global Computing Education** (ACM & IEEE-CS, 2020) define:
1. Las **cinco disciplinas clásicas de la computación** evaluadas en este estudio:
   - **Computer Engineering (`CE`):** Integración de ingeniería eléctrica y ciencias de la computación para el diseño de hardware, sistemas digitales, arquitectura de computadores y sistemas embebidos.
   - **Computer Science (`CS`):** Fundamentos teóricos y algorítmicos de la computación, estructuras discretas, teoría de lenguajes, sistemas inteligentes y arquitectura de software/sistemas.
   - **Software Engineering (`SE`):** Desarrollo sistemático, disciplinado y cuantificable de sistemas de software confiables y de gran escala (requisitos, diseño, construcción, pruebas, calidad y mantenimiento).
   - **Information Technology (`IT`):** Infraestructura tecnológica, administración de redes y sistemas, ciberseguridad operativa, plataformas en la nube, integración de servicios y soporte a las necesidades tecnológicas de los usuarios.
   - **Information Systems (`IS`):** Integración de soluciones de tecnología de la información con los procesos organizacionales, gestión de datos corporativos, inteligencia de negocios y gobierno de TI.
2. Los **mapas conceptuales comparativos** (CC2020, Figuras 2.1–2.7 y Tablas 4.1–4.3), que contrastan el énfasis relativo de cada disciplina entre teoría/principios frente a aplicación/despliegue en el eje horizontal y entre hardware/arquitectura frente a cuestiones organizacionales en el eje vertical.

### 1.2. Adaptaciones razonables del marco CC2020 al contexto latinoamericano
En América Latina, la oferta universitaria presenta dos particularidades estructurales frente a los programas anglosajones de 4 años:
- **El tronco común de Ciencias Básicas de Ingeniería (`STEM`):** Títulos denominados *Ingeniería en Sistemas Computacionales*, *Ingeniería de Sistemas*, *Ingeniería Civil en Computación* o *Ingeniería en Informática* dedican entre el 20% y el 38% de sus créditos obligatorios a Cálculo Diferencial, Integral y Vectorial, Álgebra Lineal, Ecuaciones Diferenciales, Probabilidad, Física Clásica y Electromagnetismo.
- **Hibridación disciplinaria bajo una misma denominación:** La denominación *Ingeniería en Sistemas* o *Ingeniería en Sistemas Computacionales* opera como un título paraguas que en algunas instituciones equivale a `CS`/`CE` (p. ej., IPN-ESCOM `D017`), en otras a `SE`/`IT` (p. ej., TecNM `D034`, UV `D070`) y en otras a `IS` (p. ej., UTN `D025`, UNAC `D023`).

### 1.3. Decisiones de operacionalización propias de esta investigación
**Las coordenadas numéricas $(X, Y) \in [-5, +5]^2$, las fórmulas de radio de dispersión $R$ y los umbrales de clasificación no son escalas oficiales emitidas por ACM o IEEE-CS**, sino una operacionalización matemática original diseñada en esta investigación para proyectar mallas curriculares heterogéneas sobre un espacio métrico continuo y reproducible. Por consiguiente, las categorías resultantes se reportan como **«Afinidad Disciplinaria Estimada bajo el Marco CC2020»** y nunca como acreditaciones oficiales.

---

## 2. Estandarización del Corpus y Separación de Poblaciones Documentales

### 2.1. Estructura real del corpus (75 documentos, 73 programas, 72 instituciones, 15 países)
El corpus consta de **75 documentos oficiales (`D001`–`D075`)** procedentes de **15 países latinoamericanos**, divididos en dos poblaciones documentales con unidades de observación distintas:

1. **Población A — Perfiles de Egreso Declarativos (`D001`–`D015`, Bloque 1, $n = 15$):**
   - **Naturaleza:** Enunciados institucionales de competencias profesionales de egreso publicados en portales universitarios de México ($n=13$) y Colombia ($n=2$).
   - **Unidad de medida:** Proposiciones declarativas ($N \in [2, 10]$ por documento) con ponderación uniforme.
   - **Alcance:** Mide el **discurso institucional orientado al mercado laboral** (donde rara vez se declaran como competencias finales de egreso las asignaturas instrumentales de Cálculo o Física de primeros semestres).

2. **Población B — Planes de Estudio y Mallas Curriculares Oficiales (`D016`–`D075`, Bloques 2 a 5, $n = 60$):**
   - **Naturaleza:** Retículas y planes de estudio oficiales con 2,109 asignaturas registradas en 15 países: México ($n=13$), Colombia ($n=11$), Argentina ($n=8$), Perú ($n=7$), Chile ($n=5$), Costa Rica ($n=3$), Ecuador ($n=3$), Honduras ($n=2$), Bolivia ($n=2$), Brasil ($n=2$), El Salvador ($n=1$), Uruguay ($n=1$), Paraguay ($n=1$), Panamá ($n=1$) y Guatemala ($n=1$).
   - **Subgrupos de granularidad curricular:**
     - `Malla_Curricular_Completa` ($n = 22$, `D016`–`D031`, `D033`–`D038`): Retículas íntegras semestre por semestre.
     - `Malla_Troncal_Sintetizada` ($n = 37$, `D039`–`D075`): Núcleo troncal obligatorio completo con optativas agrupadas en bloque.
     - `Malla_Parcial_Especialidad` ($n = 1$, `D032` PUCP): Comprende únicamente los ciclos 5 a 10 de Facultad (128 créditos) sin los ciclos 1 a 4 de *Estudios Generales Ciencias* (~72 créditos). Se analiza tanto en la muestra total ($n = 60$) como excluida en análisis de robustez ($n = 59$).

3. **Solapamientos institucionales y pares exactos identificados:**
   - **`D001` (Perfil) $\leftrightarrow$ `D017` (Plan):** Ambos corresponden al mismo programa (*Ingeniería en Sistemas Computacionales, Plan 2020*) de la **ESCOM del Instituto Politécnico Nacional (IPN, México)**.
   - **`D003` (Perfil) $\leftrightarrow$ `D034` (Plan):** Ambos corresponden al mismo programa (*Ingeniería en Sistemas Computacionales, Plan ISIC-2010-224*) del **Tecnológico Nacional de México (TecNM)**.
   - **`D036` y `D075`:** Corresponden a **dos programas distintos** dentro de la misma universidad (**Universidad de Costa Rica, UCR**): *Bachillerato en Computación con Varios Énfasis* (`D036`) y *Bachillerato en Informática Empresarial* (`D075`).

---

## 3. Formulación Matemática de las Coordenadas y su Validación

### 3.1. Coordenada Global $X_{\text{global}}$ y Coordenada de Computación $X_{\text{comp}}$
Sea $w_i > 0$ el peso curricular (en créditos, unidades valorativas u horas) de la asignatura $i$, y sean $(w_{T,i}, w_{A,i}) \in \{(1,0), (0.5, 0.5), (0,1), (0,0)\}$ sus pesos epistemológicos asignados por el libro de códigos ([`CODEBOOK_CC2020.md`](file:///c:/Users/Aliximber/Desktop/DOCUMENTOS/CODEBOOK_CC2020.md)).

Definimos los pesos acumulados globales (incluyendo el tronco `STEM` de ciencias básicas):
$$P_t = \sum_{i=1}^{m} w_i w_{T,i}, \qquad P_a = \sum_{i=1}^{m} w_i w_{A,i}, \qquad n_X = P_t + P_a$$

La **Coordenada Global en el Eje $X$** es:
$$X_{\text{global}} = 5 \cdot \frac{P_a - P_t}{P_a + P_t} \in [-5, +5]$$

Para aislar el balance teórico-aplicado propio de las asignaturas de computación respecto del volumen de matemáticas y física general (`R27_STEM_BASIC`), definimos además los pesos exclusivos del núcleo de computación ($i \notin \text{R27\_STEM\_BASIC}$):
$$P_{t,\text{comp}} = \sum_{i \notin \text{STEM}} w_i w_{T,i}, \qquad P_{a,\text{comp}} = \sum_{i \notin \text{STEM}} w_i w_{A,i}, \qquad X_{\text{comp}} = 5 \cdot \frac{P_{a,\text{comp}} - P_{t,\text{comp}}}{P_{a,\text{comp}} + P_{t,\text{comp}}}$$

La diferencia $\Delta X_{\text{STEM}} = X_{\text{comp}} - X_{\text{global}} \ge 0$ mide exactamente cuántas unidades hacia el polo teórico desplaza el tronco de ciencias básicas a cada programa. En los 60 planes de estudio, el desplazamiento medio es **$\overline{\Delta X}_{\text{STEM}} = +1.88$ unidades** (pasando de una media global $\bar{X}_{\text{global}} = -0.19$ a una media del núcleo computacional $\bar{X}_{\text{comp}} = +1.69$).

### 3.2. Coordenada en el Eje $Y$
Sean $(w_{H,i}, w_{S,i}, w_{O,i})$ los pesos de estrato sociotécnico para cada asignatura con representación en el eje vertical:
$$C_h = \sum_{i=1}^{m} w_i w_{H,i}, \qquad C_s = \sum_{i=1}^{m} w_i w_{S,i}, \qquad C_o = \sum_{i=1}^{m} w_i w_{O,i}, \qquad n_Y = C_h + C_s + C_o$$

La **Coordenada en el Eje $Y$** es:
$$Y = 5 \cdot \frac{C_o - C_h}{C_h + C_s + C_o} \in [-5, +5]$$

**Interpretación algebraica exacta:** $X_{\text{global}}$ e $Y$ son exactamente las **medias aritméticas ponderadas** $\mathbb{E}[x_i]$ y $\mathbb{E}[y_i]$ de puntuaciones individuales $x_i \in \{-5, 0, +5\}$ e $y_i \in \{-5, -2.5, 0, +2.5, +5\}$. Debido a que son funciones racionales homogéneas de grado cero en los pesos $w_i$, **son invariantes ante cualquier cambio de escala lineal del sistema de créditos u horas entre países**.

### 3.3. Dispersión Interna ($\Delta X, \Delta Y, R$)
La desviación estándar interna del plan de estudios en cada eje viene dada por:
$$\Delta X = \sqrt{\mathbb{E}[x_i^2] - X^2}, \qquad \Delta Y = \sqrt{\mathbb{E}[y_i^2] - Y^2}, \qquad R = \sqrt{\Delta X^2 + \Delta Y^2}$$

Cuando todas las asignaturas clasificadas en $X$ toman valores extremos puros $\{-5, +5\}$, $\mathbb{E}[x_i^2] = 25$, por lo que $\Delta X_{\text{bin}} = \sqrt{25 - X^2}$. Esto explica matemáticamente por qué cualquier programa equilibrado ($X \approx 0$) posee $\Delta X \approx 5.0$ y $R \ge 5.0$: **el radio $R$ no es un error estándar de estimación ni un intervalo de confianza estadístico, sino la amplitud curricular interna (diversidad polar) del plan de estudios**.

### 3.4. Validación Multivariada mediante PCA de 6 Dominios
Para comprobar si el plano bidimensional $(X, Y)$ preserva adecuadamente la estructura multivariada del currículo, se calculó para cada plan el vector de proporciones en los 6 dominios $\mathbf{q} = (\text{pct\_STEM}, \text{pct\_CE}, \text{pct\_CS}, \text{pct\_SE}, \text{pct\_IT}, \text{pct\_IS})$ y se ejecutó un Análisis de Componentes Principales (PCA) sobre la matriz estandarizada ($n = 60 \times 6$):
- Las dos primeras componentes principales explican el **61.07% de la varianza total** ($\text{PC1} = 40.90\%$, $\text{PC2} = 20.18\%$; con $\text{PC3} = 18.16\%$ se alcanza el $79.23\%$).
- La primera componente principal ($\text{PC1}$, que opone `STEM`/`CE`/`CS` frente a `SE`/`IT`/`IS`) presenta una **correlación de Pearson de $r = +0.9330$ con la Coordenada $X_{\text{global}}$**.
- Esto demuestra empíricamente que el eje $X$ captura más del $87\%$ ($r^2 = 0.870$) de la variación del eje principal de diferenciación curricular latinoamericana.

---

## 4. Clasificación de Afinidad Disciplinaria Multicriterio

Para superar el sesgo hacia `CS` y el bloqueo algebraico de `IT` del script original, el módulo [`src/coordenadas.py`](file:///c:/Users/Aliximber/Desktop/DOCUMENTOS/corpus_CC2020/src/coordenadas.py) calcula para cada plan de estudios el **vector normalizado de 5 dominios de computación**:
$$\mathbf{p} = (p_{\text{CE}}, p_{\text{CS}}, p_{\text{SE}}, p_{\text{IT}}, p_{\text{IS}}), \qquad \sum_{d \in \{\text{CE,CS,SE,IT,IS}\}} p_d = 1$$

Y evalúa la afinidad disciplinaria mediante dos métodos complementarios:

1. **Regla de Umbrales Calibrada sin Sesgo STEM (`Afinidad_Regla_Corregida`):**
   - `IS` si $C_o / n_Y \ge 0.30$ o $p_{\text{IS}} \ge 0.28$.
   - `CE` si $C_h / n_Y \ge 0.24$ o $p_{\text{CE}} \ge 0.22$.
   - `CS` si $(P_{t,\text{comp}} / n_{X,\text{comp}} \ge 0.36 \text{ y } p_{\text{CS}} \ge p_{\text{SE}})$ o $p_{\text{CS}} \ge 0.32$.
   - `IT` si $p_{\text{IT}} \ge 0.255$ o $(p_{\text{IT}} \ge 0.23 \text{ y } C_o / n_Y \ge 0.16 \text{ y } p_{\text{IT}} \ge p_{\text{SE}} - 0.03)$.
   - `SE` en caso contrario (predominio de ingeniería y desarrollo de software).

2. **Similitud Coseno frente a Arquetipos Vectoriales CC2020 (`Afinidad_Vectorial_Principal` y `Etiqueta_Compuesta`):**
   - Se calcula la similitud coseno $S_d(\mathbf{p}, \mathbf{r}_d) = \frac{\mathbf{p} \cdot \mathbf{r}_d}{\|\mathbf{p}\|_2 \|\mathbf{r}_d\|_2}$ frente a los vectores arquetípicos $\mathbf{r}_d$ de cada disciplina.
   - Se reportan la disciplina primaria $d_1 = \arg\max_d S_d$, la disciplina secundaria $d_2 = \arg\max_{d \neq d_1} S_d$ y el margen $\Delta S = S_{d_1} - S_{d_2}$. Cuando $\Delta S < 0.08$, el programa se identifica explícitamente como **currículo híbrido** (`Es_Hibrido = True`, etiqueta compuesta $d_1 / d_2$).
   - La concordancia directa entre `Afinidad_Regla_Corregida` y `Afinidad_Vectorial_Principal` en los 60 planes de estudio es del **78.3% ($47/60$)**, y en el **100%** de los casos la etiqueta de regla coincide con la primera o segunda afinidad vectorial.

