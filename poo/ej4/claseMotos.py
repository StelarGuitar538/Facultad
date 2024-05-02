import numpy as np
class Motos:
    __patente: int
    __marca: str
    __nombreYApellidoDelConductor: str
    __kilometraje: int
    
    def __init_ (self, patente, marca, nya, km):
        self.patente = patente
        self.marca = marca
        self.nya = nya
        self.km = km
  
    def __lt__ (self, other):
        return self.patente < other.patente
    
    def getPatente(self):
        return self.__patente  
    
    def mostrarMoto(self):
        print("patente {}, marca{}, nya{}, km{}", format(self.__patente, self.__marca, self.__nombreYApellidoDelConductor, self.__kilometraje))
        
    def getNya(self):
        return self.__nombreYApellidoDelConductor

    
        
            
    def obtenerDatos(self):
        nya = input("ingrese nya")
        if np.where(self.__nombreYApellidoDelConductor == nya):
            return nya
    