#Programa: Aplicar el concepto de slicing
texto= "PROGRAMACION"

#1.bÁSICO [INICIO:FIN]
print(texto[0:4]) # Salida: "PROG"

#2.Atajo desde el inicio[:fin]
print(texto[:4]) #"PROG" (asume inicio en 0)

#3.Atajo hasta el final [inicio:]
print(texto[8:]) #"CION" (hasta el ultimo caracter)

#4.Usar índices negativos
print(texto[-4:]) #"CION" (últimos 4 caracteres)

#5.PASO [::paso] (Invertir cadena)
print(texto[::-1]) #"NOICAMARGORP" (cadena invertida)
print(texto[::-2]) #"NIAAA" (cada segundo caracter desde el final)
print(texto[::2]) #"PRAAI" (cada segundo caracter desde el inicio)