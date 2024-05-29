from nodo import Nodo
from libro import Libro
from cd import Cd

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
        pos = int(input("ingrese posicion: "))
        i=0
        aux = self.__comienzo
        
        while aux!= None and i< pos:
            aux = aux.getSig()
            i+=1
            
        if aux is None:
            print("posicion fuera de rango")
        else:
            publi = aux.getDato()
            if isinstance(publi, Libro):
                print(f"la posicion {pos} es un libro")
            elif isinstance(publi, Cd):
                print(f"la posicion {pos} es un cd")
            else:
                print(f"la posicion {pos} es desconocida")
                
    def contar(self):
        aux = self.__comienzo
        ccd = 0
        cli = 0
        while aux != None:
            publi = aux.getDato()
            if isinstance(publi, Libro):
                cli+=1
            elif isinstance(publi, Cd):
                ccd+=1
            aux = aux.getSig()
        print(f"cantidad de libros {cli}       cantidad de cds {ccd}")
        
    def mostrar2(self):
        aux = self.__comienzo
        while aux != None:
            publi = aux.getDato()
            print(f"titulo {publi.getTitulo()} categoria {publi.getCat()} importe de venta {publi.ImpVenta()}")
            aux = aux.getSig()