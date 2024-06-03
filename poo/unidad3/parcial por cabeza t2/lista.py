from nodo import Nodo
from vehiculos import Vehiculos
from autobuses import Autobuses
from vanes import Vanes

class Lista:
    __comienzo: Nodo
    
    def __init__(self):
        self.__comienzo = None
        
    def agregar(self, v):
        nodo = Nodo(v)
        nodo.setSig(self.__comienzo)
        self.__comienzo = nodo
        
    def mostrarL(self):
        aux = self.__comienzo
        while aux != None:
            print(aux.getDato())
            aux = aux.getSig()
            
    def punto2(self):
        pos = int(input("ingrese posicion: "))
        i= 0
        aux= self.__comienzo
        
        while aux != None and i < pos:
            aux = aux.getSig()
            i+=1
        
        if aux is None:
            print("posicion fuera de rango")
        else:
            vehiculo = aux.getDato()
            if isinstance(vehiculo, Autobuses):
                print(f"la posicion {pos} es un autobus")
            elif isinstance(vehiculo, Vanes):
                print(f"la posicion {pos} es una van")
                    
                    
    def punto3(self):
        cv = 0
        ca = 0
        aux = self.__comienzo
        
        while aux != None:
            vehi = aux.getDato()
            if isinstance(vehi, Autobuses):
                ca +=1
            else:
                cv +=1
            aux = aux.getSig()
        print(f"la cantidad de autobeses es {ca} y de vanes es {cv}")
        
    def punto4(self):
        aux = self.__comienzo
        while aux != None:
            vehi = aux.getDato()
            print(f"{vehi.getModelo()} {vehi.getAnoFabri()} {vehi.getCapPas()} {vehi.tarifa()}")
            aux = aux.getSig()