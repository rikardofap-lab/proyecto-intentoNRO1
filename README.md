# Proyecto Nro. 1: Sistema de Gestión de Empleados y Proyectos

Este sistema es una aplicación de consola desarrollada en **Python** para gestionar el personal y los proyectos de una organización, utilizando una base de datos relacional.

## 🛠️ Tecnologías Utilizadas
* **Lenguaje:** Python 3.
* **Base de Datos:** MySQL (conectada mediante `pymysql`).
* **Librerías Extra:** * `PrettyTable`: Para la visualización de datos en tablas.
    * `Cryptography (Fernet)`: Para la encriptación de contraseñas de usuario.
    * `Datetime`: Para el manejo de fechas de nacimiento y contratos.

## 🏗️ Arquitectura del Software
El proyecto sigue el patrón de diseño **DAO (Data Access Object)**, separando la lógica de negocio de la persistencia de datos.

### Clases Principales:
* **`Persona.py`**: Clase base con datos personales.
* **`Empleado.py`**: Hereda de Persona y añade datos laborales (sueldo, cargo, login).
* **`DAO.py`**: Contiene todas las consultas SQL y la conexión a la base de datos `bd_intento_nro1`.
* **`Funciones.py`**: Clase controladora que maneja los menús y validaciones de entrada.

# 📝 Bitácora de Desarrollo - Proyecto Nro. 1

## 📅 Fecha: 02 de enero, 2026
**Objetivo:** Finalizar la lógica de estadísticas y asegurar la robustez en la comunicación entre la capa DAO y la capa de Funciones.

---

### ✅ Logros y Avances

#### 1. Capa de Acceso a Datos (`DAO.py`)
* **Cálculos Estadísticos:**
    * Se implementó el método `promedioEdadesEmpleados` utilizando la función `TIMESTAMPDIFF` de SQL para obtener cálculos precisos basados en la columna `fec_nac_emp`.
    * Se implementó el método `promedioSalariosEmpleados` filtrando exclusivamente por empleados con estado habilitado (`id_est = 1`).
* **Consultas Relacionales:**
    * Se creó el método `obtenerAdministradores` mediante un `INNER JOIN` entre las tablas `empleados` y `tipo_acceso` para filtrar por el rol de Gestión de Proyectos (`id_tip_acc = 1`).
* **Robustez y Seguridad:**
    * Se aplicó una **lógica de validación explícita (versión larga)** para manejar valores nulos (`None`).
    * Se garantizó que los métodos retornen valores seguros: `0` para cálculos numéricos y listas vacías `[]` para consultas múltiples, evitando errores de ejecución en la interfaz.

#### 2. Capa de Lógica y Menús (`Funciones.py`)
* **Gestión de Salida:**
    * Desarrollo de las funciones `__promedioEdades` y `__promedioSalarios` para recibir datos del DAO y gestionar los mensajes de pantalla.
* **Presentación de Datos:**
    * Implementación de `__listarAdministradores` utilizando la librería `PrettyTable` para generar reportes tabulares limpios y profesionales.
---

### 🛠️ Pendientes para Mañana (03 de enero)

1.  **Pruebas de Borde (Testing):** * Verificar que los promedios retornen `0` correctamente cuando no existan empleados habilitados en la base de datos.
2.  **Validación de Interfaz:** * Confirmar que la tabla de administradores visualice el nombre del cargo (`nom_tip_acc`) y no el ID numérico.
3.  **Módulo de Asignación:** * Iniciar la lógica para asignar empleados a proyectos, respetando la relación 1:N definida en el diagrama de clases.

## 📅 Fecha: 06 de enero, 2026
## 🛠️ Refactorización de Arquitectura (Cierre del día)

**Mejora de Eficiencia:**
* Se eliminaron los métodos redundantes `ObtenerEmpleado`, `listarEmpleadoHabilitados` y `listarEmpleadoDeshabilitados` en el DAO.
* Se implementó el **Patrón de Listado Genérico**: una sola función centralizada que utiliza parámetros numéricos (1-5) para filtrar los resultados de la base de datos según la necesidad de la interfaz.
* Se optimizaron los llamados en `Funciones.py`, reduciendo la complejidad del controlador y facilitando futuras expansiones del sistema.

**Estado del Proyecto:**
* Código limpio (Clean Code) y sin funciones "huérfanas".
* Estructura lista para iniciar el módulo de asignación de empleados a proyectos.

# 📝 Bitácora de Desarrollo - Proyecto Nro. 1

## 📅 Fecha: 06 de enero (PARTE II), 2026
**Objetivo:** Iniciar el Módulo de Gestión de Proyectos y asegurar la integridad de datos (evitar duplicados).

---

### ✅ Logros y Avances

#### 1. Capa de Acceso a Datos (`DAO.py`)
* **Persistencia de Proyectos:**
    * Se implementó el método `insertarProyecto`, permitiendo el registro de nuevas entidades en la tabla `Proyectos` de la base de datos.
* **Validación de Integridad:**
    * Se creó el método `comprobarNombreProyecto` para verificar la existencia previa de un nombre en la base de datos antes de permitir una inserción.
    * Este método retorna un valor `None` si el nombre está disponible, facilitando la lógica de control en la capa de funciones.

### 🛠️ Pendientes para la Siguiente Sesión

1.  **Interfaz de Proyectos (`Funciones.py`):**
    * Desarrollar el método `__crearProyecto` integrando la validación de nombres duplicados.
    * Aplicar formato `.title()` o `.capitalize()` a los nombres de proyectos para estandarizar la búsqueda y visualización.
2.  **Visualización de Proyectos:**
    * Implementar `__listarProyectos` en la capa de funciones utilizando `PrettyTable` para verificar los registros actuales.
3.  **Test de Duplicados:**
    * Intentar crear un proyecto con un nombre ya existente (ej: "Desarrollo Ecologico") para confirmar que el sistema bloquea la operación.

## 📅 Fecha: 07 de enero, 2026 (Sesión Tarde)
**Objetivo:** Implementación de consultas genéricas para el módulo de Proyectos (listarProyectosGeneral).

### ✅ Logros y Avances
* **Capa de Acceso a Datos (`DAO.py`):**
    * Se creó el método `listarProyectos(criterio)` aplicando el patrón de listado genérico.
    * Integración de `INNER JOIN` con la tabla `estados` para mostrar nombres descriptivos en lugar de IDs numéricos.
    * Implementación de protección de retorno mediante listas vacías `[]` para asegurar la estabilidad de la interfaz.

* [ ] **Tarea de Testing:** Ejecutar `PruebasUnitarias.py` y verificar que el DAO responda correctamente a los casos de éxito y error.
* [ ] **Mantenimiento:** Decidir si implementar una base de datos de pruebas para no alterar los registros de producción.
* Probar y romper TODO a ver si sirve

### 🛠️ Correcciones de Infraestructura y Sincronización
* **Regularización de Base de Datos:** Se identificó y resolvió una inconsistencia crítica de esquema mediante la incorporación de la columna `id_sex` en la tabla `empleados`.
* **Integridad de Datos:** Se actualizaron los registros históricos (Wilmer, Carolina, Juancho, Bob) para asignar géneros válidos, preservando la información sensible y las credenciales encriptadas.

### ✅ Calidad y Testing
* **Certificación de Tipos (DAO):** Se estandarizaron los retornos del DAO (conversión de Tuplas a Listas y de Decimales a Floats) para asegurar la estabilidad de la interfaz.
* **Pruebas Unitarias:** Ejecución exitosa de `PruebasUnitarias.py` con resultado **OK**.
* **Test de Fuego (Integración):** El sistema superó el circuito completo de inserción, búsqueda y validación de duplicados tanto para empleados como para proyectos.

### 📂 Estado Actual del Módulo Proyectos
* **DAO:** Métodos de inserción, búsqueda y listado general totalmente operativos.
* **Lógica:** Validaciones de longitud de caracteres y prevención de nombres duplicados implementada.
---

## 📅 Fecha: 17 de enero, 2026 (Corrección de Integración)
**Objetivo:** Resolver error de atributo por desincronización de nombres entre capas.

### ✅ Logros y Avances
* **Depuración de Interfaz:**
    * Se corrigió el `AttributeError` en `__listarProyectos` al actualizar la llamada al método correcto del DAO (`listarProyectosGeneral`).
* **Consistencia de Código:**
    * Se verificó que todos los llamados desde `Funciones.py` coincidan con las firmas de los métodos definidos en `DAO.py`.

---

## 📅 Fecha: 20 de enero, 2026
**Proyecto:** Módulo de Búsqueda de Proyectos.

### ✅ Logros y Avances
* **Nueva Función:** Implementación de `__buscarProyecto` (Interfaz) y `buscarProyecto` (DAO).
* **Refactorización y "Bugfixing":**
    1. **Validación de Entradas:** Se añadió control de tipos con `.isdigit()` para evitar cierres inesperados por ingresos no numéricos.
    2. **Optimización de Flujo:** Se corrigieron errores de indentación y bloques `else` redundantes para mejorar la legibilidad y el rendimiento.
    3. **Sincronización de Objetos:** Se ajustó el DAO para mapear correctamente el nombre del estado (`nom_est`) al objeto `proyecto`.

    MODIFICAR PROYECTO EN PROCESO:
    FUNCIONES POCO AVANZADO
    DAO (MODIFICAR PROYECTO) AUN NO EMPEZADO

    ## 📅 Fecha: 21 de enero, 2026 (Cierre de Ciclo CRUD)
**Objetivo:** Implementación de baja lógica de proyectos y finalización del módulo.

---

### ✅ Logros y Avances
* **Borrado Lógico:** Se implementó `__eliminarProyecto` bajo el estándar de "Desvinculación Lógica" (UPDATE `id_est = 2`), garantizando que no se pierda la trazabilidad histórica de los datos.
* **Integridad Referencial:** Al evitar el uso de `DELETE`, se protegen las relaciones de llaves foráneas en la tabla `empleados`.
* **Robustez en DAO:** Se estandarizó el uso de bloques `finally` y `con.commit()` para asegurar transacciones limpias y cierres de conexión seguros.

## Fecha: 14 de febrero, 2026
Hito: Finalización y Certificación del Módulo Proyectos (CRUD Completo)

✅ Desarrollo de Capas
Interfaz de Usuario (Funciones.py):

Implementación de __buscarProyecto con validación de tipos y retorno de objetos para flujo dinámico.

Refactorización de __modificarProyecto y __eliminarProyecto con validación de existencia previa.

Mejora de UX: Se integraron menús de confirmación y mensajes informativos antes de cambios críticos de estado.

Capa de Datos (DAO.py):

Estandarización de bloques try-except-finally para asegurar el cierre de conexiones y evitar fugas de memoria.

Implementación de Baja Lógica: Los proyectos se deshabilitan (id_est = 2) en lugar de eliminarse físicamente para mantener la integridad referencial.

Estadísticas Avanzadas: Uso de LEFT JOIN y GROUP BY para reportar carga de empleados y costos de planilla por proyecto, incluyendo aquellos sin personal asignado.

## 🧪 Pruebas y Calidad
Test de Fuego Automatizado: Se creó TestProyecto.py con gestión dinámica de rutas (sys.path), certificando el ciclo completo: Inserción ➡️ Búsqueda ➡️ Modificación ➡️ Eliminación Lógica.

Depuración: Identificación de duplicados en la base de datos y corrección de la lógica de persistencia.

Módulo de Gestión y Asignación de Proyectos

Capa de Datos (DAO): Se estandarizó la "Navaja Suiza" (listarEmpleadosGeneral) para manejar 5 criterios de filtrado distintos, optimizando la recuperación de registros según el estado de asignación.

Lógica de Negocio: Implementación de asignarEmpleadoaProyecto con validación de impacto real en la base de datos mediante rowcount.

Interfaz de Usuario:

Creación de listados dinámicos con PrettyTable.

Uso de Slicing de Python (d[:-1]) para "purificar" la visualización de datos irrelevantes en reportes específicos.

## Bitácora (16 de febrero, 2026)

ASIGNAR Y REASIGNAR EMPLEADOS A PROYECTOS terminado y listo para probar script TestProyecto actualizado para probar todo lo que concierne a proyecto desde su creacion hasta su modificacion y eliminacion logica comprobando que se le asignen correctamente los empleados y a su vez reasignen correctamente. Sólo falta habilitar el inicio de sesion con credenciales de administrador y probar manualmente para ver errores de tipeo y UX.