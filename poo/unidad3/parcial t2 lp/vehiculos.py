from abc import ABC, abstractmethod

class Vehiculos:
    __marca: str
    __modelo: str
    __anoFabricacion: int
    __capacidadPasajeros: int
    __numeroPlazas: int
    __distancia: float
    __tarifa: float
    
    def __init__(self, marca, modelo, anoFabricacion, capacidadPasajeros, numeroPlazas, distancia, tarifa):
        self.__marca = marca
        self.__modelo = modelo
        self.__anoFabricacion = anoFabricacion
        self.__capacidadPasajeros = capacidadPasajeros
        self.__numeroPlazas = numeroPlazas
        self.__distancia = distancia
        self.__tarifa = tarifa

    def getMarca(self):
        return self.__marca

    def getModelo(self):
        return self.__modelo

    def getAnoFabricacion(self):
        return self.__anoFabricacion

    def getCapacidadPasajeros(self):
        return self.__capacidadPasajeros

    def getNumeroPlazas(self):
        return self.__numeroPlazas

    def getDistancia(self):
        return self.__distancia

    def getTarifa(self):
        return self.__tarifa
    
    def __str__(self):
        return f"{self.__marca} {self.__modelo} {self.__anoFabricacion} {self.__capacidadPasajeros} {self.__numeroPlazas} {self.__distancia} {self.__tarifa}"
        
@abstractmethod
def getImporteTarifa(self):
        pass