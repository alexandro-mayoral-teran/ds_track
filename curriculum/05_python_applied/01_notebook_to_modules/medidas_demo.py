"""Primer módulo: una función reutilizable y una demostración al ejecutar."""

from statistics import median


def resumir_saldos(saldos):
    """Conservar cero; None representa ausencia en esta lista didáctica."""
    conocidos = [saldo for saldo in saldos if saldo is not None]
    n, k = len(saldos), len(conocidos)
    return {"registros": n, "conocidos": k,
            "mediana_mxn": median(conocidos) if k else None,
            "cobertura_pct": 100 * k / n if n else None}


def main():
    print(resumir_saldos([0, 100, None, 300]))


if __name__ == "__main__":
    main()
