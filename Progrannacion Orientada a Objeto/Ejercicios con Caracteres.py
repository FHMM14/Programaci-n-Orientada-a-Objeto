#Ejercicio 13: Declara una variable inicial y asignale la primera letra de tu nombre.
inicial = 'F'  
print(f"La inicial de tu nombre es: {inicial}")
#Ejercicio 14: Pide al usuario que ingrese una letra y muestrala en pantalla.
letra = input("Ingresa una letra: ")
print(f"La letra ingresada es: {letra}")
#Ejercicio 15: Declara una variable simbolo y asignale el caracter #.
simbolo = '#'
print(f"El símbolo es: {simbolo}")
#Ejercicio 16: Comprueba si un caracter ingresado es una vocal (a, e, i, o, u).
caracter = input("Ingresa un caracter para verificar si es una vocal: ").lower()
es_vocal = caracter in 'aeiou'
if es_vocal:
 print(f"El caracter {caracter} es una vocal.")
else:
 print(f"El caracter {caracter} no es una vocal.")
