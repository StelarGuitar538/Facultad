import csv
import numpy as np
from gestormotos import gestorMotos
from gestorpedido import gestorPedidos

class menu():
    __Gm=gestorMotos()
    __Gp=gestorPedidos()
    def __init__(self):
        self.__Gm=gestorMotos()
        self.__Gp=gestorPedidos()
    def manejadorar(self):
        #Menu desplegable con las opciones
        v=int(input("1-Leer datos de moto\n2-Leer datos de Pedidos\n3-Cargar un nuevo pedido\n4-Modificar tiempo real de entrega\n5-Mostrar Tiempo promedio de entrega\n6-Generar un listado para cada moto\n7-Mostrar datos\n8-Ordenar lista\n0-Finalizar\n"))
        band=False
        while v>0 and band==False:

            if v==1:
                self.__Gm.inicializar()
            elif v==2:
                self.__Gp.inicializar()
            elif v==3:
                pa=input("ingrese una patente: ")
                pa=gestorMotos.busacrpatente(pa)
                while pa!=True:
                    print("no se encontro la patente")
                    pa=input("ingrese una patente")
                    pa=gestorMotos.busacrpatente(pa)
                gestorPedidos.agregarpedido(pa)
            elif v==4:
                pa=input("ingrese una patente:")
                idp=input("ingrese una ID:")
                tir=input("ingrese tiempo real:")
                self.__Gp.modificar(pa,idp,tir)
            elif v==5:
                pa=input("ingrese una patente: ")
                conductor = self.__Gm.mostrarconductor(pa)
                if conductor is not None:
                    print(f"el conductor: {conductor} hizo un tiempo promedio de: {self.__Gp.promedio}")
                else:
                    print("la patente ingresada no existe:")
           
            elif v==6:
                self.__Gp.ordenar()
                self.__Gp.imprimir_comisiones()
            elif v==0:
                print("opcion no valida")

            

