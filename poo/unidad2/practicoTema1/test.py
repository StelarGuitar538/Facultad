from gestorEvaluaciones import gesev
from gestorFederado import gFed

def test():
    while True:
     print("menu de opciones")
     print("0 carga")
     print("1 punto a")
     print("2 punto b")
     print("3 punto c")
     print("4 punto d")
     
     op = input("ingrese opcion: ")
     
     if op == "0":
         gesev.inicializar()
         gFed.inicializar()
         
     elif op == "1":
         gFed.puntoA()
         
     elif op == "2":
         gFed.puntoB()
        
     elif op == "3":
         gFed.puntoC()
         
     elif op == "4":
         gesev.puntoD()