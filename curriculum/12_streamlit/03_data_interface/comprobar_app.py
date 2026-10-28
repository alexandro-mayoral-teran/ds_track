"""Apoyo opcional de autoría. La API AppTest se enseñará en 12.08.

Contrasta casos manuales por ID/importe, indicadores y cambios de widgets.
No sustituye la lectura humana de la app en un navegador.
"""

from pathlib import Path
import json
import shutil
import subprocess
import sys
import tempfile
import unittest

from streamlit.testing.v1 import AppTest

APP = Path(__file__).resolve().with_name("app.py")


class FiltrosTest(unittest.TestCase):
    def test_variante_y_errores_en_procesos_independientes(self):
        # Cada copia se carga en otro proceso: no reutiliza módulos hermanos de otra app.
        with tempfile.TemporaryDirectory() as carpeta:
            destino = Path(carpeta)
            for nombre in ("app.py", "cartera.py", "configuracion.py", "cartera.csv", "ejecutar.py"):
                shutil.copyfile(APP.with_name(nombre), destino / nombre)
            fuente = destino / "cartera.csv"
            texto = fuente.read_text(encoding="utf-8").replace(",2600", ",2800")
            codigo = (
                "import json; from streamlit.testing.v1 import AppTest; "
                "a=AppTest.from_file('app.py',default_timeout=20).run(); "
                "assert not a.exception; "
                "print(json.dumps({'metricas':[m.value for m in a.metric],"
                "'errores':len(a.error),'tablas':len(a.table)}))"
            )
            for contenido, esperado in [
                (texto, {"metricas": ["1", "2800", "33.33%"], "errores": 0, "tablas": 1}),
                (texto + texto.splitlines()[1] + "\n", {"metricas": [], "errores": 1, "tablas": 0}),
                (texto.splitlines()[0] + "\n", {"metricas": ["0", "0", "N/D"], "errores": 0, "tablas": 0}),
                (None, {"metricas": [], "errores": 1, "tablas": 0}),
            ]:
                if contenido is None:
                    fuente.unlink()
                else:
                    fuente.write_text(contenido, encoding="utf-8")
                salida = subprocess.check_output([sys.executable, "-c", codigo], cwd=destino)
                self.assertEqual(json.loads(salida), esperado)
                if contenido == texto:
                    cli = json.loads(subprocess.check_output([sys.executable, "ejecutar.py"], cwd=destino))
                    self.assertEqual(cli["universo"]["saldo_mxn"], 4800)
                    self.assertEqual(cli["indicadores"]["saldo_mxn"], int(esperado["metricas"][1]))

    def test_casos_manuales_y_recuperacion(self):
        app = AppTest.from_file(str(APP), default_timeout=20).run()
        # Esperados independientes y explícitos: corte, segmentos, mínimo, pares, porcentaje.
        casos = [
            ("2026-10-31", ["comercio", "servicios"], 2000, [("003", 2600)], "33.33%"),
            ("2026-09-30", ["comercio", "servicios"], 2000, [("002", 2000), ("003", 2500)], "66.67%"),
            ("2026-09-30", ["comercio", "servicios"], 2001, [("003", 2500)], "33.33%"),
            ("2026-10-31", ["servicios"], 2000, [], "0.00%"),
            ("2026-10-31", ["servicios"], 1900, [("002", 1900)], "33.33%"),
            ("2026-10-31", ["comercio"], 0, [("001", 100), ("003", 2600)], "66.67%"),
            ("2026-09-30", ["comercio", "servicios"], 0, [("001", 0), ("002", 2000), ("003", 2500)], "100.00%"),
            ("2026-10-31", ["comercio", "servicios"], 0, [("001", 100), ("002", 1900), ("003", 2600)], "100.00%"),
            ("2026-10-31", [], 0, [], "0.00%"),
            ("2026-10-31", ["comercio", "servicios"], 2600, [("003", 2600)], "33.33%"),
            ("2026-10-31", ["comercio", "servicios"], 2601, [], "0.00%"),
            ("2026-10-31", ["comercio", "servicios"], 1000000, [], "0.00%"),
        ]
        for corte, segmentos, minimo, pares, porcentaje in casos:
            with self.subTest(corte=corte, segmentos=segmentos, minimo=minimo):
                app.selectbox[0].set_value(corte)
                app.multiselect[0].set_value(segmentos)
                app.number_input[0].set_value(minimo)
                app.run()
                self.assertFalse(app.exception)
                self.assertEqual([m.value for m in app.metric], [str(len(pares)), str(sum(v for _, v in pares)), porcentaje])
                esperado_universo = "4500" if corte == "2026-09-30" else "4600"
                self.assertTrue(any(f"3 créditos · {esperado_universo} MXN" in m.value for m in app.markdown))
                if pares:
                    tabla = app.table[0].value
                    self.assertEqual(list(zip(tabla.id_credito, tabla.saldo_mxn)), pares)
                    self.assertEqual(tabla.fecha_corte.tolist(), [corte] * len(pares))
                    etiquetas = {"001": "comercio", "002": "servicios", "003": "comercio"}
                    self.assertEqual(tabla.segmento.tolist(), [etiquetas[i] for i, _ in pares])
                    self.assertEqual(len(app.info), 0)
                else:
                    self.assertEqual(len(app.table), 0)
                    self.assertEqual(len(app.info), 1)

        # Recuperar después del vacío; no quedan cifras de una selección anterior.
        app.number_input[0].set_value(2000).run()
        self.assertFalse(app.exception)
        self.assertEqual([m.value for m in app.metric], ["1", "2600", "33.33%"])
        self.assertEqual(app.table[0].value.id_credito.tolist(), ["003"])

    def test_arranque_nuevo_y_valores_iniciales(self):
        app = AppTest.from_file(str(APP), default_timeout=20).run()
        self.assertFalse(app.exception)
        self.assertEqual(app.selectbox[0].value, "2026-10-31")
        self.assertEqual(app.multiselect[0].value, ["comercio", "servicios"])
        self.assertEqual(app.number_input[0].value, 2000)
        self.assertEqual([m.value for m in app.metric], ["1", "2600", "33.33%"])


if __name__ == "__main__":
    unittest.main()
