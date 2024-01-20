#from administrativo import administrativo
#from alumno import alumno
#from asignatura import asignatura
#from curso import curso
#from departamento import departamento
#from direccion import direccion
#from instituto import instituto
#from matricula import matricula
#from nota import nota
#from persona import persona
#from profesor import profesor
import os

def inicio():
    while True:
        # Limpiar la pantalla
        os.system('clear' if os.name == 'posix' else 'cls')

        print("-------------------------------------------------------------------")
        print("Bienvenido al asistente de creación, modificación y visualización  ")
        print("-------------------------------------------------------------------")
        print("Por favor, seleccione qué área desea consultar:                    ")
        print("                                                                   ")
        print("1. Quiero consultar o modificar información acerca del instituto")
        print("2. Quiero consultar o modificar informacion acerca del alumnado")
        print("3. Quiero consultar o modificar información acerca del equipo docente")
        print("4. Salir")

        option = input("Ingrese el número de la opción que desea: ")

        if option == "1":
            # Lógica para la opción 1
            while True:
                # Limpiar la pantalla
                os.system('clear' if os.name == 'posix' else 'cls')

                print("Ha seleccionado la opción 1.")
                print("-------------------------------------------------------------------")
                print("Informacion del Instituto, ¿Que desea hacer?                       ")
                print("-------------------------------------------------------------------")
                print("1. Crear un nuevo Instituto")
                print("2. Ver los datos de un instituto")
                print("3. Modificar la informacion de un instituto")
                print("4. Regresar al menú de selección primario")

                highschool_option = input("Ingrese el número de la opción que desea: ")
                if highschool_option == "1":
                    # Lógica para la opcion 1 del apartado de instituto
                    print("Ha seleccionado la opción 1.")

                elif highschool_option == "2":
                    # Lógica para la opcion 2 del apartado de instituto
                    print("Ha seleccionado la opción 2.")

                elif highschool_option == "3":
                    # Lógica para la opción 3 del apartado de instituto
                    print("Ha seleccionado la opción 3.")

                elif highschool_option == "4":
                    # Lógica para la opción 4 del apartado de instituto
                    print("Regresando al menú principal.")
                    break  # Salir del bucle interno y regresar al menú principal

                else:
                    print("Opción no válida. Por favor, ingrese un número válido.")

        elif option == "2":
            # Lógica para la opción 2
            print("Ha seleccionado la opción 2.")
            print("Informacion del alumnado, ¿Que desea hacer?")

        elif option == "3":
            # Lógica para la opción 3
            print("Ha seleccionado la opción 3.")
            print("Informacion del equipo docente: ¿Que desea hacer?")

        elif option == "4":
            print("Saliendo del programa. ¡Hasta la próxima!")
            break

        else:
            print("Opción no válida. Por favor, ingrese un número válido.")