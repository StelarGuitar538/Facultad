from poo.unidad3.ej1.claseDepartamentos import Dptos

class Edificio:
    __id: int
    __nombre: str
    __dir: str
    __nomEmp: str
    __cantPisos: int
    __cantDeps: int
    __departamentos: list
    
    def __init__(self, id, nom, dir, nomEmp, cantPisos, cantDeps):
        self.__id = id
        self.__nombre = nom
        self.__dir = dir
        self.__nomEmp = nomEmp
        self.__cantPisos = cantPisos
        self.__cantDeps = cantDeps
       
        idDpto = Dptos.getid()
        nya = Dptos.getnya()
        npiso = Dptos.getNpiso()
        ndep = Dptos.getNdep()
        chab = Dptos.getHab()
        cba = Dptos.getBa()
        supCub = Dptos.getSupCub()

        self.__departamentos = Dptos()
  
        def __del__ (self):
            print("borrando edificio")
            del self.__departamentos
            
        
        