class Equipo:
    __identificadorDelEquipo: str
    __nombreDelEquipo: str
    __golesAFavor: int
    __GolesEnContra: int
    __DiferenciaDeGoles: int
    __puntos: int
    
    def __init__ (self, identificadorDelEquipo, nombreDelEquipo,golesAFavor, GolesEnContra, DiferenciaDeGoles, puntos):
        self.__identificadorDelEquipo = identificadorDelEquipo
        self.__nombreDelEquipo = nombreDelEquipo
        self.__golesAFavor = golesAFavor
        self.__GolesEnContra = GolesEnContra
        self.__DiferenciaDeGoles = DiferenciaDeGoles
        self.__puntos = puntos
        
        
