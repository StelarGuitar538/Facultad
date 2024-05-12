from claseTransacciones import transacciones
class Cuenta:
    __apellido: str
    __nombre: str
    __dni:str
    __telefono: str
    __saldo: float
    __cvu: int
    __porcrend: 0.18
    
    def __init__ (self, apellido, nombre, dni, telefono, saldo, cvu):
        self.__apellido = apellido
        self.__nombre = nombre
        self.__dni = dni
        self.__telefono = telefono
        self.__saldo = saldo
        self.__cvu = cvu
        
    def getapellido(self):
        return self.__apellido
    
    def getNom(self):
        return self.__nombre
    
    def getCVU(self):
        return self.__cvu
    
    def getSaldo(self):
        return self.__saldo
    
    def getPorc(self):
        return self.__porcrend
    
    
    def actTrans(self, transacciones):
        tipo = transacciones.getTipo()
        imp = transacciones.getImp()
        if tipo == "D":
            self.__saldo -= imp
        elif tipo == "C":
            self.__saldo += imp
    
    def nuevoPorc (self):
        nuevoPorc = input("ingrese nuevo porcentaje")
    
    def modVar(self, var):
        self.__porcrend = var
        
    def actSaldo(self):
        self.__saldo *= (1 + self.nuevoPorc())