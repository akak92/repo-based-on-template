"""
Archivo: 8_solid_principles.py
Guía de estilo: Principios SOLID en Python

Reglas:
- Seguir los principios SOLID para un diseño de código limpio y mantenible.
"""

import logging
from abc import ABC, abstractmethod

logging.basicConfig(level=logging.INFO)

# 1. **Single Responsibility Principle (SRP)**: Una clase debe tener una única razón para cambiar.
class User:
    """
    Representa un usuario con información básica.
    Responsabilidad: Mantener los datos del usuario.
    """
    def __init__(self, name: str, email: str) -> None:
        self.name: str = name
        self.email: str = email


class UserRepository:
    """
    Responsabilidad: Persistir usuarios en una base de datos.
    """
    def save(self, user: User) -> None:
        # Simula la persistencia de un usuario
        logging.info(f"Usuario {user.name} guardado en la base de datos.")


# 2. **Open/Closed Principle (OCP)**: Las clases deben estar abiertas para extensión, pero cerradas para modificación.
class NotificationService(ABC):
    """
    Clase abstracta que define un servicio de notificación.
    """
    @abstractmethod
    def send(self, message: str) -> None:
        pass


class EmailNotificationService(NotificationService):
    """
    Notificación por correo electrónico.
    """
    def send(self, message: str) -> None:
        logging.info(f"Enviando correo con mensaje: {message}")


class SMSNotificationService(NotificationService):
    """
    Notificación por mensaje de texto.
    """
    def send(self, message: str) -> None:
        logging.info(f"Enviando SMS con mensaje: {message}")


# 3. **Liskov Substitution Principle (LSP)**: Las clases derivadas deben ser intercambiables por sus clases base.
def send_notification(service: NotificationService, message: str) -> None:
    """
    Enviar una notificación utilizando el servicio proporcionado.
    """
    service.send(message)


# 4. **Interface Segregation Principle (ISP)**: Los clientes no deben depender de interfaces que no usan.
class Printer(ABC):
    """
    Interfaz para impresoras.
    Define el método `print` que debe ser implementado por las clases de impresoras.
    """
    @abstractmethod
    def print(self, content: str) -> None:
        pass


class InkjetPrinter(Printer):
    """
    Impresora de inyección de tinta.
    Implementa el método `print` para imprimir usando tecnología de inyección de tinta.
    """
    def print(self, content: str) -> None:
        logging.info(f"Imprimiendo en inkjet: {content}")


class LaserPrinter(Printer):
    """
    Impresora láser.
    Implementa el método `print` para imprimir usando tecnología láser.
    """
    def print(self, content: str) -> None:
        logging.info(f"Imprimiendo en láser: {content}")


# 5. **Dependency Inversion Principle (DIP)**: Las dependencias deben ser abstraídas y no depender de clases concretas.
class NotificationSender:
    """
    Clase que depende de una abstracción para enviar notificaciones.
    """
    def __init__(self, service: NotificationService) -> None:
        self.service: NotificationService = service

    def notify(self, message: str) -> None:
        self.service.send(message)


if __name__ == "__main__":
    # Creación de objetos y pruebas
    user: User = User("Pedro", "pedro@example.com")
    user_repo: UserRepository = UserRepository()
    user_repo.save(user)

    email_service: NotificationService = EmailNotificationService()
    sms_service: NotificationService = SMSNotificationService()

    # Enviar notificaciones
    send_notification(email_service, "Bienvenido a nuestro servicio!")
    send_notification(sms_service, "Tu código de verificación es 1234")

    # Uso de Dependency Inversion Principle
    notification_sender: NotificationSender = NotificationSender(sms_service)
    notification_sender.notify("Recordatorio: Tu cita es mañana.")
