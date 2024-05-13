class Equipo:
    __identificadorDelEquipo: str
    __nombreDelEquipo: str
    __golesAFavor: int
    __golesEnContra: int
    __diferenciaDeGoles: int
    __puntos: int
    
    def __init__ (self, identificadorDelEquipo, nombreDelEquipo,golesAFavor, GolesEnContra, DiferenciaDeGoles, puntos):
        self.__identificadorDelEquipo = identificadorDelEquipo
        self.__nombreDelEquipo = nombreDelEquipo
        self.__golesAFavor = golesAFavor
        self.__golesEnContra = GolesEnContra
        self.__diferenciaDeGoles = DiferenciaDeGoles
        self.__puntos = puntos
        
    def __str__ (self):
        return f"{self.__identificadorDelEquipo}-{self.__nombreDelEquipo}-{self.__golesAFavor}-{self.__golesEnContra}-{self.__diferenciaDeGoles}-{self.__puntos}"
    
    def getid(self):
        return(self.__identificadorDelEquipo)
    
    def getNomEq(self):
        return(self.__nombreDelEquipo)
    
    def getgolesAFavor(self):
        return(self.__golesAFavor)
    
    def getgolesEnContra(self):
        return(self.__golesEnContra)
    
    def getdifGoles(self):
        return(self.__diferenciaDeGoles)
    
    def getpuntos(self):
        return(self.__puntos)