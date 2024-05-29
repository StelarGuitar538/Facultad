from clasePublicaciones import Publi
class CD(Publi):
    __minRep: int
    __narrador: str
        
    def __init__ (self,m, n, t, c, pre):
        super().__init__(t, c, pre)
        self.__minRep = m
        self.__narrador =n
            
    def mostrarCD (self):
        print(f"{self.__minRep} {self.__narrador} {self.getTitulo()} {self.getCat()} {self.getPrecio()}")
        
    def calcularImporte(self):
        impVentacd = self.getPrecio() * 1.10
        return impVentacd
    