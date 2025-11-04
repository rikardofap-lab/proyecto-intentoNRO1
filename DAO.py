from Empleado import empleado
from Proyecto import proyecto
from TipoAcceso import tipoAcceso
from os import system
import pymysql
from cryptography.fernet import Fernet

class dao:
    def __init__(self):
        pass

    # Clave para encriptar/desencriptar. DEBE ser la misma que usaste para generar la clave.
    # En una aplicación real, esto se gestionaría de forma más segura (ej. variables de entorno).
    __clave_fernet = b"5Jp-fpyG6Cx8bgaPeBMWQtCng_Gjr6eUmaTvu3R5IUs="
#---------------------------------------------------------------------------------------------

    def conectar(self):
        self.con = pymysql.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "bd_intento_nro1" 
        )
        self.cursor = self.con.cursor()
#----------------------------------------------------------------------------------------------

    def desconectar(self):
        self.con.close()

#----------------------------------------------------------------------------------------------
# COMPRUEBO SI EL RUT DEL EMPLEADO ESTÁ O NO EN LA BASE DE DATOS
    def comprobarRutEmpleado(self, rut_formateado):
        try:
            sql = "SELECT rut_emp FROM empleados WHERE rut_emp = %s"
            self.conectar()
            self.cursor.execute(sql, (rut_formateado,))
            rs = self.cursor.fetchone()
            self.desconectar()
            return rs
        except Exception as e:
            system("cls")
            print(f"Error al comprobar el RUT del empleado (DAO): {e}")

#----------------------------------------------------------------------------------------------
# CREA EMPLEADO
    def insertarEmpleado(self, empleado):
        try:
            # --- LÓGICA DE ENCRIPTACIÓN ---
            contrasena_plana = empleado.getContrasena()
            contrasena_encriptada = None

            # Solo encriptamos si se proporcionó una contraseña (para empleados con acceso)
            if contrasena_plana:
                f = Fernet(self.__clave_fernet)
                # La contraseña se convierte a bytes, se encripta, y luego se guarda como string para la BD.
                contrasena_encriptada = f.encrypt(contrasena_plana.encode()).decode('utf-8')

            # --- FIN LÓGICA DE ENCRIPTACIÓN ---

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
                contrasena_encriptada # Usamos la contraseña ya encriptada
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
            # 1. Buscar al usuario por su nombre de usuario (nom_usu)
            sql = "SELECT * FROM empleados WHERE nom_usu = %s"
            self.conectar()
            self.cursor.execute(sql, (nomUsuario,))
            rs = self.cursor.fetchone()
            self.desconectar()

            # 2. Si no se encuentra el usuario, el login falla
            if rs is None:
                return None
            
            else:
                # 3. Si se encuentra, desencriptar la contraseña de la BD y comparar
                contrasena_bd_encriptada = rs[15]

                if not contrasena_bd_encriptada: # Si no hay contraseña en la BD
                    return None
                else:
                    f = Fernet(self.__clave_fernet)

                    try:
                        contrasena_bd_desencriptada = f.decrypt(contrasena_bd_encriptada.encode()).decode()
                    except Exception:
                        return None # Si no se puede desencriptar, el login falla

                    # 4. Comparar la contraseña desencriptada con la que ingresó el usuario
                    if contrasena_bd_desencriptada == contrasena:
                        # ¡Éxito! Creamos y devolvemos el objeto empleado con sus datos
                        emp = empleado()
                        emp.setRut(rs[1])
                        emp.setNombres(rs[2])
                        emp.setIdTipoAcc(rs[13])
                        emp.setNombreUsuario(rs[14])
                        return emp
                    else:
                        return None # La contraseña no coincide
        except Exception as e:
            system("cls")
            print(f"Error al iniciar sesion (DAO): {e}")
#----------------------------------------------------------------------------------------------
# OBTENER EMPLEADOS (PARA LISTAR)
    def ObtenerEmpleado(self):
        try:
            self.conectar()
            sql = """SELECT rut_emp, nom_emp, app_emp, apm_emp, tel_emp, ema_emp, sal_emp, nom_est, id_pro 
                FROM empleados e 
                INNER JOIN estados est 
                ON e.id_est = est.id_est 
                ORDER BY nom_emp ASC"""
            self.cursor.execute(sql,)
            rs = self.cursor.fetchall()
            self.desconectar()
            return rs
                
        except Exception as e:
            system("cls")
            print(f"Error al obtener el empleado (DAO): {e}")
#----------------------------------------------------------------------------------------------
# BUSCAR EMPLEADO   
    def BuscarEmpleado(self, rut):
        try:
            self.conectar()
            sql = """SELECT rut_emp, nom_emp, app_emp, apm_emp, dir_emp, tel_emp, ema_emp, fec_nac_emp, fec_ini_emp, sal_emp, nom_est, id_pro, nom_tip_acc 
                FROM empleados e 
                INNER JOIN estados est 
                ON e.id_est=est.id_est
                INNER JOIN tipo_acceso tip_acc 
                ON e.id_tip_acc=tip_acc.id_tip_acc
                WHERE rut_emp =%s
                AND e.id_est = 1
                ORDER BY nom_emp ASC"""
            self.cursor.execute(sql, (rut,))
            rs = self.cursor.fetchone()
            self.desconectar()
            if rs is None:
                return None
            else:
                emp = empleado()
                emp.setRut(rs[0])
                emp.setNombres(rs[1])
                emp.setApellidoPaterno(rs[2])
                emp.setApellidoMaterno(rs[3])
                emp.setDireccion(rs[4])
                emp.setNroTelefono(rs[5])
                emp.setEmail(rs[6])
                emp.setFechaNacimiento(rs[7])
                emp.setFechaInicioContrato(rs[8])
                emp.setSalario(rs[9])
                emp.setIdEstado(rs[10])
                emp.setIdProyecto(rs[11])
                emp.setIdTipoAcc(rs[12])
                return emp
        except Exception as e:
            system("cls")
            print(f"Error al buscar el empleado (DAO): {e}")
#----------------------------------------------------------------------------------------------
# BUSCAR EMPLEADOS ESXISTENTES (HABILITADOS)
    def modificarEmpleado(self, dato, nuevo, rut):
        try:
            sql = ""
            if dato == 1:
                sql = "UPDATE empleados SET nom_emp = %s WHERE rut_emp = %s"
            elif dato == 2:
                sql = "UPDATE empleados SET dir_emp = %s WHERE rut_emp = %s"
            elif dato == 3:
                sql = "UPDATE empleados SET tel_emp = %s WHERE rut_emp = %s"
            elif dato == 4:
                sql = "UPDATE empleados SET ema_emp = %s WHERE rut_emp = %s"
            elif dato == 5:
                sql = "UPDATE empleados SET sal_emp = %s WHERE rut_emp = %s"
            elif dato == 6:
                sql = "UPDATE empleados SET id_est = %s WHERE rut_emp = %s"
            elif dato == 7:
                sql = "UPDATE empleados SET id_pro = %s WHERE rut_emp = %s"
            self.conectar()
            val = (nuevo, rut)
            self.cursor.execute(sql, val)
            self.con.commit()
            self.desconectar()
        except Exception as e:
            system("cls")
            print(f"Error al modificar el empleado (DAO): {e}")