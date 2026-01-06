from Empleado import empleado
from Proyecto import proyecto
from TipoAcceso import tipoAcceso
from DAO import dao
from prettytable import PrettyTable
from datetime import date
from os import system
import os

class funciones:
    dao = dao()

    def __init__(self):
        pass
#-------------------------------------------------------------------------------------------

    def menuInicial(self):
        while True:
            try:
                system("cls")
                print("-------------------------")
                print("------ MENU INICIAL------")
                print("-------------------------")
                print("\n1.- INICIAR SESION")
                print("\nTEMPORALMENTE SIN INICIO DE SESION")
                print("1.- MENU GERENTE")
                print("2.- MENU GESTION DE PROYECTOS")
                print("3.- MENU ASIGNACION DE EMPLEADOS")
                print("4.- SALIR")

                op = int(input("\nDigite una opción: "))
                if op > 0 or op <= 4:
                #if op == 1:
                    #self.__iniciarSesion()
                    if op == 1:
                        self.__menuGerente()
                    elif op == 2:
                        self.__menuGestionProyectos()
                    elif op == 3:
                        self.__asignacionProyectos()
                    elif op == 4:
                        system("cls")
                        print("¡Gracias por usar el programa!")
                        print("¡Hasta Pronto!", end="\n\n")
                        system("pause")
                        self.salir()
                    else:
                        print("\n--- Error De Opcion De Menú Inicial!! Solo Puede Seleccionar Entre 1 y 2---", end="\n\n")
                        system("pause")
                        continue                      
            except ValueError:
                    print("\n¡ERROR! LA OPCION DEBE INGRESARSE SOLO CON NUMEROS (1, 2 Y 3)")
                    system("pause")
                    continue
            except Exception as e:
                print(f"\n¡Error Al Capturar Opcion De Menú Inicial!!{e}", end="\n\n")
                system("pause")
                continue

#-------------------------------------------------------------------------------------------

    def __menuGerente(self):

        while True:
            try:
                system("cls")
                print("--------------------------")
                print("------ MENU GERENTE ------")
                print("--------------------------")
                print("\n1.- CREAR EMPLEADO")
                print("2.- LISTAR EMPLEADOS")
                print("3.- BUSCAR EMPLEADO")
                print("4.- MODIFICAR EMPLEADO")
                print("5.- ELIMINAR EMPLEADO")
                print("6.- ESTADISTICAS EMPLEADOS")
                print("7.- VOLVER")

                op = int(input("\nDigite una opción: "))

                if op > 0 or op <= 7:
                    if op == 1:
                        self.__crearEmpleado()
                    elif op == 2:
                        self.__listarEmpleados()
                    elif op == 3:
                        self.__buscarEmpleado()
                    elif op == 4:
                        self.__modificarEmpleado()
                    elif op == 5:
                        self.__eliminarEmpleado()
                    elif op == 6:
                        self.__estadisticasEmpleados()
                    elif op == 7:
                        self.menuInicial()
                    else:
                        print("\n--- Error De Opcion De Menú Gerente!! ---", end="\n\n")
                        system("pause")
                        continue
            except ValueError:
                print("\n¡ERROR! La opcion solo puede ser un numero entero positivo")
                system("pause")
                continue
            except Exception as e:
                print(f"\n¡Error Al Capturar Opcion De Menú Gerente!!{e}", end="\n\n")
                system("pause")
                continue

#-------------------------------------------------------------------------------------------
    def __menuGestionProyectos(self):
        while True:
            try:        
                system("cls")
                print("--------------------------------------")
                print("--- MENU GESTION DE PROYECTOS ---")
                print("--------------------------------------")
                print("\n1.- CREAR PROYECTO")
                print("2.- LISTAR PROYECTOS")
                print("3.- BUSCAR PROYECTO")
                print("4.- MODIFICAR PROYECTO")
                print("5.- ELIMINAR PROYECTO")
                print("6.- ESTADISTICAS PROYECTOS")
                print("7.- VOLVER")

                op = int(input("\nDigite una opción: "))

                if op > 0 or op <= 6:
                    if op == 1:
                        self.__crearProyecto()
                    elif op == 2:
                        self.__listarProyectos()
                    elif op == 3:
                        self.__buscarProyecto()
                    elif op == 4:
                        self.__modificarProyecto()
                    elif op == 5:
                        self.__eliminarProyecto()
                    elif op == 6:
                        self.__estadisticasProyectos()            
                    elif op == 7:
                        self.menuInicial()
                    else:
                        print("\n--- Error De Opcion De Menú Gestion Proyectos!! ---", end="\n\n")
            except ValueError:
                print("\n¡ERROR! La opcion solo puede ser un numero entero positivo")
                system("pause")
                continue
            except Exception as e:
                print(f"\n¡Error Al Capturar Opcion De Menú Gestion Proyectos!!{e}", end="\n\n")
                system("pause")
                continue

#-----------------------------------------------------------------------------------------------
    def __iniciarSesion(self):
        while True:
            try:
                system("cls")
                print("--- MENU INICIAL (INICIO DE SESIÓN) ---")
                rut = input("\nIngrese su rut: ")
                if len(rut.strip().isdigit()) > 12 or len(rut.strip().isdigit()) < 10:
                    print("\n--- El Rut Debe Tener Entre 10 y 12 Caracteres!! ---", end="\n\n")
                    system("pause")
                    continue
                else:
                    break
            except ValueError:
                print("\nEl rut debe ser escrito solo con numeros y guion")
                system("pause")
                continue
            except Exception as e:
                print(f"\n--- Error Al Capturar Rut (Login)!! --- {e}", end="\n\n")
                system("pause")
                continue
        #-----------------------------------------------------------------------------------------
        while True:
            try:
                system("cls")
                print("--- MENU INICIAL (INICIO DE SESIÓN) ---")
                contrasena = input("\nIngrese su contraseña: ")
                if len(contrasena.strip()) > 1 or len(contrasena.strip()) < 20:
                    print("\n--- La Contraseña Debe Tener Entre 1 y 20 Caracteres!! ---", end="\n\n")
                    system("pause")
                    continue
                else:
                    break
            except Exception as e:
                print(f"\n--- Error Al Capturar Contraseña (Login)!! --- {e}", end="\n\n")
                system("pause")
                continue

    def __asignacionProyectos(self):
        while True:
            try:
                system("cls")
                print("------------------------------------")
                print("--- MENU ASIGNACION DE EMPLEADOS ---")
                print("------------------------------------")
                print("\n1.- ASIGNAR EMPLEADO A PROYECTO")
                print("2.- REASIGNAR EMPLEADO")
                print("3.- LISTAR EMPLEADOS ASIGNADOS")
                print("4.- LISTAR EMPLEADOS SIN ASIGNADOS")
                print("5.- VOLVER")

                op = int(input("\nDigite una opción: "))

                if op > 0 or op <= 5:
                    if op == 1:
                        self.__asignarEmpleado()
                    elif op == 2:
                        self.__reasignarEmpleado()
                    elif op == 3:
                        self.__listarEmpleadosAsignados()
                    elif op == 4:
                        self.__listarEmpleadosSinAsignar()
                    elif op == 5:
                        self.menuInicial()
                    else:
                        print("\n--- Error De Opcion De Menú Asignación Proyectos!! ---", end="\n\n")
                        system("pause")
                        continue
            except ValueError:
                print("\n¡ERROR! La opcion solo puede ser un numero entero positivo")
                system("pause")
                continue
            except Exception as e:
                print(f"\n¡Error Al Capturar Opcion De Menú Asignación Proyectos!!{e}", end="\n\n")
                system("pause")
                continue

#-------------------------------------------------------------------------------------------
    def salir(self):
        system("cls")
        os._exit(1)

#-------------------------------------------------------------------------------------------
#   FUNCIONES MENU GERENTE
    def __crearEmpleado(self):
        # Creamos una instancia LOCAL para este nuevo empleado.
        nuevo_empleado = empleado()

        # RUT ------------------------------------------------------------------------------
        while True:
            try:
                system("cls")
                print("----------------------------")
                print("--- CREAR EMPLEADO (RUT) ---")
                print("----------------------------")
                print("¿Estás seguro de crear un nuevo empleado?")
                print("1. Si")
                print("2. No")
                op = int(input("\nDigite una opción: "))
                if op == 2:
                    self.menuInicial()
                    return
                elif op == 1:
                    system("cls")
                    rut_formateado = self.__obtener_rut_validado(titulo_menu="CREAR EMPLEADO (RUT)")
                    if self.dao.comprobarRutEmpleado(rut_formateado) is not None:
                        print(f"\n---ERROR! El rut {rut_formateado} ya está registrado en la base de datos---", end="\n\n")
                        system("pause")
                        continue
                    else:
                        print(f"RUT {rut_formateado} registrado correctamente", end="\n\n")
                        system("pause")
                        break                  
            except Exception as e:
                print(f"\n¡ERROR! Al ingresar el rut del empleado: {e}", end="\n\n")

        # NOMBRE ---------------------------------------------------------------------------
        while True:
            try:
                system("cls")
                print("-------------------------------")
                print("--- CREAR EMPLEADO (NOMBRE) ---")
                print("-------------------------------")
                nombre_s = input("\nIngrese nombre de empleado: ")
                if nombre_s.isalpha() and len(nombre_s.strip()) >= 2 and len(nombre_s.strip()) <= 20:
                    nombre = nombre_s.capitalize()
                    print("\nNombre guardado correctamente:", nombre)
                    system("pause")
                    break
                else:
                    print("\nEl nombre debe tener entre 2 y 20 caracteres")
                    system("pause")
                    continue
            except Exception as e:
                print(f"\n¡ERROR! Al ingresar el nombre del empleado: {e}", end="\n\n")
                system("pause")
                continue

        # APELLIDO PATERNO ------------------------------------------------------------------
        app_paterno = self.__obtener_apellido("Apellido Paterno")


        # APELLIDO MATERNO ------------------------------------------------------------------
        app_materno = self.__obtener_apellido("Apellido Materno")
        
        # SEXO EMPLEADO ---------------------------------------------------------------------------
        while True:
            try:
                system("cls")
                print("-----------------------------")
                print("--- CREAR EMPLEADO (SEXO) ---")
                print("-----------------------------")
                sexo = int(input("\nIngrese sexo del empleado (1 MASCULINO, 2 FEMENINO, 3 OTRO): "))
                if 0 < sexo <= 3:
                    print("\nSexo guardado correctamente:", sexo)
                    system("pause")
                    break
                else:
                    print("\nEl sexo debe ser entre 1 y 3")
                    system("pause")
                    continue
            except ValueError:
                print("\n¡ERROR! El sexo debe ser escrito solo con numeros")
                system("pause")


        # DIRECCION ------------------------------------------------------------------------
        while True:
            try:
                system("cls")
                print("----------------------------------")
                print("--- CREAR EMPLEADO (DIRECCION) ---")
                print("----------------------------------")
                direccion_s = input("\nIngrese direccion del empleado: ")
                if len(direccion_s.strip()) >= 2 and len(direccion_s.strip()) <= 60:
                    direccion = direccion_s.capitalize()
                    print("\nDirección guardada correctamente:", direccion)
                    system("pause")
                    break
                else:
                    print("\nLa direccion debe tener entre 2 y 60 caracteres")
                    system("pause")
                    continue
            except Exception as e:
                print(f"\n¡ERROR! Al ingresar la direccion del empleado: {e}", end="\n\n")
                system("pause")
                continue
 
        # NRO TELEFONO --------------------------------------------------------------------------------
        while True:
            try:
                system("cls")
                print("---------------------------------")
                print("--- CREAR EMPLEADO (TELEFONO) ---")
                print("---------------------------------")

                nroTelefono = input("\nIngrese número de teléfono del empleado (9 dígitos) (SIN +56): ")

                if nroTelefono.isdigit() and len(nroTelefono) == 9:
                    nroTelefono = "+56" + nroTelefono
                    print("\nNúmero guardado correctamente:", nroTelefono)
                    system("pause")
                    break
                else:
                    print("\nERROR: El número debe tener exactamente 9 dígitos y solo contener números.")
                    system("pause")
                    continue

            except ValueError:
                print("\n¡ERROR! El numero de telefono debe ser escrito solo con numeros")
                system("pause")
                continue

            except Exception as e:
                print(f"\n¡ERROR! Al ingresar el numero de telefono del empleado: {e}", end="\n\n")
                system("pause")
                continue
 
        # EMAIL ----------------------------------------------------------------------------------------
        while True:
            try:
                system("cls")
                print("------------------------------")
                print("--- CREAR EMPLEADO (EMAIL) ---")
                print("------------------------------")
                email = input("\nIngrese email del empleado: ")
                if len(email.strip()) >= 10 and len(email.strip()) <= 60:
                    print("\nEmail guardado correctamente:", email)
                    system("pause")
                    break
                else:
                    print("\nEl email debe tener entre 18 y 60 caracteres")
                    system("pause")
                    continue
            except Exception as e:
                print(f"\n¡ERROR! Al ingresar el email del empleado: {e}", end="\n\n")
                continue
        # FECHA DE NACIMIENTO ----------------------------------------------------------------------------

        # Obtener fecha de nacimiento con la funcion obtener_fecha(titulo_pantalla: str) -> date     
        system("cls")
        fecha_nacimiento = self.__obtener_fecha("CREAR EMPLEADO (FECHA NACIMIENTO)")
        print(f"\nFecha de nacimiento registrada: {fecha_nacimiento.strftime('%Y-%m-%d')}")
        system("pause")

        # FECHA INICIO CONTRADO -----------------------------------------------------------

        # Obtener fecha de inicio de contrato con la funcion obtener_fecha(titulo_pantalla: str) -> date 
        system("cls")
        fecha_ini_contrato = self.__obtener_fecha("CREAR EMPLEADO (FECHA INICIO CONTRATO)")
        print(f"\nFecha de inicio de contrato registrada: {fecha_ini_contrato.strftime('%Y-%m-%d')}")
        system("pause")

        # SALARIO ------------------------------------------------------------------------------------
        while True:
            try:
                system("cls")
                print("--------------------------------")
                print("--- CREAR EMPLEADO (SALARIO) ---")
                print("--------------------------------")              
                salario = int(input("\nIngrese salario del empleado: "))
                if salario > 549_999 and salario < 4_000_000:
                    print("\nSalario guardado correctamente:", salario)
                    system("pause")
                    break
                else:
                    print("\nEl salario debe ser mayor a $549.999 y menor a $4.000.000")
                    system("pause")
                    continue
            except ValueError:
                print("\n¡ERROR! El salario debe ser escrito solo con numeros")
                system("pause")
                continue

            except Exception as e:
                print(f"\n¡ERROR! Al ingresar el salario del empleado: {e}", end="\n\n")
                system("pause")
                continue
        # TIPO DE ACCESO ---------------------------------------------------------------------------------

        while True:
            try:
                system("cls")
                print("---------------------------------------")
                print("--- CREAR EMPLEADO (TIPO DE ACCESO) ---")
                print("---------------------------------------")
                tipoAcceso = int(input("\nIngrese tipo de acceso del empleado (1 GESTION DE PROYECTOS, 2 GERENTE, 3 EMPLEADO SIN ACCESO): "))
                if 1 <= tipoAcceso <= 3:
                    print("\nTipo de acceso guardado correctamente:", tipoAcceso)
                    system("pause")
                    break
                else:
                    print("\nEl tipo de acceso debe ser entre 1 y 3")
                    system("pause")
                    continue
            except ValueError:
                print("\n¡ERROR! El tipo de acceso debe ser escrito solo con numeros")
                system("pause")
                continue

            except Exception as e:
                print(f"\n¡ERROR! Al ingresar el tipo de acceso del empleado: {e}", end="\n\n")
                system("pause")
                continue

        # USUARIO Y CONTRASEÑA ---------------------------------------------------------------------------
        nomUsuario = None
        contrasena = None # Aquí se almacenará la contraseña en texto plano, el DAO debería encriptarla antes de guardar
 
        # Si el tipo de acceso es GERENTE (2) o GESTION DE PROYECTOS (1), se debe crear un usuario.
        if tipoAcceso == 1 or tipoAcceso == 2:
            system("cls")
            print("-----------------------------------------")
            print("--- CREAR EMPLEADO (USUARIO EMPLEADO) ---")
            print("-----------------------------------------")
            print(f"\nEl tipo de acceso {tipoAcceso} requiere la creación de un usuario. Se generará automáticamente.")
            system("pause")
 
            # Generar nombre de usuario automáticamente: inicial del nombre + rut formateado
            nomUsuario = nombre[0].upper() + rut_formateado
            print(f"\nNombre de usuario generado automáticamente: {nomUsuario}")
            system("pause")
 
            # Obtener y validar contraseña
            while True:            
                system("cls")
                print("--- CREAR EMPLEADO (USUARIO EMPLEADO) ---")
                contrasena_input = input("\nIngrese contraseña para el empleado (mín 6, máx 255 caracteres): ").strip()
                if 6 <= len(contrasena_input) <= 255:
                    contrasena = contrasena_input
                    print("\nContraseña guardada correctamente.")
                    system("pause")
                    break
                else:
                    print("\nLa contraseña debe tener entre 6 y 255 caracteres.")
                    system("pause")
        else: # Si es tipo de acceso 3 (EMPLEADO SIN ACCESO)
            print("\nNo se creará un usuario para este empleado (acceso no requerido).")
            system("pause")

        # Asignar los valores al objeto empleado (usando self.emp)
        nuevo_empleado.setRut(rut_formateado)
        nuevo_empleado.setNombres(nombre)
        nuevo_empleado.setApellidoPaterno(app_paterno)
        nuevo_empleado.setApellidoMaterno(app_materno)
        nuevo_empleado.setSexo(sexo)
        nuevo_empleado.setDireccion(direccion)
        nuevo_empleado.setNroTelefono(nroTelefono)
        nuevo_empleado.setEmail(email)
        nuevo_empleado.setFechaNacimiento(fecha_nacimiento.strftime('%Y-%m-%d'))
        nuevo_empleado.setFechaInicioContrato(fecha_ini_contrato.strftime('%Y-%m-%d'))
        nuevo_empleado.setSalario(salario)
        nuevo_empleado.setIdEstado(1) # 1 significa 'HABILITADO'
        nuevo_empleado.setIdProyecto(None) # Por defecto, un nuevo empleado no tiene proyecto asignado
        nuevo_empleado.setIdTipoAcc(tipoAcceso)
        nuevo_empleado.setNombreUsuario(nomUsuario) # Asignar el nombre de usuario recolectado
        nuevo_empleado.setContrasena(contrasena)   # Asignar la contraseña recolectada (texto plano por ahora)
        
        self.dao.insertarEmpleado(nuevo_empleado)
        print("\n¡Empleado creado exitosamente!")
        system("pause")

    def __listarEmpleados(self):
        try:
            respuesta = self.dao.ObtenerEmpleado() 
            if len(respuesta)== 0:
                print("No hay empleados registrados.")
                system("pause")
                self.__menuGerente()
                return
            else:
                system("cls")
                print("----------------------------------")
                print("-------- LISTAR EMPLEADOS --------")
                print("----------------------------------")
                tabla = PrettyTable()
                tabla.field_names = ["RUT", "NOMBRE", "APELLIDO PATERNO", "APELLIDO MATERNO", "TELEFONO", "EMAIL", "SALARIO", "ESTADO", "ID PROYECTO"]
                for x in respuesta:
                    tabla.add_row(x)
                print(tabla, end="\n\n")
                system("pause")
                self.__menuGerente()
        except Exception as e:
            print(f"\n¡ERROR! Al listar los empleados: {e}", end="\n\n")
            system("pause")
            self.__menuGerente()

    def __buscarEmpleado(self):
            try:
                rut = self.__obtener_rut_validado(titulo_menu="BUSCAR EMPLEADO (RUT)")
                emp = self.dao.BuscarEmpleado(rut)
                
                if emp is None:
                    print(f"El rut {rut} no corresponde a un empleado registrado en la base de datos", end="\n\n")
                    system("pause")
                    self.__menuGerente()
                    
                else:
                    system("cls")
                    print("----------------------------------------")
                    print(f"---------- BUSCAR EMPLEADO ------------")
                    print("----------------------------------------")
                    print(f"\n---EMPLEADO ENCONTRADO---")
                    print(F"RUT:                   {emp.getRut()}")
                    print(F"NOMBRE:                {emp.getNombres()}")
                    print(F"APELLIDO PATERNO:      {emp.getApellidoPaterno()}")
                    print(F"APELLIDO MATERNO:      {emp.getApellidoMaterno()}")
                    print(F"DIRECCION:             {emp.getDireccion()}")
                    print(F"TELEFONO:              {emp.getNroTelefono()}")
                    print(F"EMAIL:                 {emp.getEmail()}")
                    print(F"FECHA NACIMIENTO:      {emp.getFechaNacimiento()}")
                    print(F"FECHA INICIO CONTRATO: {emp.getfechaInicioContrato()}")
                    print(F"SALARIO:               {emp.getSalario()}")
                    print(F"ESTADO:--------------> {emp.getIdEstado()}")
                    print(F"ID PROYECTO:---------> {emp.getIdProyecto()}")
                    print(F"TIPO ACCESO:---------> {emp.getIdTipoAcc()}", end="\n\n")
                    system("pause")
                    self.__menuGerente()

            except Exception as e:
                print(f"\n¡ERROR! Al buscar el empleado: {e}", end="\n\n")
                system("pause")
                self.__menuGerente()
        
    def __modificarEmpleado(self):
        try:
            system("cls")
            print("---------------------------------------")
            print("---------- MODIFICAR EMPLEADO ---------")
            print("---------------------------------------")
            rut = self.__obtener_rut_validado(titulo_menu ="MODIFICAR EMPLEADO (RUT)")
            emp = self.dao.BuscarEmpleado(rut)
            if emp is None:
                print("---ERROR! El empleado que quiere modificar no existe! Verifique el rut ingresado---", end="\n\n")
                system("pause")
                self.__menuGerente()
            else:
                system("cls")
                print("-----------------------------------------")
                print("---------- (MODIFICAR EMPLEADO) ---------")
                print("-----------------------------------------")
                print(f"\n---EMPLEADO ENCONTRADO---")
                print(F"RUT:                   {emp.getRut()}")
                print(F"NOMBRE:--------------> {emp.getNombres()}")
                print(F"APELLIDO PATERNO: ---> {emp.getApellidoPaterno()}")
                print(F"DIRECCION: ----------> {emp.getDireccion()}")
                print(F"TELEFONO: -----------> {emp.getNroTelefono()}")
                print(F"EMAIL: --------------> {emp.getEmail()}")
                print(F"SALARIO: ------------> {emp.getSalario()}")
                print(F"ESTADO:--------------> {emp.getIdEstado()}")
                print(F"ID PROYECTO:---------> {emp.getIdProyecto()}", end="\n\n")

                print("1- MODIFICAR NOMBRE")
                print("2- MODIFICAR DIRECCION")
                print("3- MODIFICAR TELEFONO")
                print("4- MODIFICAR EMAIL")
                print("5- MODIFICAR SALARIO")
                print("6- MODIFICAR ESTADO")
                print("7- MODIFICAR ID PROYECTO")
                print("8- VOLVER")
                dato = int(input("\nElija que dato quiere modificar con el numero correspondiente (1-8): "))
                if 1 <= dato <= 8:
                    if dato == 1:
                        nuevo = self.__obtener_apellido("MODIFICAR EMPLEADO (NOMBRE)")
                        self.dao.modificarEmpleado(dato, nuevo, rut)

                    elif dato == 2:
                        while True:
                            print("----------------------------------------")
                            print("---- MODIFICAR EMPLEADO (DIRECCION) ----")
                            print("----------------------------------------")
                            nueva_direccion = input("\nIngrese la nueva direccion del empleado: ")
                            if len(nueva_direccion.strip()) >= 10 and len(nueva_direccion.strip()) <= 60:
                                nuevo = nueva_direccion.capitalize()
                                print("\nDirección guardada correctamente:", nuevo)
                                system("pause")
                                break
                            else:
                                print("\nLa direccion debe tener entre 10 y 60 caracteres")
                                system("pause")
                                continue
                        self.dao.modificarEmpleado(dato, nuevo, rut)
                    elif dato == 3:
                        while True:
                            print("---------------------------------------")
                            print("---- MODIFICAR EMPLEADO (TELEFONO) ----")
                            print("---------------------------------------")
                            try:
                                nroTelefono = input("\nIngrese el nuevo número de teléfono del empleado (9 dígitos) (SIN +56): ")

                                if nroTelefono.isdigit() and len(nroTelefono) == 9:
                                    nuevo = "+56" + nroTelefono
                                    print("\nNúmero guardado correctamente:", nuevo)
                                    system("pause")
                                    break
                                else:
                                    print("\nERROR: El número debe tener exactamente 9 dígitos y solo contener números.")
                                    system("pause")
                                    continue
                            except ValueError:
                                print("ERROR! El numero de telefono debe ser escrito solo con numeros")
                                system("pause")
                                continue
                        self.dao.modificarEmpleado(dato, nuevo, rut)
                    elif dato == 4:
                        while True:
                            print("----------------------------------------")
                            print("------ MODIFICAR EMPLEADO (EMAIL) ------")
                            print("----------------------------------------")
                            nuevo = input("\nIngrese el nuevo email del empleado: ")
                            if len(nuevo.strip()) >= 10 and len(nuevo.strip()) <= 60:
                                print("\nEmail guardado correctamente:", nuevo)
                                system("pause")
                                break
                            else:
                                print("\nEl email debe tener entre 10 y 60 caracteres")
                                system("pause")
                                continue
                        self.dao.modificarEmpleado(dato, nuevo, rut)
                    elif dato == 5:
                        while True:
                            print("--------------------------------------")
                            print("---- MODIFICAR EMPLEADO (SALARIO) ----")
                            print("--------------------------------------")
                            try:             
                                nuevo = int(input("\nIngrese el nuevo salario del empleado: "))
                                if nuevo > 549_999 and nuevo < 4_000_000:
                                    print("\nSalario guardado correctamente:", nuevo)
                                    system("pause")
                                    break
                                else:
                                    print("\nEl salario debe ser mayor a $549.999 y menor a $4.000.000")
                                    system("pause")
                                    continue
                            except ValueError:
                                print("\n¡ERROR! El salario debe ser escrito solo con numeros")
                                system("pause")
                                continue

                            except Exception as e:
                                print(f"\n¡ERROR! Al ingresar el salario del empleado: {e}", end="\n\n")
                                system("pause")
                                continue
                        self.dao.modificarEmpleado(dato, nuevo, rut)

                    elif dato == 6:
                                        
                        if emp.getIdEstado() == 'HABILITADO':
                            nuevo = 2
                            system("cls")
                            print(f"\nSe ha cambiado el estado del empleado: {emp.getNombres()} {emp.getApellidoPaterno()} a DESHABILITADO", end="\n\n")
                            system("pause")
                            self.dao.modificarEmpleado(dato, nuevo, rut)

                        elif emp.getIdEstado() == 'DESHABILITADO':
                            nuevo = 1
                            system("cls")
                            print(f"\nSe ha cambiado el estado del empleado: {emp.getNombres()} {emp.getApellidoPaterno()} a HABILITADO", end="\n\n")
                            system("pause")
                            self.dao.modificarEmpleado(dato, nuevo, rut)

                        else: # <--- BUENA PRÁCTICA
                            print(f"ERROR: El empleado tiene un estado desconocido ({emp.getIdEstado()}). No se realizaron cambios.")
                            system("pause")
                            self.__menuGerente()

                    elif dato == 7:
                        pass
#----------------------------------                                                       --------------------------------------------------------------
#---------------------------------- AQUI TENGO QUE LISTAR LOS PROYECTOS EXISTENTES Y      --------------------------------------------------------------
#---------------------------------- PREGUNTAR A QUE PROYECTO QUIERO MOVER AL EMPLEADO     --------------------------------------------------------------
#---------------------------------- ESA VARIABLE SERA A LA QUE VOY A CAMBIAR EL EMPLEADO  --------------------------------------------------------------
#---------------------------------- LA VALIDO Y LA ENVIO AL DAO PARA QUE CAMBIE EL id_pro --------------------------------------------------------------
#----------------------------------                                                       --------------------------------------------------------------

                    else:
                        print("\nVolviendo al menú GERENTE...", end="\n\n")
                        system("pause")
                        self.__menuGerente()
                else:
                    print("\n--- Error De Opcion De Menú Modificar Empleado Debe Ser Del 1 al 8!! ---", end="\n\n")
                    system("pause")
                    self.__menuGerente()
        except ValueError:
            print("\n---ERROR!! La opcion solo puede ser un numero entero positivo---", end="\n\n")
            system("pause")
            self.__menuGerente()

        except Exception as e:
            print(f"\n¡ERROR! Al modificar el empleado: {e}", end="\n\n")
            system("pause")
            self.__menuGerente()

    def __eliminarEmpleado(self):
        while True:
            try:
                system("cls")
                print("------------------------------------------")
                print(f"---------- ELIMINAR EMPLEADO ------------")
                print("------------------------------------------")
                rut = self.__obtener_rut_validado(titulo_menu="ELIMINAR EMPLEADO (RUT)")
                emp = self.dao.BuscarEmpleado(rut)
                if emp is None:
                    print("---ERROR! El empleado que quiere eliminar no existe o ya ha sido desvinculado! Verifique el rut ingresado---", end="\n\n")
                    op = int(input("¿Desea volver a intentar con otro RUT o volver al menu Gerente? \n1- Intentar con otro RUT \n2- Volver\nDigite una opción: "))
                    if op == 1:
                        continue
                    elif op == 2:
                        self.__menuGerente()
                        return
                    else:
                        print("\n--- Error De Opcion De Menú Eliminar Empleado Debe Ser Del 1 al 2!! Volviendo al menu Eliminar Emlpeado---", end="\n\n")
                        system("pause")
                        continue                                    
                else:
                    opcion = int(input(f"\nEstá seguro de desvincular a {emp.getNombres()} {emp.getApellidoPaterno()} RUT: {emp.getRut()} ? \n1- Si \n2- No \nDigite una opción: "))
                    system("cls")
                    if opcion == 1:
                        if self.dao.eliminarEmpleado(rut):
                            print(f"\nSe ha desvinculado al empleado: {emp.getNombres()} {emp.getApellidoPaterno()} RUT: {emp.getRut()}", end="\n\n")                       
                            system("pause")
                            self.__menuGerente()
                            return
                        else:
                            print("\n¡ERROR! La base de datos no pudo procesar la desvinculación.")
                            print("Volviendo al menu Gerente...", end="\n\n")
                            system("pause")
                            self.__menuGerente()
                            return
                    elif opcion == 2:
                        continue
                    else:
                        print("Error de opción. Volviendo al menu Eliminar Empleado...", end="\n\n")
                        system("pause")
                        continue
            except Exception as e:
                print(f"\n¡ERROR! Al eliminar el empleado: {e}", end="\n\n")
                system("pause")
                continue
        
    def __estadisticasEmpleados(self):       
        system("cls")
        print("-------------------------------------------------")
        print("----- MENU GERENTE (ESTADISTICAS EMPLEADOS) -----")
        print("-------------------------------------------------")
        while True:
            try:
                print("\n1.- EMPLEADOS HABILITADOS")
                print("2.- EMPLEADOS DESHABILITADOS")
                print("3.- PROMEDIO DE EDADES (EXCEPTUANDO EMPLEADOS DESHABILITADOS)")
                print("4.- PROMEDIO DE SALARIOS (EXCEPTUANDO EMPLEADOS DESHABILITADOS)")
                print("5.- ADMINISTRADORES DE PROYECTOS")
                print("6.- VOLVER")
                op = int(input("\nDigite una opción: "))
                if op > 0 or op <= 8:
                    if op == 1:
                        self.dao.listarEmpleadoHabilitados()
                    elif op == 2:
                        self.dao.listarEmpleadoDeshabilitados()
                    elif op == 3:
                        self.__promedioEdades()
                    elif op == 4:
                        self.__promedioSalarios()
                    elif op == 5:
                        self.__listarAdministradores()
                    elif op == 6:
                        self.menuInicial()
                        return
                    else:
                        print("\n--- Error De Opcion De Menú ---", end="\n\n")
                        system("pause")
                        continue
            except Exception as e:
                print(f"ERROR! No se puede mostrar la información que necesita: {e}", end="\n\n")
                system("pause")
                continue

    def __promedioEdades(self):
        system("cls")
        print("-------------------------------------------------")
        print("----- MENU GERENTE (ESTADISTICAS EMPLEADOS) -----")
        print("-------------------------------------------------")
        
        # Llamamos al DAO y guardamos el resultado en una variable
        promedio = self.dao.promedioEdadesEmpleados()
        
        # Manejamos el resultado aquí
        if promedio == 0:
            print("\n>>> No hay empleados habilitados registrados para calcular un promedio.")
        else:
            print(f"\nEl promedio de edad de los empleados activos es: {promedio} años.")
        
        print("\n-------------------------------------------------")
        system("pause")

    def __promedioSalarios(self):
        system("cls")
        print("-------------------------------------------------")
        print("----- MENU GERENTE (ESTADISTICAS EMPLEADOS) -----")
        print("-------------------------------------------------")

        promedio = self.dao.promedioSalariosEmpleados()

        if promedio > 0:
            print(f"\nEl promedio de salarios de los empleados activos es: ${promedio}")
        else:
            print("\n>>> No hay empleados habilitados registrados para calcular un promedio. ")
        print("\n-------------------------------------------------")
        system("pause")

    def __listarAdministradores(self):
            system("cls")
            print("-------------------------------------------------")
            print("----- LISTADO DE ADMINISTRADORES DE PROYECTOS ----")
            print("-------------------------------------------------")

            lista_admin = self.dao.obtenerAdministradores()

            if len(lista_admin) > 0:
                tabla = PrettyTable()
                tabla.field_names = ["RUT", "NOMBRE", "APELLIDO PATERNO", "APELLIDO MATERNO"]
                for x in lista_admin:
                    tabla.add_row(x)
                print(tabla, end="\n\n")
                system("pause")
            else:
                print("\nNo hay administradores registrados.", end="\n\n")
                system("pause")

#-------------------------------------------------------------------------------------------
#   FUNCIONES MENU GESTION DE PROYECTOS
    def __crearProyecto(self):
        pass

    def __listarProyectos(self):
        pass

    def __buscarProyecto(self):
        pass

    def __modificarProyecto(self):
        pass

    def __eliminarProyecto(self):
        pass

    def __estadisticasProyectos(self):
        pass

#-------------------------------------------------------------------------------------------
#   FUNCIONES MENU ASIGNACION DE PROYECTOS
    def __asignarEmpleado(self):
        pass

    def __reasignarEmpleado(self):
        pass

    def __listarEmpleadosAsignados(self):
        pass

    def __listarEmpleadosSinAsignar(self):
        pass

#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------
#-------------------------------------- FUNCIONES REUTILIZABLES ------------------------------------------
#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------

    def __obtener_rut_validado(self,titulo_menu: str):
        """
        Pide un RUT al usuario, lo valida (formato y dígito 'K') 
        y lo retorna formateado (ej: "12345678-K").
        Este bucle se repite hasta que el RUT ingresado sea válido.
        """
        while True:
            system("cls")
            print("-------------------------------------------")
            print(f"--------- {titulo_menu} ---------")
            print("-------------------------------------------")
            
            # 1. Pedir y limpiar (acepta "11 111 111 k")
            rut_sin_formato = input("\nIngrese RUT (SIN puntos y SIN guion) puede usar espacios para separar digitos (Ej: 11 111 111 k): ").strip().replace(" ", "")

            # 2. Validar longitud
            if (8 <= len(rut_sin_formato) <= 10):
                    # 3. Separar cuerpo y DV
                    cuerpo = rut_sin_formato[:-1]
                    dv = rut_sin_formato[-1].upper() # Convertir 'k' a 'K'
            else:
                    print("\nError: El RUT debe tener entre 8 y 10 caracteres.")
                    system("pause")
                    continue

            if cuerpo.isdigit() and (dv.isdigit() or dv == 'K'):
                rut_formateado = f"{cuerpo}-{dv}"
                return rut_formateado
            else:
                print("\nError: El RUT contiene caracteres no válidos.")
                print("(Recuerde: solo números y 'k' al final si corresponde)")
                system("pause")
                continue

    #---------------------------------------------------------------------------------------------------------
    def __obtener_fecha(self,titulo_pantalla: str) -> date:
        """
        Solicita al usuario una fecha (día, mes, año), la valida y la devuelve.
        Repite el proceso hasta que se ingrese una fecha válida.

        Args:
            titulo_pantalla (str): El título que se mostrará en la pantalla de ingreso.

        Returns:
            date: El objeto de fecha validado.
        """
        while True:
            try:
                system("cls")
                print("------------------------------------------")
                print(f"--- {titulo_pantalla.upper()} ---")
                print("------------------------------------------")

                print("\nIngrese la fecha:")
                dia = int(input("Día (DD): "))
                mes = int(input("Mes (MM): "))
                anio = int(input("Año (AAAA): "))

                # Validar y construir la fecha
                fecha_validada = date(anio, mes, dia)
                return fecha_validada # Si la fecha es válida, la retornamos y salimos de la función

            except ValueError:
                print("\nError: Fecha inválida. Verifique los valores ingresados.")
                system("pause")
                continue
    #---------------------------------------------------------------------------------------------------------

    def __obtener_apellido(self, titulo_pantalla: str) -> str:
        while True:
                try:
                    system("cls")
                    print("-------------------------------------------")
                    print(f"---- {titulo_pantalla.upper()} ----")
                    print("-------------------------------------------")

                    appellido_ingresado = input(f"\nIngrese {titulo_pantalla.lower()}  del empleado: ").strip()
                    if appellido_ingresado.isalpha() and len(appellido_ingresado) >= 2 and len(appellido_ingresado) <= 20:
                        ape_formateado = appellido_ingresado.capitalize()
                        print(f"\n{titulo_pantalla.lower()} guardado correctamente:",ape_formateado )
                        system("pause")
                        return ape_formateado
                    else:
                        print("\nEl apellido debe tener entre 2 y 20 caracteres")
                        system("pause")
                        continue
                except Exception as e:
                    print(f"\n¡ERROR! Al ingresar el apellido del empleado: {e}", end="\n\n")
                    system("pause")
                    continue

    def __listarAdministradores(self):
        pass
#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------