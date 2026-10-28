"""Apoyo de autoría: estados, mensajes, ausencia de cifras obsoletas y recuperación."""

from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

from streamlit.testing.v1 import AppTest
from preparar_practica import BASE, MODELO, preparar


class MensajesTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temporal = tempfile.TemporaryDirectory()
        cls.carpeta = preparar(Path(cls.temporal.name) / "practica")
        AppTest.from_file(str(cls.carpeta / "app.py"), default_timeout=20).run()
        cls.entradas = sys.modules["entradas"]
        cls.cache = sys.modules["cache_analisis"]

    @classmethod
    def tearDownClass(cls):
        cls.cache.analizar_con_cache.clear()
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

    def test_interpretacion_de_entradas(self):
        f = self.entradas.preparar_filtros
        for texto, valor in [("0", 0), ("2000", 2000), (" 2000 ", 2000), ("1000000", 1000000)]:
            self.assertEqual(f("2026-10-31", [], texto)["minimo_mxn"], valor)
        for texto in ["", " ", "2000.5", "2000.0", "-1", "+1", "1,000", "2e3", "0002", "1000001", "9" * 30, None, True]:
            with self.subTest(texto=texto), self.assertRaises(ValueError):
                f("2026-10-31", [], texto)
        for fecha, segmentos in [("2026-02-30", []), ("2026-10-31", ["otro"]), ("2026-10-31", ["comercio"] * 2)]:
            with self.assertRaises(ValueError):
                f(fecha, segmentos, "0")

    def test_casos_manuales_y_aviso_visible_sin_detalle(self):
        app = self.nueva()
        self.assertEqual([m.value for m in app.metric], ["1", "2600", "33.33%"])
        casos = [
            ("2026-09-30", ["comercio", "servicios"], "2000", [("002", 2000), ("003", 2500)], "66.67%"),
            ("2026-09-30", ["comercio", "servicios"], "2001", [("003", 2500)], "33.33%"),
            ("2026-10-31", ["servicios"], "2000", [], "0.00%"),
            ("2026-10-31", ["servicios"], "1900", [("002", 1900)], "33.33%"),
            ("2026-10-31", [], "0", [], "0.00%"),
        ]
        for corte, segmentos, minimo, pares, porcentaje in casos:
            self.aplicar(app, corte, segmentos, minimo)
            self.assertEqual([m.value for m in app.metric], [str(len(pares)), str(sum(v for _, v in pares)), porcentaje])
            if pares:
                tabla = app.table[0].value
                self.assertEqual(list(zip(tabla.id_credito, tabla.saldo_mxn)), pares)
                self.assertEqual(tabla.fecha_corte.tolist(), [corte] * len(pares))
            else:
                self.assertEqual(len(app.info), 1)
                app.checkbox(key="mostrar_detalle").uncheck().run()
                self.assertEqual(len(app.info), 1)
                self.assertEqual(len(app.table), 0)
                app.checkbox(key="mostrar_detalle").check().run()

    def test_intento_invalido_no_cambia_ultima_seleccion(self):
        app = self.nueva()
        self.aplicar(app, "2026-09-30", ["comercio", "servicios"], "2001")
        for texto in ["", "2000.5", "-1", "1,000", "1000001"]:
            self.aplicar(app, "2026-10-31", [], texto)
            self.assertEqual([m.value for m in app.metric], ["1", "2500", "33.33%"])
            self.assertEqual(app.session_state["envios"], 1)
            self.assertEqual(app.session_state["filtros_aplicados"]["corte"], "2026-09-30")
            self.assertEqual(len(app.error), 1)
            self.assertIn("Últimos filtros válidos", app.subheader[0].value)
        app.checkbox(key="mostrar_detalle").uncheck().run()
        self.assertEqual(len(app.error), 1)
        self.aplicar(app, "2026-09-30", ["comercio", "servicios"], " 2000 ")
        self.assertEqual(len(app.error), 0)
        self.assertEqual([m.value for m in app.metric], ["2", "4500", "66.67%"])
        self.assertEqual(app.session_state["envios"], 2)

    def test_corte_sin_registros_y_recuperacion(self):
        app = self.nueva()
        self.aplicar(app, "2026-11-30", ["comercio", "servicios"], "2000")
        self.assertEqual(len(app.warning), 1)
        self.assertIn("proporción no está definida", app.warning[0].value)
        self.assertEqual(len(app.metric), 0)
        self.assertEqual(len(app.table), 0)
        self.aplicar(app, "2026-10-31", ["comercio", "servicios"], "2000")
        self.assertEqual([m.value for m in app.metric], ["1", "2600", "33.33%"])

    def test_fuente_ausente_no_presenta_cache_y_puede_reintentar(self):
        fuente = self.carpeta / "cartera.csv"
        original = fuente.read_bytes()
        app = self.nueva()
        self.aplicar(app, "2026-09-30", ["comercio", "servicios"], "2001")
        try:
            fuente.unlink()
            app.button(key="reintentar").click().run()
            self.assertFalse(app.exception)
            self.assertIn("No se encontró", app.error[0].value)
            self.assertEqual(len(app.metric), 0)
            self.assertEqual(len(app.table), 0)
        finally:
            fuente.write_bytes(original)
        app.button(key="reintentar").click().run()
        self.assertEqual([m.value for m in app.metric], ["1", "2500", "33.33%"])
        self.assertEqual(app.session_state["envios"], 1)

    def test_fuente_invalida_encabezado_solo_y_cero_conocido(self):
        fuente = self.carpeta / "cartera.csv"
        original = fuente.read_bytes()
        lineas = original.decode("utf-8").splitlines()
        app = self.nueva()
        try:
            for contenido in [b"", b"id,importe\n1,2\n", original + (lineas[1] + "\n").encode(),
                              original.replace(b",2600", b","), b"\xff\xfe"]:
                fuente.write_bytes(contenido)
                app.button(key="reintentar").click().run()
                self.assertFalse(app.exception)
                self.assertEqual(len(app.error), 1)
                self.assertEqual(len(app.metric), 0)
            fuente.write_text(lineas[0] + "\n", encoding="utf-8")
            app.button(key="reintentar").click().run()
            self.assertEqual(len(app.warning), 1)
            self.assertEqual(len(app.error), 0)
            self.assertEqual(len(app.metric), 0)
            fuente.write_text(lineas[0] + "\n" + lineas[1] + "\n", encoding="utf-8")
            self.aplicar(app, "2026-09-30", ["comercio", "servicios"], "0")
            self.assertEqual([m.value for m in app.metric], ["1", "0", "100.00%"])
            self.assertIn("saldo conocido igual a cero", app.info[0].value)
            self.assertEqual(app.table[0].value.id_credito.tolist(), ["001"])
        finally:
            fuente.write_bytes(original)

    def test_errores_de_acceso_con_lector_inyectado(self):
        app = self.nueva()
        for error in [PermissionError("denegado para el control"), OSError("fallo de lectura simulado")]:
            with patch.object(sys.modules["cartera"], "leer_cartera", side_effect=error):
                app.button(key="reintentar").click().run()
                self.assertFalse(app.exception)
                self.assertEqual(len(app.error), 1)
                self.assertEqual(len(app.metric), 0)
        app.button(key="reintentar").click().run()
        self.assertEqual([m.value for m in app.metric], ["1", "2600", "33.33%"])

    def test_sesiones_independientes_y_preparador_exclusivo(self):
        a = self.nueva()
        self.aplicar(a, "2026-09-30", ["comercio"], "2001")
        self.aplicar(a, "2026-10-31", [], "abc")
        b = self.nueva()
        self.assertEqual(len(b.error), 0)
        self.assertEqual([m.value for m in b.metric], ["1", "2600", "33.33%"])
        self.assertEqual(len(a.error), 1)
        for nombre in ("cartera.py", "cartera.csv", "configuracion.py", "ejecutar.py"):
            self.assertEqual((self.carpeta / nombre).read_bytes(), (MODELO / nombre).read_bytes())
        self.assertEqual((self.carpeta / "cache_analisis.py").read_bytes(), (BASE.parent / "05_data_resource_cache/cache_analisis.py").read_bytes())
        with self.assertRaises(FileExistsError):
            preparar(self.carpeta)

    def test_minimo_cuatro_situaciones(self):
        app = AppTest.from_file(str(self.carpeta / "minimo.py"), default_timeout=20).run()
        self.assertEqual([m.value for m in app.metric], ["1", "0"])
        app.selectbox[0].set_value("Filtro sin coincidencias").run()
        self.assertEqual([m.value for m in app.metric], ["0", "0"])
        app.selectbox[0].set_value("Corte sin registros").run()
        self.assertEqual(len(app.warning), 1)
        self.assertEqual(len(app.metric), 0)
        app.selectbox[0].set_value("Fuente inválida").run()
        self.assertEqual(len(app.error), 1)
        self.assertEqual(len(app.metric), 0)


if __name__ == "__main__":
    unittest.main()
