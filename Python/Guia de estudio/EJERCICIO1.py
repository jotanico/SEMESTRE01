def solicitar_numeros():
  numeros = []
  cantidad = int(input("Ingrese la cantidad de numeros : \n")) 
  j = 1    
  for i in range(cantidad):
      numero = int(input("Ingrese numero " " " + str(j) + " :" ))
      j += 1
      cantidad = cantidad - 1
      numeros.append(numero)
      return numeros
      
lista_numeros = solicitar_numeros()
print("Estos son los numeros ingresados  :", lista_numeros )

def suma_pares_impares(lista):
  suma = 0
  for numero in lista:
    if numero % 2 == 0:
      suma += numero
      return suma

lista_sumada = suma_pares_impares(lista_numeros)
print("Lista suma de pares :")

def suma_impares(lista):
  suma = 0
  for numero in lista:
    if numero % 2 == 1:
      suma += numero
      return suma

lista_sumada = suma_impares(lista_numeros)
print("Lista suma de impares : ")

