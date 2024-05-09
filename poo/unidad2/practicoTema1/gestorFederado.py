from claseFederado import Patinador
from claseEvaluaciones import evaluaciones
from gestorEvaluaciones import gesev
import csv

class gFed:
    __lista:list
    
    def __init__ (self):
        self.__lista = []
        
    def inicializar (self):
        archivo = open("federados.csv" "r")
        reader = reader.csv(delimiter=";")
        for fila in reader:
            nFed = Patinador((fila[0]),(fila[1]),(fila[2]),int(fila[3]),(fila[4]))
            self.__lista.append(nFed)
            
    def puntoA (self):
        estilo = input("ingrese estilo")
        edad = input("ingrese edad")
        
        for i in self.__lista:
            if edad == i.edad:
                if estilo == evaluaciones.getEst(i):
                    print(f"apellido {i.apellido}, nombre: {i.nombre}, dni del participante: {evaluaciones.getDni(i)}")
                    
    
    def puntoB (self):
        max = 0
        for i in self.__lista:
            if evaluaciones.PromVa(i) > max:
                max = evaluaciones.PromVa(i)
                apellido = i.apellido
                nombre = i.nombre
                estilo = evaluaciones.getEst(i)
                clubR = i.clubr(i)
        return print(f"apellido:{apellido}, nombre:{nombre}, estilo:{estilo}, club representado: {clubR}")
    
    def puntoC (self):
        for i in self.__lista:
            if evaluaciones.getEst(i) == "libre":
                print(f"estilo libre \n {i.nombre} {i.apellido} {i.dni} {i.edad} {i.clubr}")
                
            elif evaluaciones.getEst(i) == "escuela":
                print(f"estilo escuela \n {i.nombre} {i.apellido} {i.dni} {i.edad} {i.clubr}")
                
       
    