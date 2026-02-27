from database.EmpleadoDAO import empleadoDAO
from core.Empleado import empleado
from utils.validaciones import Validaciones
from prettytable import PrettyTable
from os import system

class MenuGerente:

    def __init__(self, emp_logeado):

        self.emp = emp_logeado
        self.dao = empleadoDAO()
        self.validaciones = Validaciones()

    def mostrar_menu(self):

        while True:
            try:
                system("cls")
                print("----------------------------------------------------------------------")
                print("--------------------------- MENU GERENTE -----------------------------")
                print(f"{self.emp.getNombreUsuario()} | Rol: {self.emp.getNomTipoAcc()}")
                print("----------------------------------------------------------------------")
                print("\n1.- CREAR EMPLEADO")
                print("2.- LISTAR EMPLEADOS")
                print("3.- BUSCAR EMPLEADO")
                print("4.- MODIFICAR EMPLEADO")
                print("5.- ELIMINAR EMPLEADO")
                print("6.- ESTADISTICAS EMPLEADOS")
                print("7.- VOLVER")

                op = int(input("\nDigite una opción: "))

                if 1 <= op <= 7:
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
                        return
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
                    rut_formateado = Validaciones.obtener_rut_validado(titulo_menu="CREAR EMPLEADO (RUT)")
                    if self.dao.comprobarRutEmpleado(rut_formateado) is not None:
                        print(f"\n---ERROR! El rut {rut_formateado} ya está registrado en la base de datos---", end="\n\n")
                        system("pause")
                        continue
                    else:
                        print(f"RUT {rut_formateado} registrado correctamente", end="\n\n")
                        system("pause")
                        break
                else:
                    print("\n--- Error De Opcion De Menú Crear Empleado Debe Ser Del 1 al 2!! ---", end="\n\n")
                    system("pause")
                    continue
                   
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
        app_paterno = Validaciones.obtener_apellido("Apellido Paterno")


        # APELLIDO MATERNO ------------------------------------------------------------------
        app_materno = Validaciones.obtener_apellido("Apellido Materno")
        
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
        fecha_nacimiento = Validaciones.obtener_fecha("CREAR EMPLEADO (FECHA NACIMIENTO)")
        print(f"\nFecha de nacimiento registrada: {fecha_nacimiento.strftime('%Y-%m-%d')}")
        system("pause")

        # FECHA INICIO CONTRADO -----------------------------------------------------------

        # Obtener fecha de inicio de contrato con la funcion obtener_fecha(titulo_pantalla: str) -> date 
        system("cls")
        fecha_ini_contrato = Validaciones.obtener_fecha("CREAR EMPLEADO (FECHA INICIO CONTRATO)")
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
                tipoAcceso = int(input("\nIngrese tipo de acceso del empleado \n1. GESTION DE PROYECTOS, \n2. GERENTE \n 3. ASIGNACION DE EMPLEADOS \n4. EMPLEADO SIN ACCESO): "))
                if 1 <= tipoAcceso <= 4:
                    print("\nTipo de acceso guardado correctamente:", tipoAcceso)
                    system("pause")
                    break
                else:
                    print("\nEl tipo de acceso debe ser entre 1 y 4")
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
        if tipoAcceso == 1 or tipoAcceso == 2 or tipoAcceso == 3:
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
            respuesta = self.dao.listarEmpleadosGeneral(1) 
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

    def __buscarEmpleado(self) -> empleado:
            try:
                rut = self.__obtener_rut_validado(titulo_menu="BUSCAR EMPLEADO (RUT)")
                emp = self.dao.BuscarEmpleado(rut)
                
                if emp is None:
                    print(f"El rut {rut} no corresponde a un empleado registrado en la base de datos", end="\n\n")
                    system("pause")
                    return None
                    
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
                    return emp

            except Exception as e:
                print(f"\n¡ERROR! Al buscar el empleado: {e}", end="\n\n")
                system("pause")
                self.__menuGerente()
                return None
        
    def __modificarEmpleado(self):
        try:
            system("cls")
            print("---------------------------------------")
            print("---------- MODIFICAR EMPLEADO ---------")
            print("---------------------------------------")

            rut = Validaciones.obtener_rut_validado(titulo_menu ="MODIFICAR EMPLEADO (RUT)")
            emp = self.dao.BuscarEmpleado(rut)

            if emp is None:
                print("---ERROR! El empleado que quiere modificar no existe! Verifique el rut ingresado---", end="\n\n")
                system("pause")
                return
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
                
                if dato == 8: return

                nuevo = None
                if 1 <= dato <= 7:
                    if dato == 1:
                        nuevo = Validaciones.obtener_apellido("MODIFICAR (NOMBRE)")
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

                        from database.ProyectoDAO import proyectoDAO
                        pro_dao = proyectoDAO()
                        proyectos = pro_dao.listarProyectosGeneral(2)

                        system("cls")
                        print("---------- MODIFICAR PROYECTO DEL EMPLEADO ----------")

                        if not proyectos:
                            print("\No hay proyectos habilitados para asignar.")
                            system("pause")
                            return
                        else:
                            tabla_pro = PrettyTable(["ID", "NOMBRE", "DESCRIPCIÓN"])
                            for p in proyectos:
                                tabla_pro.add_row([p[0], p[1], p[2]])
                            print(tabla_pro)
                            system("pause")
                            nuevo = input("\nIngrese el ID del nuevo proyecto (o deje vacío para desasignar): ").strip()
                            if nuevo == "":
                                nuevo = None # Permitimos que quede sin proyecto
                            if self.dao.modificarEmpleado(dato, nuevo, rut):
                                print("\n¡Proyecto actualizado con éxito!")
                                system("pause")
                                return
                            else:
                                print("\n¡Error al actualizar el proyecto!")
                                system("pause")
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