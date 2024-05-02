from claseClientes import Clientes
import csv

class gesClientes:
    __lista: list
    
    def __init__ (self):
        self.__lista = []
        
    def inicializar (self):
        archivo = open("clientesAbril2024.csv", "r")
        reader = csv.reader(archivo, delimiter=";")
        for fila in reader :
            nCliente = Clientes((fila[0]), (fila[1]), (fila[2]), fila[3], float(fila[4]))
            self.__lista.append(nCliente)
            archivo.close()
            
    """Leer por teclado el dni de un Cliente, y actualice el saldo del cliente, sumando los créditos y
    restando el pago realizado, éstos últimos datos, obtenidos del Gestor de Movimientos"""
    
    def buscarClientePorDni(self, dni):
        for cliente in self.__lista:
            if cliente.dni == dni:
                return cliente    
                   
    def actualizarSaldo(self, numeroTarjeta):
        return self.__lista[self.__lista['numeroTarjeta'] == numeroTarjeta]
    
    def listado(self):
        dni = input("ingrese un dni")
        cliente = gesClientes.buscarClientePorDni(dni)
        if cliente:
            movClientes = gesClientes.actualizarSaldo(cliente)
            print(f"Cliente: {cliente}")
            print(f"Número de tarjeta: {cliente.numtar}")
            print(f"Saldo anterior: {cliente.saldo}")
            print("Movimientos:")
            print("Fecha     Descripción                Importe   Tipo de movimiento")
            for i in self.__lista:
                print(f"{i.fecha}  {i.desc:30} {i.imp}      {i.tmov}")
                saldoAct = i.saldo
                for i in self.__lista:
                    if i.tmov == "C":
                        saldoAct += i.imp
                    elif i.tmov == "P":
                        saldoAct -= i.imp
                print(f"saldo actualizado: {saldoAct}")
        
           
    def buscarClientePorApellido(self, ap):
        for cliente in self.__lista:
            if cliente.ap == ap:
                return cliente  
            
    def buscarClientePorNom(self, nom):
        for cliente in self.__lista:
         if cliente.nom == nom:
             return cliente 
                     
    def verificarMov(self, dni):
        bandera = False
        for cliente in self.__lista:
            if cliente.dni == dni:
                if cliente.tmov == "C" or cliente.tmov == "P":
                  bandera = True
                if bandera == True:
                    print("si hubo movimientos en el mes de abril")
        
                elif bandera == False:
                    print("no hubo movimientos en abril")