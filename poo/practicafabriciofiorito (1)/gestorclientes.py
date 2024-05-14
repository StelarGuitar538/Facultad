from cliente import cliente
import csv

class gestorcliente:
    def __init__(self):
        self.__listaclientes = []

    def instanciar(self):
        f = open("/home/la-net-05/Escritorio/practica1/clientesabril.csv", "r")
        reader = csv.reader(f, delimiter=",")
        for linea in reader:
            if all(linea):
                instancia = cliente(linea[0], linea[1], linea[2], linea[3], linea[4])
                self.__listaclientes.append(instancia)
        f.close()
    
    def actualizarsaldo(self, dni, gm):
        i = 0
        bandera = 0
        #cliente = self.__listaclientes[i]
        while bandera == 0 and i < len(self.__listaclientes):
            if self.__listaclientes[i].getdni() == dni:
                cliente = self.__listaclientes[i]
                bandera = 1
            else: 
                i += 1
        if bandera == 1:
            print("mostrar datos de cliente")
            s=gm.Actualiza(cliente.getTarjeta(),cliente.getSaldo())
            print("saldo actualiza", s)
            cliente.setSaldo(s)
        elif bandera == 0:
            print("no se encontro")
    
    def mostrarpornum(self, numtar, gm, dimension):
        i = 0
        bandera = 0
        while bandera == 0 and i < dimension:
            movimiento = gm.getmov(i)
            if movimiento.getnumtar() == numtar:
                bandera = 1
                salida = str(f"nombre: {self.__listaclientes[i].getnom()}, apellido: {self.__listaclientes[i].getapellido()}")
                return(salida)
            else:
                print("no se encontro")
    
    def ordenar(self):
        self.__listaclientes.sort()