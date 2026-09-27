def mostrar_menu():
    print("MENÚ PRINCIPAL")
    print("1. AGREGAR ESTUDIANTE")
    print("2. MOSTRAR TODOS LOS ESTUDIANTES")
    print("3. BUSCAR ESTUDIANTE ")
    print("4. ELIMINAR ESTUDIANTE")
    print("5. SALIR")

estudiantes={}

while True:
    mostrar_menu()
    opcion=input("Seleccionar una opción:")

    if opcion=="1":
        nombre= input("ingresa el nombre del estudiante: ")
        nota=input("ingresa la nota del estudiante: ")
        estudiantes[nombre]=nota
        print(f"EL/LA ESTUDIANTE {nombre} AGREGADO CON NOTA {nota}")

    elif opcion =="2":
        if estudiantes:
            print("lista de estudiantes ")
            for nombre, nota in estudiantes.items():
                print(f"{nombre} : {nota}")
        else:
            print("No hay estudiantes registrados.")

    elif opcion =="3":
        nombre= input("Ingresa el nombre a buscar: ")

        if nombre in estudiantes:
            print(f"{nombre}tiene la nota {estudiantes[nombre]}. ")
        else:
            print("Estudiante no encontrado.")

    elif opcion=="4":
        nombre=input("Ingresa el nombre a eliminar: ")
        if nombre in estudiantes:
            del estudiantes[nombre]
            print(f"Estudiante {nombre} eliminado.")
        else:
            print("estudiante no encontrado")

    elif opcion=="5":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Intenta nuevamente.")
