"""
* Creación y acceso
Para crear una lista, elementos entre corchetes []:
"""
print("--Creacion y acceso--")
frutas = ["manzana", "banana", "naranja"]

#Para acceder a los elementos de una lista, utiliza el índice del elemento entre corchetes. Los índices comienzan desde 0.

print(frutas[0])  # Imprime "manzana"
print(frutas[1])  # Imprime "banana"
print(frutas[2])  # Imprime "naranja"

#También se puede acceder a los elementos desde el final de la lista utilizando 
#índices negativos. El índice -1 representa el último elemento, -2 representa el penúltimo, y así sucesivamente.

print(frutas[-1])  # Imprime "naranja"
print(frutas[-2])  # Imprime "banana"
print(frutas[-3])  # Imprime "manzana"

"""
Métodos de listas
Las listas en Python tienen varios métodos incorporados que nos permiten manipular y modificar los elementos de la lista. Algunos métodos comunes son:

append(elemento): agrega un elemento al final de la lista.
insert(indice, elemento): inserta un elemento en una posición específica de la lista.
remove(elemento): elimina la primera aparición de un elemento en la lista.
pop(indice): elimina y devuelve el elemento en una posición específica de la lista.
sort(): ordena los elementos de la lista en orden ascendente.
reverse(): invierte el orden de los elementos en la lista.
"""
print("--Metodos--")

frutas = ["manzana", "banana", "naranja"]

frutas.append("pera")
print(frutas)                       # Agrega pera a la lista

frutas.insert(1, "uva")
print(frutas)                       # Agrega una a una posicion especifica

frutas.remove("banana")
print(frutas)                       # Elimina banana de la lista

fruta_eliminada = frutas.pop(2)     #Elomona el elemento y lo almacena en una variable
print(frutas)                       # Imprime las que no se han eliminado
print(fruta_eliminada)              # Imprime el elemento almacenado 

frutas.sort()                       # ordena alfabeticamente
print(frutas)  
frutas.reverse()                    #Invierte el orden actual de la lista
print(frutas)  


"""
* Listas de comprensión
Las listas de comprensión son una forma concisa de crear nuevas listas basadas 
en una secuencia existente. Permiten filtrar y transformar los elementos de 
una lista en una sola línea de código.

nueva_lista = [expresion for elemento in secuencia if condicion]
"""
print ("--Listad de compresion--")
numeros = [1, 2, 3, 4, 5]
cuadrados = [x ** 2 for x in numeros if x % 2 == 0]
print(cuadrados)  # Imprime [4, 16]