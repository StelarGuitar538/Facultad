from pedido import pedidos
import csv
import numpy as np
class gestorPedidos:
    __lista: list



    def __init__(self):
        __lista=[]
    
    def inicializar(self):
        archivo=open("datospedidos.csv","r")
        reader=csv.reader(archivo,delimiter=";")
        bandera=False
        for fila in reader:
            if bandera==False:
                bandera=True
            else:
                unpedido=(fila[0],fila[1],fila[2],fila[3],fila[4])
                self.__lista.append(unpedido)
    
    def agregarpedido(self,pa):
        print("ingrese los valores del nuevo pedido:")
        i=input("ingrese el id del pedido:")
        c=input("comidas:")
        te=input("ingrese el tiempo estimado:")
        pr=float(input("Precio total: "))
        unpedido=pedidos(pa,i,c,te,pr)
        self.__lista.append(unpedido)
    def modificar(self,pa,idp,tir):
        i=0
        while i < len(self.__lista):
            if((self.__lista[i].getpatente()==pa)and (self.__lista[i].getid()==idp)):
                self.__lista[i].modtr(tir)
            i+=1
    def promedio(self,pa):
        i=0
        acum=0
        contador=0
        for i in range (len(self.__lista)):
            if(self.__lista[i].getpatente()==pa):
                acum+=self.__lista[i].gettiemporeal()
                contador+=1
        return float(acum/contador)
    def ordenar(self):
        np.sort(self.__lista)
    
    def imprimir_comisiones(self):
        for pedido in self.__lista:
            print(f"Patente de Moto: {pedido.patente}")
            print(f"Conductor: {pedido.conductor}")
            print(f"Identificador de pedido: {pedido.identificador}")
            print(f"Tiempo estimado: {pedido.tiempo_estimado}")
            print(f"Tiempo real: {pedido.tiempo_real}")
            print(f"Precio: $ {pedido.precio}")
            print(f"Comisión: $ {pedido.precio * 0.20}")  # 20% del total
            print()
