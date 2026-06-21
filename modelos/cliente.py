# modelos/cliente.py

class Cliente:
    """Clase que representa a un cliente del restaurante."""
    
    def __init__(self, nombre, telefono, correo=None):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        # Podrías tener una lista de pedidos realizados, si quieres.
    
    def __str__(self):
        return f"Cliente: {self.nombre} | Tel: {self.telefono}"
    
    # Métodos adicionales: modificar datos, agregar pedido, etc.