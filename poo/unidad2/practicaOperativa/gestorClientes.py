from claseClientes import Clientes
import csv

class gesClientes:
    __lista : list
    
    def __init__ (self):
        self.__lista = []
        
    def inicializar(self):
        archivo = open("poo/unidad2/practicaOperativa/archivoscsv/clientesAbril2024.csv", "r")
        reader = csv.reader(archivo,delimiter=";")
        for fila in reader:
            nCliente = Clientes((fila[0]), (fila[1]), (fila[2]), fila[3], float(fila[4]))
            self.__lista.append(nCliente)
        archivo.close()
        
    def mostar(self):
        for clientes in self.__lista:
            print(clientes)
            
    def actualiza(self, dni, m):
        i=0
        b= False
        while not b and i < len(self.__lista):
            if dni == self.__lista[i].getdni():
                lista = self.__lista[i]
                b= True
            else: i+=1
        if b==True:
            s= m.ActualizaSaldo(lista.getsaldo(), lista.getnumtar())
            print(f"cliente: {lista.getap()} {lista.getnom()}, numero de tarjeta: {lista.getnumtar()}")
            print(f"saldo anterior: {lista.getsaldo()}")
            print("movimientos \n  fecha  descripcion  importe  tipo de movimiento")
            m.mostrar()
            lista.setSaldo(s)
            print(f"saldo actualizado: {lista.getsaldo()}")
        else: print("no se encontro")
    
    

       
        
            