"""
Archivo: 3_constants.py
Guía de estilo: Constantes en Python

Reglas:
- Usar `UPPER_CASE` con guiones bajos para nombres de constantes.
- Declarar las constantes al inicio del archivo o en un módulo separado (`constants.py`).
- No modificar el valor de una constante una vez definida.
- Las constantes deben tener nombres descriptivos.
"""

import logging

# Configuración básica de logging
logging.basicConfig(level=logging.INFO)

# Constantes globales
MAX_USERS: int = 100
DEFAULT_TIMEOUT_SECONDS: float = 5.0
API_BASE_URL: str = "https://api.example.com/v1"
STATUS_ACTIVE: str = "active"
STATUS_INACTIVE: str = "inactive"

# Uso dentro de funciones
def connect_to_api(timeout: float = DEFAULT_TIMEOUT_SECONDS) -> None:
    """
    Simula la conexión a una API externa con un tiempo de espera.
    """
    logging.info(f"Conectando a {API_BASE_URL} con timeout={timeout}s")

# ❌ Ejemplos incorrectos (solo como referencia):
# max_users = 100            ← minúsculas no es una constante
# ApiBaseUrl = "..."         ← PascalCase no corresponde
# TIMEOUT = 10; TIMEOUT = 15 ← Las constantes no deben redefinirse
