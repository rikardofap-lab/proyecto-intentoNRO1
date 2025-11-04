from Persona import persona


class empleado(persona):
    __fechaInicioContrato = ""
    __salario = 0
    __idEmpleado = 0 
    __idEstado = 0
    __idTipoAcc = 0
    __idProyecto = None  # Corresponde a id_pro en la BD (puede ser NULL)
    __nombreUsuario = None
    __contrasena = None


    def __init__(self):
        pass

    #         GETTERS Y SETTERS 

#------------------------------------------------------------
#   FECHA INICIO CONTRATO 
    def getfechaInicioContrato(self):
        return self.__fechaInicioContrato
    
    def setFechaInicioContrato(self, fechaInicioContrato):
        self.__fechaInicioContrato = fechaInicioContrato

#------------------------------------------------------------
#   SALARIO 
    def getSalario(self):
        return self.__salario
    def setSalario(self, salario):
        self.__salario = salario

#------------------------------------------------------------
#   ID EMPLEADO 
    def getIdEmpleado(self):
        return self.__idEmpleado
    
    def setIdEmpleado(self, idEmpleado):
        self.__idEmpleado = idEmpleado

#------------------------------------------------------------
#   ID ESTADO 
    def getIdEstado(self):
        return self.__idEstado
    
    def setIdEstado(self, idEstado):
        self.__idEstado = idEstado
    
#------------------------------------------------------------
#   ID TIPO DE ACCESO (INT)
    def getIdTipoAcc(self):
        return self.__idTipoAcc
    
    def setIdTipoAcc(self, idTipoAcc):
        self.__idTipoAcc = idTipoAcc

#------------------------------------------------------------
#   ID PROYECTO (INT o None)
    def getIdProyecto(self):
        return self.__idProyecto
    
    def setIdProyecto(self, idProyecto):
        self.__idProyecto = idProyecto

#------------------------------------------------------------
#   NOMBRE DE USUARIO (STRING o None)
    def getNombreUsuario(self):
        return self.__nombreUsuario
    
    def setNombreUsuario(self, nombreUsuario):
        self.__nombreUsuario = nombreUsuario

#------------------------------------------------------------
#   CONTRASEÑA (STRING/BYTES o None)
    def getContrasena(self):
        return self.__contrasena
    
    def setContrasena(self, contrasena):
        self.__contrasena = contrasena