class Alquiler:
    __nombre: str
    __id: str
    __horaAlquilada: str
    __minutosAlquilados: str
    __duracion: int
    
    def __init__(self, n, id, ha, ma, d):
        self.__nombre = n
        self.__id = id
        self.__horaAlquilada = ha
        self.__minutosAlquilados = ma
        self.__duracion = d
        
    def __str__(self):
        return f"{self.__nombre} {self.__id} {self.__horaAlquilada} {self.__minutosAlquilados} {self.__duracion}"
    
    def __gt__ (self, other):
        return (self.__horaAlquilada, self.__minutosAlquilados > other.__horaAlquilada, other.__minutosAlquilados)
    
    def getHora(self):
        return self.__horaAlquilada
    
    def getId(self):
        return self.__id
    
    def getDuracion(self):
        return self.__duracion
    
    def getMin(self):
        return self.__minutosAlquilados
    
    