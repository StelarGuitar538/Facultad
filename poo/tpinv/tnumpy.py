import numpy as np

class InventarioProductos:
    def __init__(self):
        #Lista de cantidades de productos en almacén
        self.productosAlmacen = np.array([234, 452, 567, 823, 900])
        
        #Lista de ventas diarias de un producto durante una semana
        self.ventasDiarias = np.array([22, 15, 54, 70, 15, 34, 49, 15])
        self.copiaInventario = None
        self.vistaVentas = None
        self.juntarVentas = None
        self.dividirInventario = None
        self.dondeEncontrar = None
        self.ordenarInventario = None

    # Función para hacer una copia del inventario de productos
    def hacer_copia(self):
        self.copiaInventario = np.copy(self.productos_en_almacen)

    # Función para obtener una vista de las ventas diarias
    def obtener_vista_ventas(self):
        self.vistaVentas = np.view(self.ventas_diarias)

    # Función para agregar las ventas diarias al inventario
    def agregar_ventas(self):
        self.juntarVentas = np.concatenate((self.productos_en_almacen, self.ventas_diarias))

    # Función para dividir el inventario en partes
    def dividir_inventario(self):
        self.dividirInventario = np.split(self.productos_en_almacen, 3)

    # Función para encontrar la posición de un valor específico en las ventas
    def donde_encontrar_valor(self):
        self.dondeEncontrar = np.where(self.ventas_diarias == 15)

    # Función para ordenar el inventario de productos
    def ordenar_inventario(self):
        self.ordenarInventario = np.sort(self.productos_en_almacen)
