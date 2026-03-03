from datetime import date
from os import system

class Validaciones:

    @staticmethod
    def obtener_rut_validado(titulo_menu: str):
        """
        Pide un RUT al usuario, lo valida (formato y dígito 'K') 
        y lo retorna formateado (ej: "12345678-K").
        Este bucle se repite hasta que el RUT ingresado sea válido.
        """
        while True:
            system("cls")
            print("-------------------------------------------------------------------------------------")
            print(f"--------- {titulo_menu} ---------")
            print("-------------------------------------------------------------------------------------")
            
            # 1. Pedir y limpiar (acepta "11 111 111 k")
            rut_sin_formato = input("\nIngrese RUT (SIN puntos y SIN guion) puede usar espacios para separar digitos (Ej: 11 111 111 k): ").strip().replace(" ", "")

            # 2. Validar longitud
            if (8 <= len(rut_sin_formato) <= 10):
                    # 3. Separar cuerpo y DV
                    cuerpo = rut_sin_formato[:-1]
                    dv = rut_sin_formato[-1].upper() # Convertir 'k' a 'K'
            else:
                    print("\nError: El RUT debe tener entre 8 y 10 caracteres.")
                    system("pause")
                    continue

            if cuerpo.isdigit() and (dv.isdigit() or dv == 'K'):
                rut_formateado = f"{cuerpo}-{dv}"
                return rut_formateado
            else:
                print("\nError: El RUT contiene caracteres no válidos.")
                print("(Recuerde: solo números y 'k' al final si corresponde)")
                system("pause")
                continue
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def obtener_fecha(titulo_pantalla: str) -> date:
        """
        Solicita al usuario una fecha (día, mes, año), la valida y la devuelve.
        Repite el proceso hasta que se ingrese una fecha válida.

        Args:
            titulo_pantalla (str): El título que se mostrará en la pantalla de ingreso.

        Returns:
            date: El objeto de fecha validado.
        """
        while True:
            try:
                system("cls")
                print("------------------------------------------------------------------------------------")
                print(f"--- {titulo_pantalla.upper()} ---")
                print("------------------------------------------------------------------------------------")

                print("\nIngrese la fecha:")
                dia = int(input("Día (DD): "))
                mes = int(input("Mes (MM): "))
                anio = int(input("Año (AAAA): "))

                # Validar y construir la fecha
                fecha_validada = date(anio, mes, dia)
                return fecha_validada # Si la fecha es válida, la retornamos y salimos de la función

            except ValueError:
                print("\nError: Fecha inválida. Verifique los valores ingresados.")
                system("pause")
                continue
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def validar_texto(titulo_pantalla: str, etiqueta_campo: str) -> str:
        while True:
            try:
                system("cls")
                print("-------------------------------------------------------------------------------------")
                print(f"---- {titulo_pantalla.upper()} ----")
                print("-------------------------------------------------------------------------------------")

                valor = input(f"\nIngrese {etiqueta_campo.lower()}: ").strip()

                # Misma lógica: solo letras y longitud entre 2 y 60
                if valor.isalpha() and 2 <= len(valor) <= 60:
                    print(f"\n{etiqueta_campo.lower()} guardado correctamente:", valor)
                    system("pause")
                    return valor.capitalize()
                else:
                    print(f"\nError: El {etiqueta_campo.lower()} debe tener entre 2 y 60 letras (sin números).")
                    system("pause")
                    continue
            except Exception as e:
                print(f"\n¡ERROR! Al ingresar el {etiqueta_campo.lower()}: {e}", end="\n\n")
                system("pause")
                continue

    @staticmethod
    def validar_telefono(titulo_pantalla: str) -> str:
        while True:
            try:
                system("cls")
                print("------------------------------------------------------------------------------------")
                print(f"---- {titulo_pantalla.upper()} ----")
                print("------------------------------------------------------------------------------------")
                nro = input("\nIngrese número de teléfono (9 dígitos, sin +56): ").strip()

                if nro.isdigit() and len(nro) == 9:
                    print("\nTeléfono guardado: +56", nro)
                    system("pause")
                    return "+56" + nro
                
                print("\nError: Debe ingresar exactamente 9 números."); system("pause")
            except Exception as e:
                print(f"Error: {e}")
                system("pause")

    @staticmethod
    def validar_email(titulo_pantalla: str) -> str:
        while True:
            try:
                system("cls")
                ("----------------------------------------------------------------------------------------")
                print(f"---- {titulo_pantalla.upper()} ----")
                ("----------------------------------------------------------------------------------------")
                email = input("\nIngrese email: ").strip()

                if 15 <= len(email) <= 50 and "@" in email and "." in email:
                    print("\nEmail guardado:", email)
                    system("pause")
                    return email
                else:
                    print("\nError: Ingrese un email válido (10-60 caracteres).")
                    system("pause")
            except Exception as e:
                print(f"Error: {e}")
                system("pause")
    
    @staticmethod
    def validar_numero_rango(titulo: str, etiqueta: str, min_v: int, max_v: int) -> int:
        while True:
            try:
                system("cls")
                ("----------------------------------------------------------------------------------------")
                print(f"---- {titulo.upper()} ----")
                ("----------------------------------------------------------------------------------------")
                num = int(input(f"\nIngrese {etiqueta} ({min_v} - {max_v}): "))

                if min_v <= num <= max_v:
                    return num
                
                print(f"\nError: El valor debe estar entre {min_v} y {max_v}."); system("pause")
            except ValueError:
                print("\nError: Debe ingresar solo números.")
                system("pause")