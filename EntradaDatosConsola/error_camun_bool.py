#Error comun de principiante

respuesta_usuario =  "False" #Esto es texto

#La función bool evalúa si el string está vacio

es_verdad = bool(respuesta_usuario)

print(f"El valor es: {es_verdad}")

#output: El valor es: True
#¿Por qué? Porque el string "False" no está vacío

#Forma correcta de validar vacío:
texto_vacio = ""
print(bool(texto_vacio))  #False