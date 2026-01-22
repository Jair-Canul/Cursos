#Sistemas Descuentos  VIP
# una tienda de supermercado ofrece un descuento especial a clientes 
# que compren 10 o más artículos por día y además sean miembros de la tienda.
#El sistema debe solicitar al clientre que indique cuántos arrtículos 
# ha comprado en el día y preguntarle si cuenta con la membresía de
# la tienda.
# 
# En caso de haber comprado 10 o más productos y
# ser miembro de la tienda entonces tendrá accrsso al descuento VIP#

print("*** Sistema de Descuentos VIP ***")
NO_PRODUCTOS_DESCUENTOS = 10
cantidad_productos = int(input("¿Cuántos productos compraste hoy?: "))
tiene_membresia = input("¿Tienes la membresía de la tienda? (si/no): ")

es_elegible_descuento = (cantidad_productos >= NO_PRODUCTOS_DESCUENTOS 
                         and tiene_membresia.strip().lower() == 'si')

print(f'¿Tienes accesso al descuento VIP?: {es_elegible_descuento}')
