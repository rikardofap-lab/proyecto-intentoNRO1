from database.DB_config import DBConfig
from core.Proyecto import proyecto

class proyectoDAO(DBConfig):

    def __init__(self):
        super().__init__()

    
    def comprobarNombreProyecto(self, nombre):
            try:
                # Buscamos el nombre exacto en la tabla Proyectos
                sql = "SELECT nom_pro FROM Proyectos WHERE nom_pro = %s"
                self.conectar()
                self.cursor.execute(sql, (nombre,))
                rs = self.cursor.fetchone() # Devuelve el nombre si existe, o None si no
                self.desconectar()
                return rs
            except Exception as e:
                print(f"Error al comprobar nombre del proyecto (DAO): {e}")
                return None

#--------------------------------------------------------------------------------------------------------------------------------
# CREAR EL PROYECTO
    def insertarProyecto(self, proyecto):
        try:
            sql = """INSERT INTO proyectos (
                nom_pro, des_pro, fec_ini_pro, id_est) VALUES (%s, %s, %s, %s)"""
            valores = (
                proyecto.getNomProyecto(),
                proyecto.getDescripcion(),
                proyecto.getFechaInicio(),
                proyecto.getIdEstado()
            )
            self.conectar()
            self.cursor.execute(sql, valores)
            self.con.commit()
            self.desconectar()
            return True
        except Exception as e:
            print(f"Error al insertar el proyecto (DAO): {e}")
            return False
#--------------------------------------------------------------------------------------------------------------------------------
# HERRAMIENTA PARA LISTAR TODOS LOS PROYECTOS SEGÚN SU ESTADO
    def listarProyectosGeneral(self, criterio):
        try:
            sql = """SELECT id_pro, nom_pro, des_pro, fec_ini_pro, nom_est 
                    FROM proyectos p INNER JOIN estados e ON p.id_est = e.id_est """
            if criterio == 1: sql += "ORDER BY nom_pro ASC" # Todos
            elif criterio == 2: sql += "WHERE e.id_est = 1 ORDER BY nom_pro ASC" # Habilitados
            elif criterio == 3: sql += "WHERE e.id_est = 2 ORDER BY nom_pro ASC" # Deshabilitados

            self.conectar()
            self.cursor.execute(sql)
            rs = self.cursor.fetchall()
            self.desconectar()
            return list(rs) if rs else []
        except Exception as e:
            print(f"Error en listado de proyectos (DAO): {e}")
            return []
#--------------------------------------------------------------------------------------------------------------------------------

    def buscarProyecto(self, id_proyecto):
        try:
            sql = """SELECT id_pro, nom_pro, des_pro, fec_ini_pro, nom_est 
            FROM proyectos p
            INNER JOIN estados e
            ON p.id_est = e.id_est 
            WHERE id_pro = %s"""
            self.conectar()
            self.cursor.execute(sql, (id_proyecto,))
            rs = self.cursor.fetchone()
            self.desconectar()
            if rs is None:
                return None
            else:
                pro = proyecto()
                pro.setIdProyecto(rs[0])
                pro.setNomProyecto(rs[1])
                pro.setDescripcion(rs[2])
                pro.setFechaInicio(rs[3])
                pro.setNombreEstado(rs[4])
                return pro
        except Exception as e:
            print(f"Error al buscar el proyecto (DAO): {e}")
#--------------------------------------------------------------------------------------------------------------------------------

    def modificarProyecto(self, dato, nuevo, id_proyecto):
        try:
            sql = ""
            if dato == 1:
                sql = "UPDATE proyectos SET nom_pro = %s WHERE id_pro = %s"
            elif dato == 2:
                sql = "UPDATE proyectos SET des_pro = %s WHERE id_pro = %s"
            elif dato == 3:
                sql = "UPDATE proyectos SET fec_ini_pro = %s WHERE id_pro = %s"
            elif dato == 4: 
                sql = "UPDATE proyectos SET id_est = %s WHERE id_pro = %s"
            self.conectar()
            self.cursor.execute(sql, (nuevo, id_proyecto))
            self.con.commit()
            self.desconectar()
            return True
        except Exception as e:
            print(f"Error al modificar el proyecto (DAO): {e}")
            return False
#--------------------------------------------------------------------------------------------------------------------------------
        
    def eliminarProyecto(self, id_proyecto):
        try:
            sql = "UPDATE proyectos SET id_est = 2 WHERE id_pro = %s"
            self.conectar()
            self.cursor.execute(sql, (id_proyecto,))
            self.con.commit()
            self.desconectar()
            return True
        except Exception as e:
            print(f"Error al eliminar el proyecto (DAO): {e}")
            return False
        finally:
            self.desconectar()
#--------------------------------------------------------------------------------------------------------------------------------

    def obtenerEstadisticasProyecto(self):
        try:
            sql = """
                SELECT p.nom_pro, COUNT(e.id_emp), SUM(IFNULL(e.sal_emp, 0))
                FROM proyectos p
                LEFT JOIN empleados e
                ON p.id_pro = e.id_pro
                AND e.id_est = 1
                GROUP BY p.nom_pro
                """
            self.conectar()
            self.cursor.execute(sql)
            rs = self.cursor.fetchall()
            return rs
        except Exception as e:
            print(f"Error al obtener las estadísticas de proyectos (DAO): {e}")
            return []
        finally:
            self.desconectar()
#--------------------------------------------------------------------------------------------------------------------------------

    def asignarEmpleadoaProyecto(self, rut_empleado, id_proyecto):
        try:
            sql = """ UPDATE empleados 
            SET id_pro = %s
            WHERE rut_emp = %s"""
            self.conectar()
            self.cursor.execute(sql, (id_proyecto, rut_empleado))
            self.con.commit()
            return self.cursor.rowcount > 0
        except Exception as e:
            print(f"Error al asignar el empleado al proyecto (DAO): {e}")
        finally:
            self.desconectar()
#--------------------------------------------------------------------------------------------------------------------------------

    def reasignarEmpleado(self, rut, id_proyecto):
        try:
            sql = """ UPDATE empleados
            SET id_pro = %s
            WHERE rut_emp = %s"""
            self.conectar()
            self.cursor.execute(sql, (id_proyecto, rut))
            self.con.commit()
            return self.cursor.rowcount
        except Exception as e:
            print(f"Error al reasignar el empleado al proyecto (DAO): {e}")
        finally:
            self.desconectar()
            