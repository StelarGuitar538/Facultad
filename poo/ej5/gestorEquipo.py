import csv
from claseEquipo import Equipo
from gestorFechaFutbol import gestorFecha as gf
import numpy as np

class gestorE:
    __listaEquipo: list
    def __init__(self):
        self.__listaEquipo = []
    
    def __gt__(self, other):
        if self.puntos == other.puntos:
            if(self.diferenciaGoles == other.diferenciaGoles):
                return self.golesAFavor > other.golesAFavor    
            return self.diferenciaGoles > other.diferenciaGoles
        return self.puntos > other.puntos
    
    def inicializar(self):
        datos = np.loadtxt("datosEquipo.csv", delimiter=";")
        for fila in datos:
         nuevoEquipo = Equipo((fila[0]), fila[1], int(fila[2]), int(fila[3]), int(fila[4]), int(fila[5]) )
         self.__listaEquipo.append(nuevoEquipo)
         self.__listaEquipo.sort(reverse=True)
         
    def listado(self):
        nombreEquipo = input("ingrese nombre equipo")
        for i in self.__listaEquipo:
            if nombreEquipo == i.nombreEquipo:
                f = gf.buscarFecha(i.identificadorDelEquipo)
                print(f"equipo:{nombreEquipo}")
                print("fecha |  goles a favor | goles en contra | diferencia de goles | puntos")
                for fecha in f:
                    j+=1
                    print(f"{fecha}{i.golesAFavor}{i.golesEnContra}{i.diferenciaDeGoles}{i.puntos}")
                    print(f"total:{j* i.golesAFavor}{j* i.golesEnContra}{j* i.diferenciaDeGoles}{j* i.puntos}")
                    
                    
    def actualizar(self):
         for i in self.__listaEquipo:
             print("fecha |  goles a favor | goles en contra | diferencia de goles | puntos")
             print(f"{i.golesAFavor}{i.golesEnContra}{i.DifGoles}")
             golesAFavor = gf.getGolesAFavor(i.identificadorDelEquipo)
             golesEnContra = gf.getGolesEnContra(i.identificadorDelEquipo)
             DifGoles = golesAFavor - golesEnContra
             
             
    def mostrar(self):
        for i in self.__listaEquipo:
                f = gf.buscarFecha(i.identificadorDelEquipo)
                print(f"equipo:{i.nombreDelEquipo}")
                print("fecha |  goles a favor | goles en contra | diferencia de goles | puntos")
                for fecha in f:
                    j+=1
                    print(f"{fecha}{i.golesAFavor}{i.golesEnContra}{i.diferenciaDeGoles}{i.puntos}")
                    print(f"total:{j* i.golesAFavor}{j* i.golesEnContra}{j* i.diferenciaDeGoles}{j* i.puntos}")
                    
    def cargarArchivo(self):
        archivo = "equiposOrdenados.csv"
        with open(archivo, "w") as file:
            writer = csv.writer(file)
            for i in self.__listaEquipo:
             fila = [i.nombreDelEquipo, i.identificadorDelEquipo, i.golesAFavor, i.golesEnContra, i.diferenciaDeGoles, i.puntos]
             writer.writerow(fila)