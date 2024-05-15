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
        
        if op == "1":
            m.inicializar()
            c.inicializar()
            m.mostrar()
            c.mostar()

        elif op =="2":
            dni = input("ingrese dni: ")
            funcion = c.actualiza(dni, m)
            print(funcion)

        elif op == "3":
            c.movAbril(m)
            
        elif op == "4":
            m.ordenar()