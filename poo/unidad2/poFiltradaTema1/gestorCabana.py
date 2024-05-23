from claseCabana import Cabana
import numpy as np
import csv

class gesCab:
    __arregloCab: np.ndarray
    __dimension: int
    __cantidad: int
    __incremento: int
    
    def __init__(self):
        self.__arregloCab = np.empty([0], dtype=Cabana)
        self.__dimension = 0
        self.__cantidad = 0
        self.__incremento = 1
        
    def agregar(self, c):
        if self.__dimension == self.__cantidad:
            self.__dimension += self.__incremento
            self.__arregloCab.resize(self.__dimension)
        self.__arregloCab[self.__cantidad] = c
        self.__cantidad +=1
        
    def inicializar(self):
        archivo = open("C:/Users/danie/Documents/GitHub/Facultad/poo/unidad2/poFiltradaTema1/archivos.csv/Cabañas.csv")
        reader = csv.reader(archivo, delimiter=";")
        for fila in reader:
            nCabana = Cabana(int(fila[0]), int(fila[1]), int(fila[2]), int(fila[3]), float(fila[4]))
            self.agregar(nCabana)
        archivo.close()
        
    def mostrar(self):
        for cabana in self.__arregloCab:
            print(cabana)

           
    def puntoa(self, r):
        cantHues = input("ingrese cantidad de huespedes ")
        for cant in self.__arregloCab:
            capCab = cant.getGrandes() * 2 + cant.getChicas()
            if cantHues  == capCab and :
                print(f"{cant.getNum()}")
            
    