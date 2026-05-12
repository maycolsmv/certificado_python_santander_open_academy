"""
Un diccionario es una estructura de datos mutable y no ordenada que permite 
almacenar pares de clave-valor. Cada elemento en un diccionario consiste en 
una clave única y su valor correspondiente. Los diccionarios se encierran
entre llaves {}, y los pares clave-valor se separan por comas.
"""

"""
* Creación y acceso
Para crear un diccionario, utiliza llaves y separa las claves y valores con dos puntos.
Para acceder a los valores de un diccionario, utiliza la clave correspondiente entre corchetes:
"""
print("--Creacion y acceso--")
persona = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}
print(persona["nombre"])  
print(persona["edad"])    
print(persona["ciudad"])  

"""
* Métodos de diccionarios
Los diccionarios en Python tienen varios métodos incorporados para manipular y acceder a los elementos. 

- keys(): devuelve una vista de todas las claves del diccionario.
- values(): devuelve una vista de todos los valores del diccionario.
- items(): devuelve una vista de todos los pares clave-valor del diccionario.
- update(otro_diccionario): actualiza el diccionario con los pares clave-valor de otro diccionario.
"""
print("--metodos de diccionario--")
persona = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}

print(persona.keys())    # Imprime todas las claves
print(persona.values())  # Imprime todos los valores
print(persona.items())   # Imprime todos los pares clave-valor

persona.update({"profesion": "Ingeniero"}) #agrega una un nuevo par clave-valor
print(persona)  # Imprime todo el diccionario