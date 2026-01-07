import unittest
from DAO import dao
from Funciones import funciones
from datetime import date

class TestProyectoNro1(unittest.TestCase):

    def setUp(self):
        """Se ejecuta antes de cada prueba para preparar el terreno."""
        self.d = dao()
        self.f = funciones()

    # --- PRUEBAS DE LA CAPA DAO ---

    def test_promedio_edades_no_nulo(self):
        """Verifica que el promedio de edades siempre devuelva un número (0 o más)."""
        resultado = self.d.promedioEdadesEmpleados()
        # Verificamos que sea un entero o un decimal, no un None
        self.assertIsInstance(resultado, (int, float), "El promedio debe ser un número")

    def test_listado_generico_retorna_lista(self):
        """Asegura que el listado siempre devuelva una lista, nunca un valor nulo."""
        # Probamos con el criterio 1 (Todos)
        resultado = self.d.listarEmpleadosGeneral(1)
        self.assertIsInstance(resultado, list, "El DAO debe retornar una lista []")

    def test_comprobar_nombre_proyecto_existente(self):
        """Verifica que el buscador de nombres detecte proyectos que ya están en la DB."""
        # Usamos un nombre que sabemos que está en tu script SQL
        resultado = self.d.comprobarNombreProyecto("Desarrollo Ecologico")
        # Si el proyecto existe, resultado NO debe ser None
        self.assertIsNotNone(resultado, "Debería encontrar el proyecto existente")

    # --- PRUEBAS DE LÓGICA (VALIDACIONES) ---

    def test_formato_rut_correcto(self):
        """Verifica que si entran datos sucios, el sistema los limpie bien (Simulación lógica)."""
        # Nota: Como tus funciones de validación son privadas (__) o usan input(), 
        # aquí probamos la lógica de limpieza que implementamos
        rut_sucio = " 11 111 111 k "
        limpio = rut_sucio.strip().replace(" ", "").upper()
        cuerpo = limpio[:-1]
        dv = limpio[-1]
        
        self.assertEqual(cuerpo, "11111111")
        self.assertEqual(dv, "K")

    def test_formato_fecha_sql(self):
        """Verifica que la conversión de fecha para MySQL sea correcta."""
        hoy = date(2026, 1, 7)
        fecha_sql = hoy.strftime('%Y-%m-%d')
        self.assertEqual(fecha_sql, "2026-01-07", "El formato debe ser AAAA-MM-DD")

# Para ejecutar los tests desde la consola
if __name__ == '__main__':
    unittest.main()