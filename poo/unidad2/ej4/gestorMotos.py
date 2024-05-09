from claseMotos import Motos
import csv

class gestorMotos: 
    __lista__: list
    
    def __init__(self):
        self.__lista__ = []
        
    def cargarmotos (self) :
        archivo = open("datosMotos.csv" "r")
        reader = csv.reader(delimiter=";")
        for fila in reader:
            nuevaMoto = Motos(fila[0],fila[1],fila[2],float(fila[3]))
            self.__lista__.append(nuevaMoto)
            self.__lista__.sort()
            archivo.close()
            
    def mostrar(self):
        for moto in self.__lista__:
            print(moto)
            
    def verificarPatente(self):
        patente = input("ingrese patente")
        for moto in self.__lista__:
            if patente == moto.patente:
                return patente
        

        