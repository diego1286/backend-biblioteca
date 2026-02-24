"""
Archivo principal del sistema de biblioteca.
Contiene el menú interactivo del programa.
"""

from entities.libro import Libro


def mostrar_menu() -> None:
    """Muestra el menú principal."""
    print("\n📚 SISTEMA DE BIBLIOTECA")
    print("1. Agregar libro")
    print("2. Prestar libro")
    print("3. Devolver libro")
    print("4. Buscar libros por autor")
    print("5. Actualizar datos de un libro")
    print("6. Mostrar todos los libros")
    print("7. Salir")


def agregar_libro(libros: list[Libro]) -> None:
    """Agrega un libro a la lista."""
    titulo = input("Ingrese el título: ").strip()
    autor = input("Ingrese el autor: ").strip()
    isbn = input("Ingrese el ISBN: ").strip()

    if titulo == "" or autor == "" or isbn == "":
        print("Todos los campos son obligatorios.")
        return

    # Validar que no exista el mismo ISBN
    existente = Libro.buscar_por_isbn(libros, isbn)
    if existente is not None:
        print("Ya existe un libro con ese ISBN.")
        return

    libro = Libro(titulo, autor, isbn)
    libros.append(libro)
    print(" Libro agregado correctamente.")


def prestar_libro(libros: list[Libro]) -> None:
    """Presta un libro por ISBN."""
    isbn = input("Ingrese el ISBN del libro: ").strip()
    libro = Libro.buscar_por_isbn(libros, isbn)

    if libro is None:
        print("Libro no encontrado.")
        return

    libro.prestar()


def devolver_libro(libros: list[Libro]) -> None:
    """Devuelve un libro por ISBN."""
    isbn = input("Ingrese el ISBN del libro: ").strip()
    libro = Libro.buscar_por_isbn(libros, isbn)

    if libro is None:
        print("Libro no encontrado.")
        return

    libro.devolver()


def buscar_por_autor(libros: list[Libro]) -> None:
    """Busca libros por autor."""
    autor = input("Ingrese el nombre del autor: ").strip()

    if autor == "":
        print(" Debe ingresar un autor.")
        return

    resultados = Libro.buscar_por_autor(libros, autor)

    if not resultados:
        print("No se encontraron libros de ese autor.")
        return

    print("\nResultados encontrados:")
    for libro in resultados:
        print(libro)


def actualizar_libro(libros: list[Libro]) -> None:
    """Actualiza los datos de un libro."""
    isbn = input("Ingrese el ISBN del libro a actualizar: ").strip()
    libro = Libro.buscar_por_isbn(libros, isbn)

    if libro is None:
        print("Libro no encontrado.")
        return

    nuevo_titulo = input("Nuevo título (dejar vacío si no cambia): ")
    nuevo_autor = input("Nuevo autor (dejar vacío si no cambia): ")

    libro.actualizar_datos(nuevo_titulo, nuevo_autor)
    print(" Datos actualizados correctamente.")


def mostrar_libros(libros: list[Libro]) -> None:
    """Muestra todos los libros registrados."""
    if not libros:
        print(" No hay libros registrados.")
        return

    print("\n Lista de libros:")
    for libro in libros:
        print(libro)


def main() -> None:
    """Función principal del programa."""
    libros: list[Libro] = []
    ejecutando = True

    while ejecutando:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            agregar_libro(libros)

        elif opcion == "2":
            prestar_libro(libros)

        elif opcion == "3":
            devolver_libro(libros)

        elif opcion == "4":
            buscar_por_autor(libros)

        elif opcion == "5":
            actualizar_libro(libros)

        elif opcion == "6":
            mostrar_libros(libros)

        elif opcion == "7":
            ejecutando = False
            print("Saliendo del sistema...")

        else:
            print(" Opción inválida.")


if __name__ == "__main__":
    main()
