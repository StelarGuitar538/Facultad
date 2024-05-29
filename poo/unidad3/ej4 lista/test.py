from gestor import gestor

def test():
    g = gestor()

    while True:
        print("1, carga")
        print("2, punto a")

        op = input("ingrese opcion ")

        if op == "1":
            g.inicializarCD()
            g.inicializarLibro()


