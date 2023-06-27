#EJERCICIO 1 
lista = []
mayor = 0
menor = 0
i = 1


Cantidad = int(input("Ingrese la cantidad de numeros: \n"))

while Cantidad > 0:
    numero = int(input("ingrese el numero" + str(i) + ": "))
    lista.append(numero)
    i = i + 1
    Cantidad = Cantidad - 1


mayor = max(lista)
menor = min(lista)

print("Litsa:", list)
print("mayor:", mayor)
print("menor:", menor)

#""lista.append()"" FUNCIONA PARA AGREGAR UN ELEMENTO A LA LISTA
#En este caso ""i = i + 1"" Se utiliza para aumentar el digito
#str : se utiliza para configurar una variable como texto numerico, la cual puede modificarse


#Ejercicio 3

import math

lados =[]
a = float(input("Ingrese lado A"))

b = float(input("Ingrese lado B"))

c = float(input("Ingrese lado C"))


if(a==b and b == c):
    print("Es un Triangulo Equilatero:")
elif (a==b or b==c or a==c):
    print("El triangulo es ISOCELES:")
else:
    print("El triangulo es ESCALENO:")


p = (a + b + c)/2
print("En donde su perimetro es:", p)

Area = p*(p - a)(p - b)(p - c)


print("En donde su AREA es:", Area)