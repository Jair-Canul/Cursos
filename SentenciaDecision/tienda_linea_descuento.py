print('*** Sistema de Descuentos ***')

MONTO = 1000

monto_compra = float(input('¿Cuál fue el monto de tu compra? $'))
membresia = input('¿Eres miembro de la tienda (Si/No)? ')

if monto_compra >= MONTO and membresia.strip().lower() == 'si':
    descuento1 =monto_compra * 0.10
    monto_descuento1 = monto_compra - descuento1
    print(f'''
Felicidades, has obtenido un descuento del 10%
Monto de la compra: ${monto_compra:.2f}
Monto del descuento: ${descuento1:.2f}
Monto final de la compra con descuento: ${monto_descuento1:.2f}''')

elif monto_compra < MONTO and membresia.strip().lower() == 'si':
    descuento2 = monto_compra *0.05
    monto_descuento2= monto_compra - descuento2
    print(f'''
    Felicidades, has obtenido un descuento del 5%
    Monto de la compra: ${monto_compra:.2f}
    Monto del descuento: ${descuento2:.2f}
    Monto final de la compra con descuento: ${monto_descuento2:.2f}''')
else:
    print(f'''
No obtuviste ningun tipo de descuento
Te invitamos a hacerte miembro de la tienda
Monto final de la compra: ${monto_compra:.2f}''')