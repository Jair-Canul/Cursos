#Programa: función bool

#1. Numeros (int y float)

print(bool(0))       #False
print(bool(0.0))     #False
print(bool(42))      #True


#2. Teto (STR)
#Cadena vacía = nada = False
print(bool(""))     #False

#Cadena con espacio o texto = Algo = True
print(bool(" "))   #True
print(bool("Hola")) #True

#3.None ( Ausencia total de valor)

vacio = None
print(bool(vacio))   #False

print(bool(False)) #False
print(bool(True)) #True
