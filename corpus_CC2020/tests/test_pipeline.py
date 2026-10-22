"""Suite de pruebas automatizadas (unittest) para validar la integridad matemática,
metodológica, estadística y documental del proyecto CC2020 (Fases 4 a 15 y Segunda Auditoría).
"""
from __future__ import annotations
from collections import Counter
import csv
import json
import math
import sys
import unittest
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ROOT_DIR = BASE_DIR.parent
DEPS_DIR = BASE_DIR / ".deps"
if DEPS_DIR.exists() and str(DEPS_DIR) not in sys.path:
    sys.path.insert(0, str(DEPS_DIR))
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from src.codebook import CODEBOOK_RULES, classify_course
from src.coordenadas import build_full_corpus
from src.estadistica import kde_2d_hdr, nadaraya_watson_loocv, nadaraya_watson_fit


class TestCC2020AuditPipeline(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.corpus = build_full_corpus(BASE_DIR)
        cls.all_docs = cls.corpus["all_docs"]
        cls.plan_docs = cls.corpus["plan_docs"]
        cls.profile_docs = cls.corpus["profile_docs"]

    def test_01_corpus_counts_and_populations(self) -> None:
        """Verifica que existan exactamente 75 documentos: 15 perfiles (D001-D015) y 60 planes (D016-D075)."""
        self.assertEqual(len(self.all_docs), 75)
        self.assertEqual(len(self.profile_docs), 15)
        self.assertEqual(len(self.plan_docs), 60)

        # Verificar instituciones únicas (72) y programas únicos (73)
        inst_ids = {r["Institucion_ID"] for r in self.all_docs}
        prog_ids = {r["Programa_ID"] for r in self.all_docs}
        self.assertEqual(len(inst_ids), 72)
        self.assertEqual(len(prog_ids), 73)

        # Verificar países reales (15 países en total)
        paises = {r["Pais"] for r in self.all_docs}
        self.assertEqual(len(paises), 15)

    def test_02_zero_unmatched_courses(self) -> None:
        """Verifica que ninguna de las 2,109 asignaturas de los Bloques 2-5 quede sin regla (R00_UNMATCHED)."""
        total_courses = 0
        for b in range(2, 6):
            for c in self.corpus["courses_by_block"][b]:
                total_courses += 1
                self.assertNotEqual(
                    c["Regla_ID"],
                    "R00_UNMATCHED",
                    f"Asignatura sin clasificar en {c['ID']}: {c['Asignatura']}",
                )
        self.assertEqual(total_courses, 2109)

    def test_03_semantic_collision_fixes(self) -> None:
        """Comprueba que todos los errores de colisión de subcadenas detectados en la auditoría estén corregidos."""
        # 1. 'logica' dentro de 'tecnologica' no debe ser Teoría (T, S)
        c1 = classify_course("Fundamentos de Infraestructura Tecnológica", "Obligatoria")
        self.assertEqual(c1["Pole_X"], "A")
        self.assertEqual(c1["Dominio_Principal"], "IT")

        # 2. 'Física de los Sistemas de Información' (D041 UBA) es Física (STEM), no Sistemas de Información (A, O)
        c2 = classify_course("Física de los Sistemas de Información", "Obligatoria")
        self.assertEqual(c2["Pole_X"], "T")
        self.assertEqual(c2["Pole_Y"], "")
        self.assertEqual(c2["Dominio_Principal"], "STEM")

        # 3. 'Cálculo Avanzado y Aplicaciones' (D033 UChile) es Matemática (STEM), no Software Aplicado (A, S)
        c3 = classify_course("Cálculo Avanzado y Aplicaciones", "Obligatoria")
        self.assertEqual(c3["Pole_X"], "T")
        self.assertEqual(c3["Pole_Y"], "")
        self.assertEqual(c3["Dominio_Principal"], "STEM")

        # 4. 'Arquitectura y Organización de Computadores' es Hardware (H), no Negocios (A, O)
        c4 = classify_course("Arquitectura y Organización de Computadores", "Obligatoria")
        self.assertEqual(c4["Pole_X"], "T")
        self.assertEqual(c4["Pole_Y"], "H")
        self.assertEqual(c4["Dominio_Principal"], "CE")

        # 5. 'Modelado y Automatización de Procesos Empresariales' es Organización/IS (A, O), no Robótica/Hardware (A, H)
        c5 = classify_course("Modelado y Automatización de Procesos Empresariales", "Obligatoria")
        self.assertEqual(c5["Pole_X"], "A")
        self.assertEqual(c5["Pole_Y"], "O")
        self.assertEqual(c5["Dominio_Principal"], "IS")

        # 6. 'Principios Eléctricos y Aplicaciones Digitales' (D034 TecNM) es Hardware (CE), no Software (A, S)
        c6 = classify_course("Principios Eléctricos y Aplicaciones Digitales", "Obligatoria")
        self.assertEqual(c6["Pole_Y"], "H")
        self.assertEqual(c6["Dominio_Principal"], "CE")

        # 7. 'Aplicación Práctica de Programación' (D050 UANL) no debe excluirse como práctica profesional
        c7 = classify_course("Aplicación Práctica de Programación", "Obligatoria")
        self.assertEqual(c7["Pole_X"], "A")
        self.assertEqual(c7["Pole_Y"], "S")

        # 8. Consistencia singular/plural en Lenguaje(s) de Programación
        c8_pl = classify_course("Lenguajes de Programación I", "Obligatoria")
        c8_sg = classify_course("Lenguaje de Programación I", "Obligatoria")
        self.assertEqual(c8_pl["Regla_ID"], c8_sg["Regla_ID"])

        # 9. Electivas de catálogo en D023 se excluyen en modo estándar
        c9 = classify_course("Robótica", "Electivo", modo="estandar")
        self.assertEqual(c9["Regla_ID"], "R01_EXCL_OPT")
        self.assertEqual(c9["Condicion_Normalizada"], "Optativa_Catalogo")

        # 10. 'Modelos estocásticos y simulación en computación y comunicaciones' (D020) es STEM (T, None)
        c10 = classify_course("Modelos estocásticos y simulación en computación y comunicaciones", "Obligatoria")
        self.assertEqual(c10["Regla_ID"], "R27_STEM_BASIC")
        self.assertEqual(c10["Pole_X"], "T")
        self.assertEqual(c10["Pole_Y"], "")
        self.assertEqual(c10["Dominio_Principal"], "STEM")

    def test_04_coordinate_bounds_and_formulas(self) -> None:
        """Verifica que todas las coordenadas X e Y estén en [-5, +5] y cumplan las identidades algebraicas."""
        for r in self.plan_docs:
            x = r["Coordenada_X"]
            y = r["Coordenada_Y"]
            xc = r["X_Computacion"]
            self.assertGreaterEqual(x, -5.0)
            self.assertLessEqual(x, 5.0)
            self.assertGreaterEqual(y, -5.0)
            self.assertLessEqual(y, 5.0)
            self.assertGreaterEqual(xc, -5.0)
            self.assertLessEqual(xc, 5.0)

            # Verificar fórmula exacta de X e Y
            pt, pa = r["Pt"], r["Pa"]
            ch, cs, co = r["Ch"], r["Cs"], r["Co"]
            self.assertGreater(pt + pa, 0.0)
            self.assertGreater(ch + cs + co, 0.0)
            x_calc = round(5.0 * (pa - pt) / (pa + pt), 2)
            y_calc = round(5.0 * (co - ch) / (ch + cs + co), 2)
            self.assertAlmostEqual(x, x_calc, places=2)
            self.assertAlmostEqual(y, y_calc, places=2)

            # Verificar que el vector de 5 dominios de computación sume 100%
            sum_vec5 = r["vec_CE"] + r["vec_CS"] + r["vec_SE"] + r["vec_IT"] + r["vec_IS"]
            self.assertAlmostEqual(sum_vec5, 100.0, delta=0.1)

    def test_05_all_five_cc2020_disciplines_represented(self) -> None:
        """Verifica que la clasificación corregida desbloquee IT y represente las 5 disciplinas CC2020."""
        af_counts = {}
        for r in self.plan_docs:
            af = r["Afinidad_Regla_Corregida"]
            af_counts[af] = af_counts.get(af, 0) + 1
        for disc in ("CE", "CS", "SE", "IT", "IS"):
            self.assertGreater(
                af_counts.get(disc, 0),
                0,
                f"La disciplina {disc} tiene 0 programas asignados en Afinidad_Regla_Corregida",
            )

    def test_06_generated_files_and_images_exist(self) -> None:
        """Verifica que todos los archivos CSV, JSON e imágenes PNG requeridos se hayan generado."""
        required_files = [
            "corpus_CC2020_consolidado_75.csv",
            "corpus_CC2020_completo_75.csv",
            "corpus_CC2020_planes_60.csv",
            "corpus_CC2020_perfiles_15.csv",
            "auditoria_muestra_estratificada.csv",
            "evaluacion_ciega_resultados_120.json",
            "plantilla_evaluacion_ciega_120.csv",
            "analisis_sensibilidad.csv",
            "auditoria_estadistica_resumen.json",
            "corpus_CC2020_master_mancha_regresion.png",
            "distribucion_60_planes.png",
            "distribucion_15_perfiles_vs_pares.png",
            "distribucion_disciplinas_y_vectores.png",
            "distribucion_paises_y_denominaciones.png",
            "comparacion_original_vs_corregido_sensibilidad.png",
        ]
        for fname in required_files:
            fpath = BASE_DIR / fname
            self.assertTrue(fpath.exists(), f"Archivo requerido no encontrado: {fname}")
            self.assertGreater(fpath.stat().st_size, 500, f"Archivo vacío o truncado: {fname}")

    def test_07_country_counts_exact_sums(self) -> None:
        """Verifica que la distribución geográfica sume exactamente 15 en Perfiles, 60 en Planes y 75 en Total."""
        prof_countries = Counter(r["Pais"] for r in self.profile_docs)
        plan_countries = Counter(r["Pais"] for r in self.plan_docs)
        all_countries = Counter(r["Pais"] for r in self.all_docs)

        self.assertEqual(sum(prof_countries.values()), 15)
        self.assertEqual(prof_countries, {"México": 13, "Ecuador": 1, "Honduras": 1})

        self.assertEqual(sum(plan_countries.values()), 60)
        self.assertEqual(plan_countries["Honduras"], 1)
        self.assertEqual(plan_countries["México"], 13)
        self.assertEqual(plan_countries["Colombia"], 11)

        self.assertEqual(sum(all_countries.values()), 75)
        self.assertEqual(all_countries["Honduras"], 2)
        self.assertEqual(all_countries["Ecuador"], 4)

    def test_08_blind_validation_kappa_metrics(self) -> None:
        """Verifica que la evaluación ciega independiente (n=120) supere kappa > 0.70 en X, Y y Dominio."""
        summary_path = BASE_DIR / "auditoria_estadistica_resumen.json"
        data = json.loads(summary_path.read_text(encoding="utf-8"))
        blind = data["validacion_empirica"]["inter_rater_blind_validation"]["S1_vs_Blind_Evaluator"]

        self.assertGreater(blind["Polo_X"]["kappa"], 0.70)
        self.assertGreater(blind["Polo_Y"]["kappa"], 0.75)
        self.assertGreater(blind["Polo_Y"]["weighted_kappa_linear"], 0.80)
        self.assertGreater(blind["Dominio_CC2020"]["kappa"], 0.75)
        self.assertEqual(blind["Polo_Y"]["polar_reversals_H_vs_O"], 0)
        self.assertLessEqual(blind["Polo_X"]["polar_reversals_T_vs_A"], 2)

    def test_09_reconciled_fuentes_bloque_03(self) -> None:
        """Verifica que fuentes_bloque_03 esté reconciliada por ID real y sin archivos _fuentes_lote sueltos."""
        fb3 = BASE_DIR / "fuentes_bloque_03"
        self.assertTrue((fb3 / "INDICE_CORRESPONDENCIA_FUENTES.md").exists())
        for stem in ("D031", "D032", "D033", "D035", "D038", "D041", "D042", "D045"):
            self.assertTrue((fb3 / f"{stem}.txt").exists(), f"Falta {stem}.txt en fuentes_bloque_03")
        lotes_left = list(fb3.glob("_fuentes_lote*.json"))
        self.assertEqual(len(lotes_left), 0, "No deben quedar archivos _fuentes_lote*.json en fuentes_bloque_03")

    def test_10_markdown_relative_links_and_rule_ids(self) -> None:
        """Verifica que ningún archivo .md contenga enlaces locales file:/// y que CODEBOOK_CC2020.md liste los 27 IDs reales."""
        md_files = list(ROOT_DIR.glob("*.md")) + list(BASE_DIR.glob("*.md"))
        self.assertGreaterEqual(len(md_files), 8)
        for md in md_files:
            content = md.read_text(encoding="utf-8")
            self.assertNotIn(
                "file:///",
                content.lower(),
                f"Enlace absoluto local file:/// detectado en {md}",
            )

        codebook_md = (ROOT_DIR / "CODEBOOK_CC2020.md").read_text(encoding="utf-8")
        for rule_id, *_ in CODEBOOK_RULES:
            self.assertIn(
                rule_id,
                codebook_md,
                f"El ID de regla {rule_id} de src/codebook.py no figura en CODEBOOK_CC2020.md",
            )


if __name__ == "__main__":
    unittest.main()
