from claseFecha import Fecha
import numpy as np
import csv

class gesFecha:
    __arregloFecha: np.ndarray
    __cantidad:int
    __dimension: int
    __incremento : int
    
    def __init__ (self):
        self.__arregloFecha = np.empty([0], dtype=Fecha)
        self.__cantidad =0
        self.__dimension = 0
        self.__incremento = 1
        
    def getArreglo(self):
        return self.__arregloFecha
 
    def agregar(self, c):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__arregloFecha.resize(self.__dimension)
        self.__arregloFecha[self.__cantidad] = c
        self.__cantidad += 1
    
    def inicializar(self):
        archivo = open("datosFechaFutbol.csv", "r")
        reader = csv.reader(archivo, delimiter=";")
        for fila in reader:
            nuevaFecha = Fecha((fila[0]), (fila[1]),(fila[2]),int(fila[3]),int(fila[4]))
            self.agregar(nuevaFecha)
        archivo.close()
        
    def mostrar(self):
        for fecha in self.__arregloFecha:
            print(fecha)