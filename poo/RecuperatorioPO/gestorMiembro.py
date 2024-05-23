from claseMiembro import miembro
import numpy as np
import csv
class gestor_miembro:
    __arregloMiembro= np.ndarray
    __cantidad=int
    __dimension=int
    __incremento=int
    def __init__(self):
        self.__cantidad=0
        self.__incremento=1
        self.__dimension=0
        self.__arregloMiembro=np.empty(self.__dimension,dtype=miembro)
    def agregarmiem(self,miem):
        if self.__cantidad==self.__dimension:
            self.__dimension += self.__incremento
            self.__arregloMiembro.resize(self.__dimension)
        self.__arregloMiembro[self.__cantidad]=miem
        self.__cantidad +=1
    def leerdatos(self):
        archivo=open('miembros.csv')
        reader=csv.reader (archivo,delimiter=";")
        for linea in reader:
            m=miembro(int(linea[0]),str(linea[1]),str(linea[2]))
            m.mostrardatos()
            self.agregarmiem(m)
        archivo.close()
    def buscarid(self,mail,gv):
        ban=True
        i=0
        id=int
        while ban==True and i<len(self.__arregloMiembro):
            correomiembro=self.__arregloMiembro[i].getcorreo()
            if correomiembro==mail:
                ban=False
                id=self.__arregloMiembro[i].getidnum()
                gv.cantminutos(mail,id)
            else:
                i=i+1
        if ban==True:
            print("Mail no encontrado")
    def visusimul(self):
        for i in range(len(self.__arregloMiembro)):
            for j in range (i+1,len(self.__arregloMiembro)):
                if self.__arregloMiembro[i]==self.__arregloMiembro[j]:
                    print(f"apellido y nombre: {self.__arregloMiembro[i].getayn()} correo: {self.__arregloMiembro[i].getcorreo()}")