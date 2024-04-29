import csv
from claseEquipo import Equipo
import numpy as np

class gestorE:
    __listaEquipo: list
    def __init__(self):
        self.__listaEquipo = []
    
    def inicializar(self):
        archivo= open("C:\Users\danie\Documents\GitHub\Facultad\poo\ej5\datosEquipo.csv", "r")
        reader=csv.reader(archivo, delimiter=';')
        for fila in reader:
            nuevoEquipo = Equipo(fila[0], int(fila[1]), int(fila[2]), int(fila[3]), int(fila[4]), int(fila[5]))
            self.__listaEquipo.append(nuevoEquipo)
        archivo.close()
        
    