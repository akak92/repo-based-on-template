"""
Archivo: 6_no_duplicate_code.py
Guía de estilo: Evitar código duplicado

Reglas:
- Extraer código repetido en funciones reutilizables.
- Aplicar el principio DRY (Don't Repeat Yourself).
- Usar estructuras de datos adecuadas en lugar de múltiples condiciones similares.
- Modularizar responsabilidades en componentes pequeños.
"""

import logging

logging.basicConfig(level=logging.INFO)

def format_user_info(name: str, age: int) -> str:
    """
    Formatea la información del usuario para mostrarla o almacenarla.

    Args:
        name (str): Nombre del usuario.
        age (int): Edad del usuario.

    Returns:
        str: Cadena formateada.
    """
    return f"Usuario: {name.title()}, Edad: {age} años"


def print_user_info(users: list[dict[str, str | int]]) -> None:
    """
    Imprime la información de varios usuarios usando una función reutilizable.

    Args:
        users (list): Lista de diccionarios con claves 'name' y 'age'.
    """
    for user in users:
        try:
            info: str = format_user_info(user["name"], user["age"])
            logging.info(info)
        except KeyError as e:
            logging.warning(f"Usuario con datos incompletos: {e}")


# ❌ Ejemplo duplicado (NO hacer):
# def show_user_juan(): print(f"Usuario: Juan, Edad: 30 años")
# def show_user_lucia(): print(f"Usuario: Lucia, Edad: 25 años")

# ✅ En su lugar, usar:
users = [
    {"name": "juan", "age": 30},
    {"name": "lucia", "age": 25},
]

print_user_info(users)