from Empleado import Empleado

class Usuario(Empleado):
    __idUsuario = 0
    __nombreUsuario = ""
    __contrasena = ""

    def __init__ (self):
        pass

#       GETTERS Y SETTERS

#------------------------------------------------------------
#   ID USUARIO
    def getIdUsuario(self):
        return self.__idUsuario
    def setIdUsuario(self, idUsuario):
        self.__idUsuario = idUsuario

#------------------------------------------------------------
#   NOMBRE USUARIO
    def getNombreUsuario(self):
        return self.__nombreUsuario
    def setNombreUsuario(self, nombreUsuario):
        self.__nombreUsuario = nombreUsuario

#------------------------------------------------------------
#   CONTRASENA
    def getContrasena(self):
        return self.__contrasena
    def setContrasena(self, contrasena):
        self.__contrasena = contrasena