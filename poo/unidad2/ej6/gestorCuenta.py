from claseCuenta import Cuenta
import numpy as np

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
        if self.__arregloCuenta == self.__dimension:
            self.__dimension += self.__incremento
            self.__arregloCuenta.resize(self.__dimension)
        self.__arregloCuenta[self.__cantidad] = c
        self.__cantidad += 1
    
    def buscar(self):
        dni = input("ingrese un dni")
        buscarDni = np.where(self.__arregloCuenta[:, 2] == dni)[0]
        if len(buscarDni) > 0:
            cvu = self.__arregloCuenta[buscarDni[0]][5]
            print(f"{Cuenta.getapellido()}, {Cuenta.getNom()}, {Cuenta.getCVU()}, {Cuenta.getSaldo()}")
        
        
    def modpor(self):
        Cuenta.modVar(Cuenta.nuevoPorc())
        print(f"nuevo porcentaje {Cuenta.getPorc()}")
        
    def ActSaldo(self):
        for i in self.__arregloCuenta:
            Cuenta.actSaldo()
            print(f"saldo actualizado {Cuenta.getSaldo()}")
            
    
            
        