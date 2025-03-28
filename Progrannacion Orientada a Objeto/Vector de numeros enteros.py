#Realizar un programa que defina un vector llamado "vector_numeros" de 10 enteros, 
#a continuación lo inicialice con valores aleatorios (del 1 al 10) 
#y posteriormente muestre en pantalla cada elemento del vector junto con su cuadrado y su cubo.
import random
vector_numeros = [random.randint(1, 10) for _ in range(10)]
for numero in vector_numeros:
 cuadrado = numero ** 2
 cubo = numero ** 3
 print(f"Número: {numero}, Cuadrado: {cuadrado}, Cubo: {cubo}")
