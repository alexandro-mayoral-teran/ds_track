"""Pruebas con iteradores de un uso y muestras CSV temporales."""

import csv
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

import pandas as pd
from pandas.testing import assert_frame_equal

from analisis_cartera.flujo import build_analysis
from analisis_cartera.iteracion import batch_indicators, iter_batches
from pruebas_0504.muestras import CREDITS, CUT, CUTS, write_sources


class PruebasIteradores(unittest.TestCase):
    def test_consumo_compartido_sin_adelantar_toda_entrada(self):
        source = iter([1, 2, 3, 4, 5])
        batches = iter_batches(source, 2)
        self.assertIs(iter(batches), batches)
        self.assertEqual(next(batches), [1, 2])
        self.assertEqual(next(source), 3)
        self.assertEqual(next(batches), [4, 5])
        with self.assertRaises(StopIteration):
            next(batches)
        self.assertEqual(list(batches), [])

    def test_vacio_ultimo_corto_y_listas_distintas(self):
        self.assertEqual(list(iter_batches([], 2)), [])
        batches = list(iter_batches(range(5), 2))
        self.assertEqual(batches, [[0, 1], [2, 3], [4]])
        self.assertIsNot(batches[0], batches[1])

    def test_tamano_invalido_falla_al_consumir(self):
        for size, error in [(0, ValueError), (-1, ValueError), (True, TypeError),
                            (2.5, TypeError), ("2", TypeError)]:
            with self.subTest(size=size):
                batches = iter_batches([1], size)
                with self.assertRaises(error):
                    next(batches)
        batches = iter_batches(7, 2)
        with self.assertRaises(TypeError):
            next(batches)

    def test_error_tardio_no_se_disfraza_de_fin(self):
        def source():
            yield 1
            yield 2
            raise ValueError("Falla de la fuente")

        batches = iter_batches(source(), 2)
        self.assertEqual(next(batches), [1, 2])
        with self.assertRaisesRegex(ValueError, "Falla de la fuente"):
            next(batches)
        with self.assertRaises(ValueError):
            next(iter_batches(source(), 3))

    def test_iterable_puede_reiniciarse_iterador_no(self):
        rows = [1, 2, 3]
        self.assertEqual(list(iter_batches(rows, 2)), list(iter_batches(rows, 2)))
        iterator = iter(rows)
        self.assertEqual(list(iter_batches(iterator, 2)), [[1, 2], [3]])
        self.assertEqual(list(iter_batches(iterator, 2)), [])

    def test_archivo_del_llamador_cierra_con_salida_temprana(self):
        with TemporaryDirectory() as folder:
            source = write_sources(folder)
            with (source / "cortes.csv").open(encoding="utf-8", newline="") as handle:
                reader = csv.DictReader(handle)
                batches = iter_batches(reader, 2)
                for batch in batches:
                    self.assertEqual(len(batch), 2)
                    break
                self.assertFalse(handle.closed)
            self.assertTrue(handle.closed)
            batches.close()


class PruebasIndicadores(unittest.TestCase):
    def setUp(self):
        temporary = TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.source = write_sources(Path(temporary.name) / "fuentes")

    def test_tamanos_distintos_concilian_fuentes_intactas(self):
        before = {p.name: p.read_bytes() for p in self.source.iterdir()}
        expected = build_analysis(self.source, CUT)["indicadores"]
        for size in [1, 2, 4, 6, 20]:
            with self.subTest(size=size):
                actual = batch_indicators(self.source, CUT, batch_size=size)
                assert_frame_equal(actual, expected, check_exact=True)
                total = actual.iloc[-1]
                self.assertEqual(tuple(total[["registros", "conocidos", "mediana_mxn", "cobertura_pct"]]),
                                 (5, 3, 1, 60))
        self.assertEqual({p.name: p.read_bytes() for p in self.source.iterdir()}, before)

    def test_cero_ausencia_y_grupo_sin_registros(self):
        rows = batch_indicators(self.source, batch_size=2).set_index("segmento")
        self.assertEqual(rows.loc["comercio", "mediana_mxn"], 0.5)
        self.assertEqual(rows.loc["educacion", "cobertura_pct"], 0)
        self.assertTrue(pd.isna(rows.loc["educacion", "mediana_mxn"]))
        self.assertTrue(pd.isna(rows.loc["servicios", "cobertura_pct"]))

    def test_mediana_no_es_promedio_de_medianas_por_lote(self):
        cuts = [["001", CUT, "0", "0"], ["002", CUT, "0", "0"],
                ["003", CUT, "100", "0"]]
        write_sources(self.source, cuts=cuts, credits=CREDITS[:3])
        rows = batch_indicators(self.source, batch_size=2).set_index("segmento")
        self.assertEqual(rows.loc["comercio", "mediana_mxn"], 0)
        self.assertEqual(rows.loc["Todos", "mediana_mxn"], 0)

    def test_duplicado_entre_lotes_y_fuera_del_corte(self):
        write_sources(self.source, cuts=[*CUTS, CUTS[-1]])
        with self.assertRaisesRegex(ValueError, "Clave crédito/fecha"):
            batch_indicators(self.source, CUT, batch_size=1)

    def test_catalogo_y_relacion_invalidos(self):
        for credits, message in [([*CREDITS, CREDITS[0]], "Clave de crédito"),
                                 (CREDITS[1:], "sin crédito correspondiente"),
                                 ([["001", "C01", "otro"]], "Segmento")]:
            with self.subTest(message=message):
                write_sources(self.source, credits=credits)
                with self.assertRaisesRegex(ValueError, message):
                    batch_indicators(self.source, batch_size=2)

    def test_valores_invalidos_incluso_despues_del_corte(self):
        for column, value in [(1, "2026-02-30"), (1, "2026-9-30"), (2, "-1"),
                               (2, "1_000"), (2, str(2**63)), (3, "texto")]:
            with self.subTest(column=column, value=value):
                cuts = [row.copy() for row in CUTS]
                cuts[-1][column] = value
                write_sources(self.source, cuts=cuts)
                with self.assertRaises(ValueError):
                    batch_indicators(self.source, CUT, batch_size=2)

    def test_campos_faltantes_adicionales_y_cabecera(self):
        path = self.source / "cortes.csv"
        header = "id_credito,fecha_corte,saldo_mxn,dias_atraso\n"
        for text in [header + "001,2026-10-31,0\n", header + "001,2026-10-31,0,0,extra\n",
                     "id_credito,saldo_mxn\n001,0\n"]:
            with self.subTest(text=text):
                path.write_text(text, encoding="utf-8")
                with self.assertRaises(ValueError):
                    batch_indicators(self.source)
        path.write_text(header + '001,2026-10-31,0,"0\n', encoding="utf-8")
        with self.assertRaises(csv.Error):
            batch_indicators(self.source)

    def test_csv_vacios_y_corte_sin_filas(self):
        actual = batch_indicators(self.source, "2027-01-31")
        self.assertEqual(actual["registros"].tolist(), [0] * 5)
        self.assertTrue(actual["mediana_mxn"].isna().all())
        self.assertTrue(actual["cobertura_pct"].isna().all())
        write_sources(self.source, cuts=[], credits=[])
        assert_frame_equal(batch_indicators(self.source), actual, check_exact=True)

    def test_parametros_y_fuente_ausente(self):
        absent = self.source / "no_existe"
        with self.assertRaises(ValueError):
            batch_indicators(absent, batch_size=0)
        with self.assertRaises(ValueError):
            batch_indicators(absent, "2026-02-30")
        with self.assertRaises(FileNotFoundError):
            batch_indicators(absent)
