"""
* For
El bucle for se utiliza para iterar sobre una secuencia (como una lista, una tupla o una cadena) o cualquier objeto iterable.

for variable in secuencia:

    # Bloque de código a repetir
    instrucciones
"""
frutas = ["manzana", "banana", "naranja"]

for fruta in frutas:
    print(fruta)


"""
* While
El bucle while se utiliza para repetir un bloque de código mientras una condición sea verdadera. 

while condicion:

    # Bloque de código a repetir
    instrucciones
"""
contador = 0

while contador < 5:

    print(contador)
    contador += 1



#CONTOL DE BUCLES


"""
* Break
La instrucción break se utiliza para salir prematuramente de un bucle, independientemente 
de la condición. Cuando se encuentra un break, el bucle se detiene y el flujo de ejecución c
ontinúa con la siguiente instrucción fuera del bucle.
"""
contador = 0

while True:

    print(contador)
    contador += 1


    if contador == 5:
        break


"""
* Continue
La instrucción continue se utiliza para saltar el resto del bloque de código dentro de un bucle y pasar a la siguiente iteración.
"""
for i in range(10):

    if i % 2 == 0:
        continue
    print(i)


"""
* Pass
La instrucción pass es una operación nula que no hace nada. 
Se utiliza como marcador de posición cuando se requiere una 
instrucción sintácticamente, pero no se desea realizar ninguna acción.
"""
for i in range(5):
    pass