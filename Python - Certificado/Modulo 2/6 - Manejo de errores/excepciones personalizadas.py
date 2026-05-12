"""
también puedes crear tus propias excepciones personalizadas. Esto es útil cuando deseas manejar situaciones específicas de tu programa.

Para crear una excepción personalizada, debes crear una clase que herede de la clase base Exception o de una de sus subclases.
"""

def funcion():
    # Código que puede generar una excepción personalizada
    #if condicion:
        raise Exception("Descripción del error")

try:
    funcion()
except Exception as e:
    print(f"Error: {str(e)}")

"""
En este ejemplo, se define una función llamada funcion(). Dentro de la función, se verifica una condición y, 
si se cumple, se genera una excepción utilizando la declaración raise. En lugar de crear una clase personalizada,
 se utiliza directamente la clase base Exception para generar la excepción.

Luego, se utiliza un bloque try-except para capturar y manejar la excepción. La variable e se utiliza para 
acceder a la descripción del error proporcionada al generar la excepción.

El manejo de errores y excepciones es una parte fundamental de la programación en Python. Te permite manejar
 situaciones inesperadas de manera controlada y evitar que tu programa se bloquee o se detenga abruptamente.

Cuando ocurre un error en tu código, Python genera una excepción. Al utilizar bloques try-except, puedes capturar 
y manejar estas excepciones de manera adecuada. Puedes especificar diferentes bloques except para manejar distintos
tipos de excepciones y realizar acciones específicas en cada caso.
"""