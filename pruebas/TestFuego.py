import unittest
from database.DAO import dao
from core.Empleado import empleado
from core.Proyecto import proyecto

class TestFuegoTotal(unittest.TestCase):
    def setUp(self):
        self.d = dao()

    def test_circuito_completo_empleado(self):
        """Prueba insertar, buscar y promediar en un solo flujo."""
        print("\n🔥 Probando circuito de Empleados...")
        
        # 1. Crear objeto de prueba
        e = empleado()
        rut_test = "99999999-9"
        e.setRut(rut_test)
        e.setNombres("Test")
        e.setApellidoPaterno("Fuego")
        e.setApellidoMaterno("Pura")
        e.setSexo(1)
        e.setDireccion("Calle Test 123")
        e.setNroTelefono("+56900000000")
        e.setEmail("test@fuego.cl")
        e.setFechaNacimiento("1990-01-01")
        e.setFechaInicioContrato("2024-01-01")
        e.setSalario(1000000)
        e.setSexo(1)
        e.setIdEstado(1)
        e.setIdTipoAcc(3)

        # 2. Insertar y verificar
        self.d.insertarEmpleado(e)
        buscado = self.d.BuscarEmpleado(rut_test)
        self.assertIsNotNone(buscado, "❌ El empleado no se guardó en la DB")
        print("✅ Inserción y Búsqueda: OK")

        # 3. Probar Promedios
        promedio = self.d.promedioSalariosEmpleados()
        self.assertGreater(promedio, 0, "❌ El promedio de salarios falló")
        print(f"✅ Promedio de Salarios: ${promedio}")

    def test_circuito_proyectos(self):
        """Prueba la creación y validación de proyectos."""
        print("\n🔥 Probando circuito de Proyectos...")
        
        # 1. Crear proyecto de prueba
        p = proyecto()
        nombre_p = "Proyecto Purificacion"
        p.setNomProyecto(nombre_p)
        p.setDescripcion("Una descripcion de mas de veinte caracteres para pasar el filtro")
        p.setFechaInicio("2026-01-07")
        p.setIdEstado(1)

        # 2. Insertar
        self.d.insertarProyecto(p)
        
        # 3. Verificar duplicado (Debe dar NO NONE porque ya existe)
        existe = self.d.comprobarNombreProyecto(nombre_p)
        self.assertIsNotNone(existe, "❌ El validador de nombres no detectó el proyecto")
        print(f"✅ Validación de Duplicados para '{nombre_p}': OK")

        # 4. Listar
        lista = self.d.listarProyectosGeneral(1)
        self.assertGreater(len(lista), 0, "❌ El listado de proyectos volvió vacío")
        print(f"✅ Listado General de Proyectos: OK ({len(lista)} encontrados)")

if __name__ == '__main__':
    unittest.main()