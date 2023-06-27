Nombres = ["emilio","Gustavo","Alejandro","Bernardo","Hector"]
Edad = ["18 años","24 años","55 años","38 años","43 años"]

Trabajador1 = Nombres[0] + Edad[0]
Trabajador2= Nombres[1] +Edad[1]
Trabajador3 = Nombres[2] + Edad[2]
Trabajador4 = Nombres[3] + Edad[3]
Trabajador5 = Nombres[4] + Edad[4]

trabajadores = dict(zip(Nombres, Edad))
print(trabajadores)


print(Trabajador1)
print(Trabajador2)
print(Trabajador3)
print(Trabajador4)
print(Trabajador5)