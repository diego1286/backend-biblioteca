from Libro import Libro


class Biblioteca:
    def __init__(self):
        self.__libros = []

    def agregar_libro(self, libro: Libro) -> None:
        """
        este metodo agrega un objeto de la clase Libros en el atributo __libros de la biblioteca
        parametros: libro: Libro
        return: None
        """
        self.__libros.append(libro)

    def eliminar_libro_por_id(self, id_libro: int) -> None:
        """
        este metodo elimina un objeto Libro del atributo __libros de la biblioteca
        parametros: id_libro: int
        return: None
        """

        for libro in self.__libros:
            if id_libro == libro.get_id_libro():
                self.__libros.remove(libro)
                print("Libro eliminado con exito")
                return

        print("No se encontro el libro en la biblioteca")

    def listar_libros(self) -> None:
        """
        Lista todos los libros que estan en el atributo __libro de Biblioteca
        return: None
        """

        for libro in self.__libros:

            print(f"*{libro}*")

    def prestar_libro(self, id_libro: int) -> None:
        """
        Presta un libro
        parametro:
            id_libro: int
        return: None
        """
        for libro in self.__libros:
            if id_libro == libro.get_id_libro():
                if libro.get_is_prestado():
                    print("Este libro ya esta prestado!")
                    return

                else:
                    libro.prestar_libro()
                    return
        print("No se encontro el libro en la biblioteca")

    def devolver_libro(self, id_libro: int) -> None:
        """
        Devuelve un libro
        parametro:
            id_libro: int
        return: None
        """
        for libro in self.__libros:
            if id_libro == libro.get_id_libro():
                if not libro._Libro__isprestado:
                    print("Este libro no esta prestado!")
                    return

                else:
                    libro.devolver_libro()
                    return
        print("No se encontro el libro en la biblioteca")

    def consultar_libro(self, id_libro: int) -> None:
        """
        recibe el id del libro como entero e imprime el libro
        parametro:
            id_libro: int
        return: None
        """
        for libro in self.__libros:
            if id_libro == libro.get_id_libro():
                print(libro)
                return
        print("No se encontro el libro en la biblioteca")
