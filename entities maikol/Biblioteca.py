from Libro import Libro


class Biblioteca:
    """Gestiona una colección de libros."""

    def __init__(self) -> None:
        self.libros: list[Libro] = []

    def agregar_libro(self, libro: Libro) -> None:
        """Agrega un libro a la biblioteca."""
        self.libros.append(libro)
        print(f"Libro '{libro.titulo}' agregado.")

    def eliminar_libro(self, titulo: str) -> bool:
        """Elimina un libro por título."""
        libro = self.buscar_por_titulo(titulo)
        if libro:
            self.libros.remove(libro)
            print(f"Libro '{titulo}' eliminado.")
            return True
        print("Libro no encontrado.")
        return False

    def prestar_libro(self, titulo: str) -> bool:
        """Presta un libro si está disponible."""
        libro = self.buscar_por_titulo(titulo)
        if libro and libro.prestar():
            print(f"Libro '{titulo}' prestado.")
            return True
        print("No se pudo prestar el libro.")
        return False

    def recibir_libro(self, titulo: str) -> bool:
        """Recibe (devuelve) un libro."""
        libro = self.buscar_por_titulo(titulo)
        if libro:
            libro.devolver()
            print(f"Libro '{titulo}' recibido.")
            return True
        print("Libro no encontrado.")
        return False

    def buscar_por_titulo(self, titulo: str) -> Libro | None:
        """Busca un libro por su título."""
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                return libro
        return None

    def mostrar_libros(self) -> None:
        """Muestra todos los libros."""
        if not self.libros:
            print("No hay libros en la biblioteca.")
            return

        for libro in self.libros:
            print(libro)
