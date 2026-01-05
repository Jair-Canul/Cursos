#Concatenación de Cadenas
cadena1 = "Jair"
cadena2 = "David"
#utilizando el operador +
concatenacion = cadena1 + " " + cadena2
print("usando + : " + concatenacion)

#Usando el método print
edad = 28
print("Usamdo comas:", "Nombre:", concatenacion, ", Edad:", edad)

#utilizando el método join
concatenacion = "".join([cadena1," ",cadena2])
print(concatenacion)

#Concatenación con f-strings (Python 3.6+)
nombre = "Jair"
edad = 24
print(f"Hola {nombre}, tienes {edad - 0} años.")