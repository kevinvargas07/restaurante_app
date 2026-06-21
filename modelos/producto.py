# modelos/producto.py

class Producto:
    """Clase que representa un producto del restaurante."""
    
    def __init__(self, nombre, precio, categoria="Sin categoría"):
        # Completa con los atributos que consideres necesarios
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        # Puedes agregar más, como disponibilidad, código, etc.
    
    def __str__(self):
        # Devuelve una cadena amigable para mostrar el producto
        return f"{self.nombre} - ${self.precio:.2f} ({self.categoria})"
    
    # Puedes agregar otros métodos, como aplicar descuento, cambiar disponibilidad, etc.