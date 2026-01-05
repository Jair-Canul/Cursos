print('*** Aplicación de Salud y Fitness ***')

#Constantes
META_PASOS_DIARIOS = 1000
CALORIAS_POR_PASO = 0.04 #vALOR APROXIMADO, SON KIKOCALORÍAS

#Pedimos los valores al usuario:
nombre_usuario = input('¿Cuál es tu nombre? ')
pasos_diarios = int(input('¿Cuántos pasos has caminado hoy? '))

#Verificar si el usuario alcanzó la meta de pasos diarios
meta_alcanzada = pasos_diarios >= META_PASOS_DIARIOS
meta_alcanzada_txt = 'Si' if meta_alcanzada else 'No'
#calculamos las calorías quemadas
calorias_quemadas = pasos_diarios * CALORIAS_POR_PASO

#Mostramos la información
print(f'''
Usuario: {nombre_usuario}
Pasos dados hoy: {pasos_diarios}
Calorías quemadas: {calorias_quemadas} kcal
meta de pasos diarios alcanzados: {meta_alcanzada_txt}
La meta de pasos diarias es de: {META_PASOS_DIARIOS} pasos''')
