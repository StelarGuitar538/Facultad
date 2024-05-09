import csv
import numpy as np
from motos import moto


class gestorMotos:
    __lista: list



    def __init__(self):
        __lista=[]
    
    def inicializar(self):
        archivo=open("datosmotos.csv","r")
        reader=csv.reader(archivo,delimiter=";")
        bandera=False
        for fila in reader:
            if bandera==False:
                bandera=True
            else:
                unamoto=(fila[0],fila[1],fila[2],fila[3])
                self.__lista.append(unamoto)
    
    def busacrpatente(self,pa,o=0):
        i=0
        while i < len(self.__lista):
            if pa == self.__lista[i].getpatente():
                return True
            i+=1
            return False
        
    def mostarlista(self):
        for i in range (len(self.__lista)):
            print(self.__lista)


    def mostrarconductor(self, pa):
        existe = self.busacrpatente(pa, 1)
        if existe:
            for i in range(len(self.__lista)):
                if self.__lista[i].getpatente() == pa:
                    print("El conductor es: \n Nombre: {}".format(self.__lista[i].getnombre()))
                    return self.__lista[i].getnombre()
                return None
       
