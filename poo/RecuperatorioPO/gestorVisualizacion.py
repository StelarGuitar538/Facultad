from claseVisualizacion import visualizacion
import csv
class Gestor_Visualizacion:
    __listavisualizacion=list
    def __init__(self):
        self.__listavisualizacion=[]
    def leerdatos(self):
        archivo=open('Visualizaciones.csv')
        reader=csv.reader(archivo,delimiter=';')
        for linea in reader:
            v=visualizacion(int(linea[0]),linea[1],linea[2],linea[3],int(linea[4]))
            v.mostrardatos()
            self.__listavisualizacion.append(v)
        archivo.close()
    def cantminutos(self,mail,id):
        cant=0
        for i in range(len(self.__listavisualizacion)):
            idv=self.__listavisualizacion[i].getidmiembro()
            if id==idv:
                cant=cant+self.__listavisualizacion[i].getmin()
        print(f"La cantidad de minutos que el usuario con mail {mail} vio fue: {cant}")