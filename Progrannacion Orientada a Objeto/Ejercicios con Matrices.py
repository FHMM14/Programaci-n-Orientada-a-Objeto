#Ejercicio 23: Crear una matriz de 2x2 e imprimir el promedio de todos sus elementos.
matriz = [[1, 2],[3, 4]]
suma_elementos = sum(sum(fila) for fila in matriz)
cantidad_elementos = len(matriz) * len(matriz[0])
promedio = suma_elementos / cantidad_elementos
print(f"El promedio de los elementos de la matriz {matriz} es: {promedio}")
#Ejercicio 24: Crear una matriz 2x3 y luego transponerla (convertir filas en columnas y viceversa).
matriz = [[1, 2, 3],[4, 5, 6]]
transpuesta = [[fila[i] for fila in matriz] for i in range(len(matriz[0]))]
print(f"La matriz original es: {matriz}")
print(f"La matriz transpuesta es: {transpuesta}")
