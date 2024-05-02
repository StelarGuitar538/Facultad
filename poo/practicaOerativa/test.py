from gestorClientes import gesClientes
from gestorMovimientos import gesMov

def test():
    while True:
        print("\nMenú de opciones:")
        print("1. Actualizar saldo y mostrar movimientos de un cliente.")
        print("2. Verificar si un cliente tuvo movimientos por número de tarjeta.")
        print("3. Salir.")
        
        op = input("ingrese opcion")
        
        if op == "1":
           gesClientes.listado()
        elif op == "2":
            gesMov.movAbril()
        