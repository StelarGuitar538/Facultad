from pedidos import Pedido
import csv
class ManejadorP:
    __listaP:list
    
    def __init__(self):
        self.__listaP=[]
    
    def cargarpedidos(self):
        archivo=open('pedido.csv')
        reader=csv.reader(archivo,delimiter=';')
        for fila in reader:
            p=Pedido(fila[0],int(fila[1]),int(fila[2]),int(fila[3]),int(fila[4]), float(fila[5]))
            self.__listaP.append(p)
        archivo.close()
    
    def mostrar(self):
        for pedido in self.__listaP:
            pedido.mostrarPedido()
    
    def ordenado(self):
        self.__listaP.sort()
        for pedido in self.__listaP:
            pedido.mostrarPedido()
        