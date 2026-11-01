"""Pruebas de equivalencia, fronteras y conservación del estado de instrumentos."""

import cProfile
import sys
import tracemalloc
import unittest

from analisis_cartera.medicion import (profile_operation, repeat_timings, trace_peak,
                                     validate_dates_each, validate_dates_reusing)


class PruebasFechas(unittest.TestCase):
    def test_equivalencia_vacios_repetidos_y_consumo(self):
        dates = ["2026-09-30", "2026-10-31", "2026-09-30"]
        before = dates.copy()
        for operation in [validate_dates_each, validate_dates_reusing]:
            with self.subTest(operation=operation.__name__):
                self.assertEqual(operation([]), 0)
                self.assertEqual(operation(dates), 3)
                iterator = iter(dates)
                self.assertEqual(operation(iterator), 3)
                self.assertEqual(list(iterator), [])
        self.assertEqual(dates, before)

    def test_errores_en_misma_posicion_y_tipos(self):
        for bad, error in [(None, TypeError), (31, TypeError), ("", ValueError),
                           ("2026-02-29", ValueError), ("2026-9-30", ValueError)]:
            for operation in [validate_dates_each, validate_dates_reusing]:
                with self.subTest(bad=bad, operation=operation.__name__):
                    iterator = iter(["2026-10-31", "2026-10-31", bad, "2026-09-30"])
                    with self.assertRaises(error):
                        operation(iterator)
                    self.assertEqual(next(iterator), "2026-09-30")

    def test_no_conserva_cache_ni_resultado_entre_llamadas(self):
        dates = ["2026-10-31"] * 3
        self.assertEqual(validate_dates_reusing(dates), 3)
        dates[-1] = "fecha inválida"
        with self.assertRaises(ValueError):
            validate_dates_reusing(dates)


class PruebasCronometro(unittest.TestCase):
    def test_repeticiones_calentamiento_orden_y_check(self):
        calls, checks = [], []

        def first():
            calls.append("A")
            return "A"

        def second():
            calls.append("B")
            return "B"

        actual = repeat_timings({"A": first, "B": second}, repeats=3, warmups=1,
                                check=checks.append)
        self.assertEqual(calls, ["A", "B", "A", "B", "B", "A", "A", "B"])
        self.assertEqual(checks, calls)
        self.assertEqual(actual["variante"].tolist(), ["A", "B", "B", "A", "A", "B"])
        self.assertEqual(actual["repeticion"].tolist(), [1, 1, 2, 2, 3, 3])
        self.assertEqual(actual["posicion"].tolist(), [1, 2, 1, 2, 1, 2])
        self.assertTrue(actual["segundos"].ge(0).all())

    def test_parametros_invalidos_no_ejecutan_operacion(self):
        calls = []

        def operation():
            calls.append(1)

        for kwargs, error in [({"repeats": 0}, ValueError), ({"repeats": True}, TypeError),
                              ({"warmups": -1}, ValueError), ({"warmups": 0.5}, TypeError),
                              ({"check": 3}, TypeError)]:
            with self.subTest(kwargs=kwargs):
                with self.assertRaises(error):
                    repeat_timings({"base": operation}, **kwargs)
        with self.assertRaises(ValueError):
            repeat_timings({})
        with self.assertRaises(TypeError):
            repeat_timings({"base": 3})
        self.assertEqual(calls, [])

    def test_falla_de_operacion_se_propaga(self):
        error = ValueError("No publicar tiempos parciales")

        def operation():
            raise error

        with self.assertRaises(ValueError) as caught:
            repeat_timings({"base": operation}, warmups=0)
        self.assertIs(caught.exception, error)

    def test_falla_de_check_fuera_del_instrumento(self):
        calls = []

        def operation():
            calls.append(1)
            return 0

        def check(result):
            self.assertFalse(tracemalloc.is_tracing())
            self.assertIsNone(sys.getprofile())
            raise ValueError("Resultado no equivalente")

        with self.assertRaisesRegex(ValueError, "no equivalente"):
            repeat_timings({"base": operation}, repeats=2, warmups=0, check=check)
        self.assertEqual(calls, [1])


class PruebasInstrumentos(unittest.TestCase):
    def test_trazado_aislado_resultado_vivo_y_check_posterior(self):
        states = []

        def operation():
            states.append(tracemalloc.is_tracing())
            return bytearray(4096)

        def check(result):
            states.append(tracemalloc.is_tracing())
            self.assertEqual(len(result), 4096)

        actual = trace_peak(operation, check=check)
        self.assertEqual(states, [True, False])
        self.assertGreaterEqual(actual["pico_trazado_bytes"], actual["actual_trazada_bytes"])
        self.assertGreater(actual["actual_trazada_bytes"], 0)
        self.assertFalse(tracemalloc.is_tracing())

    def test_trazado_se_detiene_ante_error(self):
        error = OSError("Falla didáctica")

        def operation():
            raise error

        with self.assertRaises(OSError) as caught:
            trace_peak(operation)
        self.assertIs(caught.exception, error)
        self.assertFalse(tracemalloc.is_tracing())

    def test_sesion_tracemalloc_ajena_no_se_detiene(self):
        tracemalloc.start()
        try:
            for operation in [lambda: repeat_timings({"base": lambda: 1}),
                              lambda: trace_peak(lambda: 1),
                              lambda: profile_operation(lambda: 1)]:
                with self.assertRaises(RuntimeError):
                    operation()
                self.assertTrue(tracemalloc.is_tracing())
        finally:
            tracemalloc.stop()

    def test_perfil_efectivo_y_limpieza_ante_error(self):
        states = []

        def operation():
            # Observar el instrumento real en ambas versiones de CPython.
            monitoring = getattr(sys, "monitoring", None)
            states.append(sys.getprofile() is not None or
                          (monitoring is not None and monitoring.get_tool(2) == "cProfile"))
            return sum(range(10))

        text = profile_operation(operation)
        self.assertEqual(states, [True])
        self.assertIn("operation", text)
        self.assertIn("function calls", text)
        self.assertIsNone(sys.getprofile())

        def failing():
            raise ValueError("Falla perfilada")

        with self.assertRaises(ValueError):
            profile_operation(failing)
        self.assertIsNone(sys.getprofile())
        with self.assertRaises(ValueError):
            profile_operation(operation, limit=0)

    def test_cprofile_ajeno_no_se_reemplaza(self):
        profiler = cProfile.Profile()
        profiler.enable()
        try:
            for operation in [lambda: repeat_timings({"base": lambda: 1}),
                              lambda: trace_peak(lambda: 1),
                              lambda: profile_operation(lambda: 1)]:
                with self.assertRaises(RuntimeError):
                    operation()
            # El perfil conserva llamadas posteriores al rechazo.
            sum(range(3))
        finally:
            profiler.disable()
        profiler.create_stats()
        self.assertTrue(any("sum" in key[2] for key in profiler.stats))

    def test_perfil_ajeno_no_se_reemplaza(self):
        previous = sys.getprofile()

        def hook(frame, event, arg):
            return None

        sys.setprofile(hook)
        try:
            for operation in [lambda: repeat_timings({"base": lambda: 1}),
                              lambda: trace_peak(lambda: 1),
                              lambda: profile_operation(lambda: 1)]:
                with self.assertRaises(RuntimeError):
                    operation()
                self.assertIs(sys.getprofile(), hook)
        finally:
            sys.setprofile(previous)
