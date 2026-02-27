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
            print("-------------------------------------------")
            print(f"--------- {titulo_menu} ---------")
            print("-------------------------------------------")
            
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
                print("------------------------------------------")
                print(f"--- {titulo_pantalla.upper()} ---")
                print("------------------------------------------")

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
    @staticmethod
    def obtener_apellido(titulo_pantalla: str) -> str:
        while True:
                try:
                    system("cls")
                    print("-------------------------------------------")
                    print(f"---- {titulo_pantalla.upper()} ----")
                    print("-------------------------------------------")

                    apellido_ingresado = input(f"\nIngrese {titulo_pantalla.lower()}  del empleado: ").strip()

                    if apellido_ingresado.isalpha() and 2 <= len(apellido_ingresado) <= 20:
                        ape_formateado = apellido_ingresado.capitalize()
                        print(f"\n{titulo_pantalla.lower()} guardado correctamente:",ape_formateado )
                        system("pause")
                        return ape_formateado
                    
                    else:
                        print("\nEl apellido debe tener entre 2 y 20 caracteres")
                        system("pause")
                        continue

                except Exception as e:
                    print(f"\n¡ERROR! Al ingresar el apellido del empleado: {e}", end="\n\n")
                    system("pause")
                    continue
