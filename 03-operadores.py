#01 - OPERADORES ARITMETICOS

#Declarando varible de tipo entero

a = 20
b = 5
c = 4
d = 20

#Operacion Comunes
print("##### 01- OPERADORES ARITMETICOS #########")
print("Suma entre a + b es:", a + b)
print("Resta a - b es:", a - b)
print("Multiplicacion entre a * b es:", a * b)
print("Division entre a / b es:", a/b)
print("El modulo entre a y b",  a%b)
print("El cociente entre b/c es:", b//c)
print("El resultado de b elevado a c(5^4:",b ** c,"\n")

#Declaron vriable de tipo flotantes
t = 5.39 #tiempo en segundos
g = 9.81 #la aceleracion de gravedad

#Operacion aritmeticas con flotantes
v = g * t

print(f"La velocidad del objeto en caida libre es de : {v} m/s")
print("La velocidad del objetivo en caida libre es de: {:,2f}", format(v))
print(f"La velocidad deñ objeto en caida libre es de {v:,2f}")
print("La velocidad del objeto en caida libre es de:", "%.2f" %v)
print("\n")

#Declarando variables de tipo compleja
cl = 4 + 3j
print(type(cl))

#Creando un numero completa con complex
c2 = complex(3, -5)

print("El numero es:", c2)

print(c2.real) #Obteniendo la parte  del  numero complejo
print(c2.imag) #Objetivo la parte imaginaria del numero complejo


#¿Se puede realizar esta operacion? ¿Multiplicar un String por un entero?
print("Hola" * 5)

#¿y lasiguiente multiplicacion?
#print("Hola" * 3,5*2)
#Si el resultado es un 7 (numero entero), ¿por qué sale error?

print("Hola" * (int((10 * 2) / 5)),"\n")

#¿y por último esta operación de suma?
#print("Hola" + 20)

#02-OPERADORES DE COMPARACIÓN
print("######## 02-OPERADORES DE COMPARACIÓN ########")
print(a == b) #igual a
print(a != b) #desigual a
print(a > b)  #mayor que
print(a < b)  #menor que
print(c >= d) #mayor o igual que
print(c <= d) #menor o igual que

#Comparando cadenas de caracteres
animal_domestico = "gato"
animal_salvaje= "leopardo"
print("\nComparando Cadenas de Caracteres")
print(animal_domestico == animal_salvaje)   #igual a
print(animal_domestico != animal_salvaje)   #desigual a
print(animal_domestico > animal_salvaje)    #mayor que
print(animal_domestico < animal_salvaje)    #menor que
print(animal_domestico >= animal_salvaje)   #mayor o igual que
print(animal_domestico <= animal_salvaje)   #menor o igual que


#03-OPERADORES LÓGICOS
print("######## 03-OPERADORES LÓGICOS ########")
#Trabajaremos con el siguiente ejemplo:
#Tenemos un vehiculo que tiene bencina (variable bencina) y una opcion 
#que dice si esta encendido o no (variable encendido). Dependiendo del 
#estado de cada variable, se irá cambiando por False o True

bencina = True
encendido = False
edad = 19

#Utilizando el operador AND
if bencina and encendido:
    print("El vehiculo puede avanzar")
else:
    print("El vehiculo no puede arrancar")

#Utilizando el operador OR
if bencina or encendido:
    print("El vehiculo puede avanzar")
else:
    print("El vehiculo no puede arrancar")

#Utilizando el operador NOT junto al AND
if not bencina and encendido:
    print("El vehiculo puede avanzar")
else:
    print("El vehiculo no puede arrancar")

#Utilizando el operador NOT junto al OR
if not bencina or encendido:
    print("Utilizando NOT Y OR:  El vehiculo puede avanzar")
else:
    print("El vehiculo no puede arrancar")

#Utilizando el operador NOT junto al AND y OR
if not bencina or (encendido and edad >= 18):
    print("El vehiculo puede avanzar")
else:
    print("El vehiculo no puede arrancar")