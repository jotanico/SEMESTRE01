Algoritmo Menu_Food_Trock
	Definir pedido como entero
		a=1500
		b=2000
		c=800
		d=2500
		e=1000
		iva<-0.19
		
		Escribir"Menu Food Trock ,"
		Escribir"Menu 1:Papas Fritas Chicas ," a
		Escribir"Menu 2:Completo italiano ," b
		Escribir"Menu 3:Vaso de Bebida ," c
		Escribir"Menu 4:Empanada de Carne ," d
		Escribir"Menu 5:Sandwich de jamón y queso ," e
		Escribir"Porfavor introduzca el numero del menu"
		Leer pedido
		
		Segun pedido Hacer
		1:
			
			Escribir "Su pedido es Papas fritas Chicas y su precio es $" ,a " tu iva es de $", iva * a
	
		2:
			
				Escribir "Su pedido es Completo italiano y su precio es $" ,b " tu iva es de $", iva * b
			
		3:
				Escribir "Vaso de Bebida $" ,c " tu iva es de $", iva * c
		
		4:
				Escribir "Empanada de Carne $" ,d " tu iva es de $", iva * d
		
		5:
				Escribir "Sandwich de jamón y queso $" ,e " tu iva es de $", iva * e
			De Otro Modo:
				Escribir "Introduzca un numero del menu" 
	Fin Segun
	
	
	
FinAlgoritmo
