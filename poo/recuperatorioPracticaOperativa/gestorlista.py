from claseClientes import Clientes
import csv

class gesClientes:
    __lista : list
    
    def __init__ (self):
        self.__lista = []
        
    def inicializar(self):
        archivo = open("poo/unidad2/practicaOperativa/archivoscsv/clientesAbril2024.csv", "r")
        reader = csv.reader(archivo,delimiter=";")
        for fila in reader:
            nCliente = Clientes((fila[0]), (fila[1]), (fila[2]), fila[3], float(fila[4]))
            self.__lista.append(nCliente)
        archivo.close()
        
    def mostar(self):
        for clientes in self.__lista:
            print(clientes)