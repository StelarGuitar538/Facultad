from publi import Publi

class Libro(Publi):
    __autor: str
    __fecha: int
    __paginas: int
    
    def __init__(self, a, f, pa, t, c, pre):
        super().__init__(t, c, pre)
        self.__autor = a
        self.__fecha = f
        self.__paginas = pa
        
    def mostrar(self):
        print(f"{self.__autor} {self.__fecha} {self.__paginas} {self.getTitulo()} {self.getCat()} {self.getPrecio()}")
        
    
    
    def ImpVenta(self):
        diferencia= 2024 - int(self.__fecha)
        return  (diferencia / 100) * self.getPrecio()
        