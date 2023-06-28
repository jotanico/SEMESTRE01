Algoritmo Viaje_Concepcion
	definir alumnos como entero
	Escribir "Ingrese el N° de alumnos";
	leer alumnos
	
	Si alumnos >= 100 Entonces
	precio <- (alumnos * 15000)*0.10
	Escribir "El total a pagar por la cantidad de alumnos es", "" "$" precio, "+$550.000 del bus"
FinSi


si alumnos < 100 y alumnos >= 50 Entonces
	precio = (alumnos * 17000)*0.5
	Escribir "El total a pagar por la cantidad de alumnos es", "" "$" precio, "+$550.000 del bus"
FinSi

Si alumnos > 30 y alumnos <= 49 Entonces
	precio = (alumnos * 19500)
	Escribir "El total a pagar por la cantidad de alumnos es", "" "$" precio, "+$550.000 del bus"
FinSi

	Si alumnos > 0 y alumnos < 30 Entonces
	precio = (alumnos * 19500)
	Escribir "El total a pagar por la cantidad de alumnos es", "" "$" precio, "+$550.000 del bus"
FinSi

	
FinAlgoritmo
