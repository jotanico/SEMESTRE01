dic = []
Nombre1 = input("Ingrese su Nombre: \n")
dic.append(Nombre1)
Nombre2 = input("Ingrese su Nombre: \n")
dic.append(Nombre2)


if Nombre1[0] == Nombre2[0]:
   print("Los 2 nombres comienzan con la misma Letra")
elif Nombre1[-1] == Nombre2[-1]:
   print("Los 2 nombres terminan con la misma letra ")
else:
   print("Los 2 nombres no tienen ninguna relacion")


