class Moto:
    __patente:str
    __marca:str
    __nya:str
    __km:float
    
    def __init__(self, patente,marca,nya,km):
        self.__patente=patente
        self.__marca=marca
        self.__nya=nya
        self.__km=km
        
    def getPatente(self):
        return self.__patente

    def mostrarMoto(self):
        print('Patente {} Marca {} Nombre y Apellido del Conductor {} Kilometraje {}'.format(self.__patente,self.__marca,self.__nya,self.__km))
    def getNya(self):
        return self.__nya