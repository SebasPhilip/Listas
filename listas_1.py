notas=[]
contador=0
promedio=0
nota_semestre=0 
while len(notas)==5:
    for i in range(5):
        try:
            nota_semestre=float(input("Ingrese las notas del semestre: "))

        except:
            print ("Nota no válida. ")
        else:
            if nota_semestre < 1:
                print("La nota no puede ser menor a 1.0")
            elif nota_semestre >7:
                print("La nota no puede ser mayor a 7.0")
            else:
                print ("Nota añadida con éxito.")

            notas.append(nota_semestre)
            if nota_semestre >=5:
                contador+=1


promedio=sum(notas)/len(notas)
print (notas)

print("La nota más alta es: ", max(notas))
print("La nota más baja es: ", min(notas))
print("El promedio obtenido es: ", promedio)
print("Cantidad de notas mayores o igual a 5,0 son: ", contador)
