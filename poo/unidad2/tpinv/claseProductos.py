#clase productos
class Productos:
    __productos: str
    __ventasDiarias: float
    
    def __init__ (self, prod, vd):
        self.__productos = prod
        self.__ventasDiarias = vd
        
    def getprod(self):
        return self.__productos
    
    def getventas(self):
        return self.__ventasDiarias