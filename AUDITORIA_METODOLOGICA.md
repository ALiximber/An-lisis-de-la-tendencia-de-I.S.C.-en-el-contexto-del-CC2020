# AUDITORÍA METODOLÓGICA, ESTADÍSTICA Y COMPUTACIONAL DEL PROYECTO CC2020

## 1. Resumen Ejecutivo de la Auditoría

El presente documento registra los hallazgos técnicos, metodológicos, estadísticos y documentales derivados de la auditoría integral (Primera y Segunda Ronda de Verificación) practicada sobre el repositorio del proyecto **«Análisis de la tendencia de Ingeniería en Sistemas Computacionales (I.S.C.) en el contexto del CC2020»** (`D001`–`D075`).

La auditoría examinó recursivamente:
- Los 75 registros documentales (`D001`–`D015` en el Bloque 1 y `D016`–`D075` en los Bloques 2 a 5).
- Las 2,109 asignaturas transcritas en `bloque_02_transcripcion.json` a `bloque_05_transcripcion.json` (1,241 nombres únicos normalizados).
- Los archivos de respaldo textual en `corpus_CC2020/fuentes_bloque_02/`, `corpus_CC2020/fuentes_bloque_03/` y `corpus_CC2020/fuentes/`.
- Los scripts originales de procesamiento (archivados en `corpus_CC2020/datos_originales_backup/scripts_originales/`) frente al nuevo pipeline unificado (`corpus_CC2020/ejecutar_pipeline.py` y paquete `corpus_CC2020/src/`).
- La documentación principal (`README.md`, `bloque_01_analisis.md` a `bloque_05_analisis.md`).

---

## 2. Respuesta a las 10 Preguntas de Investigación de la Fase 1

### 2.1. ¿Cómo se generan las coordenadas $(X, Y)$?
- **En el Bloque 1 (`D001`–`D015`, perfiles de egreso):** No existía un script generador de clasificación automática (`calcular_bloque_01.py` no existía). Las coordenadas se codificaron manualmente descomponiendo el texto del perfil de egreso en pequeñas unidades discretas ($N \in [1, 15]$ proposiciones o viñetas por perfil) y asignándoles conteos $P_t, P_a, C_h, C_s, C_o$. Debido al número reducido de viñetas por documento, 11 de los 15 perfiles recibieron $P_t = 0$, colapsando directamente en el extremo algebraico $X = +5.00$.
- **En los Bloques 2 a 5 (`D016`–`D075`, planes de estudio):** Las coordenadas se calculaban originalmente mediante los scripts `calcular_bloque_02.py` a `05.py` aplicando una lista ordenada de expresiones regulares (`RULES`, donde gana la primera coincidencia) sobre el título de cada asignatura y acumulando su peso curricular ($w_i$) en $P_t, P_a$ y $C_h, C_s, C_o$. En la arquitectura actual, este cálculo lo ejecuta de forma unificada [`corpus_CC2020/src/coordenadas.py`](corpus_CC2020/src/coordenadas.py).

### 2.2. ¿Qué datos se extraen de las fuentes?
- **Bloque 1 (`D001`–`D015`, $n = 15$):** Párrafos o viñetas de perfiles de egreso publicados en páginas web institucionales de **México ($n = 13$), Ecuador ($n = 1$, `D013` UCSG) y Honduras ($n = 1$, `D015` UJN)**.
- **Bloques 2 a 5 (`D016`–`D075`, $n = 60$):** Planes de estudio y mallas curriculares oficiales de **15 países**: **México ($n=13$), Colombia ($n=11$), Argentina ($n=8$), Perú ($n=7$), Chile ($n=5$), Costa Rica ($n=3$), Ecuador ($n=3$), Bolivia ($n=2$), Brasil ($n=2$), El Salvador ($n=1$), Honduras ($n=1$, `D038` UNAH), Uruguay ($n=1$), Paraguay ($n=1$), Panamá ($n=1$) y Guatemala ($n=1$)**, que suman exactamente $60$ planes ($15 + 60 = 75$ documentos).
- **Truncamiento detectado en `D032` (PUCP, Perú):** El PDF oficial descargado (`corpus_CC2020/fuentes_bloque_03/D032.pdf`) corresponde únicamente al plan de facultad FCI (ciclos 5 a 10, 128 créditos) y **omite los ciclos 1 a 4 (*Estudios Generales Ciencias*, ~72 créditos de Cálculo, Física, Álgebra Lineal y Química)**. Esta omisión inflaba la coordenada de `D032` hasta $X = +3.09$ ($+3.15$ tras normalización léxica).
- **Granularidad en `D039`–`D075`:** Mientras que `D016`–`D031` y `D033`–`D038` ($n = 22$) transcriben la malla curricular completa asignatura por asignatura, los registros `D039`–`D075` ($n = 37$) contienen mallas troncales sintetizadas (entre 24 y 38 entradas por programa) con asignaturas optativas agrupadas en bloque.

### 2.3. ¿Cómo se clasifican las asignaturas y qué defectos presentaban las expresiones regulares originales?
Cada script original (`calcular_bloque_02.py` a `05.py`) definía su propia lista `RULES` evaluada secuencialmente (`first-match-wins`). Se detectaron tres fallos estructurales:

1. **Inconsistencia entre bloques (deriva de reglas):** Las listas `RULES` fueron editadas incrementalmente entre el Bloque 2 y el Bloque 5 sin retroportar los cambios. Al evaluar las 1,241 denominaciones únicas de asignaturas del corpus contra los cuatro scripts originales, **132 nombres únicos de asignaturas recibían diferente clasificación $(X, Y)$ según el bloque en que se procesaran**:
   - *Ejemplo 1:* `Telecomunicaciones` y `Conmutación y Enrutamiento` se clasificaban como `(A, S)` en el Bloque 2, pero pasaron a `(T, H)` en los Bloques 3, 4 y 5.
   - *Ejemplo 2:* `Minería de Datos` se clasificaba como `(A, S)` en el Bloque 2, pero pasó a `(T, S)` en los Bloques 3, 4 y 5.
   - *Ejemplo 3:* Términos como `calidad`, `servidores`, `graficación`, `ensamblador` o `microcontroladores` estaban ausentes en las reglas del Bloque 2 y se añadieron recién en el Bloque 3.

2. **Colisiones de subcadenas sin delimitadores de palabra (`\b`) ni prioridad semántica:**
   - En `D039` (UniAndes), **`Fundamentos de Infraestructura Tecnológica`** coincidió con la subcadena `logica` dentro de la palabra `tecnoLOGICA`, clasificándose erróneamente como **`(T, S)` (Teoría de la Computación)** en lugar de infraestructura aplicada `(A, S)` en `IT`.
   - En `D041` (UBA), **`Física de los Sistemas de Información`** coincidió con `sistemas de informacion` antes de llegar a Ciencias Básicas (`fisica`), clasificándose como **`(A, O)` (Sistemas de Información Empresarial)** cuando es un curso de Física básica `(T, None)`.
   - En `D033` (U. de Chile), **`Cálculo Avanzado y Aplicaciones`** y **`Aplicaciones de la Biología a la Ingeniería y Ciencias`** coincidieron con `aplicaciones` antes de llegar a `calculo` y `biologia`, clasificándose como **`(A, S)` (Desarrollo de Software)**.
   - En `D047` (UNSA) y `D057` (USM), **`Arquitectura y Organización de Computadores`** no coincidió con la regla de hardware del Bloque 4 (`arquitectura (del|de) comput` ni `organizacion y arquitectura`) y cayó en la Regla 17 (`organizacion`), clasificándose como **`(A, O)` (Administración de Empresas)** en vez de `(T, H)` (Hardware).
   - En `D032` (PUCP), **`Modelado y Automatización de Procesos Empresariales`** coincidió con `automatizacion` en la regla de hardware/robótica, clasificándose como **`(A, H)` (Hardware)** en lugar de `(A, O)` (Procesos de Negocio).
   - En `D034` (TecNM), **`Principios Eléctricos y Aplicaciones Digitales`** cayó en `aplicaciones`, clasificándose como **`(A, S)` (Software)** en lugar de Hardware (`H`).
   - En `D037` (UTPL), **`Planificación Estratégica y Sistemas de Calidad Empresarial`** coincidió con `calidad` en software antes de llegar a `planificacion estrategica`, clasificándose como **`(A, S)`** en lugar de `(A, O)`.
   - En `D050` (UANL), **`Aplicación Práctica de Programación`** coincidió con `practica` en la regla de exclusión de prácticas profesionales, quedando **excluida `(None, None)`** pese a ser una asignatura obligatoria de programación de 1.º semestre.
   - En `D058` (UASLP), **`Temas Selectos de Matemáticas`** coincidió con `temas selectos` en la regla de exclusión de optativas genéricas, excluyendo un curso obligatorio de matemáticas.
   - En `D051` vs. `D052`, **`Lenguajes de Programación I/II`** (plural) se clasificó como `(T, S)`, mientras que **`Lenguaje de Programación I/II`** (singular) cayó en `programacion` como `(A, S)`.

3. **Doble/triple conteo de electivas de catálogo en `D023` (UNAC Callao):**
   - En `D023`, la malla incluye 12 asignaturas con `Condicion = "Electivo"` (36 créditos distribuidos en 3 líneas de especialidad donde el estudiante cursa solo una fracción). Como tenían nombres técnicos específicos (`Robótica`, `Peritaje y Tasación en Informática`, `Comercio Electrónico`, etc.) y la Regla 1 solo filtraba la palabra `"electivo"` dentro del campo `Asignatura` pero ignoraba el campo `Condicion`, las 12 asignaturas se sumaban íntegramente al peso obligatorio del programa.

### 2.4. ¿Qué pesos se aplican?
Los scripts ponderan cada asignatura por el campo `Peso` del archivo JSON correspondiente (créditos SATCA, créditos SCT, créditos UEA, unidades valorativas, horas reloj totales u horas semanales). Dado que las fórmulas de $X$ e $Y$ son razones homogéneas de grado cero ($\frac{P_a - P_t}{P_a + P_t}$), el factor de escala global del sistema de créditos se cancela internamente dentro de cada programa. El análisis de sensibilidad demuestra que reemplazar los pesos por pesos uniformes ($w_i = 1$) produce una correlación de $r = 0.9924$ en $X$ y $r = 0.9934$ en $Y$ ($\text{MAE}_X = 0.112$, $\text{MAE}_Y = 0.074$).

### 2.5. ¿Cómo se asignaban las afinidades disciplinarias y por qué la regla original producía 0 programas en `IT` y 66.7% en `CS`?
Los scripts originales `calcular_bloque_02.py` a `05.py` implementaban la función escalonada:
```python
def afinidad(pt, pa, ch, cs, co):
    nx, ny = pt + pa, ch + cs + co
    if co / ny >= 0.30: return "IS"
    if ch / ny >= 0.25: return "CE"
    if pt / nx >= 0.45: return "CS"
    if cs / ny >= 0.55: return "SE"
    return "IT"
```
El análisis matemático y geométrico de esta regla revela dos distorsiones estructurales severas:

1. **Restricción geométrica al 1.0% del símplex y paradoja conceptual en `IT`:**
   - Sea el 2-símplex de proporciones verticales $\Delta_2 = \{(p_H, p_S, p_O) \in [0, 1]^3 : p_H + p_S + p_O = 1\}$, donde $p_H = C_h/n_Y$, $p_S = C_s/n_Y$ y $p_O = C_o/n_Y$.
   - Para que un programa supere los cuatro condicionales previos y llegue a `return "IT"`, debe satisfacer simultáneamente:
     $$p_O < 0.30, \qquad p_H < 0.25, \qquad p_S < 0.55 \iff p_H + p_O = 1 - p_S > 0.45, \qquad \text{y} \qquad \frac{P_t}{n_X} < 0.45$$
   - **Nota de rigor algebraico:** Este sistema de desigualdades **no es algebraicamente vacío**: por ejemplo, el vector $(p_O = 0.29,\; p_H = 0.24,\; p_S = 0.47,\; P_t/n_X = 0.40)$ cumple $p_H + p_O = 0.53 > 0.45$ y alcanza `return "IT"`.
   - **Demostración geométrica y conceptual del defecto:** En el plano $(p_H, p_O)$, el dominio total del símplex $\{p_H \ge 0,\; p_O \ge 0,\; p_H + p_O \le 1\}$ tiene área $\mathcal{A}(\Delta_2) = \frac{1}{2}(1)(1) = 0.50$. La región donde `IT` es alcanzable es únicamente el pequeño triángulo rectángulo residual:
     $$\mathcal{R}_{\text{IT}} = \left\{(p_H, p_O) \in \Delta_2 : 0.15 < p_H < 0.25,\; 0.20 < p_O < 0.30,\; p_H + p_O > 0.45\right\}$$
     cuyos vértices son $(0.15, 0.30)$, $(0.25, 0.20)$ y $(0.25, 0.30)$, con catetos de longitud $0.10$ y $0.10$, y cuya área es $\mathcal{A}(\mathcal{R}_{\text{IT}}) = \frac{1}{2}(0.10)(0.10) = 0.005$. Por tanto, **$\mathcal{R}_{\text{IT}}$ representa apenas el $\frac{0.005}{0.500} = 1.0\%$ del área del símplex $\Delta_2$** (antes siquiera de intersectar con la condición adicional $P_t/n_X < 0.45$).
   - Más grave aún es la **inversión conceptual respecto a CC2020**: para entrar en $\mathcal{R}_{\text{IT}}$ ($p_H + p_O > 0.45$), un plan de estudios necesitaba tener simultáneamente una proporción alta de Hardware ($15\% < p_H < 25\%$) y una proporción alta de Gestión Organizacional ($20\% < p_O < 30\%$). Sin embargo, las asignaturas propias de *Information Technology* en CC2020 (administración de sistemas operativos y servidores, redes de datos, ciberseguridad, computación en la nube, bases de datos operativas y plataformas web) se codifican en el estrato intermedio $C_s$ ($Y = 0$). En consecuencia, cuanto más contenido de `IT` real tenía un programa, mayor era su proporción $p_S = C_s/n_Y \ge 0.55$, siendo capturado sistemáticamente por `SE` (o por `CS`). Empíricamente, en los 60 planes de estudio del corpus, **0 programas** cumplieron $p_H < 0.25 \land p_O < 0.30 \land p_H + p_O > 0.45$ (el máximo de $p_H + p_O$ bajo esas cotas fue $0.382$ en `D038`), dejando en **0 de 60** la categoría `IT` (incluso para carreras tituladas *Ingeniería en Tecnologías de la Información* como `D037` UTPL y `D059` PUCE).

2. **Sesgo de sobreclasificación en `CS` por el tronco de ciencias básicas (`STEM`):**
   - Toda asignatura de Cálculo, Álgebra, Física, Química o Biología suma a $P_t$ ($X = -5$), pero no suma a $Y$. En América Latina, el tronco general `STEM` representa en promedio el **$28.51\%$** del peso clasificado. Al sumarse ese tronco general a los cursos teóricos de computación, la razón global $P_t / n_X$ superaba $0.45$ en **40 de los 60 planes (66.7%)**, clasificándolos automáticamente como `CS` aunque su núcleo de computación estuviese dominado por `SE` o `IT`.

### 2.6. ¿Cómo se ejecutaban las operaciones estadísticas y qué problemas presentaban?
En el script original `visualizar_corpus_completo.py`:
- Se mezclaban en una misma matriz `N = 75` los **15 perfiles de egreso declarativos (`D001`–`D015`)** y los **60 planes de estudio (`D016`–`D075`)**.
- Sobre esa mezcla heterogénea se ajustaba una densidad kernel 2D con anchos fijos arbitrarios `hx = 1.05, hy = 1.05` y niveles de contorno relativos al pico (`0.07, 0.28, 0.60 * Z.max()`) que no representaban regiones de probabilidad acumulada (HDR).
- Se trazaba una curva de regresión Nadaraya–Watson (`h = 0.95`) desde $X = -2.92$ hasta $X = +5.00$. Dado que entre $X = +3.16$ y $X = +5.00$ **no existe ningún plan de estudios** (solo existen perfiles de egreso declarativos), el tramo derecho de la curva era una extrapolación sin soporte empírico en mallas curriculares.

### 2.7. Reconciliación documental en `fuentes_bloque_03/` (`D034`–`D044`)
Se auditó contenido por contenido la carpeta [`corpus_CC2020/fuentes_bloque_03/`](corpus_CC2020/fuentes_bloque_03/):
- Se comprobó que las transcripciones curriculares en [`corpus_CC2020/bloque_03_transcripcion.json`](corpus_CC2020/bloque_03_transcripcion.json) corresponden fielmente a las 15 instituciones declaradas (`D031` UNAM a `D045` ITESM).
- Sin embargo, los archivos descargados inicialmente en `fuentes_bloque_03/` provenían de cinco lotes preliminares (`_fuentes_lote1.json` a `lote5.json`) con numeración desplazada: `D040.pdf` era en realidad el flujograma oficial de `D038` (UNAH Honduras), `D034.html/.txt` era el plan de `D041` (UBA-FIUBA), `D036.html/.txt` era el plan de `D042` (PUC Chile) y `D038.html/.txt` era el plan de `D045` (ITESM).
- **Acción ejecutada:** Se reconciliaron los nombres de archivo directamente en [`corpus_CC2020/fuentes_bloque_03/`](corpus_CC2020/fuentes_bloque_03/) para que coincidan 1 a 1 con sus identificadores definitivos (`D031`, `D032`, `D033`, `D035`, `D038`, `D041`, `D042`, `D045`), se documentó la tabla completa en [`corpus_CC2020/fuentes_bloque_03/INDICE_CORRESPONDENCIA_FUENTES.md`](corpus_CC2020/fuentes_bloque_03/INDICE_CORRESPONDENCIA_FUENTES.md) y se archivaron los lotes preliminares en `corpus_CC2020/datos_originales_backup/lotes_preliminares_b3/`.

---

## 3. Síntesis de Correcciones Implementadas

| Componente Auditado | Defecto Original Detectado | Solución Implementada y Verificada |
| :--- | :--- | :--- |
| **Clasificador Curricular** | 4 scripts distintos con 132 discrepancias internas y colisiones de subcadenas (`logica` $\subset$ `tecnologica`, `aplicaciones` antes que `calculo`, `comunicaciones` antes que `modelos estocasticos`, etc.). | Creación de [`corpus_CC2020/src/codebook.py`](corpus_CC2020/src/codebook.py) y [`CODEBOOK_CC2020.md`](CODEBOOK_CC2020.md) con 27 reglas jerárquicas auditadas, delimitadores léxicos, pesos híbridos ($0.5/0.5$) y 0 asignaturas sin clasificar sobre 2,109 registros. |
| **Validación Ciega Independiente** | Ausencia de contraste contra un evaluador independiente bajo protocolo externo. | Creación de [`PROTOCOLO_REVISION_EXTERNA.md`](PROTOCOLO_REVISION_EXTERNA.md) y ejecución de evaluación ciega independiente sobre $n = 120$ asignaturas ([`corpus_CC2020/evaluacion_ciega_resultados_120.json`](corpus_CC2020/evaluacion_ciega_resultados_120.json)), elevando el Kappa de Cohen de $\kappa_X = 0.4489, \kappa_Y = 0.4403$ en `S0` a **$\kappa_X = 0.7198$ ($\kappa_w = 0.7350$), $\kappa_Y = 0.7751$ ($\kappa_w = 0.8560$) y $\kappa_{\text{Dom}} = 0.7699$** en `S1`. |
| **Efecto del Tronco STEM** | Las ciencias básicas generales inflaban $P_t$, desplazando $X$ hacia $-5$ y forzando 66.7% de los programas a `CS`. | Cálculo dual en [`corpus_CC2020/src/coordenadas.py`](corpus_CC2020/src/coordenadas.py): $X_{\text{global}}$ (con STEM) y $X_{\text{comp}}$ (solo computación), cuantificando $\Delta X_{\text{STEM}} = X_{\text{comp}} - X_{\text{global}}$ (media $+1.88$ unidades). |
| **Afinidad Disciplinaria** | `IT` quedaba confinado a un triángulo residual del $1.0\%$ del símplex ($0/60$ planes) y `CS` estaba sobreasignado ($40/60$). | Implementación de regla corregida sin sesgo STEM y clasificación vectorial por similitud coseno contra los 5 arquetipos CC2020 (`CS`: 18, `SE`: 17, `IT`: 13, `CE`: 7, `IS`: 5) con detección de programas híbridos. |
| **Unificación del Pipeline** | Coexistencia de scripts antiguos y nuevos en la misma carpeta. | Consolidación de [`corpus_CC2020/ejecutar_pipeline.py`](corpus_CC2020/ejecutar_pipeline.py) como único punto de entrada oficial y archivo de los scripts antiguos en `corpus_CC2020/datos_originales_backup/scripts_originales/`. |
