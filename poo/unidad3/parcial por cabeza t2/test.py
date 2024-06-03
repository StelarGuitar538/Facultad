from lista import Lista
from autobuses import Autobuses
from vanes import Vanes

def test():
    l = Lista()
    
    a1 = Autobuses("scania", "c100", 2020, 50, 20, 70000, 1000, "turismo", "nocturno")
    a2 = Autobuses("mercedes", "1144", 1980, 40, 15, 200000, 500, "transporte", "diurno")
    v1 = Vanes("renault", "transit", 2021, 20, 10, 10000, 200, "van")
    v2 = Vanes("ford", "boxer", 2012, 20, 5, 5000, 300, "minivan")
    
    b= False
    
    while not b:
        print("0, finaliza")
        print("1, punto 1")
        print("2, punto 2")
        print("3, punto 3")
        print("4, punto 4")
        
        op = input("selecciona una opcion: ")

        if op == "1":
            l.agregar(a1)
            l.agregar(a2)
            l.agregar(v1)
            l.agregar(v2)
            a1.mostrar()
            a2.mostrar()
            v1.mostrar()
            v2.mostrar()
        
        elif op == "2":
            l.punto2()
            
        elif op== "3":
            l.punto3()
            
        elif op == "4":
            l.punto4()
                
        else :
            b=True
        

if __name__ == "__main__":
    test()
            
        
        