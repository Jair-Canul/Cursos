#Conversión de tipo de datos

#Convertir de cadena a número
numero_cadena= ('10')
numero_entero = int(numero_cadena)
print(f'Valor numérico en cadena: {numero_cadena}')
print(f'CAdena a entero: {numero_entero}')

#convertir de cadena a flotante
numero_cadena2 = '3.14'
numero_flotante = float(numero_cadena2)
print(f'Cadena a flotante: {numero_flotante}')

#Convertir de número a cadena
numero_entero2 = 25
numero_cadena3 = str(numero_entero2)
print(f'Número a cadena {numero_cadena3}')

#Convertir a booleano
#Tipo bool es falso en los siguientes casos:
#Si el valor es 0, cadena vací, o None, entonces regresa False
#Regresa True, si el valor es distinto de 0, si es distinto de cadena vacía
#y también si es distinto de None
numero_entero3 = 0
booleano = bool(numero_entero3)
print(f'Valor booleano de 0: {booleano}')

numero_entero4 = 5
booleano2 = bool(numero_entero4)
print(f'Valor booleano de 5: {booleano2}')

cadena4 = '' #Sucede porque el largo de la cadena es 0
booleano3 = bool(cadena4)
print(f'Valor booleano de cadena vacía: {booleano3}')

cadena5 = 'Cadena con valor Jair'
booleano4 = bool(cadena5)
print(f'Valor de la cadena NO vacía: {booleano4}')

variable = None
booleano = bool(variable)
print(f'Valor cbooleano de None: {variable}')