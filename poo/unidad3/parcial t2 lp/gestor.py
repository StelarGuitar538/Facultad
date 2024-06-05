from autobuses import Autobuses
from vanes import Vanes

import csv

class Gestor:
    __lista: list
    
    def __init__(self):
        self.__lista = []
        
    def inicializar(self):
        archivo = open("poo/unidad3/parcial t2 lp/archivoscsv/vehiculos.csv", "r")
        reader = csv.reader(archivo, delimiter=";")
        for fila in reader:
            if len(fila) > 0:
                if fila[0] == "A":
                    na = Autobuses(fila[1], fila[2], int(fila[3]), int(fila[4]), int(fila[5]), float(fila[6]), float(fila[7]), fila[8], fila[9])
                    self.__lista.append(na)
                elif fila[0] == "V":
                    nv = Vanes(fila[1], fila[2], int(fila[3]), int(fila[4]), int(fila[5]), float(fila[6]), float(fila[7]), fila[8])
                    self.__lista.append(nv)
        archivo.close()
    
    def agregar(self):
        pos = input("seleccione a si quiere agregar un autobus o v si quiere agregar un van: ")
        if pos == "a":
            na = Autobuses(input("marca: "), input("modelo: "), int(input("ano de fabricacion: ")), int(input("capacidad de pasajeros: ")), int(input("numero de plazas: ")), float(input("distancia: ")), float(input("tarifa: ")), input("tipo de servicio: "), input("turno: "))
            self.__lista.append(na)
            self.guardarcsv(na)
        elif pos == "v":
            nv = Vanes(input("marca: "), input("modelo: "), int(input("ano de fabricacion: ")), int(input("capacidad de pasajeros: ")), int(input("numero de plazas: ")), float(input("distancia: ")), float(input("tarifa: ")), input("tipo de carroceria: "))
            self.__lista.append(nv)
            self.guardarcsv(nv)
    
    def guardarcsv(self, vehiculo):
        archivo = open("poo/unidad3/parcial t2 lp/archivoscsv/vehiculos.csv", "a", newline='')
        writer = csv.writer(archivo, delimiter=";")
        if isinstance(vehiculo, Autobuses):
            writer.writerow(["A", vehiculo.getMarca(), vehiculo.getModelo(), vehiculo.getAnoFabricacion(), vehiculo.getCapacidadPasajeros(), vehiculo.getNumeroPlazas(), vehiculo.getDistancia(), vehiculo.getTarifa(), vehiculo.getTipoServicio(), vehiculo.getTurno()])
        elif isinstance(vehiculo, Vanes):
            writer.writerow(["V", vehiculo.getMarca(), vehiculo.getModelo(), vehiculo.getAnoFabricacion(), vehiculo.getCapacidadPasajeros(), vehiculo.getNumeroPlazas(), vehiculo.getDistancia(), vehiculo.getTarifa(), vehiculo.getTipoCarroceria()])
        archivo.close()
    
    def mostrar(self):
        for vehiculo in self.__lista:
            print(vehiculo)
            
    def instancia(self):
        try:
            pos  = int(input("posicion: "))
        except ValueError:
            print("error")
            return
        
        if pos < len(self.__lista):
            if isinstance(self.__lista[pos], Autobuses):
                print(self.__lista[pos])
            elif isinstance(self.__lista[pos], Vanes):
                print(self.__lista[pos])
                
    def mostrar2(self):
        ca= 0
        cv=0
        for vehiculo in self.__lista:
            if isinstance(vehiculo, Autobuses):
                ca+=1
            elif isinstance(vehiculo, Vanes):
                cv+=1
        print(f"Autobuses: {ca}")
        print(f"Vanes: {cv}")
        
    def tarifa(self):
        for vehiculo in self.__lista:
            print(f"modelo: {vehiculo.getModelo()}, ano de fabricacion: {vehiculo.getAnoFabricacion()}, capacidad de pasajeros: {vehiculo.getCapacidadPasajeros()},  tarifa: {vehiculo.getTarifa()}")
    

                