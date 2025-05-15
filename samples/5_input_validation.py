"""
Archivo: 5_input_validation.py
Guía de estilo: Validación de inputs externos

Reglas:
- Validar siempre entradas que provienen del usuario o del exterior.
- Usar excepciones para manejar errores de validación.
- Utilizar funciones auxiliares para encapsular lógica de validación.
- Ser claro y específico en los mensajes de error.
"""

from typing import Any
import logging

# Configuración básica de logging
logging.basicConfig(level=logging.INFO)


def validate_age(age: Any) -> int:
    """
    Valida que la edad sea un entero válido y positivo.

    Args:
        age (Any): Entrada recibida, posiblemente desde una fuente externa.

    Returns:
        int: Edad validada.

    Raises:
        ValueError: Si el valor no es un entero positivo.
    """
    if not isinstance(age, int):
        raise ValueError("La edad debe ser un número entero")
    if age <= 0:
        raise ValueError("La edad debe ser mayor que cero")
    return age


def validate_email(email: str) -> str:
    """
    Valida el formato básico de un correo electrónico.

    Args:
        email (str): Correo electrónico a validar.

    Returns:
        str: Correo validado.

    Raises:
        ValueError: Si el formato del correo no es válido.
    """
    if "@" not in email or "." not in email.split("@")[-1]:
        raise ValueError("El correo electrónico no es válido")
    return email.strip()


def process_user_data(data: dict[str, Any]) -> None:
    """
    Procesa los datos del usuario después de validar cada campo.

    Args:
        data (dict): Diccionario con datos del usuario.
    """
    try:
        validated_age: int = validate_age(data.get("age"))
        validated_email: str = validate_email(data.get("email", ""))
        logging.info(f"Edad: {validated_age}, Email: {validated_email}")
    except ValueError as e:
        logging.error(f"Error de validación: {e}")

# ❌ Ejemplos incorrectos:
# age = input("Edad?")  ← sin validación ni tipado
# if not email: pass    ← validación insuficiente o silenciosa
