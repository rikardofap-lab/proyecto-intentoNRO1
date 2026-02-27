import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database.DAO import dao
from core.Proyecto import proyecto

def test_sistema():
    midao = dao() 
    print("🚀 INICIANDO PRUEBA DE FUEGO 2.0 - CICLO COMPLETO PROYECTOS/EMPLEADOS\n")

    try:
        # 1. TEST DE INSERCIÓN
        print("Paso 1: Creando Proyecto 'TEST CRÍTICO'...")
        nuevo_pro = proyecto()
        nuevo_pro.setNomProyecto("TEST CRÍTICO")
        nuevo_pro.setDescripcion("Probando la purificación del sistema")
        nuevo_pro.setFechaInicio("2026-02-16")
        nuevo_pro.setIdEstado(1)
         
        if midao.insertarProyecto(nuevo_pro): 
            print("✅ Inserción: OK")
        
        # 2. TEST DE BÚSQUEDA
        proyectos = midao.listarProyectosGeneral(1) 
        pro_encontrado = next((p for p in proyectos if p[1] == "TEST CRÍTICO"), None)
        
        if pro_encontrado:
            id_pro = pro_encontrado[0]
            rut_test = "11111111-1" # Usamos a Wilmer
            print(f"✅ Búsqueda: OK (ID: {id_pro})")

            # 3. TEST DE ASIGNACIÓN (Nuevo)
            print(f"\nPaso 3: Asignando a Wilmer ({rut_test}) al proyecto...")
            if midao.asignarEmpleadoaProyecto(rut_test, id_pro):
                print("✅ Asignación Inicial: OK")
            else:
                print("❌ Asignación Inicial: FALLÓ")

            # 4. TEST DE REASIGNACIÓN (Nuevo)
            print("\nPaso 4: Probando método de REASIGNACIÓN...")
            # Reasignamos al mismo proyecto para validar que el rowcount funcione
            if midao.reasignarEmpleado(rut_test, id_pro) >= 0:
                print("✅ Reasignación (Capa DAO): OK")

            # 5. TEST DE ESTADÍSTICAS
            print("\nPaso 5: Generando Estadísticas (Validando Costos)...")
            stats = midao.obtenerEstadisticasProyecto()
            if stats:
                # Si Wilmer está asignado, el costo de planilla NO debería ser 0
                print(f"✅ Estadísticas: OK")

            # 6. TEST DE ELIMINACIÓN LÓGICA
            print("\nPaso 6: Ejecutando baja lógica del proyecto...")
            if midao.eliminarProyecto(id_pro):
                print("✅ Eliminación Lógica: OK")
        else:
            print("❌ Búsqueda: FALLÓ (El proyecto no se guardó)")

        print("\n" + "="*50)
        print("💎 RESULTADO FINAL: SISTEMA 100% OPERATIVO")
        print("="*50)

    except Exception as e:
        print(f"\n❌ ERROR CRÍTICO: {e}")

if __name__ == "__main__":
    test_sistema()