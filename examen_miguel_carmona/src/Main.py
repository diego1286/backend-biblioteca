from Biblioteca import Biblioteca
from Entidades.Libro import Libro
from Entidades.Usuario import Usuario


def main() -> None:
    biblioteca = Biblioteca()

    while True:
        print("===== MENU BIBLIOTECA =====")
        print("1. Registrar usuario")
        print("2. Agregar libro")
        print("3. Mostrar libros")
        print("4. Prestar libro")
        print("5. Devolver libro")
        print("6. Salir ")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            nombre = input("Nombre del usuario: ")
            cedula = input("Cedula: ")
            usuario = Usuario(nombre, cedula)
            biblioteca.registrar_usuario(usuario)
            print("Usuario registrado\n")

        elif opcion == "2":
            titulo = input("Titulo del libro: ")
            autor = input("Autor del libro: ")
            libro = Libro(titulo, autor)
            biblioteca.agregar_libro(libro)
            print("Libro agregado\n")

        elif opcion == "3":
            biblioteca.mostrar_libros()
            print()

        elif opcion == "4":
            titulo = input("Titulo del libro a prestar: ")
            biblioteca.prestar_libro(titulo)
            print()

        elif opcion == "5":
            titulo = input("Titulo del libro a devolver: ")
            biblioteca.devolver_libro(titulo)
            print()

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opcion invalida\n")


if __name__ == "__main__":
    main()
