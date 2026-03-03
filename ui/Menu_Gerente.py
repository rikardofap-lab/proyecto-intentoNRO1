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
    def __crearEmpleado(self):
        # Creamos una instancia LOCAL para este nuevo empleado.
        nuevo_empleado = empleado()

        system("cls")
        print("----------------------------------")
        print("------ CREAR NUEVO EMPLEADO ------")
        print("----------------------------------")
        print("¿Estás seguro de crear un nuevo empleado?")
        print("1. Si")
        print("2. No")
        op = Validaciones.validar_numero_rango("CONFIRMAR CREAR EMPLEADO", "opción", 1, 2)

        if op == 2:
            return
        elif op == 1:
            system("cls")
            rut = Validaciones.obtener_rut_validado(titulo_menu="CREAR EMPLEADO (RUT)")
            if self.dao.comprobarRutEmpleado(rut) is not None:
                print(f"\n---ERROR! El rut {rut} ya está registrado en la base de datos---", end="\n\n")
                system("pause")
            else:
                # Datos personales
                nom = Validaciones.validar_texto(titulo_pantalla="CREAR EMPLEADO (NOMBRE)", etiqueta_campo="Nombre")
                app_materno = Validaciones.validar_texto(titulo_pantalla="CREAR EMPLEADO (APELLIDO MATERNO)", etiqueta_campo="Apellido")
                app_paterno = Validaciones.validar_texto(titulo_pantalla="CREAR EMPLEADO (APELLIDO PATERNO)", etiqueta_campo="Apellido")
                sex = Validaciones.validar_numero_rango("CREAR EMPLEADO (SEXO)", "Sexo", 1, 3)
                
                # Datos de contacto
                email = Validaciones.validar_email("CREAR EMPLEADO (EMAIL)")
                nroTelefono = Validaciones.validar_telefono("CREAR EMPLEADO (TELEFONO)")
                direccion = Validaciones.validar_texto("CREAR EMPLEADO (DIRECCION)", "Direccion")

                # Fechas y salario
                f_nac = Validaciones.obtener_fecha("CREAR EMPLEADO (FECHA NACIMIENTO)")
                f_ini_contrato = Validaciones.obtener_fecha("CREAR EMPLEADO (FECHA INICIO CONTRATO)")
                salario = Validaciones.validar_numero_rango("CREAR EMPLEADO (SALARIO)", "Sueldo bruto", 550000, 4000000)


                # Tipo de Acceso (Este especifica qué tiposd de acceso tendra el empleado al programa)
                print("1. GESTION DE PROYECTOS")
                print("2. GERENTE")
                print("3. ASIGNACION DE EMPLEADOS")
                print("4. EMPLEADO SIN ACCESO")

                tipoAcceso = Validaciones.validar_numero_rango("CREAR EMPLEADO (TIPO DE ACCESO)", "Nivel de acceso", 1, 4)
                nom_usu = None
                contrasena = None

                # Si requiere acceso generamos credenciales 
                if 1 <= tipoAcceso <= 3:
                    nom_usu = nom[0].upper() + rut.replace("-","") # El usuario viene siendo la inicial de su nombre en mayuscula mas el rut sin guion
                    print(f"Nombre de usuario generado: {nom_usu}")
                    while True:
                        contrasena = input("Defina una contraseña (minimo 6 caracteres): ")
                        if len(contrasena) >= 6:
                            break
                        else:
                            print("La contraseña debe tener al menos 6 caracteres.")
                            continue
                nuevo_empleado.setRut(rut) # ID
                nuevo_empleado.setNombres(nom); nuevo_empleado.setApellidoPaterno(app_paterno); nuevo_empleado.setApellidoMaterno(app_materno) # NOMBRES Y APELLIDOS
                nuevo_empleado.setSexo(sex) # SEXO MASCULINO, FEMENINO, OTRO
                nuevo_empleado.setDireccion(direccion); nuevo_empleado.setNroTelefono(nroTelefono); nuevo_empleado.setEmail(email) # DATOS DE CONTACTO
                nuevo_empleado.setFechaNacimiento(f_nac.strftime('%Y-%m-%d')); nuevo_empleado.setFechaInicioContrato(f_ini_contrato.strftime('%Y-%m-%d')) # FECHAS (INICIO DE CONTRATO Y FECHA DE NACIMIENTO)
                nuevo_empleado.setSalario(salario); nuevo_empleado.setIdEstado(1); nuevo_empleado.setIdProyecto(None) # SIEMPRE INICIA EL EMPLEADO COMO "HABILITADO" Y SIN PROYTECTO
                nuevo_empleado.setIdTipoAcc(tipoAcceso); nuevo_empleado.setNombreUsuario(nom_usu); nuevo_empleado.setContrasena(contrasena) # SI TIENE ACCESO SE CREA EL USUARIO SINO QUEDA "NONE"

                if self.dao.insertarEmpleado(nuevo_empleado):
                    print("\n¡Empleado creado exitosamente!")

                else:
                    print("\n¡Error al crear el empleado!")
                system("pause")

    def __listarEmpleados(self):
        try:
            respuesta = self.dao.listarEmpleadosGeneral(1) 
            if len(respuesta)== 0:
                print("No hay empleados registrados.")
                system("pause")
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
        except Exception as e:
            print(f"\n¡ERROR! Al listar los empleados: {e}", end="\n\n")
            system("pause")

    def __buscarEmpleado(self) -> empleado:
            try:
                system("cls")
                rut = Validaciones.obtener_rut_validado(titulo_menu="BUSCAR EMPLEADO (RUT)")
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
                        nuevo = Validaciones.validar_texto(titulo_pantalla="MODIFICAR EMPLEADO (NOMBRE)", etiqueta_campo="Nombre")
                        self.dao.modificarEmpleado(dato, nuevo, rut)
                        print("\nNombre guardado correctamente: ", nuevo)
                        system("pause")
                    
                    elif dato == 2:
                        nuevo = Validaciones.validar_texto(titulo_pantalla="MODIFICAR EMPLEADO (DIRECCION)", etiqueta_campo="Dirección")
                        self.dao.modificarEmpleado(dato, nuevo, rut)
                        print("\nDirección guardada correctamente: ", nuevo)
                        system("pause")
                    
                    elif dato == 3:
                        nuevo = Validaciones.validar_telefono("MODIFICAR EMPLEADO (TELEFONO)")
                        print("\nTeléfono guardado correctamente: ", nuevo)
                        system("pause")
                        self.dao.modificarEmpleado(dato, nuevo, rut)

                    elif dato == 4:
                        nuevo = Validaciones.validar_email("MODIFICAR EMPLEADO (EMAIL)")
                        self.dao.modificarEmpleado(dato, nuevo, rut)
                        print("\nEmail guardado correctamente: ", nuevo)
                        system("pause")

                    elif dato == 5:
                        nuevo = Validaciones.validar_numero_rango("MODIFICAR EMPLEADO (SALARIO)", "Sueldo bruto", 550000, 4000000)   
                        self.dao.modificarEmpleado(dato, nuevo, rut)
                        print("\nSalario guardado correctamente: ", nuevo)
                        system("pause")

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

                        else:
                            print(f"ERROR: El empleado tiene un estado desconocido ({emp.getIdEstado()}). No se realizaron cambios.")
                            system("pause")

                    elif dato == 7:
                        from database.ProyectoDAO import proyectoDAO
                        pro_dao = proyectoDAO()
                        proyectos = pro_dao.listarProyectosGeneral(2) # Solo habilitados

                        system("cls")
                        print("-----------------------------------------------------")
                        print("---------- MODIFICAR PROYECTO DEL EMPLEADO ----------")
                        print("-----------------------------------------------------")

                        if not proyectos:
                            print("\nNo hay proyectos habilitados para asignar.")
                            system("pause")
                        else:
                            # 1. Mostramos la tabla y guardamos los IDs que sí existen
                            tabla_pro = PrettyTable(["ID", "NOMBRE", "DESCRIPCIÓN"])
                            ids_validos = []
                            for p in proyectos:
                                tabla_pro.add_row([p[0], p[1], p[2]])
                                ids_validos.append(p[0]) # Guardamos el ID real (ej: 1, 5, 10)
                            
                            print(tabla_pro)
                            
                            # 2. Bucle de captura manual (mientras haces las Validaciones nuevas)
                            while True:
                                print("\n(Ingrese 0 para dejar al empleado sin proyecto)")
                                entrada = input("Ingrese el ID del proyecto: ").strip()
                                
                                if entrada == "0":
                                    nuevo = None # MySQL lo guarda como NULL
                                    break
                                elif entrada.isdigit() and int(entrada) in ids_validos:
                                    nuevo = int(entrada)
                                    break
                                else:
                                    print(f"\nERROR: El ID '{entrada}' no es válido o no está en la lista.")
                                    system("pause")

                            # 3. Guardado final
                            if self.dao.modificarEmpleado(dato, nuevo, rut):
                                print("\n¡Proyecto actualizado con éxito!")
                            else:
                                print("\n¡Error al actualizar en la base de datos!")
                            system("pause")
"""
                        from database.ProyectoDAO import proyectoDAO
                        pro_dao = proyectoDAO()
                        proyectos = pro_dao.listarProyectosGeneral(2)

                        system("cls")
                        print("-----------------------------------------------------")
                        print("---------- MODIFICAR PROYECTO DEL EMPLEADO ----------")
                        print("-----------------------------------------------------")

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
                            cont_proyectos = len(proyectos)
                            nuevo = Validaciones.validar_numero_rango(titulo="INGRESE ID PROYECTO", etiqueta="ID", min_v=1, max_v=cont_proyectos) #input("\nIngrese el ID del nuevo proyecto (o deje vacío para desasignar): ").strip()

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
                else:
                    print("\n--- Error De Opcion De Menú Modificar Empleado Debe Ser Del 1 al 8!! ---", end="\n\n")
                    system("pause")
        except ValueError:
            print("\n---ERROR!! La opcion solo puede ser un numero entero positivo---", end="\n\n")
            system("pause")

        except Exception as e:
            print(f"\n¡ERROR! Al modificar el empleado: {e}", end="\n\n")
            system("pause")"""