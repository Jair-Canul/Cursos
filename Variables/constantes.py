import math

print("*** Constantes en Python ***")

PI=3.1416 #En mayusculas se indica que es una constante (no debe cambiarse su valor)
print("El valor de PI es:",PI)

NOMBRE_BASE_DATOS = "clientes_db"
print("Nombre de la base de datos",NOMBRE_BASE_DATOS)

#Esto NO se debe hacer, no se debe modificar el valor de una constante
NOMBRE_BASE_DATOS = "listado_clientes_db"
print("No cambiar el valor de una constante:",NOMBRE_BASE_DATOS)

#usar una constante del lenguaje de python, aunque en este caso no está en mayúsculas
print("Valor de math.pi:", math.pi)