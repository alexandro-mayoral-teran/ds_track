"""Comprobar transporte, paginación, reglas y fallas sin solicitudes de red."""

from copy import deepcopy
from email.message import Message
import io
import json
from pathlib import Path
import unittest
from unittest.mock import patch
from urllib.error import HTTPError, URLError

from pandas.testing import assert_frame_equal

from analisis_cartera.api import ApiError, fetch_detail, http_transport, simulation_transport
from analisis_cartera.entrada import read_detail
from analisis_cartera.transformacion import summarize

SAMPLES = Path(__file__).resolve().parents[2] / "10_api_integration/muestras"
SOURCE = Path(__file__).resolve().parents[3] / "03_sql_databases/01_relational_sqlite/data"


def item(identifier="001", cut="2026-10-31", balance=0):
    return {"id_credito": identifier, "fecha_corte": cut, "saldo_mxn": balance,
            "dias_atraso": None, "segmento": "comercio"}


def response(items=None, *, total=None, next_page=None, status=200):
    items = [item()] if items is None else items
    return {"status": status, "content_type": "application/json; charset=utf-8", "retry_after": None,
            "body": json.dumps({"items": items, "total": len(items) if total is None else total,
                                "next_page": next_page}, allow_nan=False)}


def transport(responses, calls=None):
    steps = iter(responses)

    def fetch(page, timeout):
        if calls is not None:
            calls.append((page, timeout))
        value = next(steps)
        if isinstance(value, Exception):
            raise value
        return value

    return fetch


class PruebasExtraccion(unittest.TestCase):
    def test_tres_paginas_equivalentes_y_fuentes_intactas(self):
        before = {p: p.read_bytes() for p in SAMPLES.iterdir() if p.is_file()}
        actual = fetch_detail(simulation_transport(SAMPLES / "correcto.json"))
        expected = read_detail(SOURCE)
        assert_frame_equal(actual, expected, check_exact=True)
        assert_frame_equal(summarize(actual, "2026-10-31")[1], summarize(expected, "2026-10-31")[1])
        self.assertEqual(len(actual), 48)
        self.assertEqual(before, {p: p.read_bytes() for p in before})

    def test_vacio_conserva_columnas_y_tipos(self):
        actual = fetch_detail(transport([response([])]), max_rows=0)
        self.assertTrue(actual.empty)
        self.assertEqual(actual.saldo_mxn.dtype.name, "Int64")
        self.assertEqual(actual.id_credito.dtype.name, "string")
        self.assertEqual(summarize(actual, "2026-10-31")[1].registros.sum(), 0)

    def test_cero_ausencia_identificador_y_precision_intactos(self):
        rows = [item("001", balance=0), item("002", balance=None),
                item("003", balance=2**63 - 1)]
        before = deepcopy(rows)
        actual = fetch_detail(transport([response(rows)]))
        self.assertEqual(actual.id_credito.tolist(), ["001", "002", "003"])
        self.assertEqual(actual.saldo_mxn.iloc[0], 0)
        self.assertTrue(actual.saldo_mxn.isna().iloc[1])
        self.assertEqual(actual.saldo_mxn.iloc[2], 2**63 - 1)
        self.assertEqual(rows, before)

    def test_campos_invalidos_no_se_convierten_silenciosamente(self):
        for key, bad in [("id_credito", 1), ("id_credito", " "), ("fecha_corte", None),
                         ("fecha_corte", "2026-02-29"), ("fecha_corte", "2026-9-30"),
                         ("saldo_mxn", True), ("saldo_mxn", -1), ("saldo_mxn", "10"),
                         ("saldo_mxn", 1.5), ("saldo_mxn", 2**63),
                         ("dias_atraso", False), ("segmento", "otro")]:
            with self.subTest(key=key, bad=bad):
                row = item()
                row[key] = bad
                with self.assertRaises(ApiError):
                    fetch_detail(transport([response([row])]))

    def test_esquema_de_pagina_y_fila(self):
        for payload in [[], {"items": {}, "next_page": None, "total": 0},
                        {"items": [], "next_page": None, "total": True},
                        {"items": [], "next_page": None},
                        {"items": [], "next_page": None, "total": 0, "nuevo": 1},
                        {"items": [{"id_credito": "001"}], "next_page": None, "total": 1}]:
            with self.subTest(payload=payload):
                envelope = response([])
                envelope["body"] = json.dumps(payload)
                with self.assertRaises(ApiError):
                    fetch_detail(transport([envelope]))

    def test_json_invalido_constantes_y_campos_repetidos(self):
        for text in ['{', '{"items":[],"total":NaN,"next_page":null}',
                     '{"items":[],"items":[],"total":0,"next_page":null}']:
            envelope = response([])
            envelope["body"] = text
            with self.subTest(text=text), self.assertRaises(ApiError):
                fetch_detail(transport([envelope]))

    def test_tipo_de_contenido_y_sobre(self):
        for value in [None, {}, {**response(), "content_type": "text/html"},
                      {**response(), "body": b"{}"}, {**response(), "status": True}]:
            with self.subTest(value=value), self.assertRaises(ApiError):
                fetch_detail(transport([value]))

    def test_duplicado_y_segmento_cambiante_entre_paginas(self):
        for second in [item(), {**item(cut="2026-09-30"), "segmento": "consumo"}]:
            with self.subTest(second=second), self.assertRaises(ApiError):
                fetch_detail(transport([response(total=2, next_page=2), response([second], total=2)]))

    def test_paginacion_no_avanza_o_total_incompleto(self):
        for next_page in [1, 3, True, "2"]:
            with self.subTest(next_page=next_page), self.assertRaises(ApiError):
                fetch_detail(transport([response(total=2, next_page=next_page)]))
        with self.assertRaisesRegex(ApiError, "conciliar"):
            fetch_detail(transport([response(total=2)]))
        with self.assertRaises(ApiError):
            fetch_detail(transport([response([], total=1, next_page=2)]))

    def test_total_cambia_excede_y_limites_no_solicitan_otra_pagina(self):
        with self.assertRaisesRegex(ApiError, "cambió"):
            fetch_detail(transport([response(total=2, next_page=2), response([], total=3)]))
        with self.assertRaisesRegex(ApiError, "más registros"):
            fetch_detail(transport([response(total=0)]))
        with self.assertRaisesRegex(ApiError, "max_rows"):
            fetch_detail(transport([response(total=101)]))
        calls = []
        with self.assertRaisesRegex(ApiError, "max_pages"):
            fetch_detail(transport([response(total=2, next_page=2)], calls), max_pages=1)
        self.assertEqual(len(calls), 1)

    def test_503_y_timeout_recuperan_sin_duplicar_paginas(self):
        waits, calls = [], []
        simulated = simulation_transport(SAMPLES / "recuperable.json")

        def fetch(page, timeout):
            calls.append((page, timeout))
            return simulated(page, timeout)

        actual = fetch_detail(fetch, timeout=4, retry_delay=0.5, wait=waits.append)
        assert_frame_equal(actual, read_detail(SOURCE), check_exact=True)
        self.assertEqual([page for page, _ in calls], [1, 1, 2, 2, 3])
        self.assertTrue(all(timeout == 4 for _, timeout in calls))
        self.assertEqual(waits, [0.5, 0.5])

    def test_agotamiento_y_errores_no_reintentables(self):
        for failure in [TimeoutError(), URLError(TimeoutError()), response(status=503)]:
            waits, calls = [], []
            with self.subTest(failure=type(failure).__name__), self.assertRaises(ApiError):
                fetch_detail(transport([failure, failure], calls), wait=waits.append)
            self.assertEqual(len(calls), 2)
            self.assertEqual(len(waits), 1)
        for failure in [response(status=400), response(status=401), response(status=404),
                        response(status=429), response(status=500), response(status=204),
                        {**response(status=503), "retry_after": "60"}, URLError("DNS")]:
            waits, calls = [], []
            with self.subTest(failure=failure), self.assertRaises(ApiError):
                fetch_detail(transport([failure], calls), wait=waits.append)
            self.assertEqual(len(calls), 1)
            self.assertEqual(waits, [])

    def test_error_tardio_no_retorna_tabla_parcial(self):
        with self.assertRaisesRegex(ApiError, "HTTP 401 en página 2"):
            fetch_detail(simulation_transport(SAMPLES / "error_tardio.json"))

    def test_parametros_invalidos_antes_del_transporte(self):
        calls = []
        for kwargs in [{"timeout": 0}, {"timeout": float("nan")}, {"timeout": True},
                       {"max_attempts": 0}, {"max_attempts": 6}, {"max_pages": False},
                       {"max_rows": -1}, {"retry_delay": 6}, {"retry_delay": -1}, {"wait": 1}]:
            with self.subTest(kwargs=kwargs), self.assertRaises(ApiError):
                fetch_detail(transport([], calls), **kwargs)
        self.assertEqual(calls, [])


class PruebasHTTP(unittest.TestCase):
    def test_request_timeout_y_cierre_sin_red(self):
        body = io.BytesIO(b'{"items":[],"total":0,"next_page":null}')
        body.status = 200
        body.headers = Message()
        body.headers['Content-Type'] = 'application/json'
        with patch('analisis_cartera.api.urlopen', return_value=body) as open_mock:
            fetch = http_transport('https://ejemplo.invalid/cortes')
            self.assertEqual(open_mock.call_count, 0)
            result = fetch(2, 3)
        request = open_mock.call_args.args[0]
        self.assertEqual(request.full_url, 'https://ejemplo.invalid/cortes?page=2')
        self.assertEqual(request.get_method(), 'GET')
        self.assertEqual(request.get_header('Accept'), 'application/json')
        self.assertEqual(open_mock.call_args.kwargs, {'timeout': 3})
        self.assertEqual(result['status'], 200)
        self.assertTrue(body.closed)

    def test_httperror_se_lee_y_se_cierra(self):
        body = io.BytesIO(b'{}')
        headers = Message()
        headers['Content-Type'] = 'application/json'
        headers['Retry-After'] = '60'
        error = HTTPError('https://ejemplo.invalid/cortes', 503, 'No disponible', headers, body)
        with patch('analisis_cartera.api.urlopen', side_effect=error):
            result = http_transport('https://ejemplo.invalid/cortes')(1, 2)
        self.assertEqual(result['status'], 503)
        self.assertEqual(result['retry_after'], '60')
        self.assertTrue(body.closed)

    def test_limite_bytes_utf8_y_falla_de_lectura_cierran(self):
        for raw, max_bytes in [(b'1234', 3), (b'\xff', 10)]:
            body = io.BytesIO(raw)
            with self.subTest(raw=raw), patch('analisis_cartera.api.urlopen', return_value=body):
                with self.assertRaises(ApiError):
                    http_transport('https://ejemplo.invalid/cortes', max_bytes=max_bytes)(1, 2)
            self.assertTrue(body.closed)
        class Broken(io.BytesIO):
            def read(self, n):
                raise TimeoutError('Cuerpo interrumpido')
        body = Broken()
        with patch('analisis_cartera.api.urlopen', return_value=body), self.assertRaises(TimeoutError):
            http_transport('https://ejemplo.invalid/cortes')(1, 2)
        self.assertTrue(body.closed)

    def test_endpoint_y_parametros_invalidos_no_conectan(self):
        with patch('analisis_cartera.api.urlopen') as open_mock:
            for endpoint in ['http://ejemplo.invalid', 'https://u:p@ejemplo.invalid',
                             'https://ejemplo.invalid/?a=1', 'https://ejemplo.invalid/#a']:
                with self.subTest(endpoint=endpoint), self.assertRaises(ApiError):
                    http_transport(endpoint)
            with self.assertRaises(ApiError):
                http_transport('https://ejemplo.invalid', max_bytes=0)
            with self.assertRaises(ApiError):
                http_transport('https://ejemplo.invalid')(True, 1)
            open_mock.assert_not_called()
