
frase=input("ingrese una frase a continuación: ").lower()
vocales=["a","e","i","o","u"]
espacio=[" "]
caracter_repetido=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
contador_espacio=0
contador_vocales=0

lista_caracteres=list(frase)


for i in lista_caracteres:
    if i  in espacio:
        contador_espacio+=1
    elif i in vocales:
        contador_vocales+=1 
    



print (contador_espacio)
print(contador_vocales)