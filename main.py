# main.py

from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.cliente import Cliente

def main():
    # Crear el restaurante
    mi_restaurante = Restaurante("Mi Rincón Sabroso")
    
    # Crear productos (plato principal, entrada,  bebidas, postres, etc.)
    producto1 = Producto("Guiso de arroz", 15.50, "Plato Principal")
    producto2 = Producto("Refresco", 1.50, "Bebida")
    producto3 = Producto("Tarta de Queso", 4.00, "Postre")
    producto4 = Producto("Ceviche de camaron", 5.00, " entrada")
    producto5 = Producto("Encebollado de pescado", 6.50, "entrada")
    producto6 = Producto("Seco de pollo", 4.50, "Plato Principal")
    producto7 = Producto("Espumilla", 2.00, "Postre")
    producto8 = Producto("Helado de paila", 3.00, "Postre")
    producto9 = Producto("Colada morada", 1.50, "Bebida")

    # Crear clientes
    cliente1 = Cliente("Ana Gómez", "0912345678", "ana@gmail.com")
    cliente2 = Cliente("Luis Pérez", "0987654321", "luis@gmail.com")
    
    # Agregar productos y clientes al restaurante
    mi_restaurante.agregar_producto(producto1)
    mi_restaurante.agregar_producto(producto2)
    mi_restaurante.agregar_producto(producto3)
    mi_restaurante.agregar_producto(producto4)
    mi_restaurante.agregar_producto(producto5)
    mi_restaurante.agregar_producto(producto6)
    mi_restaurante.agregar_producto(producto7)
    mi_restaurante.agregar_producto(producto8)
    mi_restaurante.agregar_producto(producto9)
    mi_restaurante.agregar_cliente(cliente1)
    mi_restaurante.agregar_cliente(cliente2)
    
    # Mostrar información
    mi_restaurante.mostrar_productos()
    mi_restaurante.mostrar_clientes()


if __name__ == "__main__":
    main()
