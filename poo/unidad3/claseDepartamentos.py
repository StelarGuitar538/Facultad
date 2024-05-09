class Dptos:
    __id: int
    __nya: str
    __npiso: int
    __ndep: int
    __canthab:int
    __cantba:int
    __supCub: float
    
    def __init__(self, id, nya, npiso, ndep, hab, ba, supcub):
        self.__id = id
        self.__nya = nya
        self.__npiso = npiso
        self.__ndep = ndep
        self.__canthab = hab
        self.__cantba = ba
        self.__supCub = supcub
        
        
    def getid(self):
        return self.__id
    
    def getnya(self):
        return self.__nya
    
    def getNpiso(self):
        return self.__npiso
    
    def getNdep(self):
        return self.__ndep
    
    def getHab(self):
        return self.__canthab
    
    def getBa(self):
        return self.__cantba
    
    def getSupCub(self):
        return self.__supCub
    
    