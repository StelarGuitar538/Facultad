class Libro:
    __autor: str
    __fecha: int
    __paginas: int

    def __init__(self, a, f, pa, t, c, p):
        super().__init__(t, c, p)
        self.__autor = a
        self.__fecha = f
        self.__paginas = pa

    def mostrar(self):
        print(f"{self.getTitulo()} {self.getCat()} {self.getPrecio()} {self.__autor} {self.__fecha} {self.__paginas}")

    