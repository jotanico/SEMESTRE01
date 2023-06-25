from colorama import init, Fore

init()

#CONDICIONALES IF
print(Fore.GREEN + "###############  01 - UTILIZNDO IF Y ELSE ############")

licencia = False
edad = 19
automovil = False

#¿Estara correcto este codigo?
print(Fore.YELLOW +"\n>>> Testeando el segundo condicional IF")

if licencia:
    print(Fore.WHITE + 'Puedo conducir porque tengo licencia')
else:
    print(Fore.WHITE + 'No tengo licencia para conducir')


print(Fore.YELLOW + '\n>>> Testeando el segundo condicional IF')
if edad:
    print(Fore.WHITE + 'Puedo conducir porque soy mayor de edad\n')
else:
    print(Fore.WHITE + 'No puedo conducir soy menor de edad\n')


print(Fore.YELLOW + '>>> Utilizando el tercer condicional IF')
if edad >= 18:
    print(Fore.WHITE + 'Puedo conducir porque soy mayor de edad\n')
else:
    print(Fore.WHITE + 'No puedo conducir soy menor de edad\n')


print(Fore.GREEN + '################ 02 - UTILIZANDO IF, ELIF y ELSE ################')

if licencia and edad >= 18:
    print(Fore.WHITE + 'Puedo conducir porque soy mayor de edad y tengo licencia')
elif automovil:
    print(Fore.WHITE + 'Tengo automovil, pero no tengo licencia ni la edad necesaria')
else:
    print(Fore.WHITE + 'No puedo conducir no tengo ni la edad, ni licencia ni automovil')
