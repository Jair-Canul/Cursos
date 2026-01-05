print('*** Calculo de Área y Perímetro de un Rectángulo ***')

#Entrada
base = float(input('Ingresa el tamaño de la base del rectángulo (cm): '))
altura = float(input('Ingresa el tamaño de la altura del rectángulo (cm): '))

#área
area = base * altura

#perímetro
perimetro = 2 * (base + altura)

print(f'''
El área del rectángulo es de: {area}cm
El perímetro del rectángulo es de: {perimetro}cm''')
