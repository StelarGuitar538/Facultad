class Reserva:
    __numReserva: int
    __cliente: str
    __cabana: int
    __fecha: str
    __cantHuespedes: int
    __cantDias: int
    __importe: float
    
    def __init__ (self, res, cl, ca, f, h, d, imp):
        self.__numReserva = res
        self.__cliente = cl
        self.__cabana = ca
        self.__fecha = f
        self.__cantHuespedes = h
        self.__cantDias = d
        self.__importe = imp
        
    def __str__(self):
        return f"{self.__numReserva} {self.__cliente} {self.__cabana} {self.__fecha} {self.__cantHuespedes} {self.__cantDias} {self.__importe}"
        
    def getReserva(self):
        return self.__numReserva
    
    def getCliente(self):
        return self.__cliente
    
    def getCabana(self):
        return self.__cabana
    
    def getFecha(self):
        return self.__fecha
    
    def getHuespedes(self):
        return self.__cantHuespedes
    
    def getDias(self):
        return self.__cantDias
    
    def getImp(self):
        return self.__importe
        
        