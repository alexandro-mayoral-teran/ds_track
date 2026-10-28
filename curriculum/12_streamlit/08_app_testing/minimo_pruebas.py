"""Ejecutar con Python del entorno Streamlit desde la copia preparada."""

from pathlib import Path
import unittest

from streamlit.testing.v1 import AppTest


class PruebaMinima(unittest.TestCase):
    def test_frontera_y_vacio(self):
        app = AppTest.from_file(str(Path(__file__).with_name("minimo.py")), default_timeout=20).run()
        self.assertFalse(app.exception)
        self.assertEqual([m.value for m in app.metric], ["2", "300"])
        app.number_input(key="minimo").set_value(200).run()
        self.assertFalse(app.exception)
        self.assertEqual([m.value for m in app.metric], ["1", "200"])
        app.number_input(key="minimo").set_value(201).run()
        self.assertFalse(app.exception)
        self.assertEqual([m.value for m in app.metric], ["0", "0"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
