class Cabana:
    __numero: int
    __cantHab: int
    __cantCGrandes: int
    __cantCChicas: int
    __importe: float
    
    def __init__ (self, n, h, g, c, i):
        self.__numero = n
        self.__cantHab = h
        self.__cantCGrandes = g
        self.__cantCChicas = c
        self.__importe = i
        
    def __str__(self):
        return f"{self.__numero} {self.__cantHab} {self.__cantCGrandes} {self.__cantCChicas} {self.__importe}"
    
    def __ge__ (self, other):
        return (self.__numero >= other.__numero)
        
    def getNum(self):
        return self.__numero
    
    def getHab(self):
        return self.__cantHab
    
    def getGrandes(self):
        return self.__cantCGrandes
    
    def getChicas(self):
        return  self.__cantCChicas
        
    def getImp(self):
        return self.__importe
    
    
    