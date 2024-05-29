from gestor import gestor

def test():
    g = gestor()

    while True:
        print("1, carga")
        print("2, punto a")
        print("3, punto b")
        print("4, punto c")

        op = input("ingrese opcion ")

        if op == "1":
            g.inicializarCD()
            g.inicializarLibro()
            g.mostrar()
        
        elif op == "2":
            g.instancia()
        
        elif op == "3":
            g.cantidad()

        elif op == "4":
            g.mostrar2()
