from random import randint
print('*** Juego de Adivinanza ***')

numero_adivinanza = randint(1,50)
intentos = 0
adivinanza = None
intentos_maximos = 5
while adivinanza != numero_adivinanza and intentos <intentos_maximos:
    adivinanza = int(input('Adivina el número secreto entre 1-50: '))
    if adivinanza < numero_adivinanza:
        print('El número secreto es mayor')
    elif adivinanza > numero_adivinanza:
        print('El número secreto es menor')
    intentos += 1
if adivinanza == numero_adivinanza:
    print(f'Feliciddes, adivinaste el número secreto en {intentos} intentos')
else:
    print(f'Lo siento, has agotado tus intentos máximos: {intentos_maximos}'
          f'El número secreto era: {numero_adivinanza}')