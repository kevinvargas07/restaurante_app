# modelos/producto.py

class Producto:
    """Representa un producto del restaurante."""

    def __init__(self, nombre, categoria, precio, disponible=True):
        self._nombre = None
        self._categoria = None
        self._precio = None
        self._disponible = None

        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.disponible = disponible

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor or not valor.strip():
            raise ValueError("El nombre del producto no puede estar vacío.")
        self._nombre = valor.strip()

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, valor):
        if not valor or not valor.strip():
            raise ValueError("La categoría del producto no puede estar vacía.")
        self._categoria = valor.strip()

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        try:
            precio = float(valor)
        except (TypeError, ValueError):
            raise ValueError("El precio del producto debe ser un número válido.")

        if precio <= 0:
            raise ValueError("El precio del producto debe ser mayor que cero.")

        self._precio = precio

    @property
    def disponible(self):
        return self._disponible

    @disponible.setter
    def disponible(self, valor):
        if not isinstance(valor, bool):
            raise ValueError("El atributo disponible debe ser un valor booleano.")
        self._disponible = valor

    def mostrar_informacion(self):
        estado = "Disponible" if self.disponible else "No disponible"
        return f"Producto: {self.nombre} | Categoría: {self.categoria} | Precio: ${self.precio:.2f} | Estado: {estado}"
    def __str__(self):
        return self.mostrar_informacion()