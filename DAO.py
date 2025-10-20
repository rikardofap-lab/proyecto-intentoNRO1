from Empleado import empleado
from Proyecto import proyecto
from TipoAcceso import tipoAcceso
from Usuario import usuario
from os import system
import pymysql
from cryptography.fernet import Fernet

class dao:
    def __init__(self):
        pass
#---------------------------------------------------------------------------------------------
    def conectar(self):
        try:
            self.con = pymysql.connect(
                host = "localhost",
                user = "root",
                password = "",
                db = "BD_IntentoNro1"
            )
            self.cursor = self.con.cursor()
            print("Conexion Exitosa")
        except Exception as e:
            print(f"ERROR DE CONEXION A LA BASE DE DATOS (DAO): {e}")
#----------------------------------------------------------------------------------------------

    def desconectar(self):
        self.con.close()

#----------------------------------------------------------------------------------------------

    def comprobarRutEmpleado(self, rut_formateado):
        try:
            sql = "SELECT rut_emp FROM empleados WHERE rut_emp = %s"
            self.conectar()
            self.cursor.execute(sql, rut_formateado)
            rs = self.cursor.fetchone()
            self.desconectar()
            return rs
        except Exception as e:
            system("cls")
            print(f"Error al comprobar el RUT del empleado (DAO): {e}")
