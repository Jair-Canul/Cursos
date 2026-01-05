#inmutabilidad en cadenas
animal = "Gato"
# Intentamos cambiar el primer caracter
#animal[0] = "P" # Esto generará un error

#CORRECTO: Concatnar (Sumar)
plural= animal + "s"
print(animal)  # Salida: Gato
print(plural)  # Salida: Gatos