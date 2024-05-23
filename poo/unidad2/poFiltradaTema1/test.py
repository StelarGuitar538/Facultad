from gestorCabana import gesCab
from gestorReserva import gesReserva

def test ():
    c = gesCab()
    r = gesReserva()
    
    while True:
        print("1, carga")
        
        
        op = input("ingrese opcion ")
        
        if op == "1":
            c.inicializar()
            c.mostrar()
            r.inicializar()
            r.mostrar()
    