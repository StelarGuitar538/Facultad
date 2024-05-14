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
        for cliente in self.__lista:
            if cliente.numtar == numeroTarjeta:
                return cliente
    
    def listado(self):
        dni = input("Ingrese un DNI: ")
        cliente = self.buscarClientePorDni(dni)
        if cliente:
          movClientes = self.actualizarSaldo(cliente)
        print(f"Cliente: {cliente}")
        print(f"Número de tarjeta: {cliente.numtar}")
        print(f"Saldo anterior: {cliente.saldo}")
        print("Movimientos:")
        print("Fecha     Descripción                Importe   Tipo de movimiento")
        saldoAct = cliente.saldo
        for movimiento in movClientes:
            print(f"{movimiento.fecha}  {movimiento.desc} {movimiento.imp}      {movimiento.tmov}")
            if movimiento.tmov == "C":
                saldoAct += movimiento.imp
            elif movimiento.tmov == "P":
                saldoAct -= movimiento.imp
        print(f"Saldo actualizado: {saldoAct}")
        
        
           
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