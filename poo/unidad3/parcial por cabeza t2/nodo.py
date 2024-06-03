from vehiculos import Vehiculos

class Nodo:
    __vehiculos: Vehiculos
    __sig: object
    
    def __init__(self, v):
        self.__vehiculos =v
        self.__sig = None
        
    def getSig(self):
        return self.__sig
    
    def setSig(self, sig):
        self.__sig =sig
        
    def getDato(self):
        return self.__vehiculos
        