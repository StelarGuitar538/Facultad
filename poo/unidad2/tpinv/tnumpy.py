import numpy as np

class InventarioProductos:
    def __init__(self):
        self.__productosAlmacen = np.array([])
        self.__ventasDiarias = np.array([])

    def hacerCopia(self):
        self.copiaInventario = np.copy(self.__productosAlmacen)

    def obtenerVistaVentas(self):
        self.vistaVentas = self.__ventasDiarias[:]

    def agregarVentas(self, ventas):
        self.juntarVentas = np.concatenate((self.__productosAlmacen, ventas))

    def dividirInventario(self, num_partes):
        self.dividirInventario = np.array_split(self.__productosAlmacen, num_partes)

    def encontrarValor(self, valor):
        self.dondeEncontrar = np.where(self.__ventasDiarias == valor)

    def ordenarInventario(self):
        self.ordenarInventario = np.sort(self.__productosAlmacen)

# Crear una instancia de la clase InventarioProductos
inventario = InventarioProductos()

# Ejemplo de uso de los métodos de la instancia
inventario.hacerCopia()
inventario.obtenerVistaVentas()
inventario.agregarVentas(np.array([100, 200, 300]))
inventario.dividirInventario(3)
inventario.encontrarValor(200)
inventario.ordenarInventario()
