#01-DECLARANDO LA PRIMERA FUNCIÓN
print("################## 01-DECLARANDO UNA FUNCIÓN SIMPLE ##################")

def mi_primera_funcion():
    print("Esta es mi primera funcion")

mi_primera_funcion()

#02-DECLARANDO UNA FUNCIÓN Y UTILIZANDO LISTAS
print("\n################## 02-DECLARANDO UNA FUNCIÓN Y UTILIZANDO LISTAS ##################")

def concatenar(lista1,lista2):
    return lista1 + lista2

lista1 = [1, 2, 3]
lista2 = [4, 5 ,6]

#Concatenando
print(concatenar(lista1, lista2))

#03-DECLARANDO UNA FUNCIÓN MULTIPLICACION PASANDO PARAMETROS
print("\n################## 03-DECLARANDO UNA FUNCIÓN MULTIPLICACION PASANDO PARAMETROS ##################")

def multiplicar(num1, num2):
    return num1 * num2

num1 = 2
num2= 3

#Multiplicando
print("El resultado de la multiplicacion es: ", multiplicar(num1, num2))
print(multiplicar(50, 5))

#04-EJEMPLO DE UNA FUNCIÓN
print("\n################## 04-FUNCIONES SUMA Y RESTA (POR TECLADO) ##################")

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

a = int(input("Ingrese valor de a: "))
b = int(input("Ingrese valor de b: "))

#Se llama la funcion Suma

resultado = suma(a, b)
print("La suma es de:", resultado)

#Se llama la funcion resta
resultado2 = resta(a, b)
print("La resta es de:", resultado2)

#05-PASANDO PARAMETROS POR VALOR
print("\n################## 05-PASANDO PARÁMETROS POR VALOR ##################")

def modificar_numero(x):
    x = 10 

x = 5
print("Antes de llamar a la funcion:", x)
modificar_numero(x)
print("Despues de llamar a la funcion: ", x)

#06-PASANDO PARAMETROS POR REFERENCIA
print("\n################## 06-PASANDO PARÁMETROS POR REFERENCIA ##################")

#Paso por referencia (objetos mutables)
def op_lista(lista):
    lista.append(4)

numeros = [1, 2, 3]
op_lista(numeros)
print(numeros)

#Paso por nombre de argumento
def saludar(nombre, mensaje):
    print(mensaje +  "" + nombre)

saludar(nombre= " Jorge", mensaje= "Hola")
