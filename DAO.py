from Empleado import empleado
from Proyecto import proyecto
from TipoAcceso import tipoAcceso
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
# COMPRUEBO SI EL RUT DEL EMPLEADO ESTÁ O NO EN LA BASE DE DATOS
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

#----------------------------------------------------------------------------------------------
# COMPRUEBO SI EL NOMBRE DE USUARIO DEL EMPLEADO ESTÁ O NO EN LA BASE DE DATOS
    def comprobarNombreUsuario(self, nomUsuario):
        try:
            sql = "SELECT nom_usu FROM empleados WHERE nom_usu = %s"
            self.conectar()
            self.cursor.execute(sql, nomUsuario)
            rs = self.cursor.fetchone()
            self.desconectar()
            return rs
        except Exception as e:
            system("cls")
            print(f"Error al comprobar el NOMBRE DE USUARIO del empleado (DAO): {e}")

#----------------------------------------------------------------------------------------------
# CREA EMPLEADO
    def insertarEmpleado(self, empleado):
        try:
            sql = """INSERT INTO empleados (
                         rut_emp, nom_emp, app_emp, apm_emp, dir_emp, 
                         tel_emp, ema_emp, fec_nac_emp, fec_ini_emp, 
                         sal_emp, id_est, id_pro, id_tip_acc, 
                         nom_usu, con_usu) 
                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            valores = (
                empleado.getRut(),
                empleado.getNombres(),
                empleado.getApellidoPaterno(),
                empleado.getApellidoMaterno(),
                empleado.getDireccion(),
                empleado.getNroTelefono(),
                empleado.getEmail(),
                empleado.getFechaNacimiento(),
                empleado.getfechaInicioContrato(),
                empleado.getSalario(),
                empleado.getIdEstado(),
                empleado.getIdProyecto(),
                empleado.getIdTipoAcc(),
                empleado.getNombreUsuario(),
                empleado.getContrasena()
            )
            self.conectar()
            self.cursor.execute(sql, valores)
            self.con.commit()
            self.desconectar()
        except Exception as e:
            system("cls")
            print(f"Error al insertar el empleado (DAO): {e}")

    def Login(self, nomUsuario, contrasena):
        try:
            sql = "SELECT nom_usu, con_usu FROM empleados WHERE nom_usu = %s AND con_usu = %s"
            self.conectar()
            self.cursor.execute(sql, (nomUsuario, contrasena))
            rs = self.cursor.fetcone()
            self.desconectar()

            if rs is None:
                return None
            else:
                pass
    


            
