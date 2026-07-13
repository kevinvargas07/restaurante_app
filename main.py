# main.py

from servicios.restaurante import Restaurante


def mostrar_menu():
    """Muestra el menú principal del sistema."""
    print("\n========================================")
    print("        SISTEMA DE RESTAURANTE")
    print("========================================")
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("----------------------------------------")
    print("4. Registrar cliente")
    print("5. Listar clientes")
    print("6. Buscar cliente")
    print("----------------------------------------")
    print("7. Salir")


def main():
<<<<<<< HEAD
    """Función principal del programa."""
    restaurante = Restaurante("Mi Rincón Sabroso")

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            nombre = input("Ingrese el nombre del producto: ").strip()
            categoria = input("Ingrese la categoría del producto: ").strip()
            precio = input("Ingrese el precio del producto: ").strip()
            disponible = input("¿El producto está disponible? (s/n): ").strip().lower()

            try:
                restaurante.registrar_producto(
                    nombre=nombre,
                    categoria=categoria,
                    precio=precio,
                    disponible=(disponible == "s")
                )
            except ValueError as error:
                print(f"Error: {error}")

        elif opcion == "2":
            restaurante.listar_productos()

        elif opcion == "3":
            termino = input("Ingrese el nombre o categoría a buscar: ").strip()
            restaurante.buscar_producto(termino)

        elif opcion == "4":
            nombre = input("Ingrese el nombre del cliente: ").strip()
            correo = input("Ingrese el correo del cliente: ").strip()
            id_cliente = input("Ingrese el ID del cliente: ").strip()

            try:
                restaurante.registrar_cliente(nombre=nombre, correo=correo, id_cliente=int(id_cliente))
            except ValueError:
                print("Error: el ID del cliente debe ser un número entero.")

        elif opcion == "5":
            restaurante.listar_clientes()

        elif opcion == "6":
            termino = input("Ingrese nombre, correo o ID a buscar: ").strip()
            restaurante.buscar_cliente(termino)

        elif opcion == "7":
            print("Gracias por usar el sistema de restaurante.")
            break

        else:
            print("Opción no válida. Intente nuevamente.")
=======
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
>>>>>>> cbe94b31aabb4e20d1cd7a70facd0810c7e6d0c1


if __name__ == "__main__":
    main()
