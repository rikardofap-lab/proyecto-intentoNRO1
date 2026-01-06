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
