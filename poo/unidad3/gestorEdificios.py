from claseEdificio import Edificio
from claseDepartamentos import Dptos
import csv

class gestorEdificio:
    __lista: list
    
    def __init__ (self):
        self.__lista = []
        
    def inicializar (self):
        archivo = open("EdificioNorte.csv", "r")
        reader = csv.reader(archivo, delimiter=";")
        for fila in reader:
            insEdificio = Edificio((fila[0]), (fila[1]), (fila[3]), (fila[4]), int(fila[5]), int(fila[6]))
            self.__lista.append(insEdificio)
            archivo.close()
            
            """Dado el nombre de un edificio mostrar: Nombre y apellido de los propietarios de
cada uno de los departamentos del edificio"""

    def punto1 (self):
        nomEdi = input("ingrese nombre de edificio")
       
            