# RESULTADOS EMPÍRICOS AUDITADOS DEL PROYECTO CC2020 (`RESULTADOS.md`)

## 1. Caracterización General del Corpus Auditado (`D001`–`D075`)

El corpus analizado comprende **75 documentos curriculares oficiales** correspondientes a **73 programas académicos únicos** impartidos en **72 instituciones de educación superior** de **15 países de América Latina**. Los datos completos se encuentran en [`corpus_CC2020/corpus_CC2020_consolidado_75.csv`](file:///c:/Users/Aliximber/Desktop/DOCUMENTOS/corpus_CC2020/corpus_CC2020_consolidado_75.csv).

Al separar rigurosamente las dos poblaciones documentales que integran el estudio, se obtienen los siguientes parámetros distributivos:

| Población Documental | Registros | $n$ | Media $X_{\text{global}}$ (DE) | Mediana $X_{\text{global}}$ (IQR) | Media $X_{\text{comp}}$ (DE) | Media $Y$ (DE) | Mediana $Y$ (IQR) | Radio Medio $R$ |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Población A: Perfiles de Egreso** | `D001`–`D015` | $15$ | $+3.90$ ($0.85$) | $+3.75$ ($1.55$) | $+3.90$ ($0.85$) | $+0.82$ ($1.44$) | $+0.71$ ($2.29$) | $2.98$ |
| **Población B: Planes de Estudio (Total)** | `D016`–`D075` | $60$ | $-0.19$ ($1.24$) | $-0.35$ ($1.49$) | $+1.69$ ($1.35$) | $+0.10$ ($0.80$) | $+0.17$ ($0.90$) | $5.44$ |
| **Población B*: Planes sin `D032` (PUCP parcial)** | `D016`–`D075` $\setminus \{\text{D032}\}$ | $59$ | $-0.25$ ($1.17$) | $-0.37$ ($1.47$) | $+1.65$ ($1.34$) | $+0.07$ ($0.78$) | $+0.14$ ($0.87$) | $5.45$ |

---

## 2. Hallazgo Central 1: Hibridación Estructural y Distribución Real de Afinidades CC2020

### 2.1. Corrección del sesgo hacia `CS` y emergencia de `IT` y `SE`
En la versión previa a la auditoría, la combinación de incluir el tronco general de Ciencias Básicas (`STEM`) en $P_t$ y de exigir un umbral algebraicamente inalcanzable para `IT` llevó a clasificar **40 de los 60 planes (66.7%) como `CS`** y **0 de los 60 planes (0.0%) como `IT`**.

Una vez separado el peso del tronco general `STEM` (que representa en promedio el **$28.51\%$** del peso curricular clasificado de los planes latinoamericanos) y evaluado el vector de los 5 dominios propios de computación $(p_{\text{CE}}, p_{\text{CS}}, p_{\text{SE}}, p_{\text{IT}}, p_{\text{IS}})$, la distribución real de los **60 planes de estudio** muestra un panorama plural y equilibrado:

| Disciplina CC2020 | Conteo Original (`S0`) | Regla Corregida (`S1`) | Similitud Coseno Principal | Peso Medio del Dominio en el Núcleo Computacional | Programas Representativos (`S1`) |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Computer Science (`CS`)** | $40$ ($66.7\%$) | **$18$ ($30.0\%$)** | **$18$ ($30.0\%$)** | $27.4\%$ (mediana $27.1\%$) | `D020` (UNAL), `D033` (UChile), `D036` (UCR), `D046` (UdelaR), `D061` (USP), `D062` (UNICAMP), `D065` (UNC FAMAF), `D066` (TEC) |
| **Software Engineering (`SE`)** | $10$ ($16.7\%$) | **$17$ ($28.3\%$)** | **$15$ ($25.0\%$)** | $27.6\%$ (mediana $28.5\%$) | `D018` (UABC), `D022` (USonsonate), `D024` (UNAD), `D034` (TecNM), `D040` (EAFIT), `D045` (ITESM), `D052` (UTP), `D073` (UADY) |
| **Information Technology (`IT`)** | $0$ ($0.0\%$) | **$13$ ($21.7\%$)** | **$16$ ($26.7\%$)** | $22.4\%$ (mediana $22.7\%$) | `D016` (UDLAP), `D026` (UNLPam), `D030` (UNIR), `D037` (UTPL), `D038` (UNAH), `D039` (UniAndes), `D047` (UNSA), `D059` (PUCE), `D070` (UV) |
| **Computer Engineering (`CE`)** | $6$ ($10.0\%$) | **$7$ ($11.7\%$)** | **$6$ ($10.0\%$)** | $11.0\%$ (mediana $9.2\%$) | `D017` (IPN-ESCOM), `D031` (UNAM), `D035` (UNLP), `D043` (UAM), `D050` (UANL), `D055` (UNMSM), `D058` (UASLP) |
| **Information Systems (`IS`)** | $4$ ($6.7\%$) | **$5$ ($8.3\%$)** | **$5$ ($8.3\%$)** | $11.6\%$ (mediana $9.3\%$) | `D023` (UNAC Callao), `D025` (UTN), `D032` (PUCP*), `D054` (Univalle), `D075` (UCR Informática Empresarial) |

### 2.2. Evidencia cuantitativa del carácter generalista e híbrido («Multidisciplinar»)
El cálculo del **Índice de Herfindahl–Hirschman ($\text{HHI} \in [0.20, 1.00]$)** y de la **Entropía de Shannon Normalizada ($H_{\text{norm}} \in [0, 1]$)** sobre los 5 dominios de computación en los 60 planes revela:
- **Media de $\text{HHI} = 0.2596$** (muy cercana al mínimo teórico de perfecta equidistribución $0.2000$ y muy alejada de la especialización monodisciplinar $1.0000$).
- **Media de Entropía Normalizada $H_{\text{norm}} = 0.8925$** (el $89.3\%$ de la máxima diversidad curricular posible entre las 5 disciplinas CC2020).
- **40 de los 60 planes de estudio ($66.7\%$)** presentan un margen de similitud coseno $\Delta S = S_{d_1} - S_{d_2} < 0.08$ entre su primera y segunda disciplina de referencia (`Es_Hibrido = True`), predominando las combinaciones **`SE/IT`**, **`CS/SE`** e **`IT/SE`**.
- **Conclusión científica:** Los programas latinoamericanos de computación e ingeniería de sistemas no siguen el modelo anglosajón de nicho monodisciplinar estricto, sino un **modelo de ingeniería generalista de espectro amplio** que combina una base de ciencias de la ingeniería (`STEM` $\approx 28.5\%$) con proporciones casi equivalentes de fundamentos de Ciencias de la Computación (`CS` $\approx 27.4\%$), Ingeniería de Software (`SE` $\approx 27.6\%$) y Tecnologías de la Información (`IT` $\approx 22.4\%$), flanqueadas por núcleos menores de Hardware (`CE` $\approx 11.0\%$) y Gestión Organizacional (`IS` $\approx 11.6\%$).

---

## 3. Hallazgo Central 2: Reevaluación de la «Brecha» entre Perfiles de Egreso y Planes de Estudio

En la interpretación previa a la auditoría se afirmaba que existía una «brecha o esquizofrenia curricular» masiva entre el discurso institucional de los perfiles de egreso ($\bar{X} = +3.90$) y la realidad formativa de los planes de estudio ($\bar{X}_{\text{global}} = -0.19$, diferencia bruta de $4.09$ unidades).

La auditoría demuestra que **comparar directamente $\bar{X}_{\text{perfil}}$ contra $\bar{X}_{\text{global}}$ conlleva un sesgo metodológico**, por dos razones verificables:

1. **Descomposición del efecto del tronco `STEM`:** Los perfiles de egreso describen las competencias profesionales terminales del graduado en el mercado laboral (donde ninguna universidad redacta *«El egresado sabrá resolver integrales triples y problemas de cinemática»*), mientras que la malla curricular completa contabiliza los primeros 4 semestres de Cálculo, Álgebra y Física. Cuando se compara el perfil de egreso contra el **núcleo de asignaturas de computación del plan de estudios ($X_{\text{comp}}$)**, la media de los 60 planes pasa de $\bar{X}_{\text{global}} = -0.19$ a **$\bar{X}_{\text{comp}} = +1.69$**. Es decir, **el $46.0\%$ de la distancia aparente en el Eje $X$ ($1.88$ de $4.09$ unidades) es un efecto contable del tronco obligatorio de ciencias básicas (`STEM`)** y no una contradicción en la enseñanza de la computación.
2. **Verificación en los dos pares institucionales exactos del corpus:**
   - **Par 1 — IPN–ESCOM (`D001` Perfil vs. `D017` Plan, ISC 2020):**
     - Perfil declarativo (`D001`): $X = +2.50, Y = +1.25$.
     - Malla global con STEM (`D017`): $X_{\text{global}} = -0.35, Y = -0.51$ ($\Delta X = 2.85$ unidades).
     - Malla de computación sin STEM (`D017`): **$X_{\text{comp}} = +1.03$** ($\Delta X$ se reduce a la mitad: $1.47$ unidades). Persiste, no obstante, un desplazamiento real en $Y$ ($\Delta Y = 1.76$), pues la malla de ESCOM contiene una fuerte carga obligatoria de electrónica y diseño digital ($C_h = 60$ créditos, $Y = -0.51$) que está subrepresentada en la redacción ejecutiva del perfil de egreso.
   - **Par 2 — TecNM (`D003` Perfil vs. `D034` Plan, ISIC-2010-224):**
     - Perfil declarativo (`D003`): $X = +4.44, Y = 0.00$.
     - Malla global con STEM (`D034`): $X_{\text{global}} = -0.06, Y = +0.08$ ($\Delta X = 4.50$ unidades).
     - Malla de computación sin STEM (`D034`): **$X_{\text{comp}} = +2.00, Y = +0.08$** ($\Delta X$ se reduce a $2.44$ unidades y la alineación en $Y$ es prácticamente exacta: $\Delta Y = -0.08$). En TecNM, una vez descontadas las 10 asignaturas de Cálculo, Álgebra, Ecuaciones Diferenciales, Probabilidad, Física y Química, el núcleo de computación es netamente aplicado ($X_{\text{comp}} = +2.00$), en plena coherencia direccional con su perfil de egreso.

---

## 4. Hallazgo Central 3: Diferenciación por Familia de Denominación y Tradición Nacional

### 4.1. Identidad curricular de *Ingeniería en Sistemas Computacionales (ISC)* frente a otras denominaciones
Las pruebas de Kruskal–Wallis confirman que la denominación del programa no es arbitraria ($p = 0.0070$ en $X$, $p = 0.0004$ en $Y$):
1. **Ciencias de la Computación e Ingeniería en Computación (`IC/CC`, $n=15$):** Se ubican claramente en el Cuadrante III ($\bar{X} = -0.79, \bar{Y} = -0.65$), con el mayor peso de algoritmia/teoría y de arquitectura/hardware.
2. **Ingeniería de Sistemas (`IS`, tradición andina y rioplatense, $n=23$):** Presenta un eje $X$ ligeramente teórico ($\bar{X} = -0.35$) debido a un fuerte ciclo básico de matemáticas y física, pero se desplaza de forma estadísticamente significativa hacia el polo organizacional en el Eje $Y$ ($\bar{Y} = +0.39$, mediana $+0.37$), integrando gestión, investigación de operaciones y sistemas de información empresarial.
3. **Ingeniería en Sistemas Computacionales (`ISC`, tradición mexicana y centroamericana, $n=8$):** Ocupa una posición puente distintiva ($\bar{X}_{\text{global}} = +0.66, \bar{Y} = +0.21$), más aplicada en software e infraestructura (`SE`/`IT`) que la *Ingeniería en Computación*, pero con mucha mayor presencia de arquitectura digital y redes que la *Ingeniería de Sistemas* sudamericana.
4. **Ingeniería de Software y Tecnologías de la Información (`ISW/TI`, $n=6$):** Se sitúa en el extremo más aplicado y organizacional/servicios de las mallas curriculares ($\bar{X} = +1.15$, mediana $+1.53$; $\bar{Y} = +0.54$, mediana $+0.61$).

### 4.2. Acoplamiento positivo entre $X$ e $Y$ dentro de los Planes de Estudio
Dentro de los 60 planes de estudio existe una asociación positiva moderada y estadísticamente significativa entre $X$ e $Y$ (**$r = +0.5345, p = 0.0001$**; y excluyendo la malla parcial `D032` PUCP, **$r = +0.4841, p = 0.0002$**; en el núcleo sin STEM, **$r = +0.5117, p = 0.0002$**). Esta pendiente positiva ($\beta_1 \approx +0.35$) refleja que los programas latinoamericanos se distribuyen a lo largo de una diagonal que va desde el **polo científico-físico y de hardware (Cuadrante III: `CE`/`CS`)** hasta el **polo de desarrollo aplicado, infraestructura y gestión organizacional (Cuadrante I: `SE`/`IT`/`IS`)**, dejando prácticamente desierto el Cuadrante IV de hardware puramente aplicado sin fundamentación físico-matemática.

