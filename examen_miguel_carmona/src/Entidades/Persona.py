class Persona:
    def __init__(self, nombre:str, cedula:str) -> None:
        self.nombre= nombre
        self.cedula = cedula

    def mostrar_nombre(self) -> str:

        return self._nombre
    