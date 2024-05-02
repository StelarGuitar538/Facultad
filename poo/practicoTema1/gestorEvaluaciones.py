from claseEvaluaciones import evaluaciones
from claseFederado import Patinador
import csv

class gesev:
    __lista:list
    
    def __init__(self):
        self.__lista = []
     
    def inicializar(self):
        archivo = open("evaluacion.csv","r")
        reader = reader.csv(delimiter=";")
        for fila in reader:
            nEval = evaluaciones((fila[0]), (fila[1]), int(fila[2]), int(fila[3]), int(fila[4]))
            self.__lista.append(nEval)
            
    def puntoD (self):
        dni = input("igrese dni")
        estilo = input("ingrese estilo")
        
        for i in self.__lista:
            if dni == Patinador.getDni(i) and estilo == i.estilo:
                print(f"valoracion 1 {i.vjuez1} valoracion 2 {i.vjuez2} valoracion 3 {i.vjuez3}")
                 