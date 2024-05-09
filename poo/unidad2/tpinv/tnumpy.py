import numpy as np

class InventarioProductos:
    def __init__(self):
        self.__productosAlmacen = np.array([])
        self.__ventasDiarias = np.array([])

    # Función para hacer una copia del inventario de productos
    def hacerCopia(self):
        self.copiaInventario = np.copy(self.__productosAlmacen)

    # Función para obtener una vista de las ventas diarias
    def obtenerVistaVentas(self):
        # En NumPy, para obtener una vista se utiliza el slicing [:]
        self.vistaVentas = self.__ventasDiarias[:]

    # Función para agregar las ventas diarias al inventario
    def agregarVentas(self, ventas):
        # Se debe pasar un arreglo de ventas como argumento para agregarlo
        self.juntarVentas = np.concatenate((self.__productosAlmacen, ventas))

    # Función para dividir el inventario en partes
    def dividirInventario(self, num_partes):
        # Se debe pasar el número de partes como argumento
        self.dividirInventario = np.array_split(self.__productosAlmacen, num_partes)

    # Función para encontrar la posición de un valor específico en las ventas
    def encontrarValor(self, valor):
        # Se debe pasar el valor específico como argumento para buscarlo
        self.dondeEncontrar = np.where(self.__ventasDiarias == valor)

    # Función para ordenar el inventario de productos
    def ordenarInventario(self):
        self.ordenarInventario = np.sort(self.__productosAlmacen)
