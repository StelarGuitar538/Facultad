class Movimientos:
    __numtar: str
    __fecha: str
    __desc: str
    __tmov: str
    __imp:float
    
    def __init__ (self, numtar, fecha, desc, tmov, imp):
        self.__numtar = numtar
        self.__fecha = fecha
        self.__desc = desc
        self.__tmov = tmov
        self.__imp = imp
        
    def __str__ (self):
        return f"{self.__fecha}-{self.__desc}-{self.__imp}-{self.__tmov}"
    
    def getNumTar1(self):
        return self.__numtar
    
    def getFecha(self):
        return self.__fecha
    
    def getDesc(self): 
        return self.__desc
    
    def getMov(self):
        return self.__tmov
    
    def getImp(self):
        return self.__imp