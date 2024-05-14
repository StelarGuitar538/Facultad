from GestorClientes import GestorClientes
from GestorMovimientos import GestorMovimientos
from colorama import Style

def test():
    movimientosManager = GestorMovimientos()
    clientesManager = GestorClientes()
    clientesManager.leerClientes_desde_csv("POO Python\POO Facultad\PracticaOperativa2024\ClientesAbril2024.csv")
    movimientosManager.leerMovimientos_desde_csv("POO Python\POO Facultad\PracticaOperativa2024\MovimientosAbril2024.csv")
    
    opcion = None
    while opcion != '4':
        print("1. Actualizar el saldo de un cliente")
        print("2. Verificar si un cliente tuvo movimientos en el mes a partir de numero de tarjeta")
        print("3. Ordenar datos de movimientos por numero de tarjeta")
        
        opcion = input(Style.BRIGHT+'\n\n>>>> '+Style.RESET_ALL)
        
        if opcion == '1':
            dni = input('Ingrese el dni del cliente a actualizar: ')
            if(clientesManager.actualizarCliente(dni,movimientosManager.get_movimientosCopia()) == 'NoEncontrado'):
                print(Style.BRIGHT+"El dni ingresado no corresponde a ningun cliente en el sistema"+Style.RESET_ALL)
        
        elif opcion == '2':
            tarjeta = int(input('Ingrese la tarjeta para verificar si tuvo movimientos: '))
            movimientosManager.verificarMovimientos(tarjeta,clientesManager.get_listaClientesCopia())
        
        elif opcion  == '3':
            movimientosManager.ordenarPorTarjeta()
            print("Los movimientos se ordenaron con exito")
        elif opcion == '4':
            pass
        
        else: 
            print(Style.BRIGHT+ "La opcion ingresada no es valida"+ Style.RESET_ALL)

if __name__ == '__main__':
    test()