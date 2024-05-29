from clasePublicaciones import Publi
class Libro(Publi):
    __autor: str
    __fecha: str
    __paginas: int
    
    def __init__ (self, a, f, p, t, c, pre):
        super().__init__(t, c, pre)
        self.__autor = a
        self.__fecha =f
        self.__paginas = p
        
    def getFecha(self):
        return self.__fecha
    
    def mostrarLi (self):
        print( f"{self.__autor} {self.__fecha} {self.__paginas} {self.getTitulo()} {self.getCat()} {self.getPrecio()}")
        
    def calcularImporte(self):
        diferencia = 2024 - int(self.getFecha())
        impVentali = (diferencia / 100) * self.getPrecio()
        return impVentali