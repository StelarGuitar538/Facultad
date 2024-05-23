class visualizacion:
    __idmiembro=int
    __idpeli=str
    __fecha=str
    __hora=str
    __min=int
    def __init__(self,idmiembro,idpeli,fecha,hora,min):
        self.__idmiembro=idmiembro
        self.__idpeli=idpeli
        self.__fecha=fecha
        self.__hora=hora
        self.__min=min
    def getidmiembro(self):
        return self.__idmiembro
    def getidpeli(self):
        return self.__idpeli
    def getfecha(self):
        return self.__fecha
    def gethora(self):
        return self.__hora
    def getmin(self):
        return self.__min
    def mostrardatos(self):
        print('{},{},{},{},{}'.format(self.__idmiembro,self.__idpeli,self.__fecha,self.__hora,self.__min))
    def __eq__ (self,other):
        return (self.__idmiembro==other.__idmiembro and self.__fecha==other.__fecha and self.__hora==other.__hora)