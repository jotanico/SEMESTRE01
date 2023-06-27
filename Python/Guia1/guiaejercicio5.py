#EJERCICIO 5

import random

numeros = [random.randint(40, 350) for _ in range(20)]

print("Números generados:", numeros)
#Creamos una variable, en donde empleamos un codigo que nos permite cerar una lista limitda de numeros RANDOM

numero_buscado = int(input("Ingrese un número para buscar en la lista: "))
#creamos una variable, la cual le permita al usuario pedir el numero que quiera por pantalla


ocurrencias = numeros.count(numero_buscado)

print(f"El número {numero_buscado} aparece {ocurrencias} veces en la lista.")
#Por ultimo creamos una variable, la cual permita buscar el numero solicitado por pantalla, en la lista RANDOM. Verificando si este se esncuentra en la lista y cuuantas veces aparece
