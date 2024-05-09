class moto:
    __patente:str
    __marca:str
    __nombre:str
    __km:str

    def __init__(self,nombre,marca,patente,km):
        self.__nombre=nombre
        self.__marca=marca
        self.__km=km
        self.__patente=patente
    
    def getnombre(self):
        return self.__nombre
    def getmarca(self):
        return self.__marca
    def getkm(self):
        return self.__km
    def getpatentemoto(self):
        return self.__patente
    
