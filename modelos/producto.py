# modelos/producto.py

class Producto:
    
    def __init__(self, nombre, precio, categoria="Sin categoría"):
        # Completa con los atributos que consideres necesarios
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
    
    def __str__(self):
        # Devuelve una cadena amigable para mostrar el producto
        return f"{self.nombre} - ${self.precio:.2f} ({self.categoria})"
    
