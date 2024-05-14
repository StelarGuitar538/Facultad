from movimiento import movimiento
import numpy as np
import csv

class gestormovimiento:
    __cantidad:int
    __dimension:int
    __incremento:int
    def __init__(self,):
        self.__listamovimientos = np.empty(dimension, dtype = movimiento)
        self.__cantidad=0
        self.__dimension=0
        self.__incremento=1
    
    def agregarmov(self, m):
        self
    
    def instanciar(self):
        i = 0
        f = open("/home/la-net-05/Escritorio/practica1/movimientosabril2024.csv", "r")
        reader = csv.reader(f, delimiter=",")
        for linea in reader:
            if all(linea):
                instancia = movimiento(linea[0], linea[1], linea[2], linea[3], linea[4])
                self.__listamovimientos.agregarmov(instancia)
                i += 1
        f.close()
    def actualiza(self, tarjeta,saldo):
        for movimiento in self.__listamovimientos:
            if movimiento.getnumtar()==tarjeta:
                print("mostrar los datos ")
                if movimiento.gettipomov()=='C':
                    saldo+=movimiento.getimporte()
                else: saldo-=movimiento.getimporte()
        return saldo
    def __iter__(self):
        return iter(self.__listamovimientos)
    
    def getmov(self, i):
        return(self.__listamovimientos[i])
