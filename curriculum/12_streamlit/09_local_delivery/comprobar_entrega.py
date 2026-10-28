"""Controles de autoría de 12.09 con Python estándar; no reemplazan el lab."""

import copy
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

import entrega
from preparar_practica import preparar


class EntregaTest(unittest.TestCase):
    def setUp(self):
        temporal = tempfile.TemporaryDirectory()
        self.addCleanup(temporal.cleanup)
        self.base = Path(temporal.name)
        self.practica = preparar(self.base / "practica")
        self.referencia = self.base / "referencia.csv"
        shutil.copyfile(self.practica / "cartera.csv", self.referencia)
        self.destino = self.base / "entrega"
        self.comando("crear", self.destino)

    def comando(self, *args, codigo=0, script=None, cwd=None):
        resultado = subprocess.run([sys.executable, str(script or self.practica / "entrega.py"), *map(str, args)],
                                   capture_output=True, text=True, timeout=30, cwd=cwd)
        self.assertEqual(resultado.returncode, codigo, resultado.stderr)
        return resultado

    def actualizar_huellas(self):
        valores = {n: sha256((self.destino / n).read_bytes()).hexdigest() for n in sorted(entrega.inventario())}
        entrega.escribir_json(self.destino / "manifiesto.json", {"version": 1, "sha256": valores})

    def huellas(self, carpeta):
        return {p.relative_to(carpeta).as_posix(): sha256(p.read_bytes()).hexdigest()
                for p in carpeta.rglob("*") if p.is_file() and "__pycache__" not in p.parts}

    def test_base_y_verificador_solo_lectura(self):
        antes = self.huellas(self.destino)
        self.assertEqual(entrega.verificar(self.destino, self.referencia), {"casos": 6, "filas_fuente": 6, "archivos": 36})
        self.assertEqual(self.huellas(self.destino), antes)
        octubre = entrega.leer_json(self.destino / "resultados/octubre/analisis.json")
        self.assertEqual(octubre["seleccion"], [
            {"id_credito": "003", "segmento": "comercio", "fecha_corte": "2026-10-31", "saldo_mxn": 2600},
        ])
        self.assertEqual(octubre["universo"], {"cantidad": 3, "saldo_mxn": 4600})
        self.assertEqual((self.destino / "resultados/vacio/seleccion.csv").read_bytes(),
                         b"id_credito,segmento,fecha_corte,saldo_mxn\n")
        self.assertEqual(list((self.destino / "resultados/sin_corte").iterdir()),
                         [self.destino / "resultados/sin_corte/analisis.json"])

    def test_reconstruye_sin_repo_ni_resultados_previos(self):
        nueva = self.base / "reconstruida"
        # Los JSON calculados no son entrada del constructor: perturbarlos no debe propagarse.
        (self.destino / "resultados/octubre/analisis.json").write_text("{}", encoding="utf-8")
        self.comando("crear", nueva, script=self.destino / "entrega.py", cwd=self.base)
        entrega.verificar(nueva, self.referencia)
        self.assertEqual(self.huellas(nueva), self.huellas(self.destino) | {
            "resultados/octubre/analisis.json": sha256((nueva / "resultados/octubre/analisis.json").read_bytes()).hexdigest(),
        })

    def test_destinos_ocupados_e_internos(self):
        antes = self.huellas(self.destino)
        self.comando("crear", self.destino, codigo=2)
        self.comando("crear", self.practica / "anidada", codigo=2)
        self.assertEqual(self.huellas(self.destino), antes)
        self.assertFalse((self.practica / "anidada").exists())
        with self.assertRaises(FileExistsError):
            preparar(self.practica)

    def test_referencia_externa_obligatoria_y_acciones_exclusivas(self):
        self.comando("verificar", self.destino, codigo=2)
        self.comando("verificar", self.destino, "--referencia", self.destino / "cartera.csv", codigo=2)
        self.comando("crear", self.base / "otra", "--referencia", self.referencia, codigo=2)
        self.assertFalse((self.base / "otra").exists())

    def test_fuente_compensada_con_huellas_actualizadas(self):
        p = self.destino / "cartera.csv"
        s = p.read_text(encoding="utf-8").replace("2026-09-30,2000", "2026-09-30,2500").replace("003,comercio,2026-09-30,2500", "003,comercio,2026-09-30,2000")
        p.write_text(s, encoding="utf-8")
        self.actualizar_huellas()
        with self.assertRaisesRegex(ValueError, "Fuente distinta"):
            entrega.verificar(self.destino, self.referencia)

    def test_analisis_compensado_con_huellas_actualizadas(self):
        p = self.destino / "resultados/septiembre/analisis.json"
        datos = entrega.leer_json(p)
        datos["seleccion"][0]["saldo_mxn"] = 2500
        datos["seleccion"][1]["saldo_mxn"] = 2000
        entrega.escribir_json(p, datos)
        self.actualizar_huellas()
        with self.assertRaisesRegex(ValueError, "Análisis distinto"):
            entrega.verificar(self.destino, self.referencia)

    def test_csv_compensado_con_contexto_y_huellas_actualizados(self):
        p = self.destino / "resultados/septiembre/seleccion.csv"
        s = p.read_text(encoding="utf-8").replace(",2000", ",2500").replace("003,comercio,2026-09-30,2500", "003,comercio,2026-09-30,2000")
        p.write_text(s, encoding="utf-8")
        contexto = p.with_name("contexto.json")
        datos = entrega.leer_json(contexto)
        datos["sha256_csv"] = sha256(p.read_bytes()).hexdigest()
        entrega.escribir_json(contexto, datos)
        self.actualizar_huellas()
        with self.assertRaisesRegex(ValueError, "CSV distinto"):
            entrega.verificar(self.destino, self.referencia)

    def test_tipos_contexto_y_filtros(self):
        p = self.destino / "resultados/octubre/contexto.json"
        original = entrega.leer_json(p)
        for campo, valor in [("cantidad", True), ("saldo_mxn", 2600.0), ("porcentaje_creditos", 100)]:
            with self.subTest(campo=campo):
                datos = copy.deepcopy(original)
                datos["indicadores"][campo] = valor
                entrega.escribir_json(p, datos)
                self.actualizar_huellas()
                with self.assertRaisesRegex(ValueError, "Contexto distinto"):
                    entrega.verificar(self.destino, self.referencia)
        entrega.escribir_json(p, original)
        contrato = self.destino / "contrato.json"
        datos = entrega.leer_json(contrato)
        datos["casos"]["octubre"]["minimo_mxn"] = 0
        entrega.escribir_json(contrato, datos)
        self.actualizar_huellas()
        with self.assertRaisesRegex(ValueError, "Contrato/casos"):
            entrega.verificar(self.destino, self.referencia)

    def test_fuentes_invalidas_y_vacias_antes_de_crear(self):
        p = self.practica / "cartera.csv"
        original = p.read_bytes()
        casos = [b"", original.splitlines()[0] + b"\n", original + original.splitlines()[1] + b"\n",
                 original.replace(b",2600", b",2600.5"), original.replace(b"2026-09-30", b"2026-02-30")]
        for i, contenido in enumerate(casos):
            with self.subTest(caso=i):
                p.write_bytes(contenido)
                destino = self.base / f"invalida-{i}"
                self.comando("crear", destino, codigo=2)
                self.assertFalse(destino.exists())

    def test_referencia_invalida_fuera_del_filtro(self):
        s = self.referencia.read_bytes()
        self.referencia.write_bytes(s + s.splitlines()[1] + b"\n")
        with self.assertRaisesRegex(ValueError, "clave repetida"):
            entrega.verificar(self.destino, self.referencia)

    def test_inventario_faltantes_extras_y_manifiesto(self):
        p = self.destino / "resultados/octubre/analisis.json"
        contenido = p.read_bytes()
        p.unlink()
        with self.assertRaisesRegex(ValueError, "Inventario"):
            entrega.verificar(self.destino, self.referencia)
        p.write_bytes(contenido)
        extra = self.destino / "secreto.txt"
        extra.write_text("extra sintético", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Inventario"):
            entrega.verificar(self.destino, self.referencia)
        extra.unlink()
        manifiesto = self.destino / "manifiesto.json"
        datos = entrega.leer_json(manifiesto)
        datos["sha256"]["../fuera.csv"] = "0" * 64
        entrega.escribir_json(manifiesto, datos)
        with self.assertRaisesRegex(ValueError, "inventario incorrecto"):
            entrega.verificar(self.destino, self.referencia)

    def test_orden_fuente_y_variante_reconstruible(self):
        fuente = self.practica / "cartera.csv"
        lineas = fuente.read_text(encoding="utf-8").splitlines()
        fuente.write_text("\n".join([lineas[0], *reversed(lineas[1:])]) + "\n", encoding="utf-8")
        invertida = self.base / "invertida"
        self.comando("crear", invertida)
        entrega.verificar(invertida, self.referencia)
        fuente.write_bytes(fuente.read_bytes().replace(b",2600", b",2800"))
        nueva_ref = self.base / "variante.csv"
        shutil.copyfile(fuente, nueva_ref)
        variante = self.base / "variante"
        self.comando("crear", variante)
        entrega.verificar(variante, nueva_ref)
        with self.assertRaisesRegex(ValueError, "Fuente distinta"):
            entrega.verificar(variante, self.referencia)
        r = entrega.leer_json(variante / "resultados/octubre/analisis.json")
        self.assertEqual(r["indicadores"]["saldo_mxn"], 2800)
        self.assertEqual(r["universo"]["saldo_mxn"], 4800)


if __name__ == "__main__":
    unittest.main(verbosity=2)
