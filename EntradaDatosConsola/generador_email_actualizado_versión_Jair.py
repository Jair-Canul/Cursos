#Version con entrada de datos
#Generador de Email
#Se solicita crear una nueva versión del sistema generador de emails
# Para generar un email se debe solicitar: 
# Nombre 
# Apellidos
# Nombre Empresa
# Extensión Dominio

#Entrada de datos
nombres = input("Proporciona tu nombre(s):")
apellidos = input("Proporciona tus apellidos: ")
nombre_empresa = input("Proporciona el nombre de la empresa sin acentos: ")
extension_dominio = input("Proporciona la extensión del dominio(.com, .es, .org): ")

#Proceso:
nombres = nombres.lower().strip().replace(" ",".")
apellidos = apellidos.lower().strip().replace(" ",".")
nombre_empresa = nombre_empresa.lower().strip().replace(" ","")

#Generar email
email = nombres+"."+apellidos+"@"+nombre_empresa+extension_dominio

print(f"""Tu email generado por el sistema es: 
      {email}
      ¡Gracias por utilizar el sistema!""")