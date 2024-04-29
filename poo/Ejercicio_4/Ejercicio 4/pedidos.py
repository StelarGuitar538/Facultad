class Pedido:
    __patente:str
    __id:int
    __comidas_pedidas:int
    __tiempo_entrega:int
    __tiempo_real:int
    __precio_pedido:float
    
    def __init__(self, patente,id,pedidas,entrga,real,precio):
        self.__patente=patente
        self.__id=id
        self.__comidas_pedidas=pedidas
        self.__tiempo_entrega=entrga
        self.__tiempo_real=real
        self.__precio_pedido=precio
        
    def getPatente(self):
        return self.__patente
    def mostrarPedido(self):
        print('Patente {} Id {} Comidas Pedidas {} Tiempo de Entrega {} Tiempo Real {} Precio del Pedido {}'.format (self.__patente, self.__id,self.__comidas_pedidas,self.__tiempo_entrega,self.__tiempo_real, self.__precio_pedido))
    def getId(self):
        return self.__id
    def __lt__(self,other):
        return (self.__patente < other.getPatente())