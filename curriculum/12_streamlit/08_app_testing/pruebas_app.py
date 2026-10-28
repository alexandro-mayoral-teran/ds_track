"""Integración AppTest; cada prueba tiene CSV temporal y sesión propios."""

from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from streamlit.testing.v1 import AppTest

import configuracion
from cache_analisis import analizar_con_cache

BASE = Path(__file__).resolve().parent
SEGMENTOS = ["comercio", "servicios"]


class PruebasApp(unittest.TestCase):
    def setUp(self):
        # Se restaura la ruta incluso si una aserción falla: orden de limpieza LIFO.
        temporal = tempfile.TemporaryDirectory()
        self.addCleanup(temporal.cleanup)
        self.fuente = Path(temporal.name) / "cartera.csv"
        self.original = (BASE / "cartera.csv").read_bytes()
        self.fuente.write_bytes(self.original)
        cambio = patch.object(configuracion, "RUTA_DATOS", self.fuente)
        cambio.start()
        self.addCleanup(cambio.stop)
        analizar_con_cache.clear()
        self.addCleanup(analizar_con_cache.clear)

    def nueva(self):
        app = AppTest.from_file(str(BASE / "app.py"), default_timeout=20).run()
        self.assertFalse(app.exception)
        return app

    def aplicar(self, app, corte="2026-09-30", segmentos=None, minimo="2000"):
        app.selectbox(key="corte_borrador").set_value(corte)
        app.multiselect(key="segmentos_borrador").set_value(SEGMENTOS if segmentos is None else segmentos)
        app.text_input(key="minimo_borrador").set_value(minimo)
        app.button(key="aplicar").click().run()
        self.assertFalse(app.exception)

    def comprobar_metricas(self, app, valores):
        self.assertEqual([m.value for m in app.metric], valores)

    def test_inicio(self):
        app = self.nueva()
        self.comprobar_metricas(app, ["1", "2600", "33.33%"])
        self.assertEqual(app.table[0].value.to_dict(orient="records"), [
            {"id_credito": "003", "segmento": "comercio", "fecha_corte": "2026-10-31", "saldo_mxn": 2600},
        ])
        self.assertEqual(app.session_state["envios"], 0)

    def test_cambio_corte_y_frontera(self):
        app = self.nueva()
        self.aplicar(app)
        self.comprobar_metricas(app, ["2", "4500", "66.67%"])
        self.assertEqual(app.table[0].value.to_dict(orient="records"), [
            {"id_credito": "002", "segmento": "servicios", "fecha_corte": "2026-09-30", "saldo_mxn": 2000},
            {"id_credito": "003", "segmento": "comercio", "fecha_corte": "2026-09-30", "saldo_mxn": 2500},
        ])
        self.aplicar(app, minimo="2001")
        self.comprobar_metricas(app, ["1", "2500", "33.33%"])
        self.assertEqual(list(app.table[0].value.id_credito), ["003"])
        self.assertEqual(app.session_state["envios"], 2)

    def test_rechazo_conserva_y_recupera(self):
        app = self.nueva()
        self.aplicar(app, minimo="2.5")
        self.assertEqual(len(app.error), 1)
        self.comprobar_metricas(app, ["1", "2600", "33.33%"])
        self.assertEqual(app.session_state["envios"], 0)
        self.assertEqual(app.session_state["filtros_aplicados"]["corte"], "2026-10-31")
        self.assertTrue(all(b.proto.disabled for b in app.get("download_button")))
        self.aplicar(app)
        self.assertEqual(len(app.error), 0)
        self.assertEqual(app.session_state["envios"], 1)
        self.assertTrue(all(not b.proto.disabled for b in app.get("download_button")))

    def test_vacio_valido(self):
        app = self.nueva()
        self.aplicar(app, segmentos=[], minimo="0")
        self.comprobar_metricas(app, ["0", "0", "0.00%"])
        self.assertEqual(len(app.table), 0)
        self.assertEqual(len(app.get("vega_lite_chart")), 0)
        self.assertEqual(len(app.get("download_button")), 2)
        self.assertTrue(all(not b.proto.disabled for b in app.get("download_button")))

    def test_corte_ausente(self):
        app = self.nueva()
        self.aplicar(app, corte="2026-11-30")
        self.assertEqual(len(app.warning), 1)
        self.comprobar_metricas(app, [])
        self.assertEqual(len(app.get("download_button")), 0)

    def test_cero_observado(self):
        # Muestra independiente: un crédito conocido con saldo cero.
        self.fuente.write_text("id_credito,segmento,fecha_corte,saldo_mxn\n001,comercio,2026-10-31,0\n", encoding="utf-8")
        app = self.nueva()
        self.aplicar(app, corte="2026-10-31", minimo="0")
        self.comprobar_metricas(app, ["1", "0", "100.00%"])
        self.assertEqual(len(app.table[0].value), 1)
        self.assertEqual(len(app.get("vega_lite_chart")), 1)

    def test_fuente_invalida_aun_fuera_del_filtro_y_recuperacion(self):
        app = self.nueva()  # Primero hay resultados y una entrada en caché.
        texto = self.original.decode("utf-8")
        # Repite septiembre, mientras la app selecciona octubre.
        self.fuente.write_text(texto + texto.splitlines()[1] + "\n", encoding="utf-8")
        app.button(key="reintentar").click().run()
        self.assertFalse(app.exception)  # Error tratado por la app, no excepción sin tratar.
        self.assertEqual(len(app.error), 1)
        self.comprobar_metricas(app, [])
        self.assertEqual(len(app.table), 0)
        self.assertEqual(len(app.get("vega_lite_chart")), 0)
        self.assertEqual(len(app.get("download_button")), 0)
        self.fuente.write_bytes(self.original)
        app.button(key="reintentar").click().run()
        self.assertFalse(app.exception)
        self.assertEqual(len(app.error), 0)
        self.comprobar_metricas(app, ["1", "2600", "33.33%"])

    def test_fuente_ausente_y_encabezado_solo(self):
        app = self.nueva()
        self.fuente.unlink()  # Solo el CSV temporal creado por esta prueba.
        app.button(key="reintentar").click().run()
        self.assertFalse(app.exception)
        self.assertEqual(len(app.error), 1)
        self.comprobar_metricas(app, [])
        self.assertEqual(len(app.get("download_button")), 0)
        self.fuente.write_text("id_credito,segmento,fecha_corte,saldo_mxn\n", encoding="utf-8")
        app.button(key="reintentar").click().run()
        self.assertFalse(app.exception)
        self.assertEqual(len(app.warning), 1)
        self.comprobar_metricas(app, [])
        self.assertEqual(len(app.get("download_button")), 0)

    def test_relee_cambio_de_datos(self):
        app = self.nueva()
        self.fuente.write_bytes(self.original.replace(b",2600", b",2800"))
        app.button(key="reintentar").click().run()
        self.assertFalse(app.exception)
        self.comprobar_metricas(app, ["1", "2800", "33.33%"])
        self.assertEqual(app.session_state["envios"], 0)
        self.assertEqual(list(app.table[0].value.saldo_mxn), [2800])

    def test_sesion_nueva_y_otra_pasada(self):
        primera = self.nueva()
        self.aplicar(primera)
        primera.checkbox(key="mostrar_detalle").uncheck().run()
        self.assertFalse(primera.exception)
        self.assertEqual(len(primera.table), 0)
        self.comprobar_metricas(primera, ["2", "4500", "66.67%"])
        self.assertEqual(primera.session_state["envios"], 1)
        segunda = self.nueva()
        self.comprobar_metricas(segunda, ["1", "2600", "33.33%"])
        self.assertEqual(segunda.session_state["envios"], 0)
        self.assertEqual(primera.session_state["filtros_aplicados"]["corte"], "2026-09-30")

    def test_datos_del_grafico_y_controles_de_descarga(self):
        # Ampliación dependiente de la versión: protocolo Streamlit 1.66.1.
        from pyarrow import ipc

        app = self.nueva()
        self.aplicar(app)
        grafico = app.get("vega_lite_chart")[0]
        datos = ipc.open_stream(grafico.proto.data.data).read_all().to_pylist()
        self.assertEqual(datos, [
            {"id_credito": "002", "segmento": "servicios", "fecha_corte": "2026-09-30", "saldo_mxn": 2000},
            {"id_credito": "003", "segmento": "comercio", "fecha_corte": "2026-09-30", "saldo_mxn": 2500},
        ])
        botones = app.get("download_button")
        self.assertEqual(len(botones), 2)
        self.assertTrue(all(not b.proto.disabled and b.proto.ignore_rerun for b in botones))
        # No equivale a pulsar los botones ni a guardar sus archivos en navegador.


if __name__ == "__main__":
    unittest.main(verbosity=2)
