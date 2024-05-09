class evaluaciones:
    __dni:str
    __estilo:str
    __vjuez1:int
    __vjuez2:int
    __vjuez3:int
    
    def __init_ (self, dni, estilo, j1, j2, j3):
        self.__dni = dni
        self.__estilo = estilo
        self.__vjuez1 = j1
        self.__vjuez2 = j2
        self.__vjuez3 = j3
        
    def getDni(self):
        return self.__dni
    
    def getEst(self):
        return self.__estilo
    
    def getj1(self):
        return self.__vjuez1
    
    def getj2(self):
        return self.__vjuez2
    
    def getj3(self):
        return self.__vjuez3
    
    def PromVa(self):
        return ((self.__vjuez1 + self.__vjuez2 + self. __vjuez3) / 3)
    
    def __gt__(self, other):
        return self.PromVa() > other.PromVa()
    