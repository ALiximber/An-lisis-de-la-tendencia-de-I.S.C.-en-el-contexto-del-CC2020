# REGISTRO DE CAMBIOS METODOLÓGICOS, COMPUTACIONALES Y DE RESULTADOS (`CAMBIOS_METODOLOGICOS.md`)

## 1. Preservación de Datos Originales y Punto de Recuperación

Antes de ejecutar cualquier modificación sobre el repositorio local, se establecieron dos mecanismos de preservación íntegra:
1. **Etiqueta Git de respaldo:** Se creó el tag local `backup-original-pre-audit` apuntando al commit original previo a la intervención (`37b3643`).
2. **Copia física íntegra:** Se respaldaron todos los archivos JSON, CSV, informes Markdown, imágenes PNG y scripts Python originales en [`corpus_CC2020/datos_originales_backup/`](file:///c:/Users/Aliximber/Desktop/DOCUMENTOS/corpus_CC2020/datos_originales_backup/) y [`corpus_CC2020/datos_originales_backup/scripts_originales/`](file:///c:/Users/Aliximber/Desktop/DOCUMENTOS/corpus_CC2020/datos_originales_backup/scripts_originales/).

---

## 2. Arquitectura de Software Implementada (Fase 11)

Se refactorizó la estructura ad-hoc de scripts duplicados en un paquete modular, tipado y cubierto por pruebas unitarias dentro de [`corpus_CC2020/`](file:///c:/Users/Aliximber/Desktop/DOCUMENTOS/corpus_CC2020/):

| Archivo / Módulo | Función Técnica |
| :--- | :--- |
| [`corpus_CC2020/src/metadatos.py`](file:///c:/Users/Aliximber/Desktop/DOCUMENTOS/corpus_CC2020/src/metadatos.py) | Normalización de metadatos (`D001`–`D075`), resolución de duplicados institucionales (`Institucion_ID`, `Programa_ID`), emparejamiento exacto Perfil↔Plan (`D001`↔`D017`, `D003`↔`D034`), corrección de año verificado (`D023` $\to$ `2023`), clasificación en 5 familias de denominación y evaluación de granularidad documental y calidad de URL. |
| [`corpus_CC2020/src/codebook.py`](file:///c:/Users/Aliximber/Desktop/DOCUMENTOS/corpus_CC2020/src/codebook.py) | Implementación del libro de códigos unificado de 27 reglas jerárquicas (`R01` a `R27`), normalización de condición curricular (`Obligatoria`, `Obligatoria_Eleccion_Cerrada`, `Optativa_Generica`, `Optativa_Catalogo`), pesos híbridos ($0.5/0.5$) y mapeo simultáneo a polos $(X, Y)$ y a los 6 dominios curriculares (`STEM`, `CE`, `CS`, `SE`, `IT`, `IS`). |
| [`corpus_CC2020/src/coordenadas.py`](file:///c:/Users/Aliximber/Desktop/DOCUMENTOS/corpus_CC2020/src/coordenadas.py) | Motor de cálculo de coordenadas globales ($X_{\text{global}}, Y$), coordenadas exclusivas de computación sin sesgo `STEM` ($X_{\text{comp}}, \Delta X_{\text{STEM}}$), radio de dispersión binario y real, vectores de 5 y 6 dominios, índice HHI, entropía de Shannon, afinidad disciplinaria multicriterio (regla corregida y similitud coseno contra arquetipos CC2020) y PCA de 6 dominios. |
| [`corpus_CC2020/src/estadistica.py`](file:///c:/Users/Aliximber/Desktop/DOCUMENTOS/corpus_CC2020/src/estadistica.py) | Estimación de densidad kernel 2D (Scott, Silverman, fijo) con cálculo exacto de Regiones de Alta Densidad (HDR 50%, 80%, 95%), regresión Nadaraya–Watson con selección de ancho de banda por LOOCV, tamaño muestral efectivo $N_{\text{eff}}(x)$, bandas de confianza bootstrap al 95% ($B=1,000$), pruebas exactas por permutación ($10,000$ réplicas) para Pearson $r$ y Spearman $\rho_S$, regresión OLS/cuadrática y prueba de Kruskal–Wallis por familia y país. |
| [`corpus_CC2020/src/validacion_empirica.py`](file:///c:/Users/Aliximber/Desktop/DOCUMENTOS/corpus_CC2020/src/validacion_empirica.py) | Generación de la muestra estratificada de auditoría manual ($n=120$ asignaturas en `auditoria_muestra_estratificada.csv`) y ejecución del análisis de sensibilidad en 6 escenarios (`S0` a `S5` en `analisis_sensibilidad.csv`). |
| [`corpus_CC2020/src/visualizaciones.py`](file:///c:/Users/Aliximber/Desktop/DOCUMENTOS/corpus_CC2020/src/visualizaciones.py) | Generación de las 11 visualizaciones científicas en alta resolución (300 DPI): los 5 mapas por bloque actualizados, el mapa maestro corregido y las 5 nuevas figuras analíticas comparativas. |
| [`corpus_CC2020/ejecutar_pipeline.py`](file:///c:/Users/Aliximber/Desktop/DOCUMENTOS/corpus_CC2020/ejecutar_pipeline.py) | Orquestador reproducible de extremo a extremo que regenera todos los archivos JSON, CSV, resúmenes estadísticos y gráficos. |
| [`corpus_CC2020/tests/test_pipeline.py`](file:///c:/Users/Aliximber/Desktop/DOCUMENTOS/corpus_CC2020/tests/test_pipeline.py) | Suite de pruebas unitarias (`unittest`) que verifica conteos, ausencia de asignaturas sin clasificar, corrección de colisiones léxicas, cotas matemáticas y existencia de artefactos. |

---

## 3. Comparación Cuantitativa: Metodología Original (`S0`) vs. Metodología Corregida (`S1`)

### 3.1. Nivel de Asignaturas ($N = 2,109$ registros en Bloques 2 a 5)
- **Inconsistencias entre bloques eliminadas:** De **132 nombres únicos** que cambiaban de clasificación según el script de bloque a **0 inconsistencias** (función única determinista).
- **Asignaturas sin clasificar:** **0 asignaturas** (`100.0%` de reconocimiento por las 27 reglas del libro de códigos).
- **Asignaturas modificadas respecto al cálculo original:** **102 de 2,109 asignaturas ($4.84\%$)**, compuestas por:
  - **72 correcciones de errores léxicos o de condición ($3.41\%$):** Corrección de colisiones de subcadenas (`Fundamentos de Infraestructura Tecnológica`, `Física de los Sistemas de Información`, `Cálculo Avanzado y Aplicaciones`, `Arquitectura y Organización de Computadores`, `Modelado y Automatización de Procesos Empresariales`, `Principios Eléctricos y Aplicaciones Digitales`, `Planificación Estratégica y Sistemas de Calidad Empresarial`, `Aplicación Práctica de Programación`, `Temas Selectos de Matemáticas`) y exclusión de las 12 electivas de catálogo infiltradas en `D023` (UNAC Callao).
  - **30 refinamientos híbridos ($1.42\%$):** Asignación de pesos fraccionarios ($0.5/0.5$) a asignaturas intrínsecamente mixtas (`Lenguaje(s) de Programación`, `Minería/Ciencia de Datos`, `Computación Gráfica`, `Interacción Humano-Computador`).

### 3.2. Nivel de Coordenadas de Planes de Estudio ($n = 60$)
- **Correlación entre coordenadas originales (`S0`) y corregidas (`S1`):**
  - Eje $X$: **$r = 0.9769$**, Error Absoluto Medio $\text{MAE}_X = 0.195$ unidades.
  - Eje $Y$: **$r = 0.9639$**, Error Absoluto Medio $\text{MAE}_Y = 0.108$ unidades.
  - Distancia euclidiana 2D media: **$0.249$ unidades**.
- **Los 10 programas con mayor corrección de posición 2D (`Shift_Distancia`):**
  1. **`D029` (Universidad EAN, Colombia):** $(-1.51, +0.26) \to (-0.88, +1.20)$, $\Delta_{2D} = 1.13$ (corrección de asignaturas de gestión/sistemas y seminarios).
  2. **`D051` (UNA, Paraguay):** $(-1.12, -0.14) \to (-0.37, -0.14)$, $\Delta_{2D} = 0.75$ (unificación de *Lenguajes de Programación I/II* y *Minería de Datos* como híbridas).
  3. **`D047` (UNSA Arequipa, Perú):** $(+1.00, +1.00) \to (+0.60, +0.47)$, $\Delta_{2D} = 0.67$ (*Arquitectura y Organización de Computadores* dejó de clasificarse erróneamente como Administración `(A, O)` y pasó a Hardware `(T, H)`).
  4. **`D057` (USM, Chile):** $(-1.36, +1.25) \to (-1.05, +0.69)$, $\Delta_{2D} = 0.64$ (*Arquitectura y Organización de Computadores* corregida de `(A, O)` a `(T, H)`).
  5. **`D037` (UTPL, Ecuador):** $(+1.90, +0.71) \to (+2.41, +0.92)$, $\Delta_{2D} = 0.55$ (*Planificación Estratégica y Sistemas de Calidad Empresarial* corregida de `(A, S)` a `(A, O)`).
  6. **`D070` (Universidad Veracruzana, México):** $(0.00, -0.59) \to (+0.45, -0.29)$, $\Delta_{2D} = 0.54$ (ajuste en redes/telecomunicaciones y tecnologías).
  7. **`D042` (PUC Chile):** $(-1.36, 0.00) \to (-0.83, 0.00)$, $\Delta_{2D} = 0.53$ (refinamiento híbrido en ciencia de datos y lenguajes).
  8. **`D058` (UASLP, México):** $(-1.43, -1.39) \to (-0.92, -1.45)$, $\Delta_{2D} = 0.51$ (recuperación de *Temas Selectos de Matemáticas* y ajuste en redes/hardware).
  9. **`D032` (PUCP, Perú):** $(+3.09, +1.31) \to (+3.15, +1.80)$, $\Delta_{2D} = 0.49$ (*Modelado y Automatización de Procesos Empresariales* dejó de clasificarse como Hardware `(A, H)` y pasó a Organización `(A, O)`).
  10. **`D050` (UANL, México):** $(-1.55, -0.48) \to (-1.39, -0.94)$, $\Delta_{2D} = 0.49$ (recuperación de *Aplicación Práctica de Programación*, antes excluida por error como práctica profesional).

### 3.3. Nivel de Afinidad Disciplinaria CC2020 ($n = 60$ planes)
| Categoría | Original (`S0`) | Regla Corregida (`S1`) | Similitud Vectorial (`S1`) | Explicación del Cambio |
| :--- | :---: | :---: | :---: | :--- |
| **`CS`** | $40$ ($66.7\%$) | $18$ ($30.0\%$) | $18$ ($30.0\%$) | Se eliminó el sesgo que sumaba Cálculo, Física y Química al numerador de Ciencia de la Computación. |
| **`SE`** | $10$ ($16.7\%$) | $17$ ($28.3\%$) | $15$ ($25.0\%$) | Programas con fuerte peso de desarrollo e ingeniería de software (`D034` TecNM, `D040` EAFIT, `D045` ITESM, `D052` UTP) pasan de `CS` a `SE`. |
| **`IT`** | $0$ ($0.0\%$) | $13$ ($21.7\%$) | $16$ ($26.7\%$) | Se corrigió la imposibilidad algebraica de `IT`, identificando correctamente a `D037` (UTPL), `D059` (PUCE), `D016` (UDLAP), `D030` (UNIR), `D070` (UV), etc. |
| **`CE`** | $6$ ($10.0\%$) | $7$ ($11.7\%$) | $6$ ($10.0\%$) | Se incorpora `D050` (UANL) junto con `D017` (IPN-ESCOM), `D031` (UNAM), `D035` (UNLP), `D043` (UAM), `D055` (UNMSM) y `D058` (UASLP). |
| **`IS`** | $4$ ($6.7\%$) | $5$ ($8.3\%$) | $5$ ($8.3\%$) | Se incorpora `D054` (Univalle) junto con `D023` (UNAC), `D025` (UTN), `D032` (PUCP) y `D075` (UCR Empresarial). |
