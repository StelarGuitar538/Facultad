#clase arreglo
from claseProductos import Productos
import numpy as np

class Arreglo:
    __ArregloProductos: np.ndarray
    __cantidad: int
    __dimension: int
    __incremento: int
    
    def __init__ (self):
        self.__ArregloProductos = np.empty([0], dtype= Productos)
        self.__cantidad = 0
        self.__dimension = 0
        self.__incremento = 1
        
    def agregar (self, p):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__ArregloProductos.resize(self.__dimension)
        self.__ArregloProductos[self.__cantidad] = p
        self.__cantidad += 1
        
    def hacerCopia(self):
        copiaInventario = np.copy(self.__ArregloProductos)
        return copiaInventario

    def obtenerVistaVentas(self):
        vistaVentas = self.__ArregloProductos[:]
        return vistaVentas

    def agregarVentas(self, ventas):
        juntarVentas = np.concatenate((self.__ArregloProductos, ventas))
        return juntarVentas

    def dividirInventario(self, numPartes):
        dividirInventario = np.array_split(self.__ArregloProductos, numPartes)
        return dividirInventario

    def encontrarValor(self, valor):
        dondeEncontrar = np.where(self.__ArregloProductos == valor)
        return dondeEncontrar

    def ordenarInventario(self):
        ordenarInventario = np.sort(self.__ArregloProductos)
        return ordenarInventario