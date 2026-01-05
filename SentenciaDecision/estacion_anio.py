print('*** Identificador de la Estación del año ***')

valor_mes = int(input('Proporcione el valor del mes (1-12): '))

if 1<= valor_mes <=2 or valor_mes == 12:
    print(f'La estación para el mes {valor_mes}: Es Invierno')
#elif valor_mes == 12:
    #print(f'Es invierno')
elif 3 <= valor_mes <=5:
    print(f'La estación para el mes {valor_mes}: Es Primavera')
elif 6 <= valor_mes <=8:
    print(f'La estación para el mes {valor_mes}: Es Verano')
elif 9 <= valor_mes <= 11:
    print(f'La estación para el mes {valor_mes}: Es Otoño')
else:
    print('Estación Desconocida')

