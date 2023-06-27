#01 datos de tipo numerico------------------
estatura = 1.72
peso = 72
conjunto = 1 + 4j
#print ("yo soy jorge, y mis complexiones son:", "mido" [estatura], "y peso" [peso])

#operacion aritmetica basica
imc = peso/estatura * 2

#los ** significativo de elevado
print ("mi IMC es de:", imc)
#ahora con menos decimales
print ("Mi IMC es de {:.2}",format(imc))

#(INT)para imprimir solo numeros REALES
#(FLOAT) para imprimir solo numero DECIMALES
#(COMPLEX) para imprimir solo numero IMAGINARIOS

#02 Datos de tipo cadena de caracteres.------------------
asignatura = "programacion"
carrera = "Ingenieria Civil Informartica"

print ("Mi carrera es", str(carrera), "y actualemte estoy en", str(asignatura))

#03 valores booleanos
Jamon = False
Pan = True

#con type sabemos el tipo de dato que estamos tratando
#ejemplo
print ( type(Pan))
print ("el conjunto del pan es", type (Jamon)) 

#04 Datos tipo array (objetos de tipo coleccion)---------------
estudiantes = ["Jose", "Miguel", "Jorge", "Joaquin"]
numero = [1, 2, 3, 4, 5, 6]
print(estudiantes)
print(numero)

#declarando e inicializando una lista
nueva_lista = list ()
print("Esta es una lista vacica", nueva_lista)
otra_lista = []
print("esta es otra lista vacia", otra_lista)

#¿Se puede realizar una lista de datos compuestos
compra_de_super = ["papas", "lechuga", "tomate", "papas"]
print("Esta es la lista de compra del super", compra_de_super)
print("en total seria;" "\n", len(compra_de_super), "productos en total")

print(compra_de_super, ("papas") )

Lemguaje = ("Java Script")
print("Nuevo valor del arreglo de un elemento:", Lemguaje)

#¿Como acceder a un elemento a un elemto especifico de la lista?
print(estudiantes [0])
print(estudiantes [-2])
print(estudiantes[1])
#los numeros negativos hace que la lista sea lea del final hacia el inicio, Pero solo en python

#Inicializando otra lista de datos mistos
data_asig = [10023, "programacion", 1, True]
print("si pienso en un numero digo", data_asig[0], "estoy en la asignatura de", data_asig[1], "soy hombre", data_asig[3])

#tupla (No mutable)
grupo1 = ("Daniel", "Cristian", 100, "Nicolas", 200, "Manuel")
print( "###### 05-Tuplas ######" )
print ( grupo1)
#accediendo al primer elemento de la tupla
print ( grupo1[0])
#consultando el elemento daniel cuantas veces se encuentra en la tupla, Count es cuantas veces se repite el elemento
print( "El elemento se repite:", grupo1,("Daniel"))
#Muestra el indice del primer elemento buscado, INDICE es posicion
print(" Indice del elementos:", grupo1, ("Cristian"))
#EL INDICE NOS INDICA CUANTAS VECES SE REPITE EL MISMO EKEMENTO EN UNA VARIABLE

#grupo1[0] = "constanza"

#Entonces, ¿Se puede modificar una tupa, que puedo hacer?
grupo1 = list (grupo1)
print ( "La tupla  ahora es de tipo:", (grupo1), " \n ")
print( " \n ")
#Forma de inicializar un Set
conjunto_vacio = ()
conjunto_vacio1 = {}
print(conjunto_vacio)

conjunto_de_colores = {"Azul", "Rojo", "Morado"}
conjunto_Animales = {"Gato", "Perro", "Loro"}

print (conjunto_de_colores)
print(conjunto_Animales)
print("El primer set contiene los siguientes colores:", conjunto_de_colores)


#print(conjunto_de_colores[0])
#En los sets no se puede acceder a la posicion de un elemento
#conjunto_de_colores, añadir ("celeste")
print("el conjunto de colores esta conformado por:", conjunto_de_colores)
#onjunto_Animales, añadir ("lagarto")
print("el conjunto de animales esta conformado por:", conjunto_Animales)