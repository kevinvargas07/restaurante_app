# modelos/cliente.py

from dataclasses import dataclass


@dataclass
class Cliente:
<<<<<<< HEAD
    """Representa a un cliente del restaurante."""

    nombre: str
    correo: str
    id_cliente: int

    def __str__(self):
        return f"Cliente: {self.nombre} | Correo: {self.correo} | ID: {self.id_cliente}"
    
=======
    
    def __init__(self, nombre, telefono, correo=None):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
    
    def __str__(self):
        return f"Cliente: {self.nombre} | Tel: {self.telefono}"
    
>>>>>>> cbe94b31aabb4e20d1cd7a70facd0810c7e6d0c1
