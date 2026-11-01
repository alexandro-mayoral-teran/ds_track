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
from preparar_portal import REPO
from servir import fuentes_cambiaron


class AdaptadorTest(unittest.TestCase):
    def test_catalogo_del_modulo_00_enumera_lecciones_y_recursos_actuales(self):
        curso = json.loads((REPO / "portal/curso.json").read_text(encoding="utf-8"))
        modulo = next(m for m in curso["modulos"] if m["id"] == "00")

        self.assertTrue(modulo["integrado"])
        self.assertEqual([leccion["id"] for leccion in curso["lecciones_00"]],
                         [f"00.0{i}" for i in range(1, 7)])
        for leccion in curso["lecciones_00"]:
            for clave in ["leccion", "lab"]:
                self.assertTrue((REPO / leccion[clave]).is_file(), leccion[clave])
        for pagina in curso["paginas_00"]:
            self.assertTrue((REPO / pagina["fuente"]).is_file(), pagina["fuente"])
        for ruta in curso["archivos_00"]:
            self.assertTrue((REPO / ruta).is_file(), ruta)
        self.assertIn(
            "curriculum/00_getting_started/02_terminal_paths/practica_terminal_colab.ipynb",
            curso["archivos_00"],
        )
        self.assertIn(
            "curriculum/00_getting_started/03_git_workflow/git-areas.svg",
            curso["archivos_00"],
        )
        self.assertIn(
            "curriculum/00_getting_started/03_git_workflow/git-areas.mmd",
            curso["archivos_00"],
        )

    def test_catalogo_del_modulo_01_enumera_lecciones_y_apoyos_existentes(self):
        curso = json.loads((REPO / "portal/curso.json").read_text(encoding="utf-8"))
        modulo = next(m for m in curso["modulos"] if m["id"] == "01")
        lecciones = curso["lecciones_01"]

        self.assertTrue(modulo["integrado"])
        self.assertEqual(len(lecciones), 6)
        self.assertEqual([leccion["id"] for leccion in lecciones],
                         [f"01.0{i}" for i in range(1, 7)])
        for leccion in lecciones:
            for clave in ["leccion", "lab"]:
                self.assertTrue((REPO / leccion[clave]).is_file(), leccion[clave])
        for ruta in curso["archivos_01"] + curso["consulta_01"]:
            self.assertTrue((REPO / ruta).is_file(), ruta)

    def test_catalogo_del_modulo_02_enumera_lecciones_y_apoyos_existentes(self):
        curso = json.loads((REPO / "portal/curso.json").read_text(encoding="utf-8"))
        modulo = next(m for m in curso["modulos"] if m["id"] == "02")
        lecciones = curso["lecciones_02"]

        self.assertTrue(modulo["integrado"])
        self.assertEqual([leccion["id"] for leccion in lecciones],
                         [f"02.{i:02d}" for i in range(1, 11)])
        for leccion in lecciones:
            for clave in ["leccion", "lab"]:
                self.assertTrue((REPO / leccion[clave]).is_file(), leccion[clave])
        for ruta in curso["archivos_02"]:
            self.assertTrue((REPO / ruta).is_file(), ruta)
            self.assertNotIn("/output/", ruta)
            self.assertNotIn("__pycache__", ruta)

    def test_catalogo_del_modulo_03_enumera_lecciones_y_apoyos_existentes(self):
        curso = json.loads((REPO / "portal/curso.json").read_text(encoding="utf-8"))
        modulo = next(m for m in curso["modulos"] if m["id"] == "03")
        lecciones = curso["lecciones_03"]

        self.assertTrue(modulo["integrado"])
        self.assertEqual([leccion["id"] for leccion in lecciones],
                         [f"03.{i:02d}" for i in range(1, 10)])
        for leccion in lecciones:
            for clave in ["leccion", "lab"]:
                self.assertTrue((REPO / leccion[clave]).is_file(), leccion[clave])
        for ruta in curso["archivos_03"]:
            self.assertTrue((REPO / ruta).is_file(), ruta)
            self.assertNotIn("/output/", ruta)
            self.assertFalse(ruta.endswith((".sqlite", ".db")), ruta)

    def test_catalogo_del_modulo_04_enumera_lecciones_y_apoyos_existentes(self):
        curso = json.loads((REPO / "portal/curso.json").read_text(encoding="utf-8"))
        modulo = next(m for m in curso["modulos"] if m["id"] == "04")
        lecciones = curso["lecciones_04"]

        self.assertTrue(modulo["integrado"])
        self.assertEqual([leccion["id"] for leccion in lecciones],
                         [f"04.{i:02d}" for i in range(1, 10)])
        for leccion in lecciones:
            for clave in ["leccion", "lab"]:
                self.assertTrue((REPO / leccion[clave]).is_file(), leccion[clave])
        for ruta in curso["archivos_04"]:
            self.assertTrue((REPO / ruta).is_file(), ruta)
            self.assertNotIn("/output/", ruta)

    def test_catalogo_del_modulo_05_enumera_lecciones_y_paquete_existentes(self):
        curso = json.loads((REPO / "portal/curso.json").read_text(encoding="utf-8"))
        modulo = next(m for m in curso["modulos"] if m["id"] == "05")
        lecciones = curso["lecciones_05"]

        self.assertTrue(modulo["integrado"])
        self.assertEqual([leccion["id"] for leccion in lecciones],
                         [f"05.{i:02d}" for i in range(1, 12)])
        for leccion in lecciones:
            for clave in ["leccion", "lab"]:
                self.assertTrue((REPO / leccion[clave]).is_file(), leccion[clave])
        for ruta in curso["archivos_05"]:
            self.assertTrue((REPO / ruta).is_file(), ruta)
            self.assertNotIn("/output/", ruta)
            self.assertNotIn("__pycache__", ruta)
        self.assertIn("curriculum/05_python_applied/01_notebook_to_modules/analisis_cartera/__init__.py",
                      curso["archivos_05"])

    def test_menu_lateral_deja_los_modulos_colapsados(self):
        config = (REPO / "portal/_quarto.yml").read_text(encoding="utf-8")
        self.assertIn("collapse-level: 1", config)

    def test_sesion_de_prueba_no_se_publica_y_consulta_es_relevante(self):
        curso = json.loads((REPO / "portal/curso.json").read_text(encoding="utf-8"))
        fuentes = set(curso["consulta_00"] + curso["consulta_01"])
        navegacion = (REPO / "portal/_quarto.yml").read_text(encoding="utf-8")
        portada = (REPO / "portal/paginas/index.qmd").read_text(encoding="utf-8")

        self.assertIn("docs/vscode-guide.md", fuentes)
        self.assertIn("templates/github-profile/README.md", fuentes)
        self.assertNotIn("curriculum/02_pandas/README.md", fuentes)
        self.assertNotIn("docs/architecture.md", fuentes)
        self.assertNotIn("curriculum/00_getting_started/README.md", fuentes)
        self.assertNotIn("curriculum/05_python_applied/README.md", fuentes)
        self.assertTrue((REPO / "curriculum/02_pandas/01_series_dataframe/README.md").is_file())
        self.assertTrue((REPO / "labs/02_pandas/01_series_dataframe/README.md").is_file())
        self.assertTrue((REPO / "labs/02_pandas/01_series_dataframe/practica.ipynb").is_file())
        self.assertNotIn("sesion.qmd", navegacion)
        self.assertNotIn("bitacora.qmd", navegacion)
        self.assertNotIn("sesion.qmd", portada)

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

    def test_fragmento_numerado_en_otro_archivo_se_adapta_a_quarto(self):
        origen = REPO / "curriculum/01_python_foundations/04_functions/README.md"
        destino = (origen.parent / "../02_lists_dicts/README.md").resolve()
        texto = "[Referencias](../02_lists_dicts/README.md#5-referencias-y-copias-qué-estás-modificando)"

        self.assertEqual(
            adaptar(texto, origen, {destino: "01-02-leccion.qmd"}),
            "[Referencias](01-02-leccion.qmd#referencias-y-copias-qué-estás-modificando)\n",
        )

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

    def test_consulta_de_otro_modulo_conserva_destino_explicativo(self):
        origen = REPO / "curriculum/02_pandas/01_series_dataframe/README.md"
        externo = (origen.parent / "../02_read_inspect_export/README.md").resolve()
        self.assertEqual(adaptar('[Siguiente](../02_read_inspect_export/README.md#tipos)',
                                origen, {externo: 'fuentes.qmd#fuente-7'}),
                         '[Siguiente](fuentes.qmd#fuente-7)\n')

    def test_ruta_de_python_aplicado_lleva_a_su_modulo_en_contenido(self):
        origen = REPO / "curriculum/01_python_foundations/README.md"
        arquitectura = (REPO / "docs/architecture.md").resolve()
        texto = "[ruta de Python aplicado](../../docs/architecture.md#python-aplicado-del-notebook-al-proyecto)"

        self.assertEqual(
            adaptar(texto, origen, {arquitectura: "contenido.qmd#modulo-05"}),
            "[ruta de Python aplicado](contenido.qmd#modulo-05)\n",
        )

    def test_siguiente_leccion_fuera_del_portal_lleva_a_su_modulo(self):
        origen = REPO / "curriculum/01_python_foundations/06_validation_summary/README.md"
        siguiente = (origen.parent / "../../02_pandas/01_series_dataframe/README.md").resolve()
        texto = "[Siguiente →](../../02_pandas/01_series_dataframe/README.md)"

        self.assertEqual(
            adaptar(texto, origen, {siguiente: "contenido.qmd#modulo-02"}),
            "[Siguiente →](contenido.qmd#modulo-02)\n",
        )

if __name__ == '__main__':
    unittest.main()
