"""
Un conjunto es una estructura de datos mutable y no ordenada que permite
almacenar una colección de elementos únicos. Los conjuntos se encierran
entre llaves {} o se crean utilizando la función set().
"""

"""
* Creación y operaciones básicas
Para crear un conjunto, utiliza llaves o la función set():
"""
print("--Creacion y operacion--")

frutas = {"manzana", "banana", "naranja"}
numeros = set([1, 2, 3, 4, 5])

"""
Los conjuntos admiten operaciones matemáticas de conjuntos. 
unión (|)
intersección (&)
diferencia (-) 
diferencia simétrica (^).
"""
print("--Operaciones en conjuntos--")
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

union = conjunto1 | conjunto2
print(union)  

interseccion = conjunto1 & conjunto2
print(interseccion)  

diferencia = conjunto1 - conjunto2
print(diferencia)

diferencia_simetrica = conjunto1 ^ conjunto2
print(diferencia_simetrica)


"""
* Metodos de conjuntos

Los conjuntos en Python tienen varios métodos incorporados para manipular y acceder a los elementos. 

add(elemento): agrega un elemento al conjunto.
remove(elemento): elimina un elemento del conjunto. Si el elemento no existe, genera un error.
discard(elemento): elimina un elemento del conjunto si está presente. Si el elemento no existe, no hace nada.
clear(): elimina todos los elementos del conjunto.
"""
print("--Metodos de conjunto--")
rutas = {"manzana", "banana", "naranja"}

frutas.add("pera") #Añade pera al conjunto
print(frutas)  

frutas.remove("banana") #Elimina banana del conjunto
print(frutas)  

frutas.discard("uva") #Elimina uva del conjunto, como no esta no hace nada
print(frutas)  

frutas.clear() #Limpia todo el conjunto (elimina)
print(frutas)   