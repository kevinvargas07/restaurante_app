# modelos/cliente.py

class Cliente:
    
    def __init__(self, nombre, telefono, correo=None):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
    
    def __str__(self):
        return f"Cliente: {self.nombre} | Tel: {self.telefono}"
    
