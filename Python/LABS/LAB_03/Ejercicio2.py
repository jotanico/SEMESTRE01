a = [21,8,15,3,12]
b = [10,9,12,15,18]
c = [2,3,8,9,12]

#Concatenar todas las listas e imprimir la lista obtenida.

listaConcatenada = a + b + c
print("Lista Concatenada" ":", listaConcatenada)

#Agregar el número 20 en la penúltima posición de la lista.

listaConcatenada.insert(14, 20)
print("a" ":", listaConcatenada)

#Ordenar la lista de forma descendente.
NuevasLista = [21, 20, 18, 15, 15, 12, 12, 12, 10, 9, 9, 8, 8, 3, 3, 2]

print("Lista ordenada :", NuevasLista)

#) Insertar la lista [4,5,6] en la última posición de la lista ordenada

NuevasLista.insert(16, [4,5,6])
print("c" ":", NuevasLista)

#Sumar todos los números dentro de la lista.

nuevalista= [21, 20, 18, 15, 15, 12, 12, 12, 10, 9, 9, 8, 8, 3, 3, 2, 4, 5, 6]
lista_Sumada = sum(nuevalista)
print("Suma :", str(lista_Sumada))

# Obtener el promedio simple de la lista
promedio = lista_Sumada/19
print("Promedio :", promedio)

