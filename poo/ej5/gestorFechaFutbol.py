import csv
from claseFecha import Fecha
import numpy as np

class gestorFecha:
    def __init__(self):
        self.__listaFechas=[]
    
    def inicializar(self):
        archivo = open("C:\Users\danie\Documents\GitHub\Facultad\poo\ej5\datosFechaFutbol.csv", "r")
        reader = csv.reader(archivo, delimiter=';')
        for fila in reader:
            nuevaFecha = Fecha(int(fila[0]), int(fila[1]), int(fila[2]), int(fila[3]), int(fila[4]))
            self.__listaFechas.append(nuevaFecha)
        archivo.close
        