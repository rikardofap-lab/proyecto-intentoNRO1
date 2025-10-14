from Empleado import Empleado
from Proyecto import Proyecto
from TipoAcceso import TipoAcceso
from Usuario import Usuario
from os import system
import pymysql
from cryptography.fernet import Fernet

class DAO:
    def __init__(self):
        pass
#----------------------------------------------------------------------------------------------
    def conectar(self):
        try:
            self.con = pymysql.connect(
                host = "localhost",
                user = "root",
                password = "",
                db = "proyecto_Vera_Wil"
            )
            self.cursor = self.con.cursor()
            print("Conexion Exitosa")
        except Exception as e:
            print(f"ERROR DE CONEXION A LA BASE DE DATOS (DAO): {e}")

    def desconectar(self):
        self.con.close()

#----------------------------------------------------------------------------------------------