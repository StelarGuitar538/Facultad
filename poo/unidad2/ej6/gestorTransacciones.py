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
            
    
    def actTrans(self, cvu):
        if cvu:
          if transacciones.getTipo() == "D":
              Cuenta.__saldo -= transacciones.getImp()
        elif transacciones.getTipo() == "C":
            Cuenta.__saldo += transacciones.getImp()
        
          
    def procesarTransacciones(self):
        cvu = input("ingrese cvu")
        i = 0
        b = False
        while i< len(self.__lista) and b == False:
         if len(self.__lista) == cvu:
            print(f"saldo inicial: {Cuenta.getSaldo()}")
            for cvu in self.__lista:
                gesTrans.actTrans(cvu)
        else:
            i+1
            
             
    def actualizarCsv(self):
        archivo = open("cuentasActualizadas.csv", "w")    
        writer = csv.writer(archivo)
        for fila in self.__lista:
            actualizado = transacciones(int(fila[0]), int(fila[1]), float(fila[2]), (fila[3]) )
           
            