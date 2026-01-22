#Generación ticket venta
# 
# Supongamos que compramos varios artículos en el supermercado y 
# queremos obtener el ticket de venta total incluyendo impuestos
# 
# El sistema solicitará el precio de cada producto a comprar y 
# el usuario deberá indicar su precio (valor de tipo con punto decimal)
# 
# El sistema debe realizar la suma de cada productom calcular el
# impuesto y finalmente imprimir el total de la compra
# 
# Solicitar un descuento #

print('*** Generación de Ticket de Venta ***')

precio_leche = float(input('Precio leche: '))
precio_pan = float(input('Precio pan: '))
precio_lechuga = float(input('Precio lechuga: '))
precio_platanos = float(input('Precio plátanos: '))
descuento_porcentaje = float(input('Descuento a aplicar (%): '))

#Calculo del subtotal(sin incluir impuestos)
subtotal = precio_leche + precio_pan + precio_lechuga + precio_platanos

#Aplicar descuento al subtotal
descuento = subtotal * (descuento_porcentaje / 100)

#Calcular subtotal con descuento
subtotal_con_descuento = subtotal - descuento

#Calculo impuesto (16%)
impuesto = subtotal_con_descuento* 0.16

#Calculo total de la compra (con impuestos)
costo_totla_compra = subtotal_con_descuento + impuesto 

print(f'''
subtotal: ${subtotal:.2f}
descuento ({descuento_porcentaje}%): ${descuento:.2f}
subtotal con descuento: ${subtotal_con_descuento:.2f}
impuesto (16%): ${impuesto:.2f}
costo total de la compra: $ {costo_totla_compra:.2f} 
''')