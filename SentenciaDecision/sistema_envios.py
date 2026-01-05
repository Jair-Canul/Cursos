print(f'*** Sistema de Envíos ***')

NACIONAL = 10
INTERNACIONAL =20
#destino
destino = input('Destino (Nacional/Internacional):')
destino = destino.strip().lower()
#peso
peso = float(input('Peso del paquete(Kg): '))

costo_envio = None

if destino == 'nacional':
    costo_envio = peso * NACIONAL
elif destino == 'internacional':
    costo_envio = peso * INTERNACIONAL
else:
   print('Destino no valido. ingrese el valor de Nacional o Internacional')
if costo_envio is not None:
    print(f'El costo de envío del paquete es: ${costo_envio:.2f}')