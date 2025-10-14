from Empleado import Empleado
from TipoAcceso import TipoAcceso

class Usuario(Empleado):
    __idUsuario = 0
    __contrasena = ""
    __tipAcc = TipoAcceso()
    __idEstado = 0
    __nomEstado = ""

    def __init__ (self):
        pass

#       GETTERS Y SETTERS

#------------------------------------------------------------
#   ID USUARIO
    def getIdUsuario(self):
        return self.__idUsuario
    
    def setIdUsuario(self, idUsuario):
        self.idUsuario = idUsuario

#------------------------------------------------------------
#   CONTRASENA
    def getContrasena(self):
        return self.__contrasena
    
    def setContrasena(self, contrasena):
        self.contrasena = contrasena

#------------------------------------------------------------
#   TIPO ACCESO
    def getTipoacc(self):
        return self.__tipAcc
    
    def setTipAcc(self, tipAcc):
        self.__tipAcc = tipAcc
#------------------------------------------------------------
#   ID ESTADO 
    def getIdEstado(self):
        return self.__idEstado
    
    def setIdEstado(self, idEstado):
        self.__idEstado = idEstado
    
#------------------------------------------------------------
#   NOMBRE ESTADO 
    def getNombreEstado(self):
        return self.__nomEstado
    
    def setNombreEstado(self, nombreEstado):
        self.__nomEstado = nombreEstado