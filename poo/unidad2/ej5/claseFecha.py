class Fecha:
    __fechaDelPartido: int
    __identificadorDelEquipoLocal: int
    __identificadorDelEquipoVisitante: int
    __cantidadDeGolesLocal: int
    __cantidadDeGolesVisitante:int
    
    def __init__ (self, fp, idl, idv, cgl, cgv):
        self.__fechaDelPartido = fp
        self.__identificadorDelEquipoLocal = idl
        self.__identificadorDelEquipoVisitante = idv
        self.__cantidadDeGolesLocal = cgl
        self.__cantidadDeGolesVisitante = cgv
        
        
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