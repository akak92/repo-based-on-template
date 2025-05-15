"""
Archivo: 2_classes.py
Guía de estilo: Clases en Python

Reglas:
- Usar `PascalCase` para nombrar clases.
- Tipar atributos y métodos.
- Incluir docstrings en clases y métodos.
- Usar `__init__` para inicializar atributos.
"""

from dataclasses import dataclass
from typing import Optional


class User:
    """
    Representa a un usuario del sistema.
    """

    def __init__(self, username: str, age: int, is_active: bool = True) -> None:
        self.username: str = username
        self.age: int = age
        self.is_active: bool = is_active

    def deactivate(self) -> None:
        """
        Desactiva al usuario.
        """
        self.is_active = False

    def __str__(self) -> str:
        return f"{self.username} ({'Activo' if self.is_active else 'Inactivo'})"


@dataclass
class Product:
    """
    Clase de ejemplo utilizando @dataclass.
    """
    name: str
    price: float
    stock: int = 0
    description: Optional[str] = None

    def is_available(self) -> bool:
        """
        Verifica si hay stock disponible.
        """
        return self.stock > 0


# ❌ Ejemplos incorrectos (solo como referencia):
# class user: ← debería ser PascalCase
# class Usuario(): pass ← falta docstring y atributos
# class ProductClass: nombre no representativo del dominio