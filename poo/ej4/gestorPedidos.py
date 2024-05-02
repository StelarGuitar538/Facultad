from clasePedidos import Pedidos
from claseMotos import Motos
from gestorMotos import gestorMotos
import numpy as np
import csv

class gestorPedidos:
    __lista__ : list
    
    def __init__(self):
        self.__lista__ = []
        
    def cargarPedidos (self):
        archivo = open("datosPedidos.csv", "r")
        reader = csv.reader(delimiter=";")
        for fila in reader:
            nuevoPedido = Pedidos(fila[0],int(fila[1]),int(fila[2]),int(fila[3]),int(fila[4]), float(fila[5]))
            self.__lista__.append(nuevoPedido)
        archivo.close()
      
    def mostrarPedidos(self):
        for nuevoPedido in self.__lista__:
            print(nuevoPedido)
            
    def asignarMoto(self):
        patente = Motos.verificarPatente()
        ide = input("ingrese id del pedido")
        comida = input("ingrese comida")
        tEstimado = input("ingrese tiempo estimado")
        tReal = 0
        precio = input("ingrese precio")
        
        nuevoPedido = Pedidos(patente, ide, comida, tEstimado,tReal,precio)
        self.__lista__.append(nuevoPedido)
        
    def modTiempoReal(self):
        patente = input("ingrese patente")
        id = input("ingrese id")
        for nuevoPedido in self.__lista__:
            if (nuevoPedido.id == id) and (nuevoPedido.patenteMoto == patente) :
                nuevoPedido.tiempoDeEntregaReal = input("ingrese nuevo tiempo real")
                
    
    def leerPatente(self):
        patente = Motos.verificarPatente()
    
    def promedioReal (self):
        patente = gestorPedidos.leerPatente()
        for i in self.__lista__:
            if i.patente == patente:
                tiempoTotal += i.tReal
            
        tiempoPromedio = tiempoTotal/i
        
        for j in gestorMotos.__lista__:
            if j.patente == patente:
                conductor = j.nya
                
        print(f"{conductor}{tiempoPromedio}")
     
     
    def total (self):
        for i in gestorMotos.__lista__:
           for j in i.pedidos:
               total += j.precio 
        return total
                  
    
    def mostracomi(self):
        for i in gestorMotos.__lista__:
            for j in self.__lista__:
                comision = gestorPedidos.total() *0.2
                print(f"{i.patente},{i.nya},{j.id},{j.tiempoDeEsperaEstimado},{j.tiempoDeEsperaReal},{j.precio},{gestorPedidos.total()},{comision}")
            
    
      
            
    
        