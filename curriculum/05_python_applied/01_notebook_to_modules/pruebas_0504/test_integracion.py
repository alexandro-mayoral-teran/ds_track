"""Recorrido real de lectura, análisis, conciliación y entrega por etapas."""

from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

import matplotlib
matplotlib.use("Agg")  # En estas pruebas se guardan figuras sin abrir ventanas.
import matplotlib.pyplot as plt
import pandas as pd
from pandas.testing import assert_frame_equal

from analisis_cartera.cierre import inspect_delivery, run_delivery
from analisis_cartera.comprobacion import reconcile
from analisis_cartera.flujo import build_analysis
from pruebas_0504.muestras import CUT, write_sources


class PruebasIntegracion(unittest.TestCase):
    def setUp(self):
        temporary = TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.folder = Path(temporary.name)
        self.source = write_sources(self.folder / "fuentes")
        self.before = {p.name: p.read_bytes() for p in self.source.iterdir()}
        self.settings = {"source": self.source, "output": self.folder / "entrega",
                         "cut": CUT, "dpi": 60, "log_level": "INFO"}

    def test_indicadores_con_referencia_manual(self):
        tables = build_analysis(self.source, CUT)
        # Total: cinco filas, tres saldos conocidos [0, 1, 10], mediana 1.
        total = tables["indicadores"].set_index("segmento").loc["Todos"]
        self.assertEqual(total["registros"], 5)
        self.assertEqual(total["conocidos"], 3)
        self.assertEqual(total["mediana_mxn"], 1)
        self.assertEqual(total["cobertura_pct"], 60)
        self.assertEqual(len(tables["conciliacion"]), 20)
        self.assertTrue(tables["conciliacion"]["coincide"].all())
        self.assertEqual({p.name: p.read_bytes() for p in self.source.iterdir()}, self.before)

    def test_conciliacion_detecta_mediana_alterada(self):
        tables = build_analysis(self.source, CUT)
        altered = tables["resumen"].copy(deep=True)
        altered.loc[altered["segmento"].eq("comercio"), "mediana_mxn"] = 999
        with self.assertRaisesRegex(ValueError, "difieren"):
            reconcile(altered, tables["corte"], tables["referencia_csv"])

    def test_cierre_reconstruccion_y_destino_existente(self):
        previous_figures = plt.get_fignums()
        first = run_delivery(self.settings, {}, None)
        output = self.settings["output"]
        self.assertEqual(inspect_delivery(output)["estado"], "completada")
        saved = {p.relative_to(output): p.read_bytes() for p in output.rglob("*") if p.is_file()}
        reconstructed = run_delivery({**self.settings, "source": output / "fuentes",
                                     "output": self.folder / "reconstruccion"}, {}, None)
        for name in ["resumen", "indicadores", "conciliacion"]:
            assert_frame_equal(first[name], reconstructed[name], check_exact=True)
        reloaded = pd.read_csv(output / "resumen.csv")
        self.assertEqual(reloaded.loc[reloaded["segmento"].eq("comercio"), "mediana_mxn"].iloc[0], 0.5)
        with self.assertRaises(FileExistsError):
            run_delivery(self.settings, {}, None)
        self.assertEqual({p.relative_to(output): p.read_bytes() for p in output.rglob("*") if p.is_file()}, saved)
        self.assertEqual({p.name: p.read_bytes() for p in self.source.iterdir()}, self.before)
        self.assertEqual(plt.get_fignums(), previous_figures)

    def test_fallas_por_etapa_no_publican_cierre(self):
        for stage, has_record in [("after-export", False), ("record", False), ("before-close", True)]:
            with self.subTest(etapa=stage):
                output = self.folder / stage
                with self.assertRaises(OSError):
                    run_delivery({**self.settings, "output": output}, {}, None, stage)
                self.assertTrue((output / "entrega.json").is_file())
                self.assertEqual((output / "ejecucion.json").is_file(), has_record)
                self.assertFalse((output / "cierre.json").exists())
                self.assertEqual(inspect_delivery(output)["estado"], "incompleta")

    def test_datos_rechazados_no_crean_entrega(self):
        (self.source / "creditos.csv").write_text("id_credito,id_cliente,segmento\n", encoding="utf-8")
        with self.assertRaises(ValueError):
            run_delivery(self.settings, {}, None)
        self.assertFalse(self.settings["output"].exists())
