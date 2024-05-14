class movimiento:
    def __init__(self, numtar, fecha, descripcion, tipomov, importe):
        self.__numtar = int(numtar)
        self.__fecha = str(fecha)
        self.__descripcion = str(descripcion)
        self.__tipomov = str(tipomov)
        self.__importe = float(importe)

    def getnumtar(self):
        return(self.__numtar)
    
    def gettipomov(self):
        return(self.__tipomov)
    
    def getimporte(self):
        return(self.__importe)
    
    def getfecha(self):
        return(self.__fecha)
    
    def getdescripcion(self):
        return(self.__descripcion)