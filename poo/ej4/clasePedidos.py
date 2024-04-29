class Pedidos:
    def __init__ (self, patenteMoto, id, comidasPedidas, tiempoDeEntregaEstimado, tiempoDeEntregaReal, precio):
        self.patenteMoto = patenteMoto
        self.id = id
        self.comidasPedidas = comidasPedidas
        self.tiempoDeEntregaEstimado = tiempoDeEntregaEstimado
        self.tiempoDeEntregaReal = tiempoDeEntregaReal
        self.precio = precio