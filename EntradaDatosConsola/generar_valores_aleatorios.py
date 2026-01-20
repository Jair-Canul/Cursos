#Valores aleatorios con la función randint

# import random 
#Si utilizamos el de arriba tendríamos que hacer : 
# numero = random.randint(1,10) #Esto en todas las líneas de codigo que se utilice randint
from random import randint # Esta forma de importar es más especifica 

#Generar un número aleatrorio entre 1 y 10
numero = randint(1,10)

print(f'Número aleatorio entre 1-10: {numero}')

dado = randint(1,6)
print(f'Resultado de lanzar el dado: {dado}')