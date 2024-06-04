from abc import ABC, abstractmethod 
class Vehiculos(ABC):
    __marca: str
    __modelo: str
    __anoFabri: int
    __capPas: int
    __plazas: int
    __distancia: int
    __tarifa: float
    
    def __init__ (self, marca, modelo, anoFabri, capPas, plazas, distancia, tarifa):
        self.__marca = marca
        self.__modelo = modelo
        self.__anoFabri = anoFabri
        self.__capPas = capPas
        self.__plazas = plazas
        self. __distancia = distancia
        self.__tarifa = tarifa
        
    def getMarca(self):
        return self.__marca
    
    def getModelo(self):
        return self.__modelo
    
    def getAnoFabri(self):
        return self.__anoFabri
    
    def getCapPas(self):
        return self.__capPas
    
    def getPlazas(self):
        return self.__plazas
    
    def getDistancia(self):
        return self.__distancia
    
    def getTarifa(self):
        return self.__tarifa
    
    def mostrar(self):
        print(f"{self.__marca} {self.__modelo} {self.__anoFabri} {self.__capPas} {self.__plazas} {self.__distancia} {self.__tarifa}")
        
    @abstractmethod
    def tarifa(self):
        pass