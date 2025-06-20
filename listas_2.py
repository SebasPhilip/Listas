lista_super=["pan", "leche", "huevos", "queso", "manzanas"]
eleccion=0
opcion_agregada=""
indice=0
indice_real=0
print ("La lista actual es: ", lista_super)

while True:
    print ("Quieres agregar o eliminar algo: 1 para agregar, 2 para , 3 para salir")

    try:
        eleccion=int(input("--> "))
    except ValueError:
        print ("Opción debe ser un número entero.")
    else:
        if eleccion == 1:
            opcion_agregada=input("ingrese el nombre del producto a agregar.").lower()
            lista_super.append(opcion_agregada)
        elif eleccion==2:
            try:
                indice=int(input("Ingrese la posición del producto a eliminar: "))
            except ValueError:
                print("La posición no puede ser un string")
            else:
                indice_real=indice+1
                lista_super.pop(indice_real)
        elif eleccion==3:
            print ("la lista final es: ", lista_super)
            print("hasta luego")
            break
        else: 
            print("Valor ingresado no válido")

