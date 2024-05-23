class Miembros:
    __id: int
    __nya: str
    __mail: str
    
    def __init__ (self, id, nya, mail):
        self.__id = id
        self.__nya = nya
        self.__mail = mail
        
    def __str__ (self):
        return f"{self.__id} {self.__nya} {self.__mail}"
    
    def getId(self):
        return self.__id
    
    def getNya(self):
        return self.__nya
    
    def getMail(self):
        return self.__mail