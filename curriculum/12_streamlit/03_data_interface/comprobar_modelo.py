"""Controles opcionales de autoría; ejecutar con Python estándar."""

import copy
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

from cartera import analizar, leer_cartera
from configuracion import RUTA_DATOS

BASE = Path(__file__).resolve().parent


class ModeloTest(unittest.TestCase):
    def setUp(self):
        self.filas = leer_cartera(RUTA_DATOS)

    def test_referencias_fronteras_y_ningun_segmento(self):
        casos = [
            ("2026-10-31", ["comercio", "servicios"], 2000, [("003", 2600)], 4600),
            ("2026-09-30", ["comercio", "servicios"], 2000, [("002", 2000), ("003", 2500)], 4500),
            ("2026-09-30", ["comercio", "servicios"], 2001, [("003", 2500)], 4500),
            ("2026-10-31", ["servicios"], 2000, [], 4600),
            ("2026-10-31", ["servicios"], 1900, [("002", 1900)], 4600),
            ("2026-09-30", ["comercio"], 0, [("001", 0), ("003", 2500)], 4500),
            ("2026-10-31", [], 0, [], 4600),
            ("2026-10-31", ["comercio"], 2600, [("003", 2600)], 4600),
            ("2026-10-31", ["comercio"], 2601, [], 4600),
        ]
        for corte, segmentos, minimo, pares, total in casos:
            with self.subTest(corte=corte, segmentos=segmentos, minimo=minimo):
                r = analizar(self.filas, corte, segmentos, minimo)
                self.assertEqual([(f["id_credito"], f["saldo_mxn"]) for f in r["seleccion"]], pares)
                self.assertEqual(r["universo"], {"cantidad": 3, "saldo_mxn": total})
                self.assertEqual(r["indicadores"], {"cantidad": len(pares), "saldo_mxn": sum(v for _, v in pares),
                                                  "porcentaje_creditos": len(pares) / 3 * 100})

    def test_vacio_sin_universo(self):
        for filas, corte in [([], "2026-10-31"), (self.filas, "2026-11-30")]:
            r = analizar(filas, corte, [], 0)
            self.assertEqual(r["universo"], {"cantidad": 0, "saldo_mxn": 0})
            self.assertIsNone(r["indicadores"]["porcentaje_creditos"])

    def test_no_mutacion_orden_y_copias(self):
        original = copy.deepcopy(self.filas)
        r = analizar(list(reversed(self.filas)), "2026-10-31", ["comercio"], 0)
        self.assertEqual([f["id_credito"] for f in r["seleccion"]], ["001", "003"])
        r["seleccion"][0]["saldo_mxn"] = 999
        self.assertEqual(self.filas, original)

    def test_errores_fuera_del_filtro(self):
        for campo, valor in [("saldo_mxn", None), ("saldo_mxn", True), ("saldo_mxn", -1),
                             ("saldo_mxn", 1_000_001), ("saldo_mxn", 2.5), ("id_credito", "01"),
                             ("fecha_corte", "2026-02-30"), ("fecha_corte", "2026-9-30"),
                             ("fecha_corte", "1800-09-30"), ("segmento", "otro")]:
            with self.subTest(campo=campo, valor=valor):
                filas = copy.deepcopy(self.filas)
                filas[0][campo] = valor  # Septiembre, aunque se consulta octubre.
                with self.assertRaises(ValueError):
                    analizar(filas, "2026-10-31", ["comercio"], 2000)
        with self.assertRaises(ValueError):
            analizar(self.filas + [self.filas[0]], "2026-10-31", [], 0)

    def test_parametros(self):
        for corte, segmentos, minimo in [("2026-02-30", [], 0), ("2026-10-31", None, 0),
                                        ("2026-10-31", ["otro"], 0), ("2026-10-31", ["comercio"] * 2, 0),
                                        ("2026-10-31", [], True), ("2026-10-31", [], -1)]:
            with self.assertRaises(ValueError):
                analizar(self.filas, corte, segmentos, minimo)

    def test_csv_contrato_y_vacio(self):
        texto = RUTA_DATOS.read_text(encoding="utf-8")
        casos = [texto.replace(",2000", ",2000.0"), texto.replace(",2000", ","),
                 texto.replace(",2000", ",02000"), texto.replace(",2000", ",2000,extra"),
                 texto.replace("id_credito", "id"), texto + texto.splitlines()[1] + "\n"]
        with tempfile.TemporaryDirectory() as carpeta:
            ruta = Path(carpeta) / "variante.csv"
            for contenido in casos:
                ruta.write_text(contenido, encoding="utf-8")
                with self.assertRaises(ValueError):
                    leer_cartera(ruta)
            ruta.write_text(texto.splitlines()[0] + "\n", encoding="utf-8")
            self.assertEqual(leer_cartera(ruta), [])
            with self.assertRaises(FileNotFoundError):
                leer_cartera(Path(carpeta) / "ausente.csv")

    def test_cli_nuevo_proceso_otro_directorio_y_variante(self):
        with tempfile.TemporaryDirectory() as carpeta:
            comando = [sys.executable, str(BASE / "ejecutar.py")]
            salida = subprocess.check_output(comando, cwd=carpeta, text=True, encoding="utf-8")
            r = json.loads(salida)
            self.assertEqual(r["indicadores"]["saldo_mxn"], 2600)
            self.assertEqual(r, analizar(self.filas, "2026-10-31", ["comercio", "servicios"], 2000))
            fuente = Path(carpeta) / "variante.csv"
            fuente.write_text(RUTA_DATOS.read_text(encoding="utf-8").replace(",2600", ",2800"), encoding="utf-8")
            r = json.loads(subprocess.check_output(comando + ["--fuente", "variante.csv"], cwd=carpeta))
            self.assertEqual(r["indicadores"]["saldo_mxn"], 2800)
            self.assertEqual(r["universo"]["saldo_mxn"], 4800)
            r = json.loads(subprocess.check_output(comando + ["--segmentos"], cwd=carpeta))
            self.assertEqual(r["seleccion"], [])
            fallo = subprocess.run(comando + ["--fuente", "ausente.csv"], cwd=carpeta, capture_output=True)
            self.assertEqual(fallo.returncode, 2)
            self.assertEqual(fallo.stdout, b"")

    def test_importar_no_necesita_csv_ni_streamlit(self):
        with tempfile.TemporaryDirectory() as carpeta:
            for nombre in ["cartera.py", "configuracion.py", "ejecutar.py"]:
                shutil.copyfile(BASE / nombre, Path(carpeta) / nombre)
            codigo = "import sys; import cartera, configuracion, ejecutar; assert 'streamlit' not in sys.modules"
            salida = subprocess.check_output([sys.executable, "-c", codigo], cwd=carpeta)
            self.assertEqual(salida, b"")


if __name__ == "__main__":
    unittest.main()
