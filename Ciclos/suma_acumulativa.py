print('*** Suma Acumulativa ***')

#Sumar los primeros 5 números
MAXIMO = 5
numero = 1
acumulador_suma = 0

#Empezamos a iterar
while numero <= MAXIMO:

    #imprimir lo que se va a sumar
    print(f'(acumulador_suma + numero) --> {acumulador_suma} + {numero}')

    acumulador_suma += numero #Aqui se aplica la suma por cada iteración
    numero += 1 #Sirve como contaodr

    #imprimir el resultado de la suma parcial
    print(f'Suma parcial acumulada: {acumulador_suma}')

print(f'\nResultado suma acumulada: {acumulador_suma}')
