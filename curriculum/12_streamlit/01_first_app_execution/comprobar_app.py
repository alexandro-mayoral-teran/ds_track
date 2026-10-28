"""Comprobación de autoría opcional; AppTest se estudia en 12.08.

Ejecutar con el entorno de 12.01: python ruta/comprobar_app.py.
Simula interacciones; no sustituye abrir la app real en un navegador.
"""

from pathlib import Path
import unittest

from streamlit.testing.v1 import AppTest

APP = Path(__file__).resolve().with_name("app.py")


class PrimeraAppTest(unittest.TestCase):
    def test_pasadas_detalle_boton_y_sesion_nueva(self):
        app = AppTest.from_file(str(APP), default_timeout=20).run()
        self.assertFalse(app.exception)
        self.assertEqual(app.metric[0].value, "660")
        self.assertEqual(len(app.table), 0)
        primera_marca = app.caption[0].value
        self.assertEqual(app.markdown[1].value, "Variable local pasadas: 1")

        app.checkbox[0].check().run()
        self.assertFalse(app.exception)
        self.assertNotEqual(app.caption[0].value, primera_marca)
        self.assertEqual(app.metric[0].value, "660")
        detalle = app.table[0].value
        self.assertEqual(detalle["venta_id"].tolist(), ["V001", "V002", "V003", "V004"])
        self.assertEqual(detalle["importe_mxn"].tolist(), [300, 240, 0, 120])
        self.assertEqual(detalle["unidades"].tolist(), [4, 2, 0, 3])
        self.assertEqual(detalle["precio_mxn"].tolist(), [75, 120, 50, 40])
        self.assertEqual(app.markdown[1].value, "Variable local pasadas: 1")

        marca_detalle = app.caption[0].value
        app.button[0].click().run()
        self.assertFalse(app.exception)
        self.assertNotEqual(app.caption[0].value, marca_detalle)
        self.assertEqual(len(app.info), 1)
        self.assertTrue(app.checkbox[0].value)
        self.assertEqual(app.metric[0].value, "660")

        app.checkbox[0].uncheck().run()
        self.assertFalse(app.exception)
        self.assertEqual(len(app.table), 0)
        self.assertEqual(len(app.info), 0)  # El botón no queda True en la siguiente pasada.
        self.assertEqual(app.metric[0].value, "660")

        nueva = AppTest.from_file(str(APP), default_timeout=20).run()
        self.assertFalse(nueva.exception)
        self.assertFalse(nueva.checkbox[0].value)
        self.assertEqual(nueva.metric[0].value, "660")

    def test_minimo(self):
        app = AppTest.from_file(str(APP.with_name("hola.py")), default_timeout=20).run()
        self.assertFalse(app.exception)
        self.assertEqual(app.metric[0].value, "300")


if __name__ == "__main__":
    unittest.main()
