# LIMITACIONES METODOLÓGICAS, DOCUMENTALES Y DE VALIDEZ (`LIMITACIONES.md`)

Para que esta investigación sea defendible ante un comité doctoral o arbitraje académico por pares (*peer review*), se declaran de forma explícita y transparente las siguientes limitaciones del estudio:

## 1. Limitaciones de la Fuente Documental y Granularidad del Corpus (Fase 9)

1. **Clasificación basada en denominaciones de asignaturas (ausencia de sílabos/programas analíticos completos):**
   - En los 60 planes de estudio (`D016`–`D075`), la información disponible consiste en la retícula curricular (nombre oficial de la asignatura, semestre/periodo, peso en créditos u horas y condición obligatoria/optativa). No se dispone de los sílabos extensos (*syllabi*) con el desglose semanal de temas y bibliografía de las 2,109 asignaturas.
   - Aunque el libro de códigos ([`CODEBOOK_CC2020.md`](CODEBOOK_CC2020.md)) corrige las colisiones léxicas e introduce pesos híbridos ($0.5/0.5$) para asignaturas mixtas, dos cursos con el mismo título (p. ej., *Ingeniería de Software I* o *Sistemas Operativos*) pueden impartirse con un enfoque más formal o más práctico según la cátedra de cada universidad.

2. **Diferencias de granularidad entre `D016`–`D038` y `D039`–`D075`:**
   - Los registros `D016`–`D031` y `D033`–`D038` ($n = 22$, etiquetados como `Malla_Curricular_Completa`) transcriben la totalidad de las asignaturas de la retícula oficial (entre 42 y 67 asignaturas por plan).
   - Los registros `D039`–`D075` ($n = 37$, etiquetados como `Malla_Troncal_Sintetizada`) contienen el núcleo troncal obligatorio completo pero sintetizan las asignaturas electivas y complementarias en registros agrupados (entre 24 y 38 entradas por plan), además de no disponer de archivo `.txt` local en `fuentes_bloque_04/` o `05/`.
   - En 12 registros de los Bloques 4 y 5 (`D047`, `D049`, `D052`, `D053`, `D056`, `D058`, `D064`, `D069`, `D070`, `D072`, `D073`, `D074`), el campo `URL_Fuente` apunta al dominio raíz de la universidad (`Dominio_Institucional_Raiz`) en lugar del enlace profundo al PDF de la malla.

3. **Truncamiento de los Estudios Generales en `D032` (PUCP, Perú):**
   - El documento oficial de la Facultad de Ciencias e Ingeniería de la PUCP (`corpus_CC2020/fuentes_bloque_03/D032.txt`) reporta exclusivamente los ciclos 5 a 10 de la carrera (128 créditos de especialidad) y omite los ciclos 1 a 4 correspondientes a *Estudios Generales Ciencias* (~72 créditos de Cálculo, Física, Álgebra Lineal y Química).
   - Esta omisión desplaza artificialmente a `D032` hasta $X_{\text{global}} = +3.15$ (el valor más alto de los 60 planes). Por esta razón, `D032` se etiqueta explícitamente como `Malla_Parcial_Especialidad` (`Comparable_Estrictamente = False`) y todas las pruebas de correlación y regresión en [`VALIDACION_ESTADISTICA.md`](VALIDACION_ESTADISTICA.md) se reportan tanto con $n = 60$ como con $n = 59$ (excluyendo `D032`).

4. **Reconciliación y cobertura parcial de descargas crudas en `corpus_CC2020/fuentes_bloque_03/`:**
   - Durante la recolección original del Bloque 3, los archivos descargados en `fuentes_bloque_03/` habían quedado numerados según lotes preliminares (`_fuentes_lote1.json` a `lote5.json`). En la segunda auditoría se reconciliaron todos los nombres de archivo con su ID definitivo real y se documentó su trazabilidad en [`corpus_CC2020/fuentes_bloque_03/INDICE_CORRESPONDENCIA_FUENTES.md`](corpus_CC2020/fuentes_bloque_03/INDICE_CORRESPONDENCIA_FUENTES.md) (respaldando los lotes preliminares en `corpus_CC2020/datos_originales_backup/lotes_preliminares_b3/`).
   - De los 15 planes del Bloque 3 (`D031`–`D045`), 8 cuentan con archivo fuente crudo local (`D031`, `D032`, `D033`, `D035`, `D038`, `D041`, `D042`, `D045`), mientras que los 7 restantes (`D034`, `D036`, `D037`, `D039`, `D040`, `D043`, `D044`) están registrados directamente en `corpus_CC2020/bloque_03_transcripcion.json` con su URL institucional verificada.

---

## 2. Limitaciones de la Comparación entre Perfiles de Egreso y Planes de Estudio (Fase 7)

1. **Incomparabilidad directa de unidades de observación:**
   - El Bloque 1 (`D001`–`D015`, $n = 15$) codifica proposiciones discursivas breves de perfiles de egreso ($N \in [2, 10]$ unidades por documento), mientras que los Bloques 2 a 5 (`D016`–`D075`, $n = 60$) codifican mallas curriculares ponderadas por créditos u horas ($24$ a $67$ asignaturas por documento).
   - En perfiles muy breves (`D004` con 2 unidades recuperadas de índice web, o `D002`, `D008`, `D009`, `D011`, `D015`), la ausencia de una mención explícita a fundamentos teóricos produce $P_t = 0 \implies X = +5.00$ por simple discretización de muestra pequeña.

2. **Tamaño reducido de pares institucionales exactos ($n = 2$):**
   - Aunque el corpus incluye 15 perfiles y 60 planes, solo existen **dos pares exactos del mismo programa e institución** (`D001`↔`D017` en IPN-ESCOM y `D003`↔`D034` en TecNM). Por tanto, el contraste entre perfil declarativo y malla curricular a nivel individual tiene carácter de estudio de casos múltiples ($n = 2$) y comparación ecológica a nivel de distribuciones ($n = 15$ vs. $n = 60$), sin que pueda inferirse una brecha uniforme para las 70 instituciones restantes cuyos perfiles declarativos no fueron muestreados.

---

## 3. Limitaciones de la Operacionalización Matemática y Validación Inter-Evaluador (Fases 5, 6 y 8)

1. **Carácter no oficial de las coordenadas $(X, Y)$ y de las etiquetas de afinidad:**
   - Como se establece en [`METODOLOGIA.md`](METODOLOGIA.md), el informe oficial **ACM/IEEE-CS CC2020** utiliza representaciones conceptuales cualitativas y semi-cuantitativas, pero no prescribe la fórmula $X = 5(P_a - P_t)/(P_a + P_t)$ ni umbrales numéricos de corte. Las etiquetas asignadas representan proximidades tipológicas dentro del modelo de esta investigación.

2. **Acoplamiento estructural parcial entre los ejes $X$ e $Y$:**
   - Dado que las asignaturas de Física de Semiconductores, Circuitos y Arquitectura de Computadoras son simultáneamente teóricas ($X = -5$) y de hardware ($Y = -5$), y que las asignaturas de Sistemas de Información, Gestión de Proyectos y Administración son simultáneamente aplicadas ($X = +5$) y organizacionales ($Y = +5$), los ejes $X$ e $Y$ no son ortogonales por construcción en el catálogo de asignaturas. Parte de la correlación positiva observada ($r = +0.5324$ en $n = 60$; $r = +0.4816$ en $n = 59$) refleja este acoplamiento epistémico inherente a las disciplinas de la computación.

3. **Alcance de la validación ciega independiente ($\kappa$ de Cohen sobre títulos sin sílabos):**
   - En esta versión se ejecutó una evaluación independiente ciega sobre la muestra estratificada de **120 asignaturas** siguiendo [`PROTOCOLO_REVISION_EXTERNA.md`](PROTOCOLO_REVISION_EXTERNA.md), obteniendo una concordancia sustancial a casi perfecta con `S1` ($\kappa_X = 0.7198, \kappa_{w,X} = 0.7350$; $\kappa_Y = 0.7751, \kappa_{w,Y} = 0.8560$; $\kappa_{\text{Dom}} = 0.7699$).
   - No obstante, tanto el clasificador `S1` como el evaluador ciego operan sobre la **denominación oficial de la asignatura** y el contexto del programa, sin contar con los sílabos extensos (*syllabi*). Asimismo, para un arbitraje multicéntrico futuro, la plantilla abierta [`corpus_CC2020/plantilla_evaluacion_ciega_120.csv`](corpus_CC2020/plantilla_evaluacion_ciega_120.csv) permite replicar la prueba con paneles adicionales de docentes universitarios de distintas subdisciplinas para estimar el $\alpha$ de Krippendorff multi-evaluador.
