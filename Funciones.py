from Empleado import Empleado
from Proyecto import Proyecto
from TipoAcceso import TipoAcceso
from Usuario import Usuario
from DAO import DAO
from prettytable import PrettyTable
from os import system
import os

emp = Empleado()
pro = Proyecto()
tip = TipoAcceso()
usu = Usuario()
dao = DAO()

class Funciones:
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
                        
            except ValueError:
                    print("\n¡ERROR! LA OPCION DEBE INGRESARSE SOLO CON NUMEROS (1, 2 Y 3)")
                    system("pause")
                    self.menuInicial()
            except Exception as e:
                print("\n¡Error Al Capturar Opcion De Menú Inicial!!", end="\n\n")
                system("pause")
                self.menuInicial()

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
            except ValueError:
                print("\n¡ERROR! La opcion solo puede ser un numero entero positivo")
                system("pause")
                self.__menuGerente()
            except Exception as e:
                print("\n¡Error Al Capturar Opcion De Menú Gerente!!", end="\n\n")
                system("pause")
                self.__menuGerente()

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
                self.__menuGestionProyectos()
            except Exception as e:
                print("\n¡Error Al Capturar Opcion De Menú Gestion Proyectos!!", end="\n\n")
                system("pause")
                self.__menuGestionProyectos()
                system("pause")

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
                else:
                    break
            except ValueError:
                print("\nEl rut debe ser escrito solo con numeros y guion")
                system("pause")
                self.menuInicial()
            except Exception as e:
                print("\n--- Error Al Capturar Rut (Login)!! ---", end="\n\n")
                system("pause")
                self.menuInicial()
        #-----------------------------------------------------------------------------------------
        while True:
            try:
                system("cls")
                print("--- MENU INICIAL (INICIO DE SESIÓN) ---")
                contrasena = input("\nIngrese su contraseña: ")
                if len(contrasena.strip()) > 1 or len(contrasena.strip()) < 20:
                    print("\n--- La Contraseña Debe Tener Entre 1 y 20 Caracteres!! ---", end="\n\n")
                    system("pause")
                else:
                    break
            except Exception as e:
                print("\n--- Error Al Capturar Contraseña (Login)!! ---", end="\n\n")
                system("pause")
                self.menuInicial()

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
            except ValueError:
                print("\n¡ERROR! La opcion solo puede ser un numero entero positivo")
                system("pause")
                self.__asignacionProyectos()

            except Exception as e:
                print("\n¡Error Al Capturar Opcion De Menú Asignación Proyectos!!", end="\n\n")
                system("pause")
                self.__asignacionProyectos()



    def salir(self):
        system("cls")
        os._exit(1)