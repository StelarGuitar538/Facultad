from publi import Publi

class Cd(Publi):
    __repmin: int
    __narrador: str
    
    def __init__ (self, r, n, t, c, pre):
        super().__init__(t, c, pre)
        self.__repmin = r
        self.__narrador = n
        
    def mostrar(self):
        print(f"{self.__repmin} {self.__narrador} {self.getTitulo()} {self.getCat()} {self.getPrecio()}")
        
    def ImpVenta(self):
        return self.getPrecio() * 1.10