from gestorClientes import gesClientes
from gestorMovimientos import gesMov



def test():
    gm = gesMov()
    gc = gesClientes()
    while True:
        print("\nMenú de opciones:")
        print("0. carga")
        print("1. Actualizar saldo y mostrar movimientos de un cliente.")
        print("2. Verificar si un cliente tuvo movimientos por número de tarjeta.")
        print("3. Salir.")
        
        op = input("ingrese opcion")
        
        if op == "0":
            gm.inicializar()
            gc.inicializar()
        
        elif op == "1":
           gc.listado()
           
        elif op == "2":
            gm.movAbril()
        