class Patinador:
    __apellido : str
    __nombre : str
    __dni: str
    __edad: int
    __clubr: str
    
    def __init__(self, ap, nom, dni, edad, clubr):
        self.__apellido = ap
        self.__nombre = nom
        self.__dni = dni
        self.__edad = edad
        self.__clubr = clubr
        
    def getAp(self):
        return self.__apellido
    
    def getNom(self):
        return self.__nombre
    
    def getDni(self):
        return self.__dni
    
    def getEdad(self):
        return self.__edad
    
    def getClub(self):
        return self.__clubr
    
    
    