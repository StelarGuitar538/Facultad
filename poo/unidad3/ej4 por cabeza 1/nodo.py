from publi import Publi

class Nodo:
    __publi: Publi
    __sig : object
    
    def __init__(self, p):
        self.__publi = p
        self.__sig = None
        
    def getSig(self):
        return self.__sig
    
    def getDato(self):
        return self.__publi
    
    def setSig(self, sig):
        self.__sig = sig
        
        