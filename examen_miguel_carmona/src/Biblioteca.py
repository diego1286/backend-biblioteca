from Entidades.Libro import Libro
from Entidades.Usuario import Usuario


class Biblioteca:
    def __init__(self) -> None:
        self._libros = []
        self._usuarios = []

    def agregar_libro(self, libro: Libro) -> None:
        self._libros.append(libro)

    def registrar_usuario(self, usuario: Usuario) -> None:
        self._usuarios.append(usuario)

    def mostrar_libros(self) -> None:
        if len(self._libros) == 0:
            print("No hay libros registrados")
        else:
            for libro in self._libros:
                if libro.esta_disponible():
                    estado = "Disponible"
                else:
                    estado = "Prestado"

                print(libro.obtener_titulo() + " - " + estado)

    def prestar_libro(self, titulo: str) -> None:
        for libro in self._libros:
            if libro.obtener_titulo() == titulo:
                if libro.esta_disponible():
                    libro.prestar()
                    print("Libro prestado correctamente")
                else:
                    print("El libro ya esta prestado")
                return

        print("Libro no encontrado")
