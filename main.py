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


if __name__ == "__main__":
    main()