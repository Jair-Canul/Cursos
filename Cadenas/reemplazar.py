#Programa: remplazar textos en python
mensaje = "Hola mundo, mundo"

#Remplazar TODAS LAS APARICIONEs
nuevo= mensaje.replace("mundo", "Python")
print(nuevo) # Salida: Hola Python, Python

#Remplazar SOLO LA PRIMERA APARICION
uno_solo=mensaje.replace("mundo", "DEV", 1) 
print(uno_solo) # Salida: Hola DEV, mundo