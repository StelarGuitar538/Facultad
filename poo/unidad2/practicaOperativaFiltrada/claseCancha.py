class Canchas:
    __id: str
    __tPiso: str
    __importe: float
    
    def __init__ (self, id, tp, imp):
        self.__id = id
        self.__tPiso = tp
        self.__importe = imp
        
    def __str__(self):
        return f"{self.__id} {self.__tPiso} {self.__importe}"
        
    def getId(self):
        return self.__id
    
    def getPiso(self):
        return self.__tPiso
    
    def getImporte(self):
        return self.__importe
    