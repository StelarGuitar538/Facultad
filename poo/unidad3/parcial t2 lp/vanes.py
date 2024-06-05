from vehiculos import Vehiculos

class Vanes(Vehiculos):
    __tipoCarroceria: str
    
    def __init__(self, marca, modelo, anoFabricacion, capacidadPasajeros, numeroPlazas, distancia, tarifa, tipoCarroceria):
        super().__init__(marca, modelo, anoFabricacion, capacidadPasajeros, numeroPlazas, distancia, tarifa)
        self.__tipoCarroceria = tipoCarroceria
        
    def getTipoCarroceria(self):
        return self.__tipoCarroceria
    
    def __str__(self):
        return f"{self.getMarca()} {self.getModelo()} {self.getAnoFabricacion()} {self.getCapacidadPasajeros()} {self.getNumeroPlazas()} {self.getDistancia()} {self.getTarifa()} {self.__tipoCarroceria}"
    
    def getImporteTarifa(self):
        if self.__tipoCarroceria == "minivan":
            tarifa = self.getTarifa() * 0.9
        else:
            tarifa = self.getTarifa() * 1.25
        
        return tarifa
        