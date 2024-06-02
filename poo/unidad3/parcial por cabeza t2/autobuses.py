from vehiculos import Vehiculos

class Autobuses(Vehiculos):
    __servicio:str
    __turno: str
    
    def __init__ (self, marca, modelo, anoFabri, capPas, plazas, distancia, tarifa, servicio, turno):
        super().__init__(marca, modelo, anoFabri, capPas, plazas, distancia, tarifa)
        self.__servicio = servicio
        self.__turno = turno
        
    def getServicio(self):
        return self.__servicio
    
    def getTurno(self):
        return self.__turno
    
    def mostrarA(self):
        print(f"{self.__servicio} {self.__turno} {self.getMarca()} {self.getModelo()} {self.getAnoFabri()} {self.getCapPas()} {self.getPlazas()} {self.getDistancia()} {self.getTarifa()}")