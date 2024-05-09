class pedidos:
    __patente: str
    __id_pedido:str
    __comidas:str
    __tiempoestimado:str
    __tiempreal:str

    def __init__(self,id,comida,pat,tr,te):
        self.__comidas=comida
        self.__id_pedido=id
        self.__patente=pat
        self.__tiempoestimado=te
        self.__tiempreal=tr
    
    def getcomida(self):
        return self.__comidas
    def getid(self):
        return self.__id_pedido
    def getpatente(self):
        return self.__patente
    def gettiemporeal(self):
        return self.__tiempreal
    def gettiempoestimado(self):
        return self.__tiempoestimado
    def modtr(self,tir):
        self.__tiempreal=tir
    def __it__(self,other):
        return self.__patente < other.__patente
    