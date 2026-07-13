# modelos/cliente.py

from dataclasses import dataclass


@dataclass
class Cliente:
    """Representa a un cliente del restaurante."""

    nombre: str
    correo: str
    id_cliente: int

    def __str__(self):
        return f"Cliente: {self.nombre} | Correo: {self.correo} | ID: {self.id_cliente}"
    