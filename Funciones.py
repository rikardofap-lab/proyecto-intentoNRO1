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

    def menuInicial(self):
        while True:
            try:
                system("cls")
                print("-------------------------")
                print("------ MENU INICIAL------")
                print("-------------------------")
                print("1.- INICIAR SESION")
                print("3.- SALIR")
                op = int(input("\nDigite una opción: "))

                if op == 1:
                    self.__iniciarSesion()
                elif op == 2:
                    self.__salir()
                else:
                    print("\n--- Error De Opcion De Menú Inicial!! ---", end="\n\n")
                    system("pause")
                    
            except ValueError:
                print("ERROR! LA OPCION DEBE INGRESARSE SOLO CON LOS NUMEROS (1, 2 Y 3)")


    def __menuGerente(self):
        pass

    def __menuGestorEmple(self):
        pass

    def __iniciarSesion(self):
        pass

    def __salir(self):
        system("cls")
        os._exit(1)