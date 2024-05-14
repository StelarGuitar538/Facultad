class Fecha:
    __fechaDelPartido: str
    __identificadorDelEquipoLocal: str
    __identificadorDelEquipoVisitante: str
    __cantidadDeGolesLocal: int
    __cantidadDeGolesVisitante:int
    
    def __init__ (self, fp, idl, idv, cgl, cgv):
        self.__fechaDelPartido = fp
        self.__identificadorDelEquipoLocal = idl
        self.__identificadorDelEquipoVisitante = idv
        self.__cantidadDeGolesLocal = cgl
        self.__cantidadDeGolesVisitante = cgv
        
    def __str__(self):
         return f"{self.__fechaDelPartido}-{self.__identificadorDelEquipoLocal}-{self.__identificadorDelEquipoVisitante}-{self.__cantidadDeGolesLocal}-{self.__cantidadDeGolesVisitante}"
    
    def getFechaPartido(self):
            return(self.__fechaDelPartido)
    
    def getidl(self):
        return(self.__identificadorDelEquipoLocal)
    
    def getidv(self):
        return(self.__identificadorDelEquipoVisitante)
    
    def getcantgl(self):
        return(self.__cantidadDeGolesLocal)
    
    def getcantgv(self):
        return(self.__cantidadDeGolesVisitante)