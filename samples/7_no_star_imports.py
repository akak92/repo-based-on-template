"""
Archivo: 7_no_star_imports.py
Guía de estilo: Evitar `from module import *`

Reglas:
- No usar `from module import *` ya que:
  - Contamina el espacio de nombres.
  - Hace difícil rastrear de dónde provienen funciones o clases.
  - Aumenta el riesgo de colisiones de nombres.
- Usar imports explícitos o alias cuando sea necesario.
- Importar solo lo que se necesita.
"""

import logging
from math import sqrt, pi

logging.basicConfig(level=logging.INFO)

def calculate_circle_area(radius: float) -> float:
    """
    Calcula el área de un círculo dado su radio.

    Args:
        radius (float): Radio del círculo.

    Returns:
        float: Área del círculo.
    """
    if radius < 0:
        raise ValueError("El radio no puede ser negativo")
    return pi * (radius ** 2)

def calculate_diagonal(a: float, b: float) -> float:
    """
    Calcula la diagonal de un rectángulo usando el teorema de Pitágoras.

    Args:
        a (float): Longitud del lado a.
        b (float): Longitud del lado b.

    Returns:
        float: Longitud de la diagonal.
    """
    return sqrt(a ** 2 + b ** 2)

if __name__ == "__main__":
    area: float = calculate_circle_area(5)
    diagonal: float = calculate_diagonal(3, 4)
    logging.info(f"Área: {area:.2f}")
    logging.info(f"Diagonal: {diagonal:.2f}")
