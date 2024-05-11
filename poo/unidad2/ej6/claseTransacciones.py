class transacciones:
    __cvu=int
    __num=int
    __imp=float
    __tipo=str

def init(self, cvu, num, imp, tipo):
    self.__cvu=cvu
    self.__num=num
    self.__imp=imp
    self.__tipo=tipo


def getTipo(self):
    return self.__tipo

def getImp(self):
    return self.__imp