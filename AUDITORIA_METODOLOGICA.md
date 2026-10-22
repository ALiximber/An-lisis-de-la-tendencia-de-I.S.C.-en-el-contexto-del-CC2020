# AUDITORÍA METODOLÓGICA, ESTADÍSTICA Y COMPUTACIONAL DEL PROYECTO CC2020

## 1. Resumen Ejecutivo de la Auditoría

El presente documento registra los hallazgos técnicos, metodológicos, estadísticos y documentales derivados de la auditoría integral practicada sobre el repositorio local del proyecto **«Análisis de la tendencia de Ingeniería en Sistemas Computacionales (I.S.C.) en el contexto del CC2020»** (`D001`–`D075`).

La auditoría examinó recursivamente:
- Los 75 registros documentales (`D001`–`D015` en el Bloque 1 y `D016`–`D075` en los Bloques 2 a 5).
- Las 2,109 asignaturas transcritas en `bloque_02_transcripcion.json` a `bloque_05_transcripcion.json` (1,241 nombres únicos normalizados).
- Los 54 archivos de respaldo textual en `fuentes_bloque_02/`, `fuentes_bloque_03/` y `fuentes/`.
- Los scripts de procesamiento (`calcular_bloque_02.py` a `05.py`), generación de informes (`generar_informe_02.py` a `05.py`) y visualización (`visualizar_bloque_01.py` a `05.py`, `visualizar_corpus_completo.py`).
- La documentación principal (`README.md`, `bloque_01_analisis.md` a `bloque_05_analisis.md`).

---

## 2. Respuesta a las 10 Preguntas de Investigación de la Fase 1

### 2.1. ¿Cómo se generan las coordenadas $(X, Y)$?
- **En el Bloque 1 (`D001`–`D015`, perfiles de egreso):** No existía un script generador de clasificación automática (`calcular_bloque_01.py` no existía). Las coordenadas se codificaron manualmente descomponiendo el texto del perfil de egreso en pequeñas unidades discretas ($N \in [2, 10]$ proposiciones o viñetas por perfil) y asignándoles conteos enteros $P_t, P_a, C_h, C_s, C_o$. Debido al tamaño muestral diminuto por documento, perfiles como `D002`, `D004`, `D008`, `D009`, `D011` y `D015` recibieron $P_t = 0$, colapsando directamente en el extremo algebraico $X = +5.00$.
- **En los Bloques 2 a 5 (`D016`–`D075`, planes de estudio):** Las coordenadas se calculaban mediante los scripts `calcular_bloque_02.py` a `05.py` aplicando una lista ordenada de expresiones regulares (`RULES`, donde gana la primera coincidencia) sobre el título de cada asignatura y acumulando su peso curricular ($w_i$) en $P_t, P_a$ y $C_h, C_s, C_o$.

### 2.2. ¿Qué datos se extraen de las fuentes?
- Para `D001`–`D015`, se extrajeron párrafos o viñetas de perfiles de egreso publicados en páginas web institucionales (`fuentes/D001_perfil.txt` a `D015_perfil.txt`).
- Para `D016`–`D038` (con excepción de `D032`), se extrajeron las mallas curriculares completas con periodo, nombre de asignatura, peso en créditos u horas y condición (`Obligatoria` / `Electivo`).
- Para `D032` (PUCP, Perú), el PDF descargado (`fuentes_bloque_03/D032.txt`) corresponde únicamente al plan de facultad FCI (ciclos 5 a 10, 128 créditos) y **omite los ciclos 1 a 4 (*Estudios Generales Ciencias*, ~72 créditos de Cálculo, Física, Álgebra Lineal y Matemática Discreta)**. Esta omisión infló artificialmente la coordenada de `D032` hasta $X = +3.09$ ($+3.15$ tras normalización léxica), convirtiéndola en un valor extremo por truncamiento de fuente.
- Para `D039`–`D075`, las transcripciones JSON contienen mallas troncales sintetizadas (entre 24 y 38 entradas por programa) donde las asignaturas optativas se agruparon en bloques genéricos (`Optativas I`, `Electiva Profesional`, etc.).

### 2.3. ¿Cómo se clasifican las asignaturas y qué defectos presentaban las expresiones regulares?
Cada script (`calcular_bloque_02.py` a `05.py`) definía su propia lista `RULES` de expresiones regulares evaluadas secuencialmente (`first-match-wins`). Se detectaron tres fallos estructurales:

1. **Inconsistencia entre bloques (deriva de reglas):** Las listas `RULES` fueron editadas incrementalmente entre el Bloque 2 y el Bloque 5 sin retroportar los cambios. Al evaluar las 1,241 denominaciones únicas de asignaturas del corpus contra los cuatro scripts originales, **132 nombres únicos de asignaturas reciben diferente clasificación $(X, Y)$ según el bloque en que se procesen**:
   - *Ejemplo 1:* `Telecomunicaciones` y `Conmutación y Enrutamiento` se clasificaban como `(A, S)` en el Bloque 2, pero pasaron a `(T, H)` en los Bloques 3, 4 y 5.
   - *Ejemplo 2:* `Minería de Datos` se clasificaba como `(A, S)` en el Bloque 2, pero pasó a `(T, S)` en los Bloques 3, 4 y 5.
   - *Ejemplo 3:* `Calidad de Software` o términos con `calidad`, `servidores`, `graficación`, `ensamblador` o `microcontroladores` estaban ausentes en las reglas del Bloque 2 y se añadieron recién en el Bloque 3.

2. **Colisiones de subcadenas sin delimitadores de palabra (`\b`) ni prioridad semántica:**
   - En `D039` (UniAndes), **`Fundamentos de Infraestructura Tecnológica`** coincidió con la subcadena `logica` dentro de la palabra `tecnoLOGICA`, clasificándose erróneamente como **`(T, S)` (Teoría de la Computación)** en lugar de infraestructura aplicada `(A, S/H)`.
   - En `D041` (UBA), **`Física de los Sistemas de Información`** coincidió con `sistemas de informacion` (Regla 9) antes de llegar a la regla de Ciencias Básicas (`fisica`, Regla 12), clasificándose como **`(A, O)` (Gestión/Sistemas de Información)** cuando es un curso de Física básica `(T, None)`.
   - En `D033` (U. de Chile), **`Cálculo Avanzado y Aplicaciones`** y **`Aplicaciones de la Biología a la Ingeniería y Ciencias`** coincidieron con `aplicaciones` (Regla 10) antes de llegar a `calculo` y `biologia` (Regla 12), clasificándose como **`(A, S)` (Desarrollo de Software)**.
   - En `D047` (UNSA) y `D057` (USM), **`Arquitectura y Organización de Computadores`** no coincidió con la regla de hardware del Bloque 4 (`arquitectura (del|de) comput` ni `organizacion y arquitectura`) y cayó en la Regla 17 (`organizacion`), clasificándose como **`(A, O)` (Administración de Empresas)** en vez de `(T, H)` (Hardware).
   - En `D032` (PUCP), **`Modelado y Automatización de Procesos Empresariales`** coincidió con `automatizacion` en la Regla 4 de hardware/robótica, clasificándose como **`(A, H)` (Hardware)** en lugar de `(A, O)` (Procesos de Negocio).
   - En `D034` (TecNM), **`Principios Eléctricos y Aplicaciones Digitales`** no coincidió con `circuitos electricos` ni `sistemas digitales` y cayó en `aplicaciones` (Regla 10), clasificándose como **`(A, S)` (Software)** en lugar de Hardware (`H`).
   - En `D037` (UTPL), **`Planificación Estratégica y Sistemas de Calidad Empresarial`** coincidió con `calidad` en la Regla 10 de software antes de llegar a `planificacion estrategica` (Regla 11), clasificándose como **`(A, S)`** en lugar de `(A, O)`.
   - En `D050` (UANL), **`Aplicación Práctica de Programación`** coincidió con la subcadena `practica` en la Regla 1 de exclusión de prácticas profesionales, quedando **excluida `(None, None)`** pese a ser una asignatura obligatoria de programación de 1.º semestre.
   - En `D058` (UASLP), **`Temas Selectos de Matemáticas`** coincidió con `temas selectos` en la Regla 1 de exclusión de optativas genéricas, excluyendo un curso obligatorio de matemáticas.
   - En `D051` vs. `D052`, **`Lenguajes de Programación I/II`** (plural) se clasificó como `(T, S)`, mientras que **`Lenguaje de Programación I/II`** (singular) no coincidió con `lenguajes de programacion` y cayó en `programacion` como `(A, S)`.

3. **Doble/triple conteo de electivas de catálogo en `D023` (UNAC Callao):**
   - En `D023`, la malla incluye 12 asignaturas con `Condicion = "Electivo"` (36 créditos distribuidos en 3 líneas de especialidad donde el estudiante cursa solo una fracción). Como tenían nombres técnicos específicos (`Robótica`, `Peritaje y Tasación en Informática`, `Comercio Electrónico`, etc.) y la Regla 1 solo filtraba la palabra `"electivo"` dentro del campo `Asignatura` pero ignoraba el campo `Condicion`, las 12 asignaturas se sumaron íntegramente al peso obligatorio del programa.

### 2.4. ¿Qué pesos se aplican?
Los scripts ponderan cada asignatura por el campo `Peso` del archivo JSON correspondiente (créditos SATCA, créditos SCT, créditos UEA, unidades valorativas, horas reloj totales en Argentina `D025`–`D027`, `D048`, `D065`, `D068`, u horas semanales en `D056`, `D060`, `D071`). Dado que las fórmulas de $X$ e $Y$ son razones homogéneas de grado cero ($\frac{P_a - P_t}{P_a + P_t}$), el factor de escala global del sistema de créditos se cancela internamente dentro de cada programa. El análisis de sensibilidad demuestra que reemplazar los pesos por pesos uniformes ($w_i = 1$) produce una correlación de $r = 0.9923$ en $X$ y $r = 0.9934$ en $Y$ ($\text{MAE}_X = 0.113$, $\text{MAE}_Y = 0.074$).

### 2.5. ¿Cómo se asignan las afinidades disciplinarias y por qué fallaba la regla original?
Los scripts `calcular_bloque_02.py` a `05.py` implementaban la función escalonada:
```python
def afinidad(pt, pa, ch, cs, co):
    nx, ny = pt + pa, ch + cs + co
    if co / ny >= 0.30: return "IS"
    if ch / ny >= 0.25: return "CE"
    if pt / nx >= 0.45: return "CS"
    if cs / ny >= 0.55: return "SE"
    return "IT"
```
Esta función contenía dos defectos matemáticos graves:
1. **Inalcanzabilidad algebraica de `IT`:** Para llegar al retorno final `"IT"`, un programa debe cumplir simultáneamente $C_o / n_Y < 0.30$, $C_h / n_Y < 0.25$ y $C_s / n_Y < 0.55$. Pero como $C_h + C_s + C_o = n_Y$, se cumple la identidad $\frac{C_h}{n_Y} + \frac{C_s}{n_Y} + \frac{C_o}{n_Y} = 1$. Si $\frac{C_o}{n_Y} + \frac{C_h}{n_Y} \le 0.45$, entonces forzosamente $\frac{C_s}{n_Y} \ge 0.55$, por lo que la rama `SE` captura el programa antes de llegar a `IT`. Como resultado, **0 de los 60 planes de estudio fueron clasificados como `IT`** (incluso programas explícitamente denominados *Ingeniería en Tecnologías de la Información* como `D037` UTPL y `D059` PUCE).
2. **Sesgo de sobreclasificación en `CS` por el tronco de ciencias básicas (`STEM`):** Toda asignatura de Cálculo, Álgebra, Física, Química o Biología suma a $P_t$ ($X = -5$), pero no suma a $Y$. En América Latina, casi cualquier título de Ingeniería incluye entre 25% y 35% de ciencias básicas generales. Al sumar ese tronco general a los cursos teóricos de computación (Algoritmos, Discreta, Arquitectura), la razón $P_t / n_X$ supera fácilmente $0.45$, forzando **40 de los 60 planes (66.7%) a la categoría `CS`**, incluso en programas cuyo núcleo computacional es mayoritariamente Ingeniería de Software o Tecnologías de la Información.

### 2.6. ¿Cómo se ejecutan las operaciones estadísticas y qué problemas presentaban?
En `visualizar_corpus_completo.py`:
- Se mezclaron en una misma matriz `N = 75` los **15 perfiles de egreso declarativos (`D001`–`D015`)** y los **60 planes de estudio (`D016`–`D075`)**.
- Sobre esa mezcla heterogénea se ajustó una densidad kernel 2D con anchos fijos arbitrarios `hx = 1.05, hy = 1.05` y niveles de contorno relativos al pico (`0.07, 0.28, 0.60 * Z.max()`) que no representan regiones de probabilidad acumulada (HDR).
- Se trazó una curva de regresión Nadaraya–Watson (`h = 0.95`) desde $X = -2.92$ hasta $X = +5.00$. Dado que entre $X = +3.15$ y $X = +5.00$ **no existe ningún plan de estudios** (solo existen los 15 perfiles de egreso del Bloque 1), el tramo derecho de la curva de regresión era un artefacto de extrapolación causado por mezclar dos poblaciones documentales distintas.

### 2.7. ¿Qué inconsistencias existían entre scripts, datos, documentación y resultados?
En `README.md` se detectaron contradicciones directas con los archivos CSV y JSON del propio repositorio:
1. **Número de países:** El `README.md` afirmaba repetidamente que el estudio abarca **8 países**, cuando los archivos de datos contienen **15 países** (México [26], Colombia [11], Argentina [8], Perú [7], Chile [5], Ecuador [4], Costa Rica [3], Honduras [2], Bolivia [2], Brasil [2], El Salvador [1], Uruguay [1], Paraguay [1], Panamá [1] y Guatemala [1]).
2. **Composición de los bloques:** El `README.md` describía el Bloque 2 (`D016`–`D030`) como *«Planes de Estudio Oficiales de México (UNAM, IPN, UAM, TecNM, UANL, UV, BUAP)»*, cuando en realidad `D016`–`D030` contiene programas de México, Perú, Colombia, El Salvador y Argentina, y las instituciones UNAM (`D031`), TecNM (`D034`), UAM (`D043`), UANL (`D050`) y UV (`D070`) se encuentran en los Bloques 3, 4 y 5.
3. **Tabla de afinidades y radios medios:** La tabla de la Sección 5 del `README.md` asignaba ejemplos institucionales que contradecían los propios archivos CSV (p. ej., ubicaba a TecNM, UV y UADY en `IT` cuando en los CSV había 0 programas `IT` en los Bloques 2–5) y reportaba radios medios de $1.68$ a $2.21$, cuando el radio calculado en los Bloques 2–5 oscilaba entre $4.37$ y $5.91$ por su definición binaria en $\{-5, +5\}$.
4. **Trazabilidad en `fuentes_bloque_03/`:** Los archivos `fuentes_bloque_03/D034.txt` a `D044.txt` fueron descargados mediante scripts preliminares por lotes (`_fuentes_lote2.json` a `lote5.json`) cuya numeración no coincide con los identificadores finales `D034`–`D044` de `bloque_03_datos.json`.

---

## 3. Síntesis de Correcciones Implementadas

| Componente Auditado | Defecto Original Detectado | Solución Implementada y Verificada |
| :--- | :--- | :--- |
| **Clasificador Curricular** | 4 scripts distintos con 132 discrepancias internas y colisiones de subcadenas (`logica` $\subset$ `tecnologica`, `aplicaciones` antes que `calculo`, etc.). | Creación de [`src/codebook.py`](file:///c:/Users/Aliximber/Desktop/DOCUMENTOS/corpus_CC2020/src/codebook.py) y [`CODEBOOK_CC2020.md`](file:///c:/Users/Aliximber/Desktop/DOCUMENTOS/CODEBOOK_CC2020.md) con 27 reglas jerárquicas auditadas, delimitadores léxicos, pesos híbridos ($0.5/0.5$) y 0 asignaturas sin clasificar sobre 2,109 registros. |
| **Efecto del Tronco STEM** | Las ciencias básicas generales inflaban $P_t$, desplazando $X$ hacia $-5$ y forzando 66.7% de los programas a `CS`. | Cálculo dual en [`src/coordenadas.py`](file:///c:/Users/Aliximber/Desktop/DOCUMENTOS/corpus_CC2020/src/coordenadas.py): $X_{\text{global}}$ (con STEM) y $X_{\text{comp}}$ (solo computación), cuantificando $\Delta X_{\text{STEM}} = X_{\text{comp}} - X_{\text{global}}$ (media $+1.88$ unidades). |
| **Afinidad Disciplinaria** | `IT` era algebraicamente inalcanzable ($0/60$ planes) y `CS` estaba sobreasignado ($40/60$). | Implementación de regla corregida sin sesgo STEM y clasificación vectorial por similitud coseno contra los 5 arquetipos CC2020 (`CS`: 18, `SE`: 17, `IT`: 13, `CE`: 7, `IS`: 5) con detección de programas híbridos. |
| **Poblaciones Documentales** | Mezcla indebida de 15 perfiles de egreso y 60 planes de estudio en KDE y regresión. | Separación estricta de ambas poblaciones en [`src/estadistica.py`](file:///c:/Users/Aliximber/Desktop/DOCUMENTOS/corpus_CC2020/src/estadistica.py) y [`src/visualizaciones.py`](file:///c:/Users/Aliximber/Desktop/DOCUMENTOS/corpus_CC2020/src/visualizaciones.py), más análisis directo de los 2 pares institucionales exactos (`D001`↔`D017` IPN-ESCOM y `D003`↔`D034` TecNM). |
| **Modelado Estadístico** | Anchos de banda fijos sin validación, contornos relativos al pico y extrapolación sin soporte. | Selección óptima por LOOCV ($h_{\text{opt}} = 0.65$), regiones de probabilidad acumulada HDR (50%, 80%, 95%), tamaño muestral efectivo $N_{\text{eff}}(x) \ge 2.5$ y bandas de confianza bootstrap al 95% ($B = 1,000$). |

