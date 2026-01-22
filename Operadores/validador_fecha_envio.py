#Imagina que trabajas en una empresa de logística. 
# El sistema recibe una fecha de entrega en un solo 
# texto (formato día-mes-año) y tú debes 
# determinar si el paquete se entrega en el 
# "Mes de Ofertas".#
print('*** Validador de Fecha de Envío ***')
fecha_envio = input("Ingresa fecha de envío (dd-mm-aaaa): ")

fecha = fecha_envio.split('-')

entra_descuento = (fecha[0] == '24' and fecha[1] == '12')

print(f'¿El envío del paquete tiene desceuento?: {entra_descuento}')