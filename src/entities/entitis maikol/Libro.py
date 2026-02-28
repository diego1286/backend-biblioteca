class Libro:
    """Representa un libro dentro de una biblioteca."""

    def __init__(self, titulo: str, autor: str, anio: int) -> None:
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.disponible = True

    def prestar(self) -> bool:
        """Marca el libro como prestado si está disponible."""
        if self.disponible:
            self.disponible = False
            return True
        return False

    def devolver(self) -> None:
        """Marca el libro como disponible."""
        self.disponible = True

    def __str__(self) -> str:
        estado = "Disponible" if self.disponible else "Prestado"
        return f"{self.titulo} - {self.autor} ({self.anio}) [{estado}]"
