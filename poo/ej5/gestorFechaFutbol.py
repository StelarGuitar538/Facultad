import csv
from claseFecha import Fecha
from gestorEquipo import gestorE as ge
import numpy as np

class gestorFecha:
    def __init__(self):
        self.__listaFechas=[]
    
 
    def inicializar(self):
        datos = np.loadtxt("datosFechaFutbol.csv", delimiter=";")
        for fila in datos:
            nuevaFecha = Fecha(int(fila[0]), int(fila[1]),int(fila[2]),int(fila[3]),int(fila[4]),int(fila[5]))
            self.__listaFechas.append(nuevaFecha)
            
    def buscarFecha(self, idd):
        f =[]
        for i in self.__listaFechas:
            if idd == i.identificadorDelEquipoLocal or idd == i.identificadorDelEquipoVisitante:
                f.append(i.fechaDelPartido)
        return f
    
    def getGolesAFavor(self):
        for i in self.__listaFechas:
            suma = ge.golesAFavor
        return suma
    
    def getGolesEnContra(self):
        for i in self.__listaFechas:
            suma = ge.golesEnContra
        return suma