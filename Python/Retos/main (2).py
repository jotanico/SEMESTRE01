num = int(input("Ingrese digito del 0 al 100"))
print(num)
resto = num%2


#el numero es par o impar
while num > 0:
    if resto == 0:
     print("El digito es PAR")
    else:
     print("El digito es IMPAR")
     break
# el numero es primo

if num == 2 and 3 and  5 and  7 and 11 and 13 and 17 and 19 and 23 and 29 and 31 and 37 and 41 and  43 and 47 and 53 and 59 and 61 and 67 and 71and 73and 79and 83and 89 and 97:
  print("El digito es numero primo")

#El numero es mayor o menor a 50
while num > 0: 
  if num >= 50:
    print("El numero es Mayor a 50")
  else:
   print("El numero es MENOR a 50")
  break 