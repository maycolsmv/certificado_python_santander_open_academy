base_de_datos = []


accion = 0
key = 0
dato = ("")

#variables para actualizar el diccionarion
n_mombre = 0
n_apellido = 0
m_edad = 0
n_curso = 0

#variable buscar
b_nombre = 0

e_nombre = 0
confirmar = 0

while accion != 5: 
    
    print("¿Que accion quieres hacer?\n1. Agregar estudiante \n2. Mostrar estudiante \n3. Buscar estudiante \n4. Eliminar estudiante \n5. Salir") 
    accion = int(input("Elige la opcion: "))

    if accion == 1: 
        estudiantes = {
            "nombre":"",
            "apellido":"",
            "edad":"",
            "curso":""
        }

        n_mombre = input("Nombre del estudiante: ")
        estudiantes.update({"nombre": n_mombre})

        n_apellido = input("Apellido del estudiante: ")
        estudiantes.update({"apellido": n_apellido})

        n_edad = input("edad del estudiante: ")
        estudiantes.update({"edad": n_edad})

        n_curso = input("Curso del estudiante: ")
        estudiantes.update({"curso": n_curso})
        
        base_de_datos.insert(0, estudiantes)

        print("Estudiante agregado con exito")

    if accion == 2:
        for mostar in base_de_datos:
            print(mostar.values())

    if accion == 3:

        b_nombre = input("Escribe el nombre del estudiante: ")
        encontrar = False
        for buscar in base_de_datos:

            if buscar["nombre"] == b_nombre:
                
                print(f"Estudiante {b_nombre} encontrado")
                print (buscar)
                
                encontrar = True

                break

        if encontrar == False: 
            print("estudiante no encontrado")

    if accion == 4:
        e_nombre = input("Escribe el nombre del estudiante: ")
        eliminar = False
        for buscar in base_de_datos:

            if buscar["nombre"] == e_nombre:
                
                print(f"Estudiante {e_nombre} encontrado")
                print (buscar)
                eliminar = True
                print(f"Quieres eliminar a {e_nombre}? \n 1. SI \n 2. NO")
                confirmar = int(input("Elige la opcion: "))
                if confirmar == 1:
                    base_de_datos.remove(buscar)

                else:
                    break

        if eliminar == False: 
            print("estudiante no encontrado")
    

    if accion == 5:
        break