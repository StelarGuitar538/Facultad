class Visualizaciones:
    __idM: int
    __idP: str
    __fecha: str
    __hora: str
    __minutos: int
    
    def __init__ (self, idm, idp, fecha, hora, min):
        self.__idM = idm
        self.__idP = idp
        self.__fecha = fecha
        self.__hora = hora
        self.__minutos = min
        
    def __str__(self):
        return f"{self.__idM} {self.__idP} {self.__fecha} {self.__hora} {self.__minutos}"
    
    def _eq_ (self, other):
        return (self.__idM, self.__fecha, self.__hora == other.__idM, other.__fecha, other.__hora)
    
    def getIdm(self): 
        return self.__idM
    
    def getIdp(self):
        return self.__idP
    
    def getFecha(self):
        return self.__fecha
    
    def getHora(self):
        return self.__hora
    
    def getMin(self):
        return self.__minutos
    
    