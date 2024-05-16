from gestorLadrillo import gesLadrillo
from gestorMRefractario import gesRef

def test():
    m = gesLadrillo()
    c = gesRef()
    while True:
        print("menu de opciones")
        print("1, carga")
        print("2, punto a")
        print("3, punto b")
        print("4, punto c")
        
        op = input("ingrese op: ")
        
        if op == "1":
            