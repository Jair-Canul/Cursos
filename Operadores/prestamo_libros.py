#Sistema Préstamo de Libros
# 
# Se pide crear un sistema para una biblioteca, la cual desea prestar
# libros si cumple con cualquera de las siguientes condiciciones:
# 
# 1. El usuario tiene credencial de estudiantes
# 2.EL usuario vive a no más de 3Km a la redonda
# 
# Si cumple con cualquiera de estas condiciones 
# se le puede prestar el libro#

print('*** Sistema de préstamos de Libros ***')

DISTANCIA_PERMITIDA_KM = 3
tiene_credencial = input('¿Cuentas con credencial de estudiante? (si/no): ')
distancia_biblioteca_km = int(input('¿A cuantos km vives de la biblioteca?: '))

es_elegible_prestamo = (tiene_credencial.strip().lower() == 'si'
                        or distancia_biblioteca_km <= DISTANCIA_PERMITIDA_KM )

print(f'¿Eres elegible para prestamo de libros?: {es_elegible_prestamo}')