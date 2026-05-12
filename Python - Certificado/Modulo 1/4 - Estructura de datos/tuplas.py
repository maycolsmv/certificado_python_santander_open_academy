"""
* Creación y acceso
Para crear una tupla, encierra los elementos entre paréntesis. 
A diferencia de las listas, las tuplas son inmutables, lo que significa que no se pueden modificar una vez creadas.

punto = (3, 4)
Para acceder a los elementos de una tupla, se utiliza el índice del elemento entre corchetes, similar a las listas:
"""
print("--Creacion y acceso--")
punto = (3, 4)

print(punto[0])  # Imprime 3

print(punto[1])  # Imprime 4


"""
* Métodos de tuplas
Aunque las tuplas son inmutables, Python proporciona varios métodos útiles para trabajar con ellas:

- count(elemento): devuelve el número de veces que aparece un elemento en la tupla. 
- index(elemento): devuelve el índice de la primera aparición de un elemento en la tupla. 
  Opcionalmente, se puede especificar el inicio y fin de la búsqueda. 
len(tupla): aunque no es un método de tupla propiamente dicho, esta función incorporada devuelve la longitud de la tupla.
"""
print("--Metodos de tuplas")
mi_tupla = (1, 2, 3, 2, 4, 2)

print (mi_tupla.index(2))   # Salida: 1

print (mi_tupla.index(2, 2))   #Salida: 3

print (mi_tupla.index(2, 2, 4))   #Salida: 3