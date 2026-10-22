# ÍNDICE DE RECONCILIACIÓN Y VERIFICACIÓN DE FUENTES — BLOQUE 3 (`D031`–`D045`)

## 1. Reconciliación de Identificadores de Archivos Descargados

Durante la recolección inicial del Bloque 3, el script preliminar `descargar_bloque_03.py` ejecutó descargas de prueba mediante cinco lotes auxiliares (`_fuentes_lote1.json` a `_fuentes_lote5.json`, archivados en `../datos_originales_backup/lotes_preliminares_b3/`) cuya numeración temporal no coincidía con la numeración definitiva de `bloque_03_transcripcion.json` y `bloque_03_datos.json`.

En la presente auditoría se verificó el contenido interno de cada archivo PDF, HTML y TXT y se reconciliaron los nombres de archivo en esta carpeta para que coincidan 1 a 1 con el identificador oficial `D031`–`D045`:

| ID Oficial | Institución y Programa | Estado en `bloque_03_transcripcion.json` | Archivo Local Reconciliado en `fuentes_bloque_03/` | Nombre Histórico en Lotes Preliminares |
| :---: | :--- | :--- | :--- | :--- |
| **`D031`** | UNAM — Facultad de Ingeniería (Ing. en Computación, Plan 2016/2023) | 44 asignaturas verificadas (408 créditos) | `D031.pdf`, `D031.txt` | `D031` (Lote 1 — sin cambio) |
| **`D032`** | PUCP — Facultad de Ciencias e Ingeniería (Ing. Informática, Plan 2026-2) | 39 asignaturas de ciclos 5–10 (128 créditos; omite Estudios Generales Ciencias ciclos 1–4) | `D032.pdf`, `D032.txt` | `D032` (Lote 1 — sin cambio) |
| **`D033`** | Universidad de Chile — FCFM-DCC (Ing. Civil en Computación, Plan 2019) | 46 asignaturas verificadas (300 créditos SCT) | `D033.html`, `D033.txt` | `D033` (Lote 1 — sin cambio) |
| **`D034`** | Tecnológico Nacional de México — TecNM (Ing. en Sistemas Computacionales, ISIC-2010-224) | 45 asignaturas verificadas (260 créditos SATCA; par exacto del perfil `D003`) | Transcrito en `construir_bloque_03.py` | No tenía archivo en lotes 1–5 (`D034.txt` antiguo correspondía a UBA) |
| **`D035`** | Universidad Nacional de La Plata — UNLP (Ing. en Computación, Plan 2024) | 36 asignaturas verificadas (216 horas/créditos) | `D035.html`, `D035.txt`, `D035_tables.json` | `D035` (Lote 2 — sin cambio) |
| **`D036`** | Universidad de Costa Rica — UCR-ECCI (Bachillerato en Computación con Varios Énfasis) | 28 registros troncales verificados (142 créditos) | Transcrito en `construir_bloque_03.py` | No tenía archivo en lotes 1–5 (`D036.txt` antiguo correspondía a PUC Chile) |
| **`D037`** | Universidad Técnica Particular de Loja — UTPL (Ing. en Tecnologías de la Información) | 45 asignaturas verificadas (135 créditos) | Transcrito en `construir_bloque_03.py` | No tenía archivo en lotes 1–5 (`D037.txt` antiguo correspondía a ITESM) |
| **`D038`** | Universidad Nacional Autónoma de Honduras — UNAH (Ing. en Sistemas Computacionales) | 50 asignaturas verificadas (205 UV: `ISC-101`, `MM-110`, etc.) | `D038.pdf`, `D038.txt` | Reconciliado desde `D040.pdf` / `D040.txt` (Lote 3/5) |
| **`D039`** | Universidad de los Andes — UniAndes (Ing. de Sistemas y Computación, ISIS 134) | 24 registros troncales verificados (135 créditos) | Transcrito en `construir_bloque_03.py` | `D039.txt` antiguo correspondía a UdelaR (`D046`) |
| **`D040`** | Universidad EAFIT (Ing. de Sistemas) | 30 registros troncales verificados (146 créditos) | Transcrito en `construir_bloque_03.py` | `D040.pdf` antiguo fue movido a `D038.pdf` (UNAH) |
| **`D041`** | Universidad de Buenos Aires — UBA FIUBA (Ing. en Informática, Plan 2020) | 28 registros troncales verificados (232 créditos) | `D041.html`, `D041.txt` | Reconciliado desde `D034.html` / `D034.txt` (Lote 2) |
| **`D042`** | Pontificia Universidad Católica de Chile — PUC Chile (Lic. en Ciencias de la Ing. / Civil Computación) | 25 registros troncales verificados (400 créditos UC) | `D042.html`, `D042.txt` | Reconciliado desde `D036.html` / `D036.txt` (Lote 2) |
| **`D043`** | Universidad Autónoma Metropolitana — UAM Azcapotzalco (Lic. en Ing. en Computación) | 32 registros troncales verificados (459 créditos UEA) | Transcrito en `construir_bloque_03.py` | `D043.txt` antiguo era duplicado de PUC Chile |
| **`D044`** | Universidad de Guadalajara — UdeG CUCEI (Ing. en Computación, ICOM) | 31 registros troncales verificados (370 créditos) | Transcrito en `construir_bloque_03.py` | `D044.pdf` antiguo era un folleto de la Escuela de Física UNAH |
| **`D045`** | Tecnológico de Monterrey — ITESM (Ing. en Tecnologías Computacionales, Modelo Tec21) | 25 bloques/módulos verificados (144 créditos) | `D045.html`, `D045.txt`, `D045_tables.json` | Reconciliado desde `D038.html` / `D038.txt` (Lote 2) |

