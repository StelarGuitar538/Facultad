class Ladrillo:
    __alto: int
    __largo:int
    __ancho:int
    __cantidad:int
    __id: int
    __kgMatPrimUti: float
    __costo: float
    __Mrefractario: list
    
    def __init__(self, alto, largo, ancho, cant, id, kgmpu, costo, mref = None):
        self.__alto = alto
        self.__largo = largo
        self.__ancho = ancho
        self.__cantidad = cant
        self.__id = id
        self.__kgMatPrimUti = kgmpu
        self.__costo = costo
        if mref != None:
            self.addMRef(mref, 1)
     
    def addMRef(self, mref ,cantidad):
         for i in range(cantidad):
             self.__Mrefractario.append(mref)
       
    def getAlto(self):
        return self.__alto
    
    def getLargo(self):
        return self.__largo
    
    def getAncho(self):
        return self.__ancho
    
    def getCantidad(self):
        return self.cantidad
    
    def getId(self):
        return self.__id
    
    def getCosto(self):
        return self.__costo
    
        