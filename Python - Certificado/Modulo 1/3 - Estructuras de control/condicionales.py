#ESTRUCTURAS CONDICIONALES 

"""
* if
if condicion:

   # Bloque de código a ejecutar si la condición es verdadera instrucciones
"""
edad = 18

if edad >= 18:
   print ("Eres mayor de edad.")


#* if-else
edad = 15

if edad >= 18:
   print ("Eres mayor de edad.")

else:
   print ("eres menor de edad.")


"""
* if - elise - else
if condicion1:

   # Bloque de código a ejecutar si la condicion1 es verdadera
   instrucciones

elif condicion2:

   # Bloque de código a ejecutar si la condicion2 es verdadera
   instrucciones

else:

   # Bloque de código a ejecutar si ninguna condición anterior es verdadera
   instrucciones
"""
calificacion = 85

if calificacion >= 90:
   print ("Excelente")

elif calificacion >= 80:
   print ("Muy bueno")

elif calificacion >= 70:
   print ("Bueno")

else:
   print ("Necesita mejorar")