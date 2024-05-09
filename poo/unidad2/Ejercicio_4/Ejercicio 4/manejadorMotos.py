from moto import Moto
import csv
class ManejadorM:
    __listaM:list

    def __init__(self):
        self.__listaM=[]
    
    def cargarmotos(self):
        archivo=open('moto.csv')
        reader=csv.reader(archivo,delimiter=';')
        for fila in reader:
            m=Moto(fila[0],fila[1],fila[2],float(fila[3]))
            self.__listaM.append(m)
        archivo.close()
    def mostrar(self):
        for moto in self.__listaM:
            moto.mostrarMoto()