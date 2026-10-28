"""Valores iniciales y ruta propia; importar no lee el CSV."""

from pathlib import Path

RUTA_DATOS = Path(__file__).resolve().with_name("cartera.csv")
CORTES = ("2026-09-30", "2026-10-31")
CORTE_INICIAL = CORTES[-1]
MINIMO_INICIAL = 2000
