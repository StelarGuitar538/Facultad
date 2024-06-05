from vehiculos import Vehiculos

class Autobuses(Vehiculos):
    __tipoServicio: str
    __turno: str
    
    def __init__(self, marca, modelo, anoFabricacion, capacidadPasajeros, numeroPlazas, distancia, tarifa, tipoServicio, turno):
        super().__init__(marca, modelo, anoFabricacion, capacidadPasajeros, numeroPlazas, distancia, tarifa)
        self.__tipoServicio = tipoServicio
        self.__turno = turno
        
    def getTipoServicio(self):
        return self.__tipoServicio
        
    def getTurno(self):
        return self.__turno
    
    def __str__(self):
        return f"{self.getMarca()} {self.getModelo()} {self.getAnoFabricacion()} {self.getCapacidadPasajeros()} {self.getNumeroPlazas()} {self.getDistancia()} {self.getTarifa()} {self.__tipoServicio} {self.__turno}"
    
    def getImporteTarifa(self):
        if self.__tipoServicio == "turismo" and self.__turno == "nocturno":
            tarifa = self.getTarifa() * 1.2
        else:
            tarifa = self.getTarifa() *  1.25
            
        return tarifa