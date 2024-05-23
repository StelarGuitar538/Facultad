from claseNodo import Nodo

class Lista:
    __comienzo: Nodo
    
    def __init__(self):
        self.__comienzo = None
        
    def agregar(self, publi):
        nodo = Nodo(publi)
        nodo.setSig(self.__comienzo)
        self.__comienzo = nodo
        
    def mostrar(self):
        aux = self.__comienzo
        while aux != None:
            print(aux.getDato())
            aux = aux.getSig()
     