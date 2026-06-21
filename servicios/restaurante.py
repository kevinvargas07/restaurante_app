# servicios/restaurante.py

# Importamos las clases de modelos
from modelos.producto import Producto
from modelos.cliente import Cliente

class Restaurante:
    """Clase principal que administra el restaurante."""
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []   # Lista para almacenar objetos Producto
        self.clientes = []    # Lista para almacenar objetos Cliente
    
    def agregar_producto(self, producto):
        """Agrega un producto a la lista."""
        self.productos.append(producto)
        print(f"Producto '{producto.nombre}' agregado.")
    
    def agregar_cliente(self, cliente):
        """Agrega un cliente a la lista."""
        self.clientes.append(cliente)
        print(f"Cliente '{cliente.nombre}' registrado.")
    
    def mostrar_productos(self):
        """Muestra todos los productos registrados."""
        if not self.productos:
            print("No hay productos registrados.")
        else:
            print("\n--- LISTA DE PRODUCTOS ---")
            for prod in self.productos:
                print(prod)   # Aquí se usa __str__ de Producto
    
    def mostrar_clientes(self):
        """Muestra todos los clientes registrados."""
        if not self.clientes:
            print("No hay clientes registrados.")
        else:
            print("\n--- LISTA DE CLIENTES ---")
            for cli in self.clientes:
                print(cli)
    
    # Puedes agregar más métodos: buscar_producto, realizar_pedido, etc.