class tipoAcceso:
    __idTipoAcc = 0
    __nomTipoAcc = ""

    def __init__ (self):
        pass

    #         GETTERS Y SETTERS

#------------------------------------------------------------
#   ID TIPO DE ACCCESO
    def getIdTipoAcc(self):
        return self.__idTipoAcc
    
    def setIdTipoAcc(self, idTipoACC):
        self.__idTipoAcc = idTipoACC

#------------------------------------------------------------
#   NOMBRE TIPO DE ACCESO
    def getNomTipoAcc(self):
        return self.__nomTipoAcc
    
    def setNomTipoAcc(self, nomTipoAcc):
        self.__nomTipoAcc = nomTipoAcc
