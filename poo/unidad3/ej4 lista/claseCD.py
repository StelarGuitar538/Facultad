class Cd:
    __repmin: int
    __narrador: int

    def __init__(self, rm, n, t, c, p):
        super().__init__(t, c, p)
        self.__repmin = rm
        self.__narrador = n

             
    def mostrarCD (self):
        print(f"{self.__minRep} {self.__narrador} {self.getTitulo()} {self.getCat()} {self.getPrecio()}")
        
    def calcularImporte(self):
        impVentacd = self.getPrecio() * 1.10
        return impVentacd