"""
* Importar módulos
Para utilizar un módulo en nuestro programa, debemos importarlo utilizando la declaración 
import. Podemos importar un módulo completo o funciones específicas de un módulo.
"""

import math


resultado = math.sqrt(25)
print(resultado)  # Imprime 5.0
"""
En este ejemplo, se importa el módulo math utilizando la declaración import. 
Luego, se utiliza la función sqrt() del módulo math para calcular la raíz cuadrada de 25.

También podemos importar funciones específicas de un módulo utilizando la sintaxis from módulo import función.
"""

from math import sqrt

resultado = sqrt(25)
print(resultado)  # Imprime 5.0


"""
En este caso, se importa solo la función sqrt() del módulo math, lo que nos permite utilizarla 
directamente sin tener que precederla con el nombre del módulo.
"""
print("-----------------------------")

"""
La biblioteca estándar de Python ofrece una amplia gama de módulos con funciones y clases útiles. 
Algunos ejemplos:
math: sqrt() (raíz cuadrada), sin() (seno), cos() (coseno), entre otras.
random: genera números aleatorios, como random() (número aleatorio entre 0 y 1), randint() (número entero aleatorio en un rango), entre otras
datetime: fechas y horas, datetime.now() (fecha y hora actual), datetime.date() (fecha), datetime.time() (hora), entre otras.
"""



import random
import datetime


numero_aleatorio = random.randint(1, 10)
print(numero_aleatorio)  # Imprime un número entero aleatorio entre 1 y 10


fecha_actual = datetime.datetime.now()
print(fecha_actual)  # Imprime la fecha y hora actual