from claseLista import Lista
from claseCD import CD
from clasePublicaciones import Publi
from claseLibros import Libro

def test():
    l = Lista()
    cd = CD(130, "pepito", "orgullo y prejuicio", "novela", 35000)
    li = Libro("pepito", "02/04/2019", 200, "orgullo y prejuicio", "novela", 35000)
    l.agregar(cd)
    l.agregar(li)
    cd.mostrarCD()
    li.mostrarLi()
    

    