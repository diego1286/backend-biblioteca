from Biblioteca import Biblioteca
from Libro import Libro


def mostrar_menu() -> None:
    print("\n--- MENÚ BIBLIOTECA ---")
    print("1. Agregar libro")
    print("2. Eliminar libro")
    print("3. Prestar libro")
    print("4. Recibir libro")
    print("5. Mostrar libros")
    print("6. Salir")


def main() -> None:
    biblioteca = Biblioteca()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            anio = int(input("Año: "))
            libro = Libro(titulo, autor, anio)
            biblioteca.agregar_libro(libro)

        elif opcion == "2":
            titulo = input("Título del libro a eliminar: ")
            biblioteca.eliminar_libro(titulo)

        elif opcion == "3":
            titulo = input("Título del libro a prestar: ")
            biblioteca.prestar_libro(titulo)

        elif opcion == "4":
            titulo = input("Título del libro a recibir: ")
            biblioteca.recibir_libro(titulo)

        elif opcion == "5":
            biblioteca.mostrar_libros()

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()
