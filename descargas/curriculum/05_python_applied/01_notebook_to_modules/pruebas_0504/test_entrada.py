"""Lectura y validación con CSV temporales; no tocar las muestras anteriores."""

from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from analisis_cartera.entrada import read_detail
from pruebas_0504.muestras import CREDITS, CUTS, write_sources


class PruebasEntrada(unittest.TestCase):
    def setUp(self):
        temporary = TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.folder = Path(temporary.name)

    def test_lectura_tipos_claves_y_fuentes_intactas(self):
        write_sources(self.folder)
        before = {p.name: p.read_bytes() for p in self.folder.iterdir()}
        detail = read_detail(self.folder)
        self.assertEqual(len(detail), 6)
        self.assertEqual(str(detail["id_credito"].dtype), "string")
        self.assertEqual(str(detail["saldo_mxn"].dtype), "Int64")
        self.assertEqual(detail.iloc[0]["id_credito"], "001")
        self.assertEqual(detail["saldo_mxn"].isna().sum(), 2)
        self.assertEqual({p.name: p.read_bytes() for p in self.folder.iterdir()}, before)

    def test_clave_credito_fecha_repetida(self):
        write_sources(self.folder, cuts=[*CUTS, CUTS[0]])
        with self.assertRaisesRegex(ValueError, "Clave crédito/fecha"):
            read_detail(self.folder)

    def test_credito_repetido_no_multiplica_union(self):
        write_sources(self.folder, credits=[*CREDITS, CREDITS[0]])
        with self.assertRaisesRegex(ValueError, "Clave de crédito"):
            read_detail(self.folder)

    def test_corte_sin_correspondencia(self):
        write_sources(self.folder, credits=CREDITS[1:])
        with self.assertRaisesRegex(ValueError, "sin crédito correspondiente"):
            read_detail(self.folder)

    def test_negativos_y_fecha_imposible(self):
        for field, value in [(2, "-1"), (3, "-1"), (1, "2026-02-30")]:
            with self.subTest(columna=field, valor=value):
                cuts = [row.copy() for row in CUTS]
                cuts[0][field] = value
                write_sources(self.folder, cuts=cuts)
                with self.assertRaises(ValueError):
                    read_detail(self.folder)

    def test_archivo_ausente(self):
        with self.assertRaises(FileNotFoundError):
            read_detail(self.folder)

    def test_csv_con_cabeceras_sin_registros(self):
        write_sources(self.folder, cuts=[], credits=[])
        detail = read_detail(self.folder)
        self.assertTrue(detail.empty)
        self.assertEqual(str(detail["saldo_mxn"].dtype), "Int64")
