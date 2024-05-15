from gestorClientes import gesClientes
from gestorMovimientos import gesMov

def test():
    m = gesMov()
    c = gesClientes()
    while True:
        print("menu de opciones")
        print("1, carga")
        print("2, puntoa")
        
        op = input("ingrese op: ")
        
        if op == "1":
            m.inicializar()
            c.inicializar()
            m.mostrar()
            c.mostar()

        elif op =="2":
            dni = input("ingrese dni: ")
            funcion = c.actualiza(dni, m)
            print(funcion)
    