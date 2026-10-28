"""Controles opcionales de autoría; no sustituyen el lab ni la revisión visual."""

import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from streamlit.testing.v1 import AppTest
from preparar_practica import BASE, MODELO, preparar


class CacheTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temporal = tempfile.TemporaryDirectory()
        cls.carpeta = preparar(Path(cls.temporal.name) / "practica")
        AppTest.from_file(str(cls.carpeta / "app.py"), default_timeout=20).run()
        cls.cache = sys.modules["cache_analisis"]
        cls.modelo = sys.modules["cartera"]

    @classmethod
    def tearDownClass(cls):
        cls.cache.analizar_con_cache.clear()
        cls.temporal.cleanup()

    def setUp(self):
        self.cache.analizar_con_cache.clear()

    def nueva(self):
        app = AppTest.from_file(str(self.carpeta / "app.py"), default_timeout=20).run()
        self.assertFalse(app.exception)
        return app

    def token(self, app):
        return next(m.value.split(": ", 1)[1] for m in app.caption
                    if m.value.startswith("Identificador del cálculo:"))

    def test_acierto_corte_parametros_y_copia(self):
        filas = self.modelo.leer_cartera(self.carpeta / "cartera.csv")
        original = copy.deepcopy(filas)
        f = self.cache.analizar_con_cache
        a = f(filas, "2026-10-31", ["comercio", "servicios"], 2000, "v1")
        self.assertEqual(a["resultado"]["indicadores"]["saldo_mxn"], 2600)
        a["resultado"]["seleccion"][0]["saldo_mxn"] = 999
        b = f(filas, "2026-10-31", ["comercio", "servicios"], 2000, "v1")
        self.assertEqual(a["calculo"], b["calculo"])
        self.assertIsNot(a, b)
        self.assertEqual(b["resultado"]["seleccion"][0]["saldo_mxn"], 2600)
        self.assertEqual(filas, original)
        casos = [("2026-09-30", ["comercio", "servicios"], 2000, 4500),
                 ("2026-09-30", ["comercio", "servicios"], 2001, 2500),
                 ("2026-10-31", ["servicios"], 2000, 0),
                 ("2026-10-31", ["servicios"], 1900, 1900),
                 ("2026-10-31", [], 0, 0)]
        for corte, segmentos, minimo, saldo in casos:
            with self.subTest(corte=corte, segmentos=segmentos, minimo=minimo):
                r = f(filas, corte, segmentos, minimo, "v1")
                self.assertNotEqual(r["calculo"], b["calculo"])
                self.assertEqual(r["resultado"]["indicadores"]["saldo_mxn"], saldo)
                self.assertEqual(r["resultado"], self.modelo.analizar(filas, corte, segmentos, minimo))

    def test_version_y_contenido_no_solo_totales(self):
        filas = self.modelo.leer_cartera(self.carpeta / "cartera.csv")
        f = self.cache.analizar_con_cache
        a = f(filas, "2026-10-31", ["comercio"], 2000, "v1")
        b = f(filas, "2026-10-31", ["comercio"], 2000, "v2")
        self.assertNotEqual(a["calculo"], b["calculo"])
        compensada = copy.deepcopy(filas)
        compensada[3]["saldo_mxn"] = 200
        compensada[4]["saldo_mxn"] = 1800
        c = f(compensada, "2026-10-31", ["comercio"], 2000, "v1")
        self.assertEqual(a["resultado"]["indicadores"], c["resultado"]["indicadores"])
        self.assertEqual(a["resultado"]["universo"], c["resultado"]["universo"])
        self.assertNotEqual(a["calculo"], c["calculo"])
        f.clear()
        d = f(filas, "2026-10-31", ["comercio"], 2000, "v1")
        self.assertNotEqual(a["calculo"], d["calculo"])

    def test_formulario_otra_pasada_y_limpieza_sin_borrar_filtros(self):
        app = self.nueva()
        token = self.token(app)
        app.checkbox(key="mostrar_detalle").uncheck().run()
        self.assertEqual(self.token(app), token)
        app.selectbox(key="corte_borrador").set_value("2026-09-30")
        app.number_input(key="minimo_borrador").set_value(2001)
        app.button(key="aplicar").click().run()
        token_sep = self.token(app)
        self.assertNotEqual(token_sep, token)
        self.assertEqual([m.value for m in app.metric], ["1", "2500", "33.33%"])
        app.checkbox(key="mostrar_detalle").check().run()
        self.assertEqual(self.token(app), token_sep)
        app.button(key="limpiar_cache").click().run()
        self.assertFalse(app.exception)
        self.assertNotEqual(self.token(app), token_sep)
        self.assertEqual(app.session_state["envios"], 1)
        self.assertEqual(app.session_state["filtros_aplicados"]["corte"], "2026-09-30")
        self.assertEqual(app.table[0].value.id_credito.tolist(), ["003"])

    def test_fuente_actual_antes_de_cache_y_recuperacion(self):
        fuente = self.carpeta / "cartera.csv"
        original = fuente.read_bytes()
        app = self.nueva()
        token = self.token(app)
        try:
            texto = original.decode("utf-8").replace(",2600", ",2800")
            fuente.write_text(texto, encoding="utf-8")
            app.checkbox(key="mostrar_detalle").uncheck().run()
            self.assertFalse(app.exception)
            self.assertNotEqual(self.token(app), token)
            self.assertEqual([m.value for m in app.metric], ["1", "2800", "33.33%"])
            self.assertEqual(app.session_state["envios"], 0)
            fuente.write_text(texto + texto.splitlines()[1] + "\n", encoding="utf-8")
            app.run()
            self.assertEqual(len(app.error), 1)
            self.assertEqual(len(app.metric), 0)
            fuente.unlink()
            app.run()
            self.assertEqual(len(app.error), 1)
            self.assertEqual(len(app.metric), 0)
        finally:
            fuente.write_bytes(original)
        app.run()
        self.assertFalse(app.exception)
        self.assertEqual([m.value for m in app.metric], ["1", "2600", "33.33%"])

    def test_dos_sesiones_comparten_cache_no_filtros(self):
        a = self.nueva()
        token = self.token(a)
        b = self.nueva()
        self.assertEqual(self.token(b), token)
        a.selectbox(key="corte_borrador").set_value("2026-09-30")
        a.button(key="aplicar").click().run()
        self.assertEqual([m.value for m in a.metric], ["2", "4500", "66.67%"])
        b.run()
        self.assertEqual(self.token(b), token)
        self.assertEqual(b.session_state["envios"], 0)
        b.button(key="limpiar_cache").click().run()
        self.assertNotEqual(self.token(b), token)
        a.run()
        self.assertEqual(a.session_state["filtros_aplicados"]["corte"], "2026-09-30")

    def test_ttl_y_limite_reales_en_proceso_nuevo(self):
        with tempfile.TemporaryDirectory() as temporal:
            copia = preparar(Path(temporal) / "ttl")
            archivo = copia / "cache_analisis.py"
            archivo.write_text(archivo.read_text(encoding="utf-8").replace("TTL_SEGUNDOS = 60", "TTL_SEGUNDOS = 0.2"), encoding="utf-8")
            codigo = """
import time
from cartera import leer_cartera
from configuracion import RUTA_DATOS
from cache_analisis import analizar_con_cache as f
filas = leer_cartera(RUTA_DATOS)
a = f(filas, '2026-10-31', ['comercio'], 2000, 'v1')
b = f(filas, '2026-10-31', ['comercio'], 2000, 'v1')
assert a['calculo'] == b['calculo']
time.sleep(0.3)
c = f(filas, '2026-10-31', ['comercio'], 2000, 'v1')
assert c['calculo'] != a['calculo']
assert a['resultado'] == c['resultado']
print('TTL comprobado')
"""
            r = subprocess.run([sys.executable, "-c", codigo], cwd=copia, capture_output=True)
            self.assertEqual(r.returncode, 0, r.stderr.decode("utf-8", errors="replace"))
        filas = self.modelo.leer_cartera(self.carpeta / "cartera.csv")
        f = self.cache.analizar_con_cache
        a = f(filas, "2026-10-31", ["comercio"], 0, "limite")
        for minimo in range(1, 9):
            f(filas, "2026-10-31", ["comercio"], minimo, "limite")
        self.assertNotEqual(a["calculo"], f(filas, "2026-10-31", ["comercio"], 0, "limite")["calculo"])

    def test_minimo_datos_y_recurso(self):
        app = AppTest.from_file(str(self.carpeta / "minimo.py"), default_timeout=20).run()
        self.assertFalse(app.exception)
        ejemplos = sys.modules["cache_ejemplos"]
        a, b = ejemplos.datos_demo(), ejemplos.datos_demo()
        self.assertIsNot(a, b)
        a["importes"].append(999)
        self.assertEqual(b["importes"], [100, 200])
        recurso = ejemplos.recurso_demo()
        self.assertIs(recurso, ejemplos.recurso_demo())
        with self.assertRaises(TypeError):
            recurso["segmentos"] = ()
        ejemplos.datos_demo.clear()
        self.assertIs(recurso, ejemplos.recurso_demo())
        ejemplos.recurso_demo.clear()
        self.assertIsNot(recurso, ejemplos.recurso_demo())

    def test_preparacion_y_referencia_cli(self):
        for nombre in ("cartera.py", "cartera.csv", "configuracion.py", "ejecutar.py"):
            self.assertEqual((self.carpeta / nombre).read_bytes(), (MODELO / nombre).read_bytes())
        with self.assertRaises(FileExistsError):
            preparar(self.carpeta)
        r = json.loads(subprocess.check_output([sys.executable, str(self.carpeta / "ejecutar.py")]))
        self.assertEqual(r["indicadores"]["saldo_mxn"], 2600)
        self.assertEqual(r["universo"], {"cantidad": 3, "saldo_mxn": 4600})


if __name__ == "__main__":
    unittest.main()
