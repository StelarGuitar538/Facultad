from claseCD import Cd
from claseLibro import Libro
from clasePubli import Publi
import csv

class gestor:
    __lista: list

    def __init__ (self):
        self.__lista = []

    def inicializarCD(self):
        archivo = open("/workspaces/Facultad/poo/unidad3/ej4 lista/archivoCSV/cd.csv", "r")
        reader = csv.reader(archivo, delimiter=";")
        for fila in reader:
            nlista = Cd(int(fila[0]), (fila[1]), fila[2], fila[3], float(fila[4]))
            self.__lista.append(nlista)
        archivo.close()

    def inicializarLibro(self):
        archivo = open("/workspaces/Facultad/poo/unidad3/ej4 lista/archivoCSV/libro.csv", "r")
        reader = csv.reader(archivo, delimiter=";")
        for fila in reader:
            nlista1 = Libro(fila[0], int(fila[1]), int(fila[2]), fila[3], fila[4], float(fila[5]))
            self.__lista.append()
        archivo.close()

    
