from gestorCuenta import Arreglo
from gestorTransacciones import gesTrans

a = Arreglo()
t = gesTrans()

def test1():
    while True:
        print("1, carga")
        print("2, punto 1")
        print("3, punto 2")
        print("4, punto 3")
        print("5, punto 4")
        
        op = input("elige una opcion")
        
        if op == "1":
            t.inicialiazar()
            a.inicializar()
        
        elif op == "2":
            a.buscar()
            
        elif op == "3":
            a.modpor()
            
        elif op == "4":
            a.ActSaldo()
            
        elif op == "4":
            t.procesarTransacciones()
            t.actualizarCsv()
        
        
        
