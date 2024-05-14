class cliente:
    def __init__(self, nombre, apellido, dni, numtar, saldoanterior):
        self.__nombre = str(nombre)
        self.__apellido = str(apellido)
        self.__dni = int(dni)
        self.__numtar = int(numtar)
        self.__saldoanterior = float(saldoanterior)

    def getdni(self):
        return(self.__dni)
    
    def getnom(self):
        return(self.__nombre)
    
    def getapellido(self):
        return(self.__apellido)
    def getTarjeta(self):
        return self.__numtar
    def getSaldo(self):
        return self.__saldoanterior
    def setsaldo(self,saldo):
        self.__saldoanterior=saldo
    def saldonuevo(self, gm):
        movimientos = ""
        saldoanterior = self.__saldoanterior
        for movimiento in gm:
            if movimiento.getnumtar() == self.__numtar:
                accion = str(movimiento.getdescripcion())
                print(f"{accion}")
                if accion in ["Compra en Comercio", "Compra en Carniceria", "Compra en Supermercado", "Compra en Farmacia", "Compra en Zapateria", "Compra en Almacen", "Compra en Libreria"]:
                    self.__saldoanterior  += movimiento.getimporte()
                elif accion == "Pago de Saldo":
                    self.__saldoanterior -= movimiento.getimporte()
                movimientos += str(f"fecha: {movimiento.getfecha()} importe: {movimiento.getimporte()} tipo de movimiento: {movimiento.gettipomov()}\n")
        salida = (f"cliente:{self.__apellido} {self.__nombre} numero de tarjeta: {self.__numtar}\n saldoanterior: {saldoanterior}\n movimientos:\n {movimientos}\n saldo actual: {self.__saldoanterior}")
        return(salida)
    
    def __lt__(self, otro):
        return(self.__numtar < otro.__numtar)