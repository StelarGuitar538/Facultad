from claseCancha import Canchas
import numpy as np
import csv

class gesCanchas:
    __arregloCanchas: np.ndarray
    __dimension: int
    __cantidad: int
    __incremento: int
    
    def __init__ (self):
            self.__arregloCanchas = np.empty([0], dtype=Canchas)
            self.__cantidad = 0
            self.__dimension = 0
            self.__incremento = 1
            
    def agregar(self, c):
            if self.__dimension == self.__cantidad:
                self.__dimension += self.__incremento
                self.__arregloCanchas.resize(self.__dimension)
            self.__arregloCanchas[self.__cantidad] = c
            self.__cantidad += 1
            
    def inicializar(self):
            archivo = open("poo/unidad2/practicaOperativaFiltrada/archivoscsv/Canchas.csv", "r")
            reader = csv.reader(archivo, delimiter=";")
            for fila in reader:
                nCancha = Canchas((fila[0]), (fila[1]), float(fila[2]))
                self.agregar(nCancha)
            archivo.close()
            
    def mostrar(self):
            for cancha in self.__arregloCanchas:
                print(cancha)
                
    def impHora(self, id):
        i=0
        b=False
        while not b and i< len(self.__arregloCanchas):
            if id == self.__arregloCanchas[i].getId():
                b= True
                return self.__arregloCanchas[i].getImporte()
            else:
                i+=1

    def buscar(self, a):
        idc = input("ingrese id a buscar ")
        a.buscarId(idc)