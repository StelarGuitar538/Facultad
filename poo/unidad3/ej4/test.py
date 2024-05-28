from claseLista import Lista
from claseCD import CD
from clasePublicaciones import Publi
from claseLibros import Libro

def test():
    l = Lista()
    cd = CD(130, "pepito", "orgullo y prejuicio", "novela", 35000)
    li = Libro("pepito", "2019", 200, "orgullo y prejuicio", "novela", 35000)
    cd1 = CD(130, "juan", "los 3 chanchitos", "infantil", 10000)
    li1 = Libro("juan", "2010", 120, "los 3 chanchitos", "infantil", 10000)
    
    l.agregar(cd)
    l.agregar(li)
    l.agregar(cd1)
    l.agregar(li1)
    cd.mostrarCD()
    li.mostrarLi()
    cd1.mostrarCD()
    li1.mostrarLi()
    l.instancia()
    l.cantPubli()
    l.mostrar2()