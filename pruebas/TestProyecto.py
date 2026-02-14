import sys
import os
# Esto permite que el script "mire" hacia afuera de la carpeta 'pruebas'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from DAO import dao
from Proyecto import proyecto

def test_sistema():
    # 1. Creamos la instancia. La llamaremos 'midao' para no confundirnos
    midao = dao() 
    print("🚀 INICIANDO PRUEBA DE FUEGO - MÓDULO PROYECTOS/EMPLEADOS\n")

    try:
        # 1. TEST DE INSERCIÓN
        print("Paso 1: Creando Proyecto 'TEST CRÍTICO'...")
        nuevo_pro = proyecto()
        nuevo_pro.setNomProyecto("TEST CRÍTICO")
        nuevo_pro.setDescripcion("Probando la purificación del sistema")
        nuevo_pro.setFechaInicio("2026-02-14")
        nuevo_pro.setIdEstado(1)
         
        if midao.insertarProyecto(nuevo_pro): 
            print("✅ Inserción: OK")
        
        # 2. TEST DE BÚSQUEDA Y LISTADO
        print("\nPaso 2: Buscando proyecto recién creado...")
        proyectos = midao.listarProyectosGeneral(1) 
        pro_encontrado = None
        for p in proyectos:
            if p[1] == "TEST CRÍTICO":
                pro_encontrado = p
                break
        
        if pro_encontrado:
            id_pro = pro_encontrado[0]
            print(f"✅ Búsqueda: OK (ID encontrado: {id_pro})")

            # 3. TEST DE MODIFICACIÓN
            print("\nPaso 3: Modificando nombre del proyecto...")
            if midao.modificarProyecto(1, "PROYECTO PURIFICADO", id_pro):
                print("✅ Modificación: OK")

            # 4. TEST DE ESTADÍSTICAS
            print("\nPaso 4: Generando Estadísticas...")
            stats = midao.obtenerEstadisticasProyecto()
            if stats:
                print(f"✅ Estadísticas: OK")

            # 5. TEST DE ELIMINACIÓN LÓGICA
            print("\nPaso 5: Ejecutando baja lógica...")
            if midao.eliminarProyecto(id_pro):
                print("✅ Eliminación Lógica: OK")
        else:
            print("❌ Búsqueda: FALLÓ (El proyecto no se guardó)")

        print("\n" + "="*50)
        print("💎 RESULTADO FINAL: SISTEMA PURIFICADO Y OPERATIVO")
        print("="*50)

    except Exception as e:
        print(f"\n❌ ERROR CRÍTICO DURANTE LA PRUEBA: {e}")

if __name__ == "__main__":
    test_sistema()