#Crear un vector de 5 elementos de cadenas de caracteres, inicializa el vector con datos leídos por el teclado. 
#Copia los elementos del vector en otro vector pero en orden inverso, y muéstralo por la pantalla.
vector_cadenas = [input(f"Ingresa la cadena {i+1}: ") for i in range(5)]
vector_inverso = vector_cadenas[::-1]
print("Vector en orden inverso:")
for cadena in vector_inverso:
 print(cadena)
