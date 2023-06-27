
lab1 = float(input("Ingrese NOTA*1" ": "))
Lab2 = float(input("Ingrese NOTA*1" ": "))
Lab3 = float(input("Ingrese NOTA*1" ": "))

Promedio = lab1*0.3 + Lab2*0.4 + Lab3*0.3

if Promedio > 6.0:
    print(f"El estudiante aprobo sin distincion:, {Promedio:.1f}")
elif Promedio >= 4.0 and Promedio < 6.0:
    print(f"El estudiante aprobo:, {Promedio:.1f}")
elif Promedio < 4.0:
    print(f"El estudiante REPROBO con un:, {Promedio:1f}")
