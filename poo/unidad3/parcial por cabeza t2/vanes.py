from vehiculos import Vehiculos

class Vanes(Vehiculos):
    __tCarroceria: str
    
    def __init__(self, marca, modelo, anoFabri, capPas, plazas, distancia, tarifa, t):
        super().__init__(marca, modelo, anoFabri, capPas, plazas, distancia, tarifa)
        self.__tCarroceria = t
        
    def getT(self):
        return self.__tCarroceria
    
    def mostrarV(self):
         print(f"{self.__tCarroceria} {self.getMarca()} {self.getModelo()} {self.getAnoFabri()} {self.getCapPas()} {self.getPlazas()} {self.getDistancia()} {self.getTarifa()}")
         
    def tarifa(self):
        if self.getT() == "minivan":
            tarifa = self.getTarifa() *0.9
        else:
            tarifa = self.getTarifa() *1.025
        return tarifa