"""Integración real y alteraciones sobre copias temporales de entregas."""

import hashlib
import json
from pathlib import Path
import shutil
from tempfile import TemporaryDirectory
import unittest

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

from analisis_cartera.auditoria import compare_deliveries, verify_delivery
from analisis_cartera.cierre import inspect_delivery, run_delivery
from pruebas_0504.muestras import CUT, write_sources


def fingerprints(folder):
    return {p.relative_to(folder): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in folder.rglob("*") if p.is_file()}


class PruebasAuditoria(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temporary = TemporaryDirectory()
        cls.addClassCleanup(cls.temporary.cleanup)
        cls.folder = Path(cls.temporary.name)
        source = write_sources(cls.folder / "fuentes")
        cls.settings = {"source": source, "output": cls.folder / "base", "cut": CUT,
                        "dpi": 60, "log_level": "INFO"}
        run_delivery(cls.settings, {}, None)
        run_delivery({**cls.settings, "source": cls.folder / "base/fuentes",
                      "output": cls.folder / "reconstruida"}, {}, None)
        run_delivery({**cls.settings, "cut": "2027-01-31", "output": cls.folder / "sin_corte"}, {}, None)

    def setUp(self):
        temporary = TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.output = Path(temporary.name) / "entrega"
        shutil.copytree(self.folder / "base", self.output)

    def test_verifica_y_no_modifica_ni_abre_figuras(self):
        before, figures = fingerprints(self.output), plt.get_fignums()
        actual = verify_delivery(self.output)
        self.assertEqual(actual["estado"], "verificada")
        self.assertEqual(actual["tablas"], 5)
        self.assertEqual(actual["conciliaciones"], 20)
        self.assertEqual(actual["png_px"], [720, 330])
        self.assertEqual(before, fingerprints(self.output))
        self.assertEqual(plt.get_fignums(), figures)
        total = pd.read_csv(self.output / "indicadores.csv").iloc[-1]
        self.assertEqual((total.registros, total.conocidos, total.mediana_mxn, total.cobertura_pct), (5, 3, 1, 60))

    def test_reconstruccion_desde_copias_equivalente(self):
        actual = compare_deliveries(self.output, self.folder / "reconstruida")
        self.assertEqual(actual["estado"], "reconstruccion_equivalente")

    def test_corte_vacio_valido_y_comparacion_rechaza_otro_corte(self):
        self.assertEqual(verify_delivery(self.folder / "sin_corte")["corte"], "2027-01-31")
        with self.assertRaisesRegex(ValueError, "mismo corte"):
            compare_deliveries(self.output, self.folder / "sin_corte")

    def test_cierre_ausente_no_se_repara(self):
        (self.output / "cierre.json").unlink()
        before = fingerprints(self.output)
        with self.assertRaisesRegex(ValueError, "cierre completo"):
            verify_delivery(self.output)
        self.assertEqual(before, fingerprints(self.output))

    def test_tabla_editada_con_marcador_existente(self):
        path = self.output / "indicadores.csv"
        table = pd.read_csv(path)
        table.loc[table.segmento.eq("Todos"), "mediana_mxn"] = 999
        table.to_csv(path, index=False)
        self.assertEqual(inspect_delivery(self.output)["estado"], "completada")
        with self.assertRaisesRegex(ValueError, "indicadores.csv"):
            verify_delivery(self.output)

    def test_fuente_copiada_alterada_no_usa_original(self):
        path = self.output / "fuentes/cortes.csv"
        text = path.read_text(encoding="utf-8").replace(",10,31", ",500,31")
        path.write_text(text, encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "difiere"):
            verify_delivery(self.output)

    def test_corte_de_registros_incoherente(self):
        path = self.output / "ejecucion.json"
        record = json.loads(path.read_text(encoding="utf-8"))
        record["configuracion_efectiva"]["cut"] = "2026-09-30"
        path.write_text(json.dumps(record), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "incoherentes"):
            verify_delivery(self.output)
        record["configuracion_efectiva"] = []
        path.write_text(json.dumps(record), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Estructura"):
            verify_delivery(self.output)

    def test_spec_altair_alterada(self):
        path = self.output / "altair.json"
        spec = json.loads(path.read_text(encoding="utf-8"))
        spec["title"] = "Otro corte"
        path.write_text(json.dumps(spec), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Altair"):
            verify_delivery(self.output)

    def test_figura_truncada(self):
        (self.output / "matplotlib.png").write_bytes(b"incompleta")
        with self.assertRaisesRegex(ValueError, "tamaño"):
            verify_delivery(self.output)

    def test_svg_invalido_aunque_tamano_declarado_se_actualice(self):
        path = self.output / "matplotlib.svg"
        path.write_text("<svg", encoding="utf-8")
        formats = pd.read_csv(self.output / "formatos.csv")
        formats.loc[formats.archivo.eq("matplotlib.svg"), "bytes"] = path.stat().st_size
        formats.to_csv(self.output / "formatos.csv", index=False)
        with self.assertRaisesRegex(ValueError, "SVG"):
            verify_delivery(self.output)
