"""Pruebas 14.05. Conserva fixtures nuevas; no modifica entradas ni entregas previas."""
from pathlib import Path
import csv
import sys
import tempfile
import unittest

sys.dont_write_bytecode = True
RAIZ = Path(__file__).resolve().parent
sys.path.insert(0, str(RAIZ))
import pipeline as producto
from modelo import cargar_fuente, resolver, leer


def escribir(ruta, columnas, filas):
    with ruta.open("x", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=columnas, quoting=csv.QUOTE_ALL)
        w.writeheader()
        w.writerows(filas)


def foto(carpeta):
    return {p.name: (p.read_bytes(), p.stat().st_mtime_ns) for p in carpeta.iterdir()}


class ContratoYEntrega(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        producto.verificar_entorno()
        (RAIZ / "ensayos").mkdir(exist_ok=True)
        cls.ensayo = Path(tempfile.mkdtemp(prefix="pruebas-", dir=RAIZ / "ensayos"))
        cls.nombre = cls.ensayo.name
        for base in ("config", "datos/entrada"):
            (RAIZ / base / cls.nombre).mkdir()
        cls.columnas, cls.original = leer(RAIZ / "datos/entrada/cartera.csv")
        cls.fuente_original = (RAIZ / "datos/entrada/cartera.csv").read_bytes()
        print("Fixtures conservadas:", cls.ensayo)

    @classmethod
    def tearDownClass(cls):
        if (RAIZ / "datos/entrada/cartera.csv").read_bytes() != cls.fuente_original:
            raise AssertionError("La fuente original cambio durante las pruebas")

    def configurar(self, nombre, cambios=None, filas=None):
        entrada = f"datos/entrada/{self.nombre}/{nombre}.csv"
        escribir(RAIZ / entrada, self.columnas, filas if filas is not None else self.original)
        _, filas_config = leer(RAIZ / "config/consulta.csv")
        cfg = {f["clave"]: f["valor"] for f in filas_config}
        cfg.update(entrada=entrada, salida="salidas/" + self.nombre + "_" + nombre)
        cfg.update(cambios or {})
        archivo = f"config/{self.nombre}/{nombre}.csv"
        escribir(RAIZ / archivo, ["clave", "valor"], [dict(clave=k, valor=v) for k, v in cfg.items()])
        return archivo, RAIZ / cfg["salida"]

    def test_01_nueve_criterios_literales(self):
        # Esperados del contrato, no calculados con la funcion que se prueba.
        datos = cargar_fuente(RAIZ / "datos/entrada/cartera.csv")
        _, casos = leer(RAIZ / "referencia/criterios.csv")
        self.assertEqual(len(casos), 9)
        for c in casos:
            with self.subTest(caso=c["caso"]):
                r = resolver(datos, c["corte"], c["segmentos"], c["minimo_texto"])
                for k, v in r.items():
                    if k == "porcentaje_creditos" and v:
                        self.assertAlmostEqual(float(v), float(c[k]), places=10)
                    else:
                        self.assertEqual(v, c[k], k)

    def test_02_catorce_fuentes_invalidas(self):
        _, casos = leer(RAIZ / "referencia/calidad.csv")
        self.assertEqual(len(casos), 14)
        for c in casos:
            with self.subTest(caso=c["caso"]):
                filas = [dict(f) for f in self.original]
                columnas = list(self.columnas)
                if c["accion"] == "valor": filas[0][c["campo"]] = c["valor"]
                elif c["accion"] == "duplicar": filas.append(dict(filas[0]))
                elif c["accion"] == "quitar_columna":
                    columnas.remove(c["campo"])
                    for f in filas: del f[c["campo"]]
                elif c["accion"] == "columna_extra":
                    columnas.append(c["campo"])
                    for f in filas: f[c["campo"]] = c["valor"]
                else: self.fail("Accion desconocida en calidad.csv")
                ruta = self.ensayo / (c["caso"] + ".csv")
                escribir(ruta, columnas, filas)
                with self.assertRaises(ValueError): cargar_fuente(ruta)

    def test_03_orden_independiente_y_cero_valido(self):
        datos = cargar_fuente(RAIZ / "datos/entrada/cartera.csv")
        self.assertEqual(resolver(list(reversed(datos)), "2026-09-30", "comercio", "0")["ids"], "001|003")
        self.assertEqual(resolver(datos, "2026-09-30", "comercio", "0")["saldos_mxn"], "0|2500")

    def test_04_integracion_y_repeticion(self):
        for nombre, corte, ids, saldo in [("oct", "2026-10-31", "003", "2600"), ("sep", "2026-09-30", "002|003", "4500")]:
            with self.subTest(corte=corte):
                archivo, destino = self.configurar(nombre, {"corte": corte})
                self.assertEqual(producto.pipeline(archivo), "creada")
                _, filas = leer(destino / "seleccion.csv")
                _, contexto = leer(destino / "contexto.csv")
                self.assertEqual("|".join(f["id_credito"] for f in filas), ids)
                self.assertEqual(contexto[0]["saldo_seleccion_mxn"], saldo)
                esperado = [("003", "2600")] if nombre == "oct" else [("002", "2000"), ("003", "2500")]
                self.assertEqual([(f["id_credito"], f["saldo_mxn"]) for f in filas], esperado)
                self.assertEqual(contexto[0]["creditos_universo"], "3")
                self.assertEqual(contexto[0]["saldo_universo_mxn"], "4600" if nombre == "oct" else "4500")
                self.assertEqual(contexto[0]["creditos_seleccion"], str(len(esperado)))
                self.assertAlmostEqual(float(contexto[0]["porcentaje_creditos"]), 100 / 3 if nombre == "oct" else 200 / 3, places=10)
                self.assertEqual(sum(int(f["saldo_mxn"]) for f in filas), int(saldo))
                antes = foto(destino)
                self.assertEqual(producto.pipeline(archivo), "reutilizada")
                self.assertEqual(foto(destino), antes)

    def test_05_vacio_y_sin_universo(self):
        archivo, destino = self.configurar("vacio", {"segmentos": "servicios", "minimo_texto": "1901"})
        producto.pipeline(archivo)
        columnas, filas = leer(destino / "seleccion.csv")
        self.assertEqual(columnas, self.columnas)
        self.assertEqual(filas, [])
        _, contexto = leer(destino / "contexto.csv")
        self.assertEqual([contexto[0][k] for k in ("estado", "creditos_universo", "porcentaje_creditos")], ["vacio", "3", "0"])
        archivo, destino = self.configurar("sinuniverso", {"corte": "2026-11-30"})
        with self.assertRaisesRegex(ValueError, "sin universo"): producto.pipeline(archivo)
        self.assertFalse(destino.exists())

    def test_06_duplicado_fuera_del_corte_bloquea(self):
        archivo, destino = self.configurar("duplicado", filas=self.original + [self.original[0]])
        with self.assertRaisesRegex(ValueError, "clave repetida"): producto.pipeline(archivo)
        self.assertFalse(destino.exists())

    def test_07_compensacion_no_engana(self):
        archivo, destino = self.configurar("alterado", {"corte": "2026-09-30"})
        producto.pipeline(archivo)
        columnas, filas = leer(destino / "seleccion.csv")
        filas[0]["saldo_mxn"], filas[1]["saldo_mxn"] = "1999", "2501"
        # Solo esta entrega de ensayo se altera deliberadamente.
        with (destino / "seleccion.csv").open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=columnas); w.writeheader(); w.writerows(filas)
        with (destino / "COMPLETO.csv").open("w", encoding="utf-8", newline="") as f:
            w = csv.writer(f); w.writerow(["archivo", "md5"])
            w.writerows((n, producto.md5(destino / n)) for n in ("seleccion.csv", "contexto.csv", "insumos.csv"))
        antes = foto(destino)
        with self.assertRaisesRegex(ValueError, "calculo actual"): producto.pipeline(archivo)
        self.assertEqual(foto(destino), antes)


if __name__ == "__main__":
    unittest.main(verbosity=2)
