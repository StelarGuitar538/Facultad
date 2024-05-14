from gestorclientes import gestorcliente
from gestormovimientos import gestormovimiento
from calculardimension import calcular


def test():
    dimension = (calcular())
    gc = gestorcliente()
    gm = gestormovimiento(dimension)
    gc.instanciar()
    gm.instanciar()
    x = int(input("ingrese accion: "))
    while x in[1,2,3]:
        if x == 1:
            dni = int(input("ingrese dni:"))
            salida = gc.actualizarsaldo(dni, gm)
            print(salida)
        if x == 2:
            numtar = int(input("ingrese numero de tarjeta:"))
            salida = gc.mostrarpornum(numtar, gm, dimension)
            print(salida)
        if x == 3:
            gc.ordenar()
        x = int(input("ingrese accion: "))
