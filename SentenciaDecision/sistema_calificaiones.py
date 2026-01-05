print('*** Sistema de calificación ***')

valor_calif = float(input('Inserte la calificación (0-10) '))

if 9<=valor_calif<=10:
    print('La calificaión es una A')

elif 8<=valor_calif < 9:
    print('La calificaión es una B')

elif 7<=valor_calif < 8:
    print('La calificaión es una C')

elif 6<=valor_calif < 7:
    print('La calificaión es una D')

elif 0<=valor_calif < 6:
    print('La calificaión es una F')

else:
    print('Valor desconocido')
