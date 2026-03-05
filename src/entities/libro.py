"""
Módulo que define la clase Libro para el sistema de biblioteca.
"""

from typing import List


class Libro:
    """
    Representa un libro dentro del sistema de biblioteca.
    """

    def __init__(self, titulo: str, autor: str, isbn: str) -> None:
        """
        Inicializa un nuevo libro.
        """
        self._titulo = titulo
        self._autor = autor
        self._isbn = isbn
        self._disponible = True

    # =========================
    # PROPIEDADES (READ)
    # =========================

    @property
    def titulo(self) -> str:
        return self._titulo

    @property
    def autor(self) -> str:
        return self._autor

    @property
    def isbn(self) -> str:
        return self._isbn

    @property
    def disponible(self) -> bool:
        return self._disponible

    # =========================
    # UPDATE
    # =========================

    def actualizar_datos_libro(
        self, titulo: str | None = None, autor: str | None = None
    ) -> None:
        """
        Actualiza los datos del libro.
        """
        if titulo is not None and titulo.strip() != "":
            self._titulo = titulo

        if autor is not None and autor.strip() != "":
            self._autor = autor

    # =========================
    # OPERACIONES DE NEGOCIO
    # =========================

    def prestar_libro(self) -> None:
        """
        Marca el libro como prestado si está disponible.
        """
        if not self._disponible:
            print("El libro no está disponible para préstamo.")
            return

        self._disponible = False
        print(f"El libro '{self._titulo}' ha sido prestado.")

    def devolver_libro(self) -> None:
        """
        Marca el libro como disponible nuevamente.
        """
        if self._disponible:
            print("El libro ya estaba disponible.")
            return

        self._disponible = True
        print(f"El libro '{self._titulo}' ha sido devuelto.")

    # =========================
    # MÉTODOS DE CONSULTA
    # =========================

    @staticmethod
    def buscar_libro_x_autor(libros: List["Libro"], autor: str) -> List["Libro"]:
        """
        Busca libros por nombre de autor.
        """
        return [libro for libro in libros if libro.autor.lower() == autor.lower()]

    @staticmethod
    def buscar_libro_x_isbn(libros: List["Libro"], isbn: str) -> "Libro | None":
        """
        Busca un libro por ISBN.
        """
        for libro in libros:
            if libro.isbn == isbn:
                return libro
        return None

    # =========================
    # UTILIDADES
    # =========================

    def to_dict(self) -> dict:
        """
        Retorna una representación del libro en formato diccionario.
        """
        return {
            "titulo": self._titulo,
            "autor": self._autor,
            "isbn": self._isbn,
            "disponible": self._disponible,
        }

    def __str__(self) -> str:
        estado = "Disponible" if self._disponible else "Prestado"
        return (
            f"Título: {self._titulo} | "
            f"Autor: {self._autor} | "
            f"ISBN: {self._isbn} | "
            f"Estado: {estado}"
        )

    def __repr__(self) -> str:
        return (
            f"Libro(titulo='{self._titulo}', "
            f"autor='{self._autor}', "
            f"isbn='{self._isbn}')"
        )
