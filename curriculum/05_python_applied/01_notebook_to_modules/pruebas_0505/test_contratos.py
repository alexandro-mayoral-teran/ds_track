"""Conteos válidos/inválidos y ausencia explícita de fecha."""

import unittest

from analisis_cartera.contratos import coverage_pct, normalize_cut


class PruebasContratos(unittest.TestCase):
    def test_cobertura_con_base_y_sin_base(self):
        self.assertIsNone(coverage_pct(0, 0))
        self.assertEqual(coverage_pct(0, 3), 0.0)
        self.assertEqual(coverage_pct(3, 3), 100.0)
        self.assertAlmostEqual(coverage_pct(2, 3), 200 / 3, places=10)

    def test_conteos_de_tipo_incompatible(self):
        for known, total in [(True, 3), (1, False), ("2", 3), (2, "3"),
                             (2.0, 3), (2, 3.0), (None, 3)]:
            with self.subTest(known=known, total=total):
                with self.assertRaises(TypeError):
                    coverage_pct(known, total)

    def test_conteos_fuera_del_dominio(self):
        for known, total in [(-1, 3), (0, -1), (4, 3), (1, 0)]:
            with self.subTest(known=known, total=total):
                with self.assertRaises(ValueError):
                    coverage_pct(known, total)

    def test_corte_omitido_none_y_fecha_explicita(self):
        self.assertEqual(normalize_cut(), "2026-10-31")
        self.assertEqual(normalize_cut(None), "2026-10-31")
        self.assertEqual(normalize_cut("2024-02-29"), "2024-02-29")

    def test_cortes_invalidos(self):
        for cut in ["", "2026-02-29", "2026-2-28", "2026-10-31 "]:
            with self.subTest(cut=cut):
                with self.assertRaises(ValueError):
                    normalize_cut(cut)
        for cut in [31, True, ["2026-10-31"]]:
            with self.subTest(cut=cut):
                with self.assertRaises(TypeError):
                    normalize_cut(cut)
