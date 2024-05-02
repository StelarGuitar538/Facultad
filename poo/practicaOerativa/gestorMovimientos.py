from claseMovimientos import Movimientos
from gestorClientes import gesClientes
from claseClientes import Clientes
import csv
import numpy as np

class gesMov:
    __lista: list
    
    def __init__ (self):
        self.__lista = []
 
    def inicializar (self):
        datos = np.loadtxt("MovimientosAbril2024.csv", delimiter=";")
        for fila in datos :
            nMov = Movimientos((fila[0]), (fila[1]), (fila[2]), fila[3], float(fila[4]))
            self.__lista.append(nMov)
           
           
        """Leer por teclado un número de tarjeta, e informar por pantalla apellido y nombre del Cliente, si
este, no tuvo movimientos durante el mes de abril 2024."""

    def movAbril(self):
        numtar = input("ingrese numero de tarjeta")
        for i in self.__lista:
            if numtar == i.numtar:
                print(f"apellido {gesClientes.buscarClientePorApellido(i)} nombre {gesClientes.buscarClientePorNom(i)} {gesClientes.verificarMov(i)}")
                
    """Ordenar el Gestor de Movimientos por número de tarjeta, para facilitar el procesamiento del
punto a. """

    def ordenar(self):
        self.__lista.sort()