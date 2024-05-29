from lista import Lista
from cd import Cd
from libro import Libro
from publi import Publi


def test():
    l = Lista()
    li = Libro("veloz", "2005", 300, "la vaca lola", "infantil", 12000)
    li1 = Libro("killer", "2010", 250, "la gorda killer", "novela", 10000)
    cd = Cd(130, "pepito", "orgullo y prejuicio", "novela", 35000)
    cd1 = Cd(200, "juan", "los 3 chanchitos", "infantil", 10000)
    
    continuar = True
    
    while continuar:
        print("0, carga")
        print("1, punto a")
        print("2, punto b")
        print("3, punto c")
        print("4, finalizar")
        
        op = input("ingrese opcion: ")
        
        if op == "0":
            l.agregar(li)
            l.agregar(li1)
            l.agregar(cd)
            l.agregar(cd1)
            li.mostrar()
            li1.mostrar()
            cd.mostrar()
            cd1.mostrar()
        
        elif op == "1":
            l.instancia()
        
        elif op == "2":
            l.contar()
            
        elif op == "3":
            l.mostrar2()
         
        elif op == "4":
            continuar = False


if __name__ == "__main__":
    test()