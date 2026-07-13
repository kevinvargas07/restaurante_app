# servicios/restaurante.py

from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:
    """Clase de servicio para administrar productos y clientes del restaurante."""

    def __init__(self, nombre):
<<<<<<< HEAD
        self.nombre = nombre.strip()
        self.productos = []
        self.clientes = []

    def registrar_producto(self, nombre, categoria, precio, disponible=True):
        """Crea y registra un producto en la lista del restaurante."""
        producto = Producto(nombre, categoria, precio, disponible)
=======
        self.nombre = nombre
        self.productos = []   
        self.clientes = []    
    
    def agregar_producto(self, producto):
        """Agrega un producto a la lista."""
>>>>>>> cbe94b31aabb4e20d1cd7a70facd0810c7e6d0c1
        self.productos.append(producto)
        print(f"Producto registrado: {producto.nombre}")
        return producto

    def listar_productos(self):
        """Muestra todos los productos registrados."""
        if not self.productos:
            print("No hay productos registrados.")
            return []

        print("\n--- LISTA DE PRODUCTOS ---")
        for producto in self.productos:
            print(producto.mostrar_informacion())
        return self.productos

    def buscar_producto(self, termino):
        """Busca productos por nombre o categoría."""
        termino = termino.strip().lower()
        if not termino:
            return []

        resultados = []
        for producto in self.productos:
            if termino in producto.nombre.lower() or termino in producto.categoria.lower():
                resultados.append(producto)

        if not resultados:
            print("No se encontraron productos con ese criterio.")
            return []

        print("\n--- RESULTADOS DE BÚSQUEDA DE PRODUCTOS ---")
        for producto in resultados:
            print(producto.mostrar_informacion())
        return resultados

    def registrar_cliente(self, nombre, correo, id_cliente):
        """Crea y registra un cliente en la lista del restaurante."""
        cliente = Cliente(nombre=nombre, correo=correo, id_cliente=id_cliente)
        self.clientes.append(cliente)
        print(f"Cliente registrado: {cliente.nombre}")
        return cliente

    def listar_clientes(self):
        """Muestra todos los clientes registrados."""
        if not self.clientes:
            print("No hay clientes registrados.")
<<<<<<< HEAD
            return []

        print("\n--- LISTA DE CLIENTES ---")
        for cliente in self.clientes:
            print(cliente)
        return self.clientes

    def buscar_cliente(self, termino):
        """Busca clientes por nombre, correo o identificador."""
        termino = termino.strip().lower()
        if not termino:
            return []

        resultados = []
        for cliente in self.clientes:
            if (
                termino in cliente.nombre.lower()
                or termino in cliente.correo.lower()
                or termino == str(cliente.id_cliente).lower()
            ):
                resultados.append(cliente)

        if not resultados:
            print("No se encontraron clientes con ese criterio.")
            return []

        print("\n--- RESULTADOS DE BÚSQUEDA DE CLIENTES ---")
        for cliente in resultados:
            print(cliente)
        return resultados
=======
        else:
            print("\n--- LISTA DE CLIENTES ---")
            for cli in self.clientes:
                print(cli)
            
>>>>>>> cbe94b31aabb4e20d1cd7a70facd0810c7e6d0c1
