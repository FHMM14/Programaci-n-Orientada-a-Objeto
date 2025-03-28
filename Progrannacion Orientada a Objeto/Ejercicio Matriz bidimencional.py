#Diseñar el algoritmo correspondiente a un programa, 
# que: Crea una tabla bidimensional de longitud 5x5 y nombre matriz.
#Carga la tabla con valores numéricos enteros.
#Suma todos los elementos de cada fila y todos los elementos de cada columna visualizando los resultados en pantalla.
matriz = [[int(input(f"Ingresa el valor para la posicion ({i},{j}): ")) for j in range(5)] for i in range(5)]
suma_filas = [sum(fila) for fila in matriz]
suma_columnas = [sum(matriz[i][j] for i in range(5)) for j in range(5)]
print("Suma de los elementos de cada fila:")
for i, suma in enumerate(suma_filas):
 print(f"Fila {i+1}: {suma}")
print("Suma de los elementos de cada columna:")
for j, suma in enumerate(suma_columnas):
 print(f"Columna {j+1}: {suma}")
   