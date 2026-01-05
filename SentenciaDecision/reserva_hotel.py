print('*** Sistema de Reserva de Hotel ***')

CUARTO_SIN_VISTA = 150.50
CUARTO_CON_VISTA = 190.50

nombre_cliente = input('Nombre del Cliente: ')
dias_estadia = int(input('Días de estadía: '))
vista_mar = input('¿Con vista al mar?(Si/No): ')
vista_mar=vista_mar.strip().lower() == 'si'
vista_mar_txt = 'Si' if vista_mar else 'No'
if vista_mar:
    costo_total = dias_estadia * CUARTO_CON_VISTA
    print(f'''
Cliente: {nombre_cliente}
Dias de estadía: {dias_estadia}
Costo total: ${costo_total:.2f}
¿Habitación con vista al mar?: {vista_mar_txt}''')
else:
    costo_total = dias_estadia * CUARTO_SIN_VISTA
    print(f'''
Cliente: {nombre_cliente}
Dias de estadía: {dias_estadia}
Costo total: ${costo_total:.2f}
¿Habitación con vista al mar?: {vista_mar_txt}''')