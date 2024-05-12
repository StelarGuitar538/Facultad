from claseCuenta import Cuenta
from gestorTransacciones import transacciones
import numpy as np
import csv

class Arreglo:
    __arregloCuenta : np.ndarray
    __cantidad: int
    __dimension: int
    __incremento: int
    
    def __init__ (self):
        self.__arregloCuenta = np.empty([0], dtype= Cuenta)
        self.__cantidad = 0
        self.__dimension = 0
        self.__incremento = 1
        
    def agregar (self, c):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__arregloCuenta.resize(self.__dimension)
        self.__arregloCuenta[self.__cantidad] = c
        self.__cantidad += 1
    
    def inicializar (self):
        archivo = open("claseCuenta.csv", "r")
        reader = csv.reader(archivo, delimiter=";")
        for fila in reader:
            nuevaCuenta = Cuenta((fila[0]), (fila[1]), (fila[2]), (fila[3]), float(fila[4]), int(fila[5]))
            self.__arregloCuenta.agregar(nuevaCuenta)
        archivo.close()
       
    """Leer por teclado el DNI de un cliente e informar los datos del cliente: apellido, nombre,
CVU y saldo (actualizado por las transacciones)."""
       
    def buscar(self):
        dni = input("ingrese un dni")
        buscarDni = np.where(self.__arregloCuenta[:, 2] == dni)[0]
        if len(buscarDni) > 0:
            cuentaEncontrada = self.__arregloCuenta[buscarDni[0]]
            apellido = cuentaEncontrada.getapellido()
            nombre = cuentaEncontrada.getNom()
            cvu = cuentaEncontrada.getCVU()
            saldoAct = cuentaEncontrada.getSaldo()
            print(f"{apellido}, {nombre}, {cvu}, {saldoAct}")
        
        
    def modpor(self):
        Cuenta.modVar(Cuenta.nuevoPorc())
        print(f"nuevo porcentaje {Cuenta.getPorc()}")
        
    def ActSaldo(self):
        for i in self.__arregloCuenta:
            Cuenta.actSaldo()
            print(f"saldo actualizado {Cuenta.getSaldo()}")
            
    
            
        