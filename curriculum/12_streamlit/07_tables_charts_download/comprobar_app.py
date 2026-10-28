"""Controles de autoría; la descarga real se comprueba además en navegador."""

import copy
import csv
from hashlib import sha256
from io import StringIO
import json
from pathlib import Path
import sys
import subprocess
import tempfile
import unittest

from streamlit.testing.v1 import AppTest
from preparar_practica import BASE, MODELO, preparar


class SalidasTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temporal = tempfile.TemporaryDirectory()
        cls.carpeta = preparar(Path(cls.temporal.name) / "practica")
        AppTest.from_file(str(cls.carpeta / "app.py"), default_timeout=20).run()
        cls.modelo = sys.modules["cartera"]
        cls.salidas = sys.modules["salidas"]
        cls.graficos = sys.modules["graficos"]

    @classmethod
    def tearDownClass(cls):
        sys.modules["cache_analisis"].analizar_con_cache.clear()
        cls.temporal.cleanup()

    def nueva(self):
        app = AppTest.from_file(str(self.carpeta / "app.py"), default_timeout=20).run()
        self.assertFalse(app.exception)
        return app

    def aplicar(self, app, corte, segmentos, minimo):
        app.selectbox(key="corte_borrador").set_value(corte)
        app.multiselect(key="segmentos_borrador").set_value(segmentos)
        app.text_input(key="minimo_borrador").set_value(minimo)
        app.button(key="aplicar").click().run()
        self.assertFalse(app.exception)

    def test_mismos_registros_en_csv_grafico_y_contexto(self):
        filas = self.modelo.leer_cartera(self.carpeta / "cartera.csv")
        casos = [
            ("2026-10-31", ["comercio", "servicios"], 2000, [("003", 2600)], 4600),
            ("2026-09-30", ["comercio", "servicios"], 2000, [("002", 2000), ("003", 2500)], 4500),
            ("2026-09-30", ["comercio", "servicios"], 2001, [("003", 2500)], 4500),
            ("2026-10-31", ["servicios"], 2000, [], 4600),
            ("2026-10-31", ["servicios"], 1900, [("002", 1900)], 4600),
            ("2026-09-30", ["comercio", "servicios"], 0, [("001", 0), ("002", 2000), ("003", 2500)], 4500),
            ("2026-10-31", [], 0, [], 4600),
        ]
        for corte, segmentos, minimo, pares, total in casos:
            with self.subTest(corte=corte, segmentos=segmentos, minimo=minimo):
                r = self.modelo.analizar(filas, corte, segmentos, minimo)
                original = copy.deepcopy(r)
                salida = self.salidas.preparar_descargas(r, "1205-v1")
                lector = csv.DictReader(StringIO(salida["csv"].decode("utf-8")))
                registros = list(lector)
                self.assertEqual(lector.fieldnames, list(self.modelo.COLUMNAS))
                self.assertEqual([(f["id_credito"], int(f["saldo_mxn"])) for f in registros], pares)
                for campo in ["id_credito", "segmento", "fecha_corte"]:
                    self.assertEqual([f[campo] for f in registros], [f[campo] for f in r["seleccion"]])
                contexto = json.loads(salida["contexto"])
                self.assertEqual(contexto["universo"], {"cantidad": 3, "saldo_mxn": total})
                self.assertEqual(contexto["indicadores"]["cantidad"], len(pares))
                self.assertEqual(contexto["indicadores"]["saldo_mxn"], sum(v for _, v in pares))
                self.assertEqual(contexto["indicadores"]["porcentaje_creditos"], len(pares) / 3 * 100)
                self.assertEqual(contexto["sha256_csv"], sha256(salida["csv"]).hexdigest())
                self.assertEqual(contexto["filtros"], {"corte": corte, "segmentos": segmentos, "minimo_mxn": minimo})
                self.assertIn(corte, salida["nombre_csv"])
                grafico = self.graficos.crear_grafico(r["seleccion"], corte)
                if pares:
                    spec = grafico.to_dict()
                    self.assertEqual(spec["data"]["values"], r["seleccion"])
                    self.assertEqual(spec["layer"][0]["encoding"]["y"]["type"], "nominal")
                    self.assertEqual(spec["layer"][0]["encoding"]["x"]["scale"]["domain"][0], 0)
                    self.assertEqual(spec["layer"][1]["encoding"]["text"]["field"], "saldo_mxn")
                else:
                    self.assertIsNone(grafico)
                    self.assertEqual(salida["csv"].decode("utf-8"), ",".join(self.modelo.COLUMNAS) + "\n")
                self.assertEqual(r, original)

    def test_app_tabla_y_barras_comparten_valores(self):
        app = self.nueva()
        self.aplicar(app, "2026-09-30", ["comercio", "servicios"], "2000")
        tabla = app.table[0].value
        self.assertEqual(list(zip(tabla.id_credito, tabla.saldo_mxn)), [("002", 2000), ("003", 2500)])
        # Streamlit 1.66.1 separa especificación y datos Arrow al enviarlos al cliente.
        from pyarrow import ipc
        registros = ipc.open_stream(app.get("vega_lite_chart")[0].proto.data.data).read_all().to_pylist()
        self.assertEqual(registros, tabla.to_dict(orient="records"))
        self.assertEqual([(f["id_credito"], f["saldo_mxn"]) for f in registros], [("002", 2000), ("003", 2500)])
        self.assertEqual([m.value for m in app.metric], ["2", "4500", "66.67%"])
        descargas = app.get("download_button")
        self.assertEqual(len(descargas), 2)
        self.assertTrue(all(not b.proto.disabled and b.proto.ignore_rerun for b in descargas))
        urls = [b.proto.url for b in descargas]
        app.checkbox(key="mostrar_detalle").uncheck().run()
        self.assertEqual(len(app.table), 0)
        self.assertEqual([b.proto.url for b in app.get("download_button")], urls)

    def test_intento_rechazado_bloquea_descargas_hasta_corregir(self):
        app = self.nueva()
        self.aplicar(app, "2026-09-30", ["comercio", "servicios"], "2001")
        self.aplicar(app, "2026-10-31", [], "2000.5")
        self.assertEqual([m.value for m in app.metric], ["1", "2500", "33.33%"])
        self.assertTrue(all(b.proto.disabled for b in app.get("download_button")))
        self.assertIn("Últimos filtros válidos", app.subheader[0].value)
        self.aplicar(app, "2026-10-31", ["comercio", "servicios"], "2000")
        self.assertTrue(all(not b.proto.disabled for b in app.get("download_button")))

    def test_vacio_valido_descarga_encabezado_sin_barras(self):
        app = self.nueva()
        self.aplicar(app, "2026-10-31", [], "0")
        self.assertEqual([m.value for m in app.metric], ["0", "0", "0.00%"])
        self.assertEqual(len(app.get("vega_lite_chart")), 0)
        self.assertEqual(len(app.table), 0)
        self.assertEqual(len(app.get("download_button")), 2)
        self.assertTrue(all(not b.proto.disabled for b in app.get("download_button")))

    def test_sin_universo_no_ofrece_descarga(self):
        app = self.nueva()
        self.aplicar(app, "2026-11-30", ["comercio"], "0")
        self.assertEqual(len(app.metric), 0)
        self.assertEqual(len(app.get("vega_lite_chart")), 0)
        self.assertEqual(len(app.get("download_button")), 0)

    def test_cambio_fuente_y_fallo_eliminan_salidas_anteriores(self):
        fuente = self.carpeta / "cartera.csv"
        original = fuente.read_bytes()
        app = self.nueva()
        anterior = app.get("download_button")[0].proto.url
        try:
            texto = original.decode("utf-8").replace(",2600", ",2800")
            fuente.write_text(texto, encoding="utf-8")
            app.button(key="reintentar").click().run()
            self.assertEqual([m.value for m in app.metric], ["1", "2800", "33.33%"])
            self.assertNotEqual(app.get("download_button")[0].proto.url, anterior)
            fuente.write_text(texto + texto.splitlines()[1] + "\n", encoding="utf-8")
            app.button(key="reintentar").click().run()
            self.assertFalse(app.exception)
            self.assertEqual(len(app.error), 1)
            self.assertEqual(len(app.get("download_button")), 0)
            self.assertEqual(len(app.get("vega_lite_chart")), 0)
            fuente.write_text(texto.splitlines()[0] + "\n", encoding="utf-8")
            app.button(key="reintentar").click().run()
            self.assertEqual(len(app.get("download_button")), 0)
        finally:
            fuente.write_bytes(original)
        app.button(key="reintentar").click().run()
        self.assertEqual([m.value for m in app.metric], ["1", "2600", "33.33%"])

    def test_cero_real_y_fuentes_preservadas(self):
        fila = {"id_credito": "001", "segmento": "comercio", "fecha_corte": "2026-09-30", "saldo_mxn": 0}
        spec = self.graficos.crear_grafico([fila], "2026-09-30").to_dict()
        self.assertEqual(spec["data"]["values"], [fila])
        self.assertEqual(spec["layer"][0]["encoding"]["x"]["scale"]["domain"], [0, 1])
        for nombre in ("cartera.py", "cartera.csv", "configuracion.py", "ejecutar.py"):
            self.assertEqual((self.carpeta / nombre).read_bytes(), (MODELO / nombre).read_bytes())
        for carpeta, nombre in [("05_data_resource_cache", "cache_analisis.py"), ("06_messages_empty_cases", "entradas.py")]:
            self.assertEqual((self.carpeta / nombre).read_bytes(), (BASE.parent / carpeta / nombre).read_bytes())
        with self.assertRaises(FileExistsError):
            preparar(self.carpeta)

    def test_minimo_completo(self):
        app = AppTest.from_file(str(self.carpeta / "minimo.py"), default_timeout=20).run()
        self.assertFalse(app.exception)
        self.assertEqual(len(app.table[0].value), 2)
        self.assertEqual(len(app.get("vega_lite_chart")), 1)
        self.assertEqual(len(app.get("download_button")), 1)

    def test_revisor_relee_y_detecta_par_incoherente(self):
        filas = self.modelo.leer_cartera(self.carpeta / "cartera.csv")
        r = self.modelo.analizar(filas, "2026-10-31", ["comercio", "servicios"], 2000)
        salida = self.salidas.preparar_descargas(r, "1205-v1")
        with tempfile.TemporaryDirectory() as temporal:
            carpeta = Path(temporal)
            archivo, contexto = carpeta / "seleccion.csv", carpeta / "contexto.json"
            archivo.write_bytes(salida["csv"])
            contexto.write_bytes(salida["contexto"])
            comando = [sys.executable, str(self.carpeta / "revisar_descarga.py"), str(archivo), str(contexto)]
            correcto = subprocess.run(comando, capture_output=True)
            self.assertEqual(correcto.returncode, 0, correcto.stderr)
            archivo.write_bytes(salida["csv"].replace(b"2600", b"2800"))
            incorrecto = subprocess.run(comando, capture_output=True)
            self.assertEqual(incorrecto.returncode, 2)
            self.assertEqual(incorrecto.stdout, b"")


if __name__ == "__main__":
    unittest.main()
