from Empleado import Empleado

class Proyecto:
    __idProyecto = 0
    __nomProyecto = ""
    __descripcion = ""
    __fechaInicio = ""
    __emple = Empleado()
    __idEstado = 0
    __nomEstado = ""

    def __init__(self):
        pass

        #       GETTERS Y SETTERS

#------------------------------------------------------------
#   ID PROYECTO
    def getIdPryecto(self):
        return self.__idProyecto
    
    def setIdProyecto (self, idProyecto):
        self.__idProyecto = idProyecto

#------------------------------------------------------------
#   NOMBRE PROYECTO
    def getNomProyecto(self):
        return self.__nomProyecto
    
    def setNomProyecto(self, nomProyecto):
        self.__nomProyecto = nomProyecto

#------------------------------------------------------------
#   DESCRIPCION
    def getDescripcion(self):
        return self.__descripcion
    
    def setDescripcion(self, descripcion):
        self.__descripcion = descripcion

#------------------------------------------------------------
#   FECHA INICIO
    def getFechaInicio(self):
        return self.__fechaInicio
    
    def setFechaInicio(self, fechaInicio):
        self.__fechaInicio = fechaInicio

#------------------------------------------------------------
#   EMPLEADOS ASIGNADOS
    def getEmpleAsignados(self):
        return self.__empleAsignados
    
    def setEmpleAsignados(self, empleAsignados):
        self.__empleAsignados = empleAsignados
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