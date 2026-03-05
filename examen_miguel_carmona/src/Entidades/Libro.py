class Libro:
    def __init__(self, titulo: str, autor: str) -> None:
        self._titulo = titulo
        self._autor = autor
        self._disponible = True

    def prestar(self) -> None:
        self._disponible = False

    def devolver(self) -> None:
        self._disponible = True

    def esta_disponible(self) -> bool:
        return self._disponible

    def obtener_titulo(self) -> str:
        return self._titulo
