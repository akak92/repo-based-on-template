"""
Archivo: 4_functions.py
Guía de estilo: Funciones en Python

Reglas:
- Usar `snake_case` para nombres de funciones.
- Incluir `docstring` que explique claramente qué hace la función.
- Especificar tipos en los argumentos y el valor de retorno.
- Las funciones no deben exceder las 25 líneas.
- Evitar `print()`, usar `logging`.
- Manejar excepciones adecuadamente.
- Usar `snake_case` para nombrar variables.
- Tipar las variables siempre que sea posible.
- Usar nombres descriptivos y evitar abreviaturas innecesarias.
- 
"""

import logging

# Configuración básica de logging
logging.basicConfig(level=logging.INFO)

def calculate_discount(price: float, percentage: float) -> float:
    """
    Calcula el precio final aplicando un porcentaje de descuento.

    Args:
        price (float): Precio original.
        percentage (float): Porcentaje de descuento (0-100).

    Returns:
        float: Precio con descuento aplicado.

    Raises:
        ValueError: Si el porcentaje está fuera del rango permitido.
    """
    if not 0 <= percentage <= 100:
        raise ValueError("El porcentaje debe estar entre 0 y 100")

    discount: float = price * (percentage / 100)
    final_price: float = price - discount
    logging.info(f"Descuento aplicado: {discount:.2f}")
    return final_price


def get_user_input(prompt: str) -> str:
    """
    Simula la obtención de entrada del usuario.
    En una app real, esta función debería validar correctamente la entrada.
    """
    try:
        user_input: str = input(prompt)
        return user_input.strip()
    except Exception as e:
        logging.error("Error al obtener entrada del usuario", exc_info=e)
        raise

# ❌ Ejemplos incorrectos:
# def Descuento(p, perc):        ← Nombre en PascalCase y argumentos sin tipar
# def f(): return 1              ← Sin docstring ni claridad
# def very_long_function(...):   ← Evitar funciones extensas, dividir en tareas pequeñas