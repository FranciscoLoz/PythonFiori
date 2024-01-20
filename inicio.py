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

def inicio():
    while True:
        print("-------------------------------------------------------------------")
        print("Bienvenido al asistente de creación, modificación y visualización  ")
        print("-------------------------------------------------------------------")
        print("Por favor, seleccione qué área desea consultar:                    ")
        print("                                                                   ")
        print("1. Quiero consultar o modificar información acerca del instituto")
        print("2. Quiero consultar o modificar informacion acerca del alumnado")
        print("3. Quiero consultar o modificar información acerca del equipo docente")
        print("4. Salir")

        opcion = input("Ingrese el número de la opción que desea: ")

        if opcion == "1":
            # Lógica para la opción 1
            print("Ha seleccionado la opción 1.")

        elif opcion == "2":
            # Lógica para la opción 2
            print("Ha seleccionado la opción 2.")

        elif opcion == "3":
            # Lógica para la opción 3
            print("Ha seleccionado la opción 3.")

        elif opcion == "4":
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, ingrese un número válido.")

