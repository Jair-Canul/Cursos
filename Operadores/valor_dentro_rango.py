print('*** Valor Dentro de Rango ***')

VALOR_MINIMO = 0
VALOR_MAXIMO = 5

dato = int(input(f'Introduce un número entre {VALOR_MINIMO} Y {VALOR_MAXIMO} para validar: '))

validar = VALOR_MINIMO <= dato <= VALOR_MAXIMO
print(f'¿Valor dentro del rango? {validar}')
