from claseEquipo import Equipo
from claseFecha import Fecha
from gestorFecha import gesFecha
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
            
    
    def puntoc(self):
        gestor = gesFecha()
        arreglo = gestor.getArreglo()
        for equipo in self.__lista:
            print(f"equipo: {Equipo.getNomEq(equipo)}")
            for fecha in arreglo:
             print(f"fecha: {Fecha.getFechaPartido(fecha)}, goles a favor: {Equipo.getgolesAFavor(fecha)}, goles en contra: {Equipo.getgolesEnContra(fecha)}, diferencia de goles: {Equipo.getdifGoles(fecha)}, puntos: {Equipo.getpuntos(fecha)}")
             
             
             
    