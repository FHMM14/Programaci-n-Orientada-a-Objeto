#Ejercicio 21: Crear un vector con 5 elementos e imprimir la suma de todos los elementos del vector.
vector = [1, 2, 3, 4, 5]
suma_vector = sum(vector)
print(f"La suma de los elementos del vector {vector} es: {suma_vector}")
#Ejercicio 22: Crear un vector con 4 elementos e imprimir el resultado de multiplicar cada elemento del vector por un escalar.
vector = [1, 2, 3, 4]
escalar = int(input("Ingresa un escalar para multiplicar los elementos del vector: "))
resultado = [x * escalar for x in vector]
print(f"El resultado de multiplicar los elementos del vector {vector} por {escalar} es: {resultado}")
