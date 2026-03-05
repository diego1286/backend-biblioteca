from Entidades.Persona import Persona


class Usuario(Persona):
    def __init__(self, nombre: str, cedula: str) -> None:
        super().__init__(nombre, cedula)
