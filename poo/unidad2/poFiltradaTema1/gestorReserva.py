from claseReserva import Reserva
import csv

class gesReserva:
    __lista: list
    
    def __init__(self):
        self.__lista = []
        
    def inicializar(self):
        archivo = open("C:/Users/danie/Documents/GitHub/Facultad/poo/unidad2/poFiltradaTema1/archivos.csv/Reservas.csv", "r")
        reader = csv.reader(archivo, delimiter=";")
        for fila in reader:
            nReserva = Reserva(int(fila[0]), (fila[1]), int(fila[2]), (fila[3]), float(fila[4]))
            self.__lista.append(nReserva)
        archivo.close()
        
        
    def mostrar(self):
        for reserva in self.__lista:
            print(reserva)

