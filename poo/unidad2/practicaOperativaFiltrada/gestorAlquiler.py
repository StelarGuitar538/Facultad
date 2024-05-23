from claseAlquiler import Alquiler
import csv

class gesAlquiler:
    __lista : list
    
    def __init__ (self):
        self.__lista = []
        
    def inicializar(self):
        archivo = open("poo/unidad2/practicaOperativaFiltrada/archivoscsv/Alquiler.csv", "r")
        reader = csv.reader(archivo,delimiter=";")
        for fila in reader:
            nAlquiler = Alquiler((fila[0]), (fila[1]), (fila[2]), (fila[3]), int(fila[4]))
            self.__lista.append(nAlquiler)
        archivo.close()
        
    def mostar(self):
        for alquiler in self.__lista:
            print(alquiler)
            
    def ordenar(self):
        self.__lista.sort()
    
    def listado(self, c):
        print("hora  id de la cancha  duracion alquiler  importe por hora  importe alquiler")
        total = 0
        
        for alquiler in self.__lista:
            hora = alquiler.getHora()
            id1 = alquiler.getId()
            duracion = alquiler.getDuracion() / 60
            impHora = c.impHora(id1)
            impAlquiler = impHora * duracion
            
            print(f"{hora} {id1}   {duracion}  {impHora}   {impAlquiler}")
            total += impAlquiler
        print(f"total recaudado {total}")
     
     
    def buscarId(self, idc):
        tm = 0
        for i in self.__lista:
            if i.getId() == idc:
                tm += i.getMin()
        print(f"el total de minutos que estuvo alquilada la cancha {idc} son {tm}")