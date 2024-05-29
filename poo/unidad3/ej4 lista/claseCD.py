from clasePubli import Publi
class Cd(Publi):
    __repmin: int
    __narrador: str

    def __init__(self, rm, n, t, c, p):
        super().__init__(t, c, p)
        self.__repmin = rm
        self.__narrador = n

             
    def __str__ (self):
        return(f" {self.__repmin} {self.__narrador} {self.getTitulo()} {self.getCat()} {self.getPrecio()}")
        
    def calcularImporte(self):
        return  self.getPrecio() * 1.10