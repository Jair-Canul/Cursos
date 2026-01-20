#Programa: Entrada Datos Python

nombre = input("Proporciona tu nombre: ")

print(f"Tu nombre es {nombre}")

#Cuidado con la conversión de tipos al trabajar con valores numericos
#Forma correcta: Envolover con int() o float()

#Para enteros (edad, cantidad)
edad= int(input("Tu edad:"))
print(f"Tu edad es {edad} años")
print(f"Tu edad dentro de 5 años será: {edad+5} años")

#Para decimales (precios, estaturas)
altura = float(input("Tu altura: "))
print(f"Tu altura es {altura} metros")