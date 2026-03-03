from core.Empleado import empleado
from core.Proyecto import proyecto
from core.TipoAcceso import tipoAcceso
from database.DAO import dao
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
                if self.emp is None:
                    system("cls")
                    print("-------------------------")
                    print("------ MENU INICIAL------")
                    print("-------------------------")
                    print("\n1.- INICIAR SESION")
                    print("2.- SALIR")
                    op = int(input("\nDigite una opción: "))
                    if op == 1:
                        self.__iniciarSesion()
                    elif op == 2:
                        self.salir()
                    else:
                        print("\n--- Error De Opcion De Menú Inicial!! ---", end="\n\n")
                        system("pause")
                        continue

                else:      # Redirección automática según el ID de Acceso
                    rol = self.emp.getIdTipoAcc()

                    if rol == 1:
                        self.__menuGestionProyectos()
                    elif rol == 2:
                        self.__menuGerente()
                    elif rol == 3:
                        self.__menuAsignacionEmpleados()
                    elif rol == 4:
                        print("No tienes permisos de acceso")
                        self.emp = None
                        system("pause")             
            except ValueError:
                    print("\n¡ERROR! LA OPCION DEBE INGRESARSE SOLO CON NUMEROS (1, 2 Y 3)")
                    system("pause")
                    continue
            except Exception as e:
                print(f"\n¡Error Al Capturar Opcion De Menú Inicial!!{e}", end="\n\n")
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
                print("-------------------------------")
                print("------- INICIO SESIÓN ---------")
                print("-------------------------------")
                usu = input("\nIngrese su usuario: ")
                con = input("\nIngrese su contraseña: ")

                usuario_logeado = self.dao.Login(usu, con)
                if usuario_logeado:
                    self.emp = usuario_logeado
                    print(f"\nBienvenido {self.emp.getNombres()}")
                    system("pause")
                    return True          
                else:
                    print("\nUsuario y contraseña incorrectos. Intente de nuevo.")
                    return False
            except Exception as e:
                print(f"\n--- Error Al Capturar Rut (Login)!! --- {e}", end="\n\n")
                system("pause")
                continue
        #-----------------------------------------------------------------------------------------

    def __menuAsignacionEmpleados(self):
        while True:
            try:
                system("cls")
                print("------------------------------------")
                print("--- MENU ASIGNACION DE EMPLEADOS ---")
                print("------------------------------------")
                print("\n1.- ASIGNAR EMPLEADO A PROYECTO")
                print("2.- REASIGNAR EMPLEADO")
                print("3.- LISTAR EMPLEADOS ASIGNADOS")
                print("4.- LISTAR EMPLEADOS SIN ASIGNAR")
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
                        return
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
                        self.__listaEmpleadosHab()
                    elif op == 2:
                        self.__listaEmpleadosDesh()
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

    def __listaEmpleadosHab(self):
        try:
            system("cls")
            respuesta = self.dao.listarEmpleadosGeneral(2)
            if len(respuesta) == 0:
                print("No hay empleados habilitados registrados.", end="\n\n")
                system("pause")
            else:
                system("cls")
                print("-----------------------------------------------")
                print("-------- LISTAR EMPLEADOS (HABILITADOS)--------")
                print("-----------------------------------------------")
                tabla = PrettyTable()
                tabla.field_names = ["RUT", "NOMBRE", "APELLIDO PATERNO", "APELLIDO MATERNO", "TELEFONO", "EMAIL", "SALARIO", "ESTADO", "ID PROYECTO"]
                for x in respuesta:
                    tabla.add_row(x)
                print(f"{tabla}", end="\n\n")
                system("pause")
        except Exception as e:
            print(f"\n¡ERROR! Al listar los empleados habilitados: {e}", end="\n\n")
            system("pause")

    def __listaEmpleadosDesh(self):
        try:
            system("cls")
            respuesta = self.dao.listarEmpleadosGeneral(3)
            if len(respuesta) == 0:
                print("No hay empleados habilitados registrados.", end="\n\n")
                system("pause")
            else:
                system("cls")
                print("-----------------------------------------------")
                print("-------- LISTAR EMPLEADOS (HABILITADOS)--------")
                print("-----------------------------------------------")
                tabla = PrettyTable()
                tabla.field_names = ["RUT", "NOMBRE", "APELLIDO PATERNO", "APELLIDO MATERNO", "TELEFONO", "EMAIL", "SALARIO", "ESTADO", "ID PROYECTO"]
                for x in respuesta:
                    tabla.add_row(x)
                print(f"{tabla}", end="\n\n")
                print("-----------------------------------------------")
                system("pause")
        except Exception as e:
            print(f"\n¡ERROR! Al listar los empleados habilitados: {e}", end="\n\n")
            system("pause")

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
            while True:
                try:
                    system("cls")
                    print("------------------------------------------------")
                    print("----------- CREAR PROYECTO (INICIO) ------------")
                    print("------------------------------------------------")
                    print("¿Está seguro que quiere crear un proyecto? \n1- Si \n2- No")
                    op = int(input("\nDigite una opción: "))

                    if op == 2:
                        return 
                    
                    if op == 1:
                        nuevo_p = proyecto() 
                        
                        # --- NOMBRE ---
                        while True:
                            nombre_in = input("\nIngrese el nombre del proyecto: ").strip()
                            if 6 <= len(nombre_in) <= 60:
                                nombre_formateado = nombre_in.title()
                                if self.dao.comprobarNombreProyecto(nombre_formateado) is not None:
                                    print("El nombre ya existe. Intente con otro.")
                                    system("pause")
                                else:
                                    break 
                            else:
                                print("\nEl nombre debe tener entre 6 y 60 caracteres.")
                                system("pause")

                        # --- DESCRIPCIÓN ---
                        while True:
                            desc = input("\nIngrese la descripción (mín. 20 caracteres): ").strip()
                            if 20 <= len(desc) <= 200:
                                break
                            else:
                                print("\nLa descripción es demasiado corta o muy larga.")
                                system("pause")

                        # --- FECHA ---
                        # reutilizo la función ya validada para la fecha
                        nuevo_p.setNomProyecto(nombre_formateado)
                        nuevo_p.setDescripcion(desc.capitalize())
                        f_inicio = self.__obtener_fecha("CREAR PROYECTO (FECHA INICIO)")
                        nuevo_p.setFechaInicio(f_inicio.strftime('%Y-%m-%d'))
                        nuevo_p.setIdEstado(1) # Habilitado por defecto

                        # --- GUARDADO FINAL ---
                        if self.dao.insertarProyecto(nuevo_p): # Llamamos al DAO
                            print("\n¡Proyecto creado exitosamente!")
                        else:
                            print("\nError al guardar en la base de datos.")
                        
                        system("pause")
                        return # Este return vuelve al menu proyectos
                    else:
                        print("\n--- Opción no válida ---")
                        system("pause")
                except ValueError:
                    print("\n¡ERROR! Debe ingresar un número.")
                    system("pause")
                except Exception as e:
                    print(f"\n¡Error inesperado!: {e}")
                    system("pause")
                    return

    def __listarProyectos(self):
            try:
                respuesta = self.dao.listarProyectosGeneral(1)
                if len(respuesta) == 0:
                    print("No hay proyectos registrados.", end="\n\n")
                    system("pause")
                    return
                else:
                    system("cls")
                    print("------------------------------------------------")
                    print("--------------- LISTAR PROYECTOS ---------------")
                    print("------------------------------------------------")
                    tabla = PrettyTable()
                    tabla.field_names = ["ID", "NOMBRE", "DESCRIPCION", "FECHA INICIO", "ESTADO"]
                    for x in respuesta:
                        tabla.add_row(x)
                    print(f"{tabla}", end="\n\n")
                    system("pause")
            except Exception as e:
                print(f"\n¡ERROR! Al listar los proyectos: {e}", end="\n\n")
                system("pause")
                return

    def __buscarProyecto(self) -> proyecto:
        try:
            system("cls")
            print("---------------------------------")
            print("-------- BUSCAR PROYECTO --------")
            print("---------------------------------")
            entrada = (input("\nIngrese el ID del proyecto: "))
            if not entrada.isdigit():
                print("ERROR! El id debe ser un numero entero.", end="\n\n")
                system("pause")
                return
            id_proyecto = int(entrada)
            pro = self.dao.buscarProyecto(id_proyecto)
            if pro is None:
                print("No hay un proyecto registrado con ese ID.", end="\n\n")
                system("pause")
                return None
            else:
                system("cls")
                print("----------------------------------")
                print(f"\n----- PROYECTO ENCONTRADO -----")
                print("----------------------------------")
                print(f"\nID: {pro.getIdProyecto()}")
                print(f"NOMBRE: {pro.getNomProyecto()}")
                print(f"DESCRIPCION: {pro.getDescripcion()}")
                print(f"FECHA INICIO: {pro.getFechaInicio()}")
                print(f"ESTADO: {pro.getNombreEstado()}", end="\n\n")
                system("pause")
                return pro
        except Exception as e:
            print(f"\n¡ERROR! Al buscar el proyecto: {e}", end="\n\n")
            system("pause")
            return None

    def __modificarProyecto(self):
            try:
                system("cls")
                print("-------------------------------------------------")
                print("-------------- MODIFICAR PROYECTO ----------------")
                print("-------------------------------------------------")
                
                # Buscamos y recuperamos el objeto completo del proyecto
                pro = self.__buscarProyecto()
                
                if pro is None:
                    print("EL PROYECTO NO EXISTE, VERIFIQUE EL ID DEL PROYECTO...", end="\n\n")
                    system("pause")
                    return 
                
                id_proyecto = pro.getIdProyecto() #
                
                while True:
                    try:
                        system("cls")
                        print(f"Modificando: {pro.getNomProyecto()} (ID: {id_proyecto})")
                        print("-------------------------------------------------")
                        print("1- MODIFICAR NOMBRE PROYECTO")
                        print("2- MODIFICAR DESCRIPCIÓN PROYECTO")
                        print("3- MODIFICAR FECHA INICIO PROYECTO")
                        print("4- MODIFICAR ESTADO PROYECTO")
                        print("5- VOLVER")
                        
                        dato = int(input("\nDigite una opción: "))
                        
                        if dato == 5: return
                        
                        nuevo = None
                        if 1 <= dato <= 4:
                            if dato == 1:
                                nuevo = self.__obtener_apellido("MODIFICAR PROYECTO (NOMBRE)")
                            elif dato == 2:
                                nuevo = self.__obtener_apellido("MODIFICAR PROYECTO (DESCRIPCIÓN)")
                            elif dato == 3:
                                nuevo = self.__obtener_fecha("MODIFICAR PROYECTO (FECHA INICIO)")
                            elif dato == 4:
                                # Lógica amigable de cambio de estado
                                estado_actual = pro.getNombreEstado()
                                nuevo_nom = "DESHABILITADO" if estado_actual == "HABILITADO" else "HABILITADO"
                                
                                print(f"\nEl proyecto está actualmente {estado_actual}.")
                                print(f"¿Desea cambiarlo a {nuevo_nom}?")
                                print("1.- SÍ, CAMBIAR | 2.- NO, MANTENER")
                                
                                if input("\nSeleccione una opción: ") == "1":
                                    nuevo = 2 if estado_actual == "HABILITADO" else 1
                                else:
                                    print("\nOperación cancelada. No se realizaron cambios.")
                                    system("pause")
                                    continue # Volvemos a mostrar el menú de opciones

                            # Si llegamos aquí y 'nuevo' tiene datos, guardamos en la BD
                            if self.dao.modificarProyecto(dato, nuevo, id_proyecto):
                                print(f"\n¡ÉXITO! Se ha actualizado el proyecto correctamente.")
                            else:
                                print(f"\n¡ERROR! Hubo un problema al conectar con la base de datos.")
                            
                            system("pause")
                            return # Salimos al menú anterior tras el éxito
                        else:
                            print("\nOpción inválida. Elija entre 1 y 5.")
                            system("pause")
                            
                    except ValueError:
                        print("\n¡ERROR! El ID debe ser un número entero.")
                        system("pause")

            except Exception as e:
                print(f"\n¡ERROR! Inesperado al modificar el proyecto: {e}", end="\n\n")
                system("pause")
                return

    def __eliminarProyecto(self):
        try:
            while True:
                system("cls")
                print("--------------------------------------------")
                print("------------ ELIMINAR PROYECTO -------------")
                print("--------------------------------------------")
                pro = self.__buscarProyecto()
                if pro is None:
                    return
                if pro.getNombreEstado() == "DESHABILITADO":
                    print(f"El proyecto {pro.getNomProyecto()} (ID: {pro.getIdProyecto()}) ya se encuentra deshabilitado", end="\n\n")
                    system("pause")
                    return
                else:
                    try:
                        opcion = int(input(f"\nEstá seguro de desvincular el proyecto: {pro.getNomProyecto()} (ID: {pro.getIdProyecto()}) ? \n1- Si \n2- No \nDigite una opción: "))
                        system("cls")
                        if opcion == 1:
                            self.dao.eliminarProyecto(pro.getIdProyecto())
                            print(f"\nSe ha desvinculado el proyecto: {pro.getNomProyecto()} (ID: {pro.getIdProyecto()})", end="\n\n")
                            system("pause")
                            return
                        elif opcion == 2:
                            return
                        else:
                            print("\n--- Error De Opcion De Menú Eliminar Proyecto Debe Ser Del 1 al 2!! Volviendo al menu Eliminar Proyecto---", end="\n\n")
                            system("pause")
                            continue
                    except ValueError:
                        print("\n¡ERROR! Debe ingresar un número para ésta opcion.")
                        system("pause")
        except Exception as e:
            print(f"\n¡ERROR! Al eliminar el proyecto: {e}", end="\n\n")
            system("pause")
            return

    def __estadisticasProyectos(self):
        resumen = self.dao.obtenerEstadisticasProyecto()
        if not resumen:
            system("cls")
            print("---------------------------------------------------------")
            print("----------- ESTADÍSTICAS DE PROYECTOS ACTIVOS -----------")
            print("---------------------------------------------------------")

            print("\nNo hay datos suficientes para mostrar estadisticas.")
            system("pause")
            return
        else:
            system("cls")
            print("---------------------------------------------------------")
            print("----------- ESTADÍSTICAS DE PROYECTOS ACTIVOS -----------")
            print("---------------------------------------------------------")

            tabla = PrettyTable()
            tabla.field_names = ["PROYECTO", "CANT. EMPLEADOS", "COSTO PLANILLA"]
            for fila in resumen:
                nombre = fila[0]
                cantidad_empleados = fila[1]
                costo = fila[2] if fila[2] else 0
                tabla.add_row([nombre, cantidad_empleados, f"${costo:,.2f}"])
            print(tabla)
            system("pause")


#-------------------------------------------------------------------------------------------
#   FUNCIONES MENU ASIGNACION DE PROYECTOS
    def __asignarEmpleado(self):
        try:
            system("cls")
            print("-------------------------------------------------")
            print("-------------- ASIGNAR EMPLEADOS ----------------")
            print("-------------------------------------------------")
            self.__listarEmpleadosSinAsignar()
            self.__listarProyectos()
            print("\nINGRESE EL RUT DEL EMPLEADO A ASIGNAR:", end="\n\n")
            rut = self.__obtener_rut_validado(titulo_menu="ASIGNAR EMPLEADO (RUT)")
            pro = input("\nINGRESE EL ID DEL PROYECTO AL CUAL DESEA ASIGNAR AL EMPLEADO: ", end="\n\n")
            if not pro.isdigit():
                print("EL ID DEL PROYECTO DEBE SER UN NUMERO ENTERO", end="\n\n")
                system("pause")
                return
            else:
                pro = int(pro)
                if self.dao.asignarEmpleadoaProyecto(rut, pro):
                    print(f"EL EMPLEADO {rut} SE HA ASIGNADO AL PROYECTO {pro} EXITOSAMENTE", end="\n\n")
                    system("pause")
                    return
                else:
                    print("\nNO SE ENCONTRÓ EL EMPLEADO O EL PROYECTO ES INVÁLIDO")
                    system("pause")
        except Exception as e:
            print(f"\n¡ERROR! Al asignar el empleado: {e}", end="\n\n")
            system("pause")
          

    def __reasignarEmpleado(self):
        try:
            system("cls")
            print("-----------------------------------------------------------")
            print("------------------ REASIGNAR EMPLEADO ---------------------")
            print("-----------------------------------------------------------")
            print("Ingrese el RUT del empleado a reasignar y el ID del proyecto al cual desea asignarlo: ", end="\n\n")
            system("pause")
            empleado = self.__buscarEmpleado()
            rut = empleado.getRut()
            proyecto = self.__buscarProyecto()
            id_proyecto = proyecto.getIdProyecto()
            while True:
                print(F"Está seguro de reasignar a {empleado.getNombres()} {empleado.getApellidoPaterno()} al proyecto {proyecto.getNomProyecto()}")
                opcion = input("\n'S' para SI o 'N' para NO: ")
                if opcion.upper() == 'S':
                    if self.dao.reasignarEmpleado(rut, id_proyecto):
                        print("Empleado reasignado exitosamente.", end="\n\n")
                        system("pause")
                        return
                    else:
                        print("Error al reasignar el empleado.", end="\n\n")
                        system("pause")
                        return
                elif opcion.upper() == 'N':
                    print("Operación cancelada.", end="\n\n")
                    system("pause")
                    return
                else:
                    print("Opción inválida. Intente nuevamente.", end="\n\n")
                    system("pause")
                    continue
        except Exception as e:
            print(f"\n¡ERROR! Al reasignar el empleado: {e}", end="\n\n")
            system("pause")


    def __listarEmpleadosAsignados(self):
        try:
            datos_empleados = self.dao.listarEmpleadosGeneral(4)
            if not datos_empleados:
                print("No hay empleados asignados a ningún proyecto.", end="\n\n")
                system("pause")
                return
            else:
                tabla = PrettyTable()
                tabla.field_names = ["RUT", "NOMBRE", "AP. PATERNO", "AP. MATERNO", "TELEFONO", "EMAIL", "SALARIO", "ESTADO", "ID PROYECTO"]
                for d in datos_empleados:
                    tabla.add_row(d)
                print(tabla, end="\n\n")
                system("pause")
        except Exception as e:
            print(f"\n¡ERROR! Al listar los empleados asignados: {e}", end="\n\n")
            system("pause")
            return

    def __listarEmpleadosSinAsignar(self):
        try:
            datos_empleados = self.dao.listarEmpleadosGeneral(5)
            if not datos_empleados:
                print("Todos los empleados se encuentran asignados a un proyecto actualmente.", end="\n\n")
                system("pause")
                return
            else:
                lista = PrettyTable()
                lista.field_names = ["RUT", "NOMBRE", "AP. PATERNO", "AP. MATERNO", "TELEFONO", "EMAIL", "SALARIO", "ESTADO"]
                for d in datos_empleados:
                    lista.add_row(d[:-1])
                print(lista, end="\n\n")
                system("pause")
        except Exception as e:
            print(f"\n¡ERROR! Al listar los empleados sin asignar: {e}", end="\n\n")
            system("pause")
            return
