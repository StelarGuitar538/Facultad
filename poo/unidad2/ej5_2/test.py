from gestorEquipo import gesEquipo
from gestorFecha import gesFecha

e = gesEquipo()
f = gesFecha()

def test():
 while True:
    print("menu de opciones")
    print("1, carga")
    print("2, tabla")
    
    op = input("ingrese op")
    
    if op == "1":
        f.inicializar() 
        e.inicializar1() 
        f.mostrar()
        e.mostrar()
        
    elif op == "2":
        e.puntoc()