from gestor import Gestor

def test():
    gestor = Gestor()
    b = False
    
    while not b:
        print("0, inicializar")
        print("1, agregar")
        print("2, instancia")
        print("3, mostrar")
        print("4, tarifa")
        print("pulse cualquier tecla para salir")
        try:
            op = int(input("opcion: "))
        except ValueError:
            print("error")
            continue
        
        if op == 0:
            gestor.inicializar()
            gestor.mostrar()
        
        elif op == 1:
            gestor.agregar()
            gestor.guardarcsv(1)
            gestor.mostrar()
         
        elif op == 2:
            gestor.instancia()   
            
        elif op == 3:
            gestor.mostrar2()
        
        elif op == 4:
            gestor.tarifa()
        
        else:
            b = True
            
if __name__ == "__main__":
    test()