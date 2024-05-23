from claseMiembros import Miembros
import numpy as np
import csv

class gesMiembros:
    __arregloMiembros: np.ndarray
    __dimension: int
    __cantidad: int
    __incremento: int
        
    def __init__ (self):
            self.__arregloMiembros = np.empty([0], dtype=Miembros)
            self.__cantidad = 0
            self.__dimension = 0
            self.__incremento = 1
                
    def agregar(self, c):
            if self.__dimension == self.__cantidad:
                self.__dimension += self.__incremento
                self.__arregloMiembros.resize(self.__dimension)
            self.__arregloMiembros[self.__cantidad] = c
            self.__cantidad += 1
                
    def inicializar(self):
            archivo = open("C:/Users/danie/OneDrive/Documentos/GitHub/Facultad/poo/recPracticaOperativa/archivosCSV/Miembros.csv", "r")
            reader = csv.reader(archivo, delimiter=";")
            for fila in reader:
                nMiembros = Miembros(int(fila[0]), (fila[1]), (fila[2]))
                self.agregar(nMiembros)
            archivo.close()
                
    def mostrar(self):
            for miembros in self.__arregloMiembros:
                print(miembros)
        
    def buscarMail (self, mail):
            i=0
            b=False
            while not b and i< len(self.__arregloMiembros):
                    if mail == self.__arregloMiembros[i].getMail():
                            b= True
                            return self.__arregloMiembros[i].getId()
                    else:
                            i+=1
        
