from claseLadrillo import Ladrillo

class gesLadrillo:
    __lista: list
    
    def __init__(self):
        self.__lista: []
        
    def buscarId(self, id, gm):
        i=0
        b=False
        while not b and i< len(self.__lista):
            if self.__lista[i].getId() == id:
                costo = self.__lista[i].getCosto()
                car = self.__lista[i].getCar
        
        
        