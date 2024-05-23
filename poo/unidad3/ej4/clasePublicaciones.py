class Publi:
    __titulo: str
    __categoria: str
    __precio: float 

    def __init__(self, t, c, p):
        self.__titulo = t
        self.__categoria = c
        self.__precio = p
        
    def mostrarPubli(self):
        print(f"{self.__titulo} {self.__categoria} {self.__precio}")
        
    def getTitulo(self):
        return self.__titulo 
    
    def getCat(self):
        return self.__categoria
    
    def getPrecio(self):
        return self.__precio
    
    