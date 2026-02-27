class proyecto:
    __idProyecto = 0
    __nomProyecto = ""
    __descripcion = ""
    __fechaInicio = ""
    __empleadosAsignados = [] # Debería ser una lista para almacenar varios empleados
    __idEstado = 0
    __nomEstado = ""

    def __init__(self):
        self.__empleadosAsignados = [] # Inicializamos la lista en el constructor

        #       GETTERS Y SETTERS

#------------------------------------------------------------
#   ID PROYECTO
    def getIdProyecto(self):
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
        return self.__empleadosAsignados
    
    def setEmpleAsignados(self, empleAsignados):
        self.__empleadosAsignados = empleAsignados
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