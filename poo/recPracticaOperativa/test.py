from gestorMiembros import gesMiembros
from gestorVisualizaciones import gesVis


def test():
    m = gesMiembros()
    v = gesVis()
    

    
    while True:
        print ("1, carga")
        print ("2, punto a")
        print("3, punto b")
        
        op = input("ingrese opcion ")
        if op == "1":
                m.inicializar()
                m.mostrar()
                v.inicializar()
                v.mostrar()
        elif op == "2":
            v.buscar(m)
            
        elif op == "3":
            v.mostrar1()