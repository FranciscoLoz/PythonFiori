from administrativo import administrativo
#from alumno import alumno
from asignatura import asignatura
from curso import curso
from departamento import departamento
from direccion import direccion
from instituto import instituto
#from matricula import matricula
#from nota import nota
#from persona import persona
from profesor import profesor

import os

def inicio():

    #Todos los mockups hardcodeados

    #Direcciones Mockup
    default_direction = direccion("C/Astronomía", 51, 41015, "Pino Montano", "Sevilla")
    default_direction2 = direccion("C/Diamantino García", 40, 41310, "Brenes", "Sevilla")
    default_direction3 = direccion("Ctra. de Utrera", 1, 41013, "Utrera", "Sevilla")

    #Cursos Mockup
    default_course = curso("Grado Superior", "Desarrollo Aplicaciones Web", 20)
    default_course2 = curso("ESO", "Matemáticas", 10)
    default_course3 = curso("Bachillerato", "Lenguaje", 30)

    #Departamentos Mockup
    default_department = departamento(1, "Programación")
    default_department2 = departamento(2, "Ciencias")
    default_department3 = departamento(3, "Letras")

    #Asignaturas Mockup
    programacion = asignatura(1, "clase para aprender lenguajes de programacion como java o python", 1234, default_teacher)
    lengua = asignatura(2, "Clase para aprender la lengua de cervantes", 4321, "Maria Lopez")
    matematicas = asignatura(3, "Clase para aprender a realizar complejas operaciones", 2143, "Rodolfo Perez")

    #Institutos Mockup
    default_center = instituto("MEDAC", "B93091536", default_direction, default_course, default_department)
    default_center2 = instituto("IES Jacarandá", "41700853", default_direction2, default_course2, default_department2)
    default_center3 = instituto("UPO", "Q9150016E", default_direction3, default_course3, default_department3)

    #Profesores Mockup
    default_teacher = profesor("12345678A", "Jose Miguel Cordon Fioris", programacion, default_department, "Hombre", 35, 1500, )
    default_teacher2 = profesor("87654321B", "María Lopez", lengua, default_department3, "Mujer", 59, 2000, )
    default_teacher3 = profesor("43218765C", "Rodolfo Perez", matematicas, default_department2, "Hombre", 43, 1785, )

    #Administradores Mockup
    default_admin = administrativo("12345678A", "John Doe", "Hombre", 35, 2450, )
    default_admin2 = administrativo("87654321B", "Jane Doe", "Mujer", 30, 2400, )
    default_admin3 = administrativo("87651234C", "Jimmy Doe", "Hombre", 26, 2100, )

    #Listas de almacenamiento
    address_list = [default_direction, default_direction2, default_direction3]
    center_list = [default_center, default_center2, default_center3]
    teacher_list = [default_teacher, default_teacher2, default_teacher3]
    admin_list = [default_admin, default_admin2, default_teacher3]
    department_list = [default_department, default_department2, default_department3]
    course_list = [default_course, default_course2, default_course3]


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
                print("                                                                   ")
                print("1. Crear un nuevo Instituto")
                print("2. Ver los datos de un instituto")
                print("3. Regresar al menú de selección primario")

                highschool_option = input("Ingrese el número de la opción que desea: ")
                if highschool_option == "1":
                    # Lógica para la opcion 1 del apartado de instituto
                    os.system('clear' if os.name == 'posix' else 'cls')
                    print("Ha seleccionado la opción 1.")
                    print("Bienvenido al sistema de creacion de Instituto virtual: ")
                    center_name = input("Ingresa el nombre del Instituto: ")
                    print("")
                    center_cif = input("Ingresa el CIF del instituto: ")
                    print("")
                    print("ZONA 1: PINO MONTANO (C-ASTRONOMIA)")
                    print("ZONA 2: BRENES (C-DIAMANTINO)")
                    print("ZONA 3: UTRERA (CARRETERA UTRERA)")
                    center_address = input("Elige una zona del 1 al 3: ")
                    if center_address == "1":
                        decided_address = default_direction

                    elif center_address == "2":
                        decided_address = default_direction2
                    
                    elif center_address == "3":
                        decided_address = default_direction3
                    
                    else:
                        print("El numero introducido no es válido")
                        break
                    print("")
                    print("Curso de Desarrollo aplicaciones Web en Grado superior")
                    print("Curso de Matemáticas en ESO")
                    print("Curso de Lenguaje en Bachillerato")
                    center_course = input("Elige un curso del 1 al 3: ")
                    if center_course == "1":
                        decided_course = default_course

                    elif center_course == "2":
                        decided_course = default_course2
                    
                    elif center_course == "3":
                        decided_course = default_course3
                    
                    else:
                        print("El numero introducido no es válido")
                        break
                    print("")
                    print("Departamento de TIC en grado superior")
                    print("Departamento de Ciencias en ESO")
                    print("Departamento de humanidades en Bachillerato")
                    center_department = input("Elige un departamento del 1 al 3: ")
                    if center_department == "1":
                        decided_department = default_department

                    elif center_course == "2":
                        decided_department = default_department2
                    
                    elif center_course == "3":
                        decided_department = default_department3
                    
                    else:
                        print("El numero introducido no es válido")
                        break

                    new_center = instituto(center_name, center_cif, decided_address, decided_course, decided_department)
                    center_list.append(new_center)

                elif highschool_option == "2":
                    # Lógica para la opcion 2 del apartado de instituto
                    os.system('clear' if os.name == 'posix' else 'cls')
                    print("Ha seleccionado la opción 2.")
                    requested_center = input("Introduce el nombre del instituto que desea consultar: ")

                    # Variables para verificar si se encuentra el instituto
                    found_center = False
                    index_center = 0

                    for center in center_list:
                        index_center += 1

                        if center.get_name() == requested_center:
                            os.system('clear' if os.name == 'posix' else 'cls')
                            print(center.get_name(), center.get_address().get_info())
                            found_center = True
                            input("Pulsa enter para continuar ")
                            break  # Romper el bucle si se encuentra el instituto

                        if not found_center and index_center == len(center_list):
                            print("ERROR, No se ha encontrado ningún instituto con el nombre especificado")

                elif highschool_option == "3":
                    # Lógica para la opción 4 del apartado de instituto
                    print("Ha seleccionado la opción 3.")
                    print("Regresando al menú principal.")
                    break  # Salir del bucle interno y regresar al menú principal

                else:
                    print("Opción no válida. Por favor, ingrese un número válido.")

        elif option == "2":
            # Lógica para la opción 2
            print("Ha seleccionado la opción 2.")
            print("-------------------------------------------------------------------")
            print("Informacion del Alumnado, ¿Que desea hacer?                        ")
            print("-------------------------------------------------------------------")
            print("1. Crear un nuevo Alumno")
            print("2. Ver los datos de un Alumno")
            print("3. Regresar al menú de selección primario")

            alumn_option = input("Ingrese el número de la opción que desea: ")
            if alumn_option == "1":
                # Lógica para la opcion 1 del apartado de alumno
                print("Ha seleccionado la opción 1.")

            elif alumn_option == "2":
                # Lógica para la opcion 2 del apartado de alumno
                print("Ha seleccionado la opción 2.")
                
            elif alumn_option == "3":
                # Lógica para la opción 4 del apartado de alumno
                print("Ha seleccionado la opción 3.")
                print("Regresando al menú principal.")
                break  # Salir del bucle interno y regresar al menú principal

            else:
                print("Opción no válida. Por favor, ingrese un número válido.")
        elif option == "3":
            # Lógica para la opción 3
            print("Ha seleccionado la opción 3.")
            print("-------------------------------------------------------------------")
            print("Informacion del equipo docente: ¿Que desea hacer?")
            print("-------------------------------------------------------------------")
            print("1. Crear un nuevo Profesor")
            print("2. Crear un nuevo Administrativo")
            print("3. Consultar un Profesor existente")
            print("4. Consultar un Administrativo existente")
            print("5. Regresar al menu de selección Primario")

            staff_option = input("Ingrese el número de la opcion que desea: ")
            if staff_option == "1":
                #Lógica para la opcion 1 del apartado de personal
                print("Ha seleccionado la opción 1.")

            elif staff_option == "2":
                #Lógica para la opcion 2 del apartado de personal
                print("Ha seleccionado la opción 2.")
            
            elif staff_option == "3":
                #Lógica para la opcion 3 del apartado de personal
                print("Ha seleccionado la opción 3.")

            elif staff_option == "4":
                #Lógica para la opción 4 del apartado de personal
                print("Ha seleccionado la opción 4.")
            
            elif staff_option == "5":
                #Lógica para la opción 5 del apartado de personal
                print("Ha seleccionado la opción 5.")
                print("Regresando al menú principal.")
                break  # Salir del bucle interno y regresar al menú principal

            else:
                print("Opción no válida. Por favor, ingrese un número válido.")

        elif option == "4":
            print("Saliendo del programa. ¡Hasta la próxima!")
            break

        else:
            print("Opción no válida. Por favor, ingrese un número válido.")
            print("")
            input("Presione cualquier tecla para continuar: ")