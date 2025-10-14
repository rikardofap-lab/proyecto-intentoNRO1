from Persona import Persona
class Empleado(Persona):
    __fechaInicioContracto = ""
    __salario = 0
    __idEmpleado = 0 
    __idEstado = 0
    __nomEstado = ""

    def __init__(self):
        pass

    #         GETTERS Y SETTERS 


#------------------------------------------------------------
#   FECHA INICIO CONTRATO 
    def getfechaInicioContracto(self):
        return self.__fechaInicioContracto
    
    def setFechaInicioContrato(self, fechaInicioContrato):
        self.__fechaInicioContracto = fechaInicioContrato

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
#   NOMBRE ESTADO 
    def getNombreEstado(self):
        return self.__nomEstado
    
    def setNombreEstado(self, nombreEstado):
        self.__nomEstado = nombreEstado