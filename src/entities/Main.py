from Libro import Libro
from Biblioteca import Biblioteca


def main() -> None:
    """
    Metodo principal, desde aca se gestiona toda la biblioteca
    """
    biblioteca = Biblioteca()
    while True:
        print("*************************************************************")
        print(
            """                    1. Guardar libro
                    2. Eliminar libro
                    3. imprimir todos los libros
                    4. prestar libro
                    5. devolover libro
                    6. consultar libro
                    0. Finalizar"""
        )
        try:
            opcion = int(input("Elija una opcion: "))
        except ValueError:
            print("Elije una de las 7 opciones disponibles")

        if opcion == 1:
            try:
                nombre = input("Ingrese nombre: ")
                autor = input("Ingrese autor: ")
                paginas = int(input("Ingrese paginas: "))
                editorial = input("Ingrese editorial: ")
                anio = int(input("Ingrese año: "))

            except ValueError:
                print("Las paginas y el año deben ser un numero entero")

            else:
                libro_nuevo = Libro(
                    nombre=nombre,
                    autor=autor,
                    paginas=paginas,
                    editorial=editorial,
                    anio=anio,
                )
                biblioteca.agregar_libro(libro=libro_nuevo)

        elif opcion == 2:
            try:
                id_libro = int(input("Igrese Id del libro: "))
            except ValueError:
                print("El id debe ser numerico")

            else:
                biblioteca.eliminar_libro_por_id(id_libro=id_libro)

        elif opcion == 3:
            print("****************Lista de Libros*******************")
            biblioteca.listar_libros()

        elif opcion == 4:
            try:
                id_libro = int(input("Igrese Id del libro: "))
            except ValueError:
                print("El id debe ser numerico")

            else:
                biblioteca.prestar_libro(id_libro=id_libro)

        elif opcion == 5:
            try:
                id_libro = int(input("Igrese Id del libro: "))
            except ValueError:
                print("El id debe ser numerico")

            else:
                biblioteca.devolver_libro(id_libro=id_libro)

        elif opcion == 6:
            try:
                id_libro = int(input("Igrese Id del libro: "))
            except ValueError:
                print("El id debe ser numerico")

            else:
                biblioteca.consultar_libro(id_libro=id_libro)

        elif opcion == 0:
            break

        else:
            print("Opcion no disponible")


main()
