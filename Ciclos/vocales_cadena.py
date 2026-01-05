cadena = "Hola Mundo"
vocales = "aeiouAEIOU"
contador = 0

for letra in cadena:
    if letra in vocales:
        contador += 1

print(contador)