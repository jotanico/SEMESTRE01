dic  = []


i = 1
cantidad = int(input("Ingrese la cantidad de palabras: \n"))

while cantidad > 0:
    palabra = input("Ingrese la palabra" + str(i) + ": ")
    i = i + 1
    cantidad = cantidad - 1
    dic.append(palabra)

mayor = max(dic)
menor = min(dic)

print("Lista de palabras:", dic)
print("La palabra con mas caracteres:", mayor)
print("La palabra con menos caracteres:", menor)

