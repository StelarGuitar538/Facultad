from claseEquipo import Equipo
import csv

class gesEquipo:
    __lista: list
    
    def __init__ (self):
        self.__lista = []
        
    def inicializar1 (self):
        archivo = open("datosEquipo.csv", "r")
        reader = csv.reader(archivo, delimiter=";")
        for fila in reader:
            nuevoEquipo = Equipo((fila[0]), fila[1], int(fila[2]), int(fila[3]), int(fila[4]), int(fila[5]))
            self.__lista.append(nuevoEquipo)
        archivo.close()
        
        
    def mostrar(self):
        for fecha in self.__lista:
            print(fecha)