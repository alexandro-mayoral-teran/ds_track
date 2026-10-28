"""Apoyo opcional de autoría; AppTest se desarrolla como tema en 12.08.

Las transiciones del navegador antes de enviar se revisan además con navegador real.
"""

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from streamlit.testing.v1 import AppTest
from preparar_practica import BASE, MODELO, preparar


class EstadoTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temporal = tempfile.TemporaryDirectory()
        cls.carpeta = preparar(Path(cls.temporal.name) / "practica")

    @classmethod
    def tearDownClass(cls):
        cls.temporal.cleanup()

    def nueva(self):
        return AppTest.from_file(str(self.carpeta / "app.py"), default_timeout=20).run()

    def comprobar(self, app, valores, envios):
        self.assertFalse(app.exception)
        self.assertEqual([m.value for m in app.metric], valores)
        self.assertEqual(app.session_state["envios"], envios)

    def test_inicial_y_reejecucion_sin_aplicar(self):
        app = self.nueva()
        self.comprobar(app, ["1", "2600", "33.33%"], 0)
        app.checkbox(key="mostrar_detalle").uncheck().run()
        self.comprobar(app, ["1", "2600", "33.33%"], 0)
        self.assertEqual(len(app.table), 0)
        app.checkbox(key="mostrar_detalle").check().run()
        self.assertEqual(app.table[0].value.id_credito.tolist(), ["003"])
        app.run()
        self.comprobar(app, ["1", "2600", "33.33%"], 0)

    def test_no_aplica_sin_envio_y_no_pierde_seleccion(self):
        app = self.nueva()
        app.selectbox(key="corte_borrador").set_value("2026-09-30")
        app.number_input(key="minimo_borrador").set_value(2001)
        app.run()  # AppTest puede enviar estado; no simula la retención del navegador.
        self.comprobar(app, ["1", "2600", "33.33%"], 0)
        self.assertEqual(app.session_state["filtros_aplicados"]["corte"], "2026-10-31")
        # Volvemos a preparar el lote: una pasada ajena no conserva un borrador pendiente.
        app.selectbox(key="corte_borrador").set_value("2026-09-30")
        app.number_input(key="minimo_borrador").set_value(2001)
        app.button(key="aplicar").click().run()
        self.comprobar(app, ["1", "2500", "33.33%"], 1)
        app.checkbox(key="mostrar_detalle").uncheck().run()
        self.comprobar(app, ["1", "2500", "33.33%"], 1)
        app.run()
        self.comprobar(app, ["1", "2500", "33.33%"], 1)
        # El submit fue True una pasada; no se vuelve a aplicar por estar guardado.

    def test_casos_manuales_por_envio(self):
        app = self.nueva()
        casos = [
            ("2026-09-30", ["comercio", "servicios"], 2000, [("002", 2000), ("003", 2500)], "66.67%", 4500),
            ("2026-09-30", ["comercio", "servicios"], 2001, [("003", 2500)], "33.33%", 4500),
            ("2026-10-31", ["servicios"], 2000, [], "0.00%", 4600),
            ("2026-10-31", ["servicios"], 1900, [("002", 1900)], "33.33%", 4600),
            ("2026-10-31", [], 0, [], "0.00%", 4600),
            ("2026-09-30", ["comercio", "servicios"], 0, [("001", 0), ("002", 2000), ("003", 2500)], "100.00%", 4500),
            ("2026-10-31", ["comercio"], 2600, [("003", 2600)], "33.33%", 4600),
            ("2026-10-31", ["comercio"], 2601, [], "0.00%", 4600),
            ("2026-10-31", ["comercio", "servicios"], 2000, [("003", 2600)], "33.33%", 4600),
        ]
        for envios, (corte, segmentos, minimo, pares, porcentaje, total) in enumerate(casos, 1):
            with self.subTest(corte=corte, segmentos=segmentos, minimo=minimo):
                app.selectbox(key="corte_borrador").set_value(corte)
                app.multiselect(key="segmentos_borrador").set_value(segmentos)
                app.number_input(key="minimo_borrador").set_value(minimo)
                app.button(key="aplicar").click().run()
                self.comprobar(app, [str(len(pares)), str(sum(v for _, v in pares)), porcentaje], envios)
                self.assertTrue(any(f"3 créditos · {total} MXN" in m.value for m in app.markdown))
                self.assertEqual(app.session_state["filtros_aplicados"],
                                 {"corte": corte, "segmentos": segmentos, "minimo_mxn": minimo})
                if pares:
                    tabla = app.table[0].value
                    self.assertEqual(list(zip(tabla.id_credito, tabla.saldo_mxn)), pares)
                    self.assertEqual(tabla.fecha_corte.tolist(), [corte] * len(pares))
                    self.assertEqual(tabla.segmento.tolist(),
                                     [{"001": "comercio", "002": "servicios", "003": "comercio"}[i] for i, _ in pares])
                else:
                    self.assertEqual(len(app.table), 0)
                    self.assertEqual(len(app.info), 1)

    def test_sesiones_y_copia_de_segmentos(self):
        app = self.nueva()
        app.multiselect(key="segmentos_borrador").set_value(["servicios"])
        app.number_input(key="minimo_borrador").set_value(1900)
        app.button(key="aplicar").click().run()
        self.comprobar(app, ["1", "1900", "33.33%"], 1)
        app.multiselect(key="segmentos_borrador").set_value([]).run()
        self.assertEqual(app.session_state["filtros_aplicados"]["segmentos"], ["servicios"])
        otra = self.nueva()
        self.comprobar(otra, ["1", "2600", "33.33%"], 0)
        app.run()
        self.comprobar(app, ["1", "1900", "33.33%"], 1)

    def test_minimo_contador(self):
        app = AppTest.from_file(str(BASE / "contador.py"), default_timeout=20).run()
        for esperado in [1, 2]:
            app.button[0].click().run()
            self.assertEqual(app.session_state["contador"], esperado)
        app.checkbox[0].check().run()
        self.assertFalse(app.exception)
        self.assertTrue(any(m.value == "Variable local: 1" for m in app.markdown))
        self.assertTrue(any(m.value == "Contador de la sesión: 2" for m in app.markdown))
        otra = AppTest.from_file(str(BASE / "contador.py"), default_timeout=20).run()
        self.assertEqual(otra.session_state["contador"], 0)

    def test_preparador_conserva_fuentes_y_no_sobrescribe(self):
        for nombre in ["cartera.py", "cartera.csv", "configuracion.py", "ejecutar.py"]:
            self.assertEqual((self.carpeta / nombre).read_bytes(), (MODELO / nombre).read_bytes())
        with self.assertRaises(FileExistsError):
            preparar(self.carpeta)
        codigo = "import preparar_practica; print('importado')"
        salida = subprocess.check_output([sys.executable, "-c", codigo], cwd=BASE)
        self.assertEqual(salida.strip(), b"importado")

    def test_cli_comparte_resultado_con_app(self):
        salida = subprocess.check_output([sys.executable, str(self.carpeta / "ejecutar.py"),
                                         "--corte", "2026-09-30", "--minimo", "2001"])
        resultado = json.loads(salida)
        self.assertEqual(resultado["universo"], {"cantidad": 3, "saldo_mxn": 4500})
        self.assertEqual(resultado["seleccion"], [{"id_credito": "003", "segmento": "comercio",
                                                "fecha_corte": "2026-09-30", "saldo_mxn": 2500}])

    def test_fuente_actual_sin_reaplicar_y_error_recuperable(self):
        fuente = self.carpeta / "cartera.csv"
        original = fuente.read_bytes()
        app = self.nueva()
        app.button(key="aplicar").click().run()
        try:
            texto = original.decode("utf-8").replace(",2600", ",2800")
            fuente.write_text(texto, encoding="utf-8")
            app.checkbox(key="mostrar_detalle").uncheck().run()
            self.comprobar(app, ["1", "2800", "33.33%"], 1)
            self.assertTrue(any("3 créditos · 4800 MXN" in m.value for m in app.markdown))
            app.checkbox(key="mostrar_detalle").check().run()
            self.assertEqual(app.table[0].value.saldo_mxn.tolist(), [2800])
            fuente.write_text(texto + texto.splitlines()[1] + "\n", encoding="utf-8")
            app.run()
            self.assertFalse(app.exception)
            self.assertEqual(len(app.error), 1)
            self.assertEqual(len(app.metric), 0)
        finally:
            fuente.write_bytes(original)
        app.run()
        self.comprobar(app, ["1", "2600", "33.33%"], 1)


if __name__ == "__main__":
    unittest.main()
