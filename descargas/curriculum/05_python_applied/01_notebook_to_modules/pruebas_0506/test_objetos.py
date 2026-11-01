"""Casos de objetos pequeños sin copiar el algoritmo del análisis."""

from dataclasses import FrozenInstanceError, replace
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

import pandas as pd
from pandas.testing import assert_frame_equal

from analisis_cartera.objetos import CoverageCounts, ReviewJob, ReviewOptions
from analisis_cartera.revision import review_summary
from pruebas_0504.muestras import CREDITS, write_sources


class PruebasConteos(unittest.TestCase):
    def test_cero_y_ausencia(self):
        self.assertEqual(CoverageCounts(0, 3).percentage(), 0)
        self.assertIsNone(CoverageCounts(0, 0).percentage())
        self.assertAlmostEqual(CoverageCounts(2, 3).percentage(), 200 / 3, places=10)

    def test_estado_inicial_invalido(self):
        for known, total, error in [(True, 3, TypeError), ("2", 3, TypeError),
                                    (4, 3, ValueError), (0, -1, ValueError)]:
            with self.subTest(known=known, total=total):
                with self.assertRaises(error):
                    CoverageCounts(known, total)

    def test_instancias_y_alias_no_son_lo_mismo(self):
        first = CoverageCounts(2, 3)
        second = CoverageCounts(2, 3)
        alias = first
        alias.known = 1
        self.assertEqual(first.known, 1)
        self.assertEqual(second.known, 2)
        self.assertAlmostEqual(first.percentage(), 100 / 3, places=10)
        alias.known = 4
        with self.assertRaises(ValueError):
            first.percentage()


class PruebasOpciones(unittest.TestCase):
    def test_predeterminados_e_igualdad_por_valor(self):
        first = ReviewOptions()
        second = ReviewOptions(cut="2026-10-31", segments=None)
        self.assertEqual(first, second)
        self.assertIsNot(first, second)
        self.assertNotEqual(first, ReviewOptions(segments=()))

    def test_cortes_invalidos(self):
        for cut, error in [(None, TypeError), (31, TypeError), ("", ValueError),
                           ("2026-02-29", ValueError), ("2026-9-30", ValueError)]:
            with self.subTest(cut=cut):
                with self.assertRaises(error):
                    ReviewOptions(cut=cut)

    def test_segmentos_invalidos(self):
        for segments, error in [(["comercio"], TypeError), ("comercio", TypeError),
                                ((1,), TypeError), (("otro",), ValueError),
                                (("comercio", "comercio"), ValueError)]:
            with self.subTest(segments=segments):
                with self.assertRaises(error):
                    ReviewOptions(segments=segments)

    def test_frozen_replace_y_revalidacion(self):
        original = ReviewOptions(segments=("comercio",))
        with self.assertRaises(FrozenInstanceError):
            original.cut = "2026-09-30"
        updated = replace(original, cut="2026-09-30")
        self.assertEqual(original.cut, "2026-10-31")
        self.assertEqual(updated.cut, "2026-09-30")
        self.assertEqual(updated.segments, original.segments)
        with self.assertRaises(ValueError):
            replace(original, segments=("otro",))


class PruebasTrabajo(unittest.TestCase):
    def setUp(self):
        temporary = TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.source = write_sources(Path(temporary.name) / "fuentes")

    def test_equivalencia_y_fuentes_conservadas(self):
        before = {p.name: p.read_bytes() for p in self.source.iterdir()}
        job = ReviewJob(self.source)
        assert_frame_equal(job.summary(), review_summary(self.source), check_exact=True)
        self.assertEqual({p.name: p.read_bytes() for p in self.source.iterdir()}, before)
        self.assertEqual(job.options, ReviewOptions())

    def test_composicion_orden_y_ausencia(self):
        options = ReviewOptions(segments=("educacion", "comercio", "servicios"))
        job = ReviewJob(str(self.source), options)
        actual = job.summary()
        self.assertIs(job.options, options)
        self.assertEqual(actual["segmento"].tolist(), list(options.segments))
        self.assertTrue(pd.isna(actual.iloc[0]["mediana_mxn"]))
        self.assertEqual(actual.iloc[0]["cobertura_pct"], 0)
        self.assertEqual(actual.iloc[1]["mediana_mxn"], 0.5)
        self.assertEqual(actual.iloc[2]["registros"], 0)
        self.assertTrue(pd.isna(actual.iloc[2]["cobertura_pct"]))

    def test_tupla_vacia_y_corte_sin_filas(self):
        full = ReviewJob(self.source).summary()
        empty = ReviewJob(self.source, ReviewOptions(segments=())).summary()
        assert_frame_equal(empty, full.iloc[:0], check_exact=True)
        no_rows = ReviewJob(self.source, ReviewOptions(cut="2027-01-31")).summary()
        self.assertEqual(no_rows["registros"].tolist(), [0, 0, 0, 0])
        self.assertTrue(no_rows["mediana_mxn"].isna().all())
        self.assertTrue(no_rows["cobertura_pct"].isna().all())

    def test_construccion_sin_lectura_y_parametros_invalidos(self):
        absent = self.source / "ausente"
        job = ReviewJob(absent)
        self.assertFalse(absent.exists())
        with self.assertRaises(FileNotFoundError):
            job.summary()
        with self.assertRaises(TypeError):
            ReviewJob(3)
        with self.assertRaises(ValueError):
            ReviewJob(" ")
        with self.assertRaises(TypeError):
            ReviewJob(self.source, {"cut": "2026-10-31"})
        with self.assertRaises(FrozenInstanceError):
            job.source = self.source

    def test_relectura_sin_cache_y_tablas_independientes(self):
        job = ReviewJob(self.source)
        first = job.summary()
        first.loc[first["segmento"].eq("comercio"), "mediana_mxn"] = 999
        fresh = job.summary()
        self.assertEqual(fresh.set_index("segmento").loc["comercio", "mediana_mxn"], 0.5)
        write_sources(self.source, credits=[*CREDITS, CREDITS[0]])
        with self.assertRaisesRegex(ValueError, "Clave de crédito"):
            job.summary()

    def test_tupla_vacia_no_oculta_fuentes_invalidas(self):
        job = ReviewJob(self.source, ReviewOptions(segments=()))
        write_sources(self.source, credits=[*CREDITS, CREDITS[0]])
        with self.assertRaisesRegex(ValueError, "Clave de crédito"):
            job.summary()
