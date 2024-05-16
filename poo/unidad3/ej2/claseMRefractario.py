class mRef:
    __material: int
    __caracteristicas: str
    __cantUtilizada: float
    __costoAdicional: float
    
    def __init__(self, mat, carac, cant, cost):
        self.__material = mat
        self.__caracteristicas = carac
        self.__cantUtilizada = cant
        self.__costoAdicional= cost
        
    def getMaterial(self):
        return self.__material
        
    def getCarac(self):
        return self.__caracteristicas
    
    def getCant(self):
        return self.__cantUtilizada
    
    def getCosto(self):
        return self.__costoAdicional
    