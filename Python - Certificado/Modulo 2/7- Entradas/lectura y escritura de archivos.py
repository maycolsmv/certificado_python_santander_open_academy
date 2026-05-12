"""
* Lectura de archivos
Para leer el contenido de un archivo, primero debemos abrirlo utilizando la función open() 
en modo de lectura ("r"). Luego, podemos leer el contenido del archivo utilizando métodos 
como read() o readlines().
"""

archivo = open("datos.txt", "r")
contenido = archivo.read()
print(contenido)
archivo.close()


"""
* Escritura de archivos
Para escribir datos en un archivo, se abre en modo de escritura ("w") utilizando la función open(). Si el 
archivo no existe, se creará automáticamente. Si el archivo ya existe, su contenido se sobrescribirá.
""" 

archivo = open("datos.txt", "w")
archivo.write("Hola, mundo!")
archivo.close()

"""
También se puede utilizar la declaración with para manejar la apertura y cierre de archivos de manera automática.
"""

with open("datos.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)