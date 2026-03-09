class Libro:
    generador_id = 1

    def __init__(
        self, nombre: str, autor: str, paginas: int, editorial: str, anio: int
    ) -> None:

        self.__id_libro = Libro.generador_id
        Libro.generador_id += 1
        self.__nombre: str = nombre
        self.__autor: str = autor
        self.__paginas: int = paginas
        self.__editorial: str = editorial
        self.__anio: int = anio
        self.__isprestado: bool = False

    def __str__(self) -> str:
        """
        En esta funcion se emple el metodo str para facilitar la legibilidad
        de los datos de las instacias de la clase Libro
        :return: str
        """

        return f"ID: {self.__id_libro} | Libro: {self.__nombre} | Autor: {self.__autor} | Año: {self.__anio} | Prestado: {self.__isprestado}"

    def prestar_libro(self) -> None:
        self.__isprestado = True

    def devolver_libro(self) -> None:
        self.__isprestado = False

    def get_id_libro(self) -> int:
        return self.__id_libro

    def get_is_prestado(self) -> bool:
        return self.__isprestado
