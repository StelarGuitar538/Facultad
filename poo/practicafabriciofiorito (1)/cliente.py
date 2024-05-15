class cliente:
    def __init__(self, nombre, apellido, dni, numtar, saldoanterior):
        self.__nombre = str(nombre)
        self.__apellido = str(apellido)
        self.__dni = int(dni)
        self.__numtar = int(numtar)
        self.__saldoanterior = float(saldoanterior)

    def getdni(self):
        return(self.__dni)
    
    def getnom(self):
        return(self.__nombre)
    
    def getapellido(self):
        return(self.__apellido)
    def getTarjeta(self):
        return self.__numtar
    def getSaldo(self):
        return self.__saldoanterior
    def setsaldo(self,saldo):
        self.__saldoanterior=saldo
    def __lt__(self, otro):
        return(self.__numtar < otro.__numtar)