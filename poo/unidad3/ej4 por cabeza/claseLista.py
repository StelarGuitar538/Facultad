from claseNodo import Nodo
from claseLibros import Libro
from claseCD import CD
from clasePublicaciones import Publi

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
 
    def instancia(self):
        posicion = int(input("ingrese posicion"))
        aux = self.__comienzo
        i=0
        
        while aux != None and i < posicion:
            aux = aux.getSig()
            i+=1
        if aux is None:
                print("posicion fuera de rango")
        else:
                publi = aux.getDato()
                if isinstance(publi, Libro):
                    print(f"La publicación en la posición {posicion} es un Libro.")
                elif isinstance(publi, CD):
                     print(f"La publicación en la posición {posicion} es un CD.")
                else:
                    print(f"La publicación en la posición {posicion} es de un tipo desconocido.")
                    
                    
    def cantPubli(self):
        cl =0
        ccd = 0
        aux = self.__comienzo
        
        while aux != None:
            publi = aux.getDato()
            if isinstance(publi, Libro):
                cl+=1
            elif isinstance(publi, CD):
                ccd +=1
            aux = aux.getSig()
        print(f"la cantidad de libros {cl} y cd {ccd}")
                           
    
    def mostrar2(self):
        aux = self.__comienzo
        while aux!= None:
            publi = aux.getDato()
            print (f"titulo {publi.getTitulo()}, categoria {publi.getCat()} importe de venta {publi.calcularImporte()}")
            aux = aux.getSig()