from claseCD import Cd
from claseLibro import Libro
from clasePubli import Publi
import csv

class gestor:
    __lista: list

    def __init__ (self):
        self.__lista = []

    def inicializarCD(self):
        archivo = open("C:/Users/danie/Documents/GitHub/Facultad/poo/unidad3/ej4 lista/archivoCSV/cd.csv", "r")
        reader = csv.reader(archivo, delimiter=";")
        for fila in reader:
            nlista = Cd(int(fila[0]), (fila[1]), fila[2], fila[3], float(fila[4]))
            self.__lista.append(nlista)
        archivo.close()

    def inicializarLibro(self):
        archivo = open("C:/Users/danie/Documents/GitHub/Facultad/poo/unidad3/ej4 lista/archivoCSV/libro.csv", "r")
        reader = csv.reader(archivo, delimiter=";")
        for fila in reader:
            nlista1 = Libro(fila[0], (fila[1]), int(fila[2]), fila[3], fila[4], float(fila[5]))
            self.__lista.append(nlista1)
        archivo.close()

    def mostrar(self):
        for publi in self.__lista:
            print(publi)


    def instancia (self):
        pos = int(input("ingrese poscicion: "))
     
        if pos >= len(self.__lista) and pos < 0:
           print("posicion fuera de rango")

        item = self.__lista[pos]

        if isinstance(item, Libro):
                print(f"la posicion {pos} es un libro")
        elif isinstance(item, Cd):
                print(f"la posicion {pos} es un cd")
        else:
                print(f"la posicion {pos} es desconocida")
                
    
    def cantidad(self):
        cli = 0
        ccd = 0
        for publi in self.__lista:
            if isinstance(publi, Libro):
                cli +=1
            elif isinstance(publi, Cd):
                ccd+=1
        print(f"cantidad libros {cli}        cantidad de cds {ccd}")
    
        
    def mostrar2(self):
        for publi in self.__lista:
            print(f"titulo: {publi.getTitulo()} categoria: {publi.getCat()} importe de venta: {publi.calcularImporte()}")