#PROGRAMA: GENERADOR DE EMAIL

nombre = "Ubaldo Acosta Soto"
empresa= "Global Mentoring"
dominio= "com.mx"

#Normalizamos todo
nombre_normalizado = nombre.lower().replace(" ", ".")
empresa_normalizado =empresa.lower().replace(" ", "")
dominio_normalizado ="@"+empresa_normalizado+"."+dominio

#Generamos el email
email= nombre_normalizado+dominio_normalizado
#Imprimimos todo
print("*"*3 + " Generador de Email " + "*"*3)
print("Nombre usuario: "+nombre)
print("Nombre usuario normalizado: "+nombre_normalizado)
print()
print("Nombre empresa:"+empresa)
print("Extensión del dominio: "+dominio)
print("Extensión del dominio normalizado: "+dominio_normalizado)
print()
print("Email final Generado: "+email)





