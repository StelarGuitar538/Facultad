from claseMovimientos import Movimientos
import numpy as np
import csv

class gesMov:
    __arregloMov: np.ndarray
    __dimension: int
    __cantidad: int
    __incremento: int
    
    def __init__ (self):
        self.__arregloMov = np.empty([0], dtype=Movimientos)
        self.__cantidad = 0
        self.__dimension = 0
        self.__incremento = 1
        
    def agregar(self, m):
        if self.__dimension == self.__cantidad:
            self.__dimension += self.__incremento
            self.__arregloMov.resize(self.__dimension)
        self.__arregloMov[self.__cantidad] = m
        self.__cantidad += 1
        
    def inicializar(self):
        archivo = open("poo/unidad2/practicaOperativa/archivoscsv/MovimientosAbril204.csv", "r")
        reader = csv.reader(archivo, delimiter=";")
        for fila in reader:
            nMov = Movimientos((fila[0]), (fila[1]), (fila[2]), fila[3], float(fila[4]))
            self.agregar(nMov)
        archivo.close()
        
    def mostrar(self):
        for mov in self.__arregloMov:
            print(mov)
            