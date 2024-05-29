from clasePubli import Publi
class Libro(Publi):
    __autor: str
    __fecha: str
    __paginas: int

    def __init__(self, a, f, pa, t, c, p):
        super().__init__(t, c, p)
        self.__autor = a
        self.__fecha = f
        self.__paginas = pa
    
    def getFecha(self):
        return self.__fecha

    def __str__(self):
        return(f"{self.getTitulo()} {self.getCat()} {self.getPrecio()} {self.__autor} {self.__fecha} {self.__paginas}")

    def calcularImporte(self):
        fecha_limpia = self.getFecha().strip(' "')
        diferencia = 2024 - int(fecha_limpia)
        impVenta = (diferencia / 100) * self.getPrecio()
        return impVenta