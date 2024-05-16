from gestorClientes import gesClientes
from gestorMovimientos import gesMov

def test():
    m = gesMov()
    c = gesClientes()
    while True:
        print("menu de opciones")
        print("1, carga")
        print("2, punto a")
        print("3, punto b")
        print("4, punto c")
        
        op = input("ingrese op: ")