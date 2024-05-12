from claseTransacciones import transacciones
from claseCuenta import Cuenta
from gestorCuenta import Arreglo
import csv

class gesTrans:
    __lista: list
    
    def __init__ (self):
        self.__lista = []
        
    def inicializar (self):
        archivo = open("claseTransacciones.csv", "r")
        reader = csv.reader(archivo, delimiter=";")
        for fila in reader:
            ntrans: transacciones(int(fila[0]), int(fila[1]), float(fila[2]), (fila[3]) ) # type: ignore
            self.__lista.append(ntrans)
        archivo.close()
            
            
    def procesarTransacciones(self):
        cvu =  input("ingrese cvu")
        for cuenta in self.__lista:
            if cuenta.getCVU() == cvu:
                print(f"saldo inicial: {cuenta.getSaldo()}")
                for transaccion in self.__lista:
                    cuenta.actTrans(transaccion)
                    print(f"saldo actualizado {cuenta.getSaldo()}")
                    break
        else: print("no se encontro cvu")
                    
            
             
    def actualizarCsv(self):
        archivo = open("cuentasActualizadas.csv", "w")    
        writer = csv.writer(archivo)
        for fila in self.__lista:
            actualizado = transacciones(int(fila[0]), int(fila[1]), float(fila[2]), (fila[3]) )
           
            