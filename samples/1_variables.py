"""
Archivo: 1_variables.py
Guía de estilo: Variables en Python

Reglas:
- Usar `snake_case` para nombrar variables.
- Tipar las variables siempre que sea posible.
- Usar nombres descriptivos y evitar abreviaturas innecesarias.
"""

# Ejemplos correctos de declaración de variables

user_name: str = "Pedro Díaz"
age: int = 32
is_active: bool = True
height_meters: float = 1.80
scores: list[int] = [90, 85, 78]
user_profile: dict[str, str] = {"role": "admin", "status": "active"}

# Variables temporales en funciones deben seguir la misma convención
def calculate_bmi(weight_kg: float, height_m: float) -> float:
    bmi: float = weight_kg / (height_m ** 2)
    return bmi

# ❌ Ejemplos incorrectos (solo como referencia):
# UserName = "Pedro"         ← PascalCase no corresponde
# a = 32                     ← Nombre poco descriptivo
# HEIGHT = 1.80              ← UPPER_CASE se reserva para constantes
# scoresList = [100, 90]     ← camelCase no corresponde