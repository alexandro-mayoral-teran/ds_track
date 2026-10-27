"""Fronteras del adaptador y conservación de copias; no necesita Quarto ni pandas."""
from pathlib import Path
import hashlib
import json
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "herramientas"))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from preparar_portal import adaptar
from preparar_practica import REPO, catalogo, preparar
from servir import fuentes_cambiaron


class AdaptadorTest(unittest.TestCase):
    def test_detecta_copia_anterior_o_fuentes_cambiadas_sin_escribir(self):
        salida = REPO / 'output'
        salida.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=salida) as tmp:
            sitio = Path(tmp)
            self.assertTrue(fuentes_cambiaron(sitio))
            archivo = sitio / 'procedencia.json'
            fuente = 'portal/curso.json'
            huella = hashlib.sha256((REPO/fuente).read_bytes()).hexdigest()
            archivo.write_text(json.dumps({'sha256_fuentes': {fuente: huella}}), encoding='utf-8')
            antes = archivo.read_bytes()
            self.assertFalse(fuentes_cambiaron(sitio))
            self.assertEqual(antes, archivo.read_bytes())
            archivo.write_text(json.dumps({'sha256_fuentes': {fuente: '0'*64}}), encoding='utf-8')
            self.assertTrue(fuentes_cambiaron(sitio))
            archivo.write_text('[]', encoding='utf-8')
            self.assertTrue(fuentes_cambiaron(sitio))

    def test_indice_numerado_y_anclas_explicitas(self):
        origen = REPO / 'curriculum/00_getting_started/01_github_profile/README.md'
        texto = '[Ir](#1-mi-tema)\n## 1. Mi tema\n[Otro](#2-especial)\n## Otro {#2-especial}\n'
        res = adaptar(texto, origen, {})
        self.assertIn('[Ir](#mi-tema)', res)
        self.assertIn('[Otro](#2-especial)', res)

    def test_enlace_a_directorio_usa_su_indice(self):
        origen = REPO / 'curriculum/00_getting_started/README.md'
        destino = origen.parent / '01_github_profile/README.md'
        self.assertEqual(adaptar('[Primera](01_github_profile/)', origen,
                                 {destino.resolve(): '00-01-leccion.qmd'}),
                         '[Primera](00-01-leccion.qmd)\n')

    def test_enlaces_fragmentos_externos_y_codigo(self):
        origen = REPO / "curriculum/02_pandas/01_series_dataframe/README.md"
        destino = (origen.parent / "series_dataframe.py").resolve()
        texto = ('[Archivo](series_dataframe.py#ejemplo) y [Web](https://pandas.pydata.org/).\n'
                 '```python\n"[No adaptar](inexistente.md)"\n```\n'
                 '[En esta página](#conceptos)\n')
        adaptado = adaptar(texto, origen, {destino: "descargas/ejemplo.py"})
        self.assertIn('[Archivo](descargas/ejemplo.py#ejemplo)', adaptado)
        self.assertIn('[Web](https://pandas.pydata.org/)', adaptado)
        self.assertIn('"[No adaptar](inexistente.md)"', adaptado)
        self.assertIn('[En esta página](#conceptos)', adaptado)

    def test_no_incluye_fuentes_por_recorrido_accidental(self):
        with self.assertRaisesRegex(ValueError, "no enumerado"):
            adaptar('[Privado](../../../AGENTS.md)',
                    REPO / 'curriculum/02_pandas/01_series_dataframe/README.md', {})

    def test_consulta_fuera_del_piloto_conserva_destino_explicativo(self):
        origen = REPO / "curriculum/02_pandas/01_series_dataframe/README.md"
        externo = (origen.parent / "../02_read_inspect_export/README.md").resolve()
        self.assertEqual(adaptar('[Siguiente](../02_read_inspect_export/README.md#tipos)',
                                origen, {externo: 'fuentes.qmd#fuente-7'}),
                         '[Siguiente](fuentes.qmd#fuente-7)\n')

    def test_preparar_conserva_originales_y_destinos_ocupados(self):
        datos = catalogo()
        originales = {n: (REPO / p).read_bytes() for n, p in datos['practica'].items()}
        salida = REPO / 'output'
        salida.mkdir(exist_ok=True)
        self.assertTrue(salida.resolve().is_relative_to(REPO))
        with tempfile.TemporaryDirectory(dir=salida) as tmp:
            destino = Path(tmp) / 'personal'
            preparar(destino)
            self.assertEqual({p.name for p in destino.iterdir()}, set(originales))
            for nombre, contenido in originales.items():
                self.assertEqual((destino/nombre).read_bytes(), contenido)
            notebook = destino / 'practica.ipynb'
            notebook.write_text('Mi avance personal', encoding='utf-8')
            with self.assertRaises(FileExistsError):
                preparar(destino)
            self.assertEqual(notebook.read_text(encoding='utf-8'), 'Mi avance personal')
        for nombre, ruta in datos['practica'].items():
            self.assertEqual((REPO/ruta).read_bytes(), originales[nombre])


if __name__ == '__main__':
    unittest.main()
