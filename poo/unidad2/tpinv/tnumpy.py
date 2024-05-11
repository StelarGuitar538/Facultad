import numpy as np

class InventarioProductos:
    def __init__(self):
        self.__productosAlmacen = np.array([])
        self.__ventasDiarias = np.array([])



# Crear una instancia de la clase InventarioProductos
inventario = InventarioProductos()

# Ejemplo de uso de los métodos de la instancia
inventario.hacerCopia()
inventario.obtenerVistaVentas()
inventario.agregarVentas(np.array([100, 200, 300]))
inventario.dividirInventario(3)
inventario.encontrarValor(200)
inventario.ordenarInventario()
