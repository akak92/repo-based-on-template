"""
Script para sumar dos números siguiendo los estándares definidos
en guidelines.prompt.md.
"""

import logging

logging.basicConfig(level=logging.INFO)


def suma(a: float, b: float) -> float:
    """
    Suma dos números y devuelve el resultado.

    Args:
        a (float): Primer número.
        b (float): Segundo número.

    Returns:
        float: Resultado de la suma.

    Raises:
        ValueError: Si alguno de los argumentos no es un número.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Ambos argumentos deben ser números (int o float)")

    result: float = a + b
    logging.info(f"Suma realizada: {a} + {b} = {result}")
    return result


if __name__ == "__main__":
    # Ejemplo de uso
    try:
        numero1: float = 5
        numero2: float = 3
        resultado: float = suma(numero1, numero2)
        logging.info(f"Resultado final: {resultado}")
    except ValueError as e:
        logging.error(f"Error: {e}")
