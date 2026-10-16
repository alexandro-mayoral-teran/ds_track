"""Escrituras pequeñas: éxito, fallas previstas y conservación del anterior."""

from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from analisis_cartera.recursos import read_json, write_json_atomic


class PruebasJSON(unittest.TestCase):
    def test_reemplazo_completo(self):
        with TemporaryDirectory() as folder:
            path = Path(folder) / "registro.json"
            path.write_text('{"anterior": true}', encoding="utf-8")
            write_json_atomic(path, {"estado": "válido", "cantidad": 0})
            self.assertEqual(read_json(path), {"estado": "válido", "cantidad": 0})
            self.assertEqual(list(Path(folder).iterdir()), [path])

    def test_falla_antes_de_replace_conserva_bytes_y_causa(self):
        with TemporaryDirectory() as folder:
            path = Path(folder) / "registro.json"
            previous = b'{"anterior": true}\n'
            path.write_bytes(previous)
            with self.assertRaises(OSError) as caught:
                write_json_atomic(path, {"nuevo": 1}, simulate_failure=True)
            self.assertIsInstance(caught.exception.__cause__, OSError)
            self.assertEqual(path.read_bytes(), previous)
            self.assertEqual(list(Path(folder).iterdir()), [path])

    def test_serializacion_invalida_no_trunca(self):
        for payload, error in [({"valor": object()}, TypeError),
                               ({"valor": float("nan")}, ValueError)]:
            with self.subTest(error=error.__name__), TemporaryDirectory() as folder:
                path = Path(folder) / "registro.json"
                path.write_bytes(b'{"anterior": true}')
                with self.assertRaises(error):
                    write_json_atomic(path, payload)
                self.assertEqual(path.read_bytes(), b'{"anterior": true}')
                self.assertEqual(list(Path(folder).iterdir()), [path])
