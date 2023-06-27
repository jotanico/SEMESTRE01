numeros = [4, 3, 8, 12, 6, 10, 14, 3, 6]

#eliminar ultimo numero de la lista

numeros.pop

#agregar el 2 en la primera posicion

numeros.insert(0, 2)

#Eliminar los numeros duplicados de la lista

numeros = list(set(numeros))

#Obtener la media y la mediana de la lista

suma = sum(numeros)
cantidad = len(numeros)
media = suma/cantidad



print("nueva lista", numeros)
print("Media" ":", media)

