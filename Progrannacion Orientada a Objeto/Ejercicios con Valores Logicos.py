#Ejercicio 9: Declara una variable esMayor y asígnale Verdadero si la edad ingresada por el usuario es mayor o igual a 18.
esMayor = "Verdadero"
edad = int(input("Ingresa tu edad: "))
if edad >= 18:
 print(esMayor)
else:
 print("Usted es menor de 18 años.")
#Ejercicio 10: Crea un programa que verifique si un numero ingresado es positivo o negativo.
numero = int(input("Ingresa un numero para identificar si es positivo o negativo: "))
if numero > 0:
 print(f"El numero {numero} es positivo.")
else:
 print(f"El numero {numero} es negativo.")
#Ejercicio 11: Declara una variable llueve y usa una condicion para mostrar si debes llevar paraguas
llueve = "Debes llevar paraguas"
Pregunta = input("¿Esta lloviendo? (si/no): ").strip().lower()
if Pregunta == "si":
 print(llueve)
elif Pregunta == "no":
 print("No necesitas llevar paraguas.")
else:
 print("Respuesta no valida. Por favor, responde con si o no.")
#Ejercicio 12: Escribe un programa que compare dos numeros y muestre verdadero si son iguales.
num1 = (input("Ingresa el primer numero para compararlo con otro: "))
num2 = (input("Ingresa el segundo numero: "))
son_iguales = num1 == num2
respuesta = "Verdadero" if son_iguales else "Falso"
print(f"¿Son iguales los numeros {num1} y {num2}?  {respuesta}")
