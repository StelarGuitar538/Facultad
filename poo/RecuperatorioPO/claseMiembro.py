class miembro:
    __idnum=int
    __ayn=str
    __correo=str
    def __init__(self,idnum,ayn,correo):
        self.__idnum=idnum
        self.__ayn=ayn
        self.__correo=correo
    def getidnum(self):
        return self.__idnum
    def getayn(self):
        return self.__ayn
    def getcorreo(self):
        return self.__correo
    def mostrardatos(self):
        print('{},{},{}'.format(self.__idnum,self.__ayn,self.__correo))