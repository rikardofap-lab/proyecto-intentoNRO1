class persona():
    __rut = ""
    __nombres = ""
    __apellidoPaterno = ""
    __apellidoMaterno = ""
    __direccion = ""
    __nroTelefono = ""
    __email = ""
    __fechaNacimiento = ""


    def __init__ (self):
        pass
    
#         GETTERS Y SETTERS

#------------------------------------------------------------
#   RUT
    def getRut(self):
        return self.__rut
    
    def setRut(self, rut):
        self.__rut = rut

#------------------------------------------------------------
#   NOMBRES 
    def getNombres(self):
        return self.__nombres
    
    def setNombres(self, nombres):
        self.__nombres = nombres

#------------------------------------------------------------
#   APELLIDO PATERNO 
    def getApellidoPaterno(self):
        return self.__apellidoPaterno
    
    def setApellidoPaterno(self, apellidoPaterno):
        self.__apellidoPaterno = apellidoPaterno

#------------------------------------------------------------
#   APELLIDO MATERNO 
    def getApellidoMaterno(self):
        return self.__apellidoMaterno
    
    def setApellidoMaterno (self, apellidoMaterno):
        self.__apellidoMaterno = apellidoMaterno

#------------------------------------------------------------
#   DIRECCION 
    def getDireccion(self):
        return self.__direccion
    
    def setDireccion(self, direccion):
        self.__direccion = direccion

#------------------------------------------------------------
#   NRO TELEFONO 
    def getNroTelefono(self):
        return self.__nroTelefono
    
    def setNroTelefono(self, nroTelefono):
        self.__nroTelefono = nroTelefono

#------------------------------------------------------------
#   EMAIL
    def getEmail(self):
        return self.__email 
    
    def setEmail(self, email):
        self.__email = email
#------------------------------------------------------------
#   FECHA NACIMIENTO
    def getFechaNacimiento(self):
        return self.__fechaNacimiento
    
    def setFechaNacimiento(self, fechaNacimiento):
        self.__fechaNacimiento = fechaNacimiento