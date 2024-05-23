from claseVisualizaciones import Visualizaciones
import csv

class gesVis:
    __lista: list
    
    
    def __init__(self):
        self.__lista = []
        
    def inicializar(self):
        archivo = open("C:/Users/danie/OneDrive/Documentos/GitHub/Facultad/poo/recPracticaOperativa/archivosCSV/Visualizaciones.csv", "r")
        reader = csv.reader(archivo,delimiter=";")
        for fila in reader:
            nVis = Visualizaciones(int(fila[0]), (fila[1]), (fila[2]), (fila[3]), int(fila[4]))
            self.__lista.append(nVis)
        archivo.close()
            
    def mostrar(self):
        for visualizaciones in self.__lista:
            print(visualizaciones) 
            
    def buscar(self, m):
        mail = input("ingrese mail ")
        id = m.buscarMail(mail)
        total = 0
        for peli in self.__lista:
            if id == peli.getIdm():
                total += peli.getMin()
        print(f"la cantidad de minutos ha visto peliculas es {total}")
    
    
    def mostrar1(self, m):
            multiples = []
            i = 0
            while i < len(self.__lista):
                var = self.__lista[i]
                j = 0
                while j < len(multiples):
                    if multiples[j][0] == var:  
                        multiples[j].append(var)
                        break
                    j += 1
                else:
                    multiples.append([var])
                i += 1

            i = 0
            while i < len(multiples):
                var2 = multiples[i]
                if len(var2) > 1:
                    j = 0
                    while j < len(m.getarreglo()):
                        arreglo = m.getarreglo()[j]
                        if arreglo.get_dni() == var2[0].get_dni_madre():
                            print(f" {arreglo.getNya()}, {arreglo.getMail()}")
                            k = 0
                        j += 1