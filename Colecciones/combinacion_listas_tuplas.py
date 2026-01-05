print('*** Combinación de listas y tuplas ***')

#definir una lista que almacena tuplas de productos
productos = [
    ('P001', 'Camiseta', 20.00),
    ('P002', 'Jeans', 30.00),
]

#Imprimir la información de cada producto
#y además calcular el precio total
precio_total = 0

print('información de los productos:')
for producto in productos:
    id, descripcion,precio = producto #Umpacking
    print(f'Producto: id = {id}, descripcion = {descripcion}, precio = ${precio}')
    precio_total += precio #producto[2]
print(f'Precio total de los productos: ${precio_total}')