"""Pruebas de una envoltura que observa sin sustituir el comportamiento."""

import inspect
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

import pandas as pd
from pandas.testing import assert_frame_equal

from analisis_cartera.instrumentacion import log_call, logged_indicators
from analisis_cartera.iteracion import batch_indicators, iter_batches
from pruebas_0504.muestras import CREDITS, write_sources

LOGGER_NAME = "analisis_cartera.instrumentacion"


class PruebasEnvoltura(unittest.TestCase):
    def test_decorar_no_ejecuta_ni_registra(self):
        calls = []

        def operation():
            calls.append("llamada")

        with self.assertNoLogs(LOGGER_NAME, level="INFO"):
            wrapped = log_call(operation)
        self.assertEqual(calls, [])
        self.assertIsNot(wrapped, operation)

    def test_reenvia_argumentos_y_devuelve_el_mismo_objeto_una_vez(self):
        calls = []
        data = []

        def operation(items, amount=1, *, missing="predeterminado"):
            calls.append((items, amount, missing))
            return items

        wrapped = log_call(operation)
        with self.assertLogs(LOGGER_NAME, level="INFO") as captured:
            actual = wrapped(data, 0, missing=None)
        self.assertIs(actual, data)
        self.assertEqual(len(calls), 1)
        self.assertIs(calls[0][0], data)
        self.assertEqual(calls[0][1:], (0, None))
        self.assertEqual([r.getMessage() for r in captured.records],
                         ["Inicio: operation", "Fin: operation"])

    def test_retorno_none_tambien_es_exito(self):
        @log_call
        def operation():
            return None

        with self.assertLogs(LOGGER_NAME, level="INFO") as captured:
            self.assertIsNone(operation())
        self.assertEqual(captured.records[-1].getMessage(), "Fin: operation")

    def test_error_y_causa_conservados_sin_fin(self):
        cause = OSError("Causa didáctica")
        error = ValueError("Error didáctico")

        @log_call
        def operation():
            raise error from cause

        with self.assertLogs(LOGGER_NAME, level="INFO") as captured:
            with self.assertRaises(ValueError) as caught:
                operation()
        self.assertIs(caught.exception, error)
        self.assertIs(caught.exception.__cause__, cause)
        self.assertEqual([r.getMessage() for r in captured.records],
                         ["Inicio: operation", "Falla: operation"])

    def test_interrupciones_se_propagan_sin_exito(self):
        for error in [KeyboardInterrupt(), SystemExit(2)]:
            with self.subTest(error=type(error).__name__):
                @log_call
                def operation():
                    raise error

                with self.assertLogs(LOGGER_NAME, level="INFO") as captured:
                    with self.assertRaises(type(error)) as caught:
                        operation()
                self.assertIs(caught.exception, error)
                self.assertEqual([r.getMessage() for r in captured.records], ["Inicio: operation"])

    def test_metadatos_firma_visible_y_enlace_original(self):
        def operation(amount: int, *, label: str = "base") -> int:
            """Ejemplo propio para comprobar documentación conservada."""
            return amount

        wrapped = log_call(operation)
        self.assertEqual(wrapped.__name__, "operation")
        self.assertEqual(wrapped.__doc__, operation.__doc__)
        self.assertEqual(wrapped.__annotations__, operation.__annotations__)
        self.assertIs(wrapped.__wrapped__, operation)
        self.assertEqual(inspect.signature(wrapped), inspect.signature(operation))
        raw = inspect.signature(wrapped, follow_wrapped=False)
        self.assertEqual(list(raw.parameters), ["args", "kwargs"])
        self.assertEqual([p.kind for p in raw.parameters.values()],
                         [inspect.Parameter.VAR_POSITIONAL, inspect.Parameter.VAR_KEYWORD])

    def test_rechaza_objetos_no_admitidos_y_funciones_generadoras(self):
        for function in [3, [], len, iter_batches]:
            with self.subTest(function=function):
                with self.assertRaises(TypeError):
                    log_call(function)

    def test_retorno_iterador_no_se_consume_ni_certifica(self):
        returned = iter([0, 1])

        @log_call
        def operation():
            return returned

        with self.assertLogs(LOGGER_NAME, level="INFO") as captured:
            actual = operation()
        self.assertIs(actual, returned)
        self.assertEqual(next(actual), 0)
        self.assertEqual(captured.records[-1].getMessage(), "Fin: operation")

    def test_envolturas_separadas_conservan_su_funcion(self):
        def first():
            return 1

        def second():
            return 2

        wrapped_first = log_call(first)
        wrapped_second = log_call(second)
        with self.assertLogs(LOGGER_NAME, level="INFO"):
            self.assertEqual(wrapped_first(), 1)
            self.assertEqual(wrapped_second(), 2)


class PruebasIntegracion(unittest.TestCase):
    def setUp(self):
        temporary = TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.source = write_sources(Path(temporary.name) / "fuentes")

    def test_tablas_y_fuentes_conservadas(self):
        before = {p.name: p.read_bytes() for p in self.source.iterdir()}
        expected = batch_indicators(self.source, batch_size=2)
        with self.assertLogs(LOGGER_NAME, level="INFO"):
            actual = logged_indicators(self.source, batch_size=2)
        assert_frame_equal(actual, expected, check_exact=True)
        self.assertEqual({p.name: p.read_bytes() for p in self.source.iterdir()}, before)

    def test_ceros_ausencias_y_corte_vacio(self):
        with self.assertLogs(LOGGER_NAME, level="INFO"):
            actual = logged_indicators(self.source).set_index("segmento")
            empty = logged_indicators(self.source, "2027-01-31")
        self.assertEqual(actual.loc["comercio", "mediana_mxn"], 0.5)
        self.assertEqual(actual.loc["educacion", "cobertura_pct"], 0)
        self.assertTrue(pd.isna(actual.loc["educacion", "mediana_mxn"]))
        self.assertTrue(empty["cobertura_pct"].isna().all())

    def test_errores_de_datos_y_fuentes_no_se_vuelven_tablas(self):
        with self.assertLogs(LOGGER_NAME, level="WARNING"):
            with self.assertRaises(FileNotFoundError):
                logged_indicators(self.source / "ausente")
            with self.assertRaises(ValueError):
                logged_indicators(self.source, batch_size=0)

    def test_relectura_sin_cache_y_resultado_anterior_intacto(self):
        with self.assertLogs(LOGGER_NAME, level="INFO"):
            first = logged_indicators(self.source)
            before = first.copy(deep=True)
            write_sources(self.source, credits=[*CREDITS, CREDITS[0]])
            with self.assertRaises(ValueError):
                logged_indicators(self.source)
        assert_frame_equal(first, before, check_exact=True)
