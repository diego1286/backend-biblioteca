class Sede:
    def __init__(self, nombre: str, direccion: str) -> None:
        self._nombre = nombre
        self._direccion = direccion

    def obtener_nombre(self) -> str:
        return self._nombre
