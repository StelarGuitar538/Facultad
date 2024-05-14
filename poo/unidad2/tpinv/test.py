#funcion test
from claseArreglo import Arreglo
from claseProductos import Productos

def test():
    a = Arreglo()
    p1 = Productos("azucar", 30)
    p2 = Productos("tortitas", 120)
    p3 = Productos("bananas", 70)
    a.agregar(p1)
    a.agregar(p2)
    a.agregar(p3)
    a.hacerCopia()
    a.obtenerVistaVentas()
    a.agregarVentas(p3)
    a.dividirInventario(2)
    a.encontrarValor(120)
    a.ordenarInventario()