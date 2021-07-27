# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Comparadores
# Ingrese dos palabras cualesquiera y realice las sigueintes
# comparaciones entre ellas

texto_1 = str(input('Ingrese la primera palabra:\n')) #retenciones

texto_2 = str(input('Ingrese la segunda palabra:\n')) #percepciones

# Compare cual de las dos palabras es mayor (alfabéticamente)
# Imprima en pantalla según corresponda

if texto_1 > texto_2:
    print ("La palabra", texto_1, "es mayor a la palabra", texto_2)
elif texto_1 < texto_2:
    print("La palabra", texto_2, "es mayor a la palabra", texto_1)
else:
    print ("Las palabras", texto_1, "y", texto_2, "tienen el mismo valor alfabetico")

# Compare cual de las dos palabras tiene mayor
# cantidad de letras
# Imprima en pantalla según corresponda

if len(texto_1) > len(texto_2):
    print ("La palabra", texto_1, "es mas larga que la palabra", texto_2)
elif len(texto_1) < len(texto_2):
    print("La palabra", texto_2, "es mas larga que la palabra", texto_1)
else:
    print ("Las palabras", texto_1, "y", texto_2, "tienen la misma cantidad de letras")

# Verifique si la primera letra de la primera palabra
# es mayor a la primera letra de la segunda palabra
# Imprima en pantalla según corresponda

if texto_1[0] > texto_2 [0]:
    print("La primer letra de la palabra {} es mayor a la primer letra de la palabra {}".format(texto_1, texto_2))
elif texto_1[0] < texto_2 [0]:
    print("La primer letra de la palabra {} es mayor a la primer letra de la palabra {}".format(texto_2, texto_1))
else:
    print("Las primeras letras de la palabra {} y la palabra {} tienen el mismo valor alfabetico".format(texto_1, texto_2))


copia_texto_1 = texto_1  # Copia de la variable texto_1

# Verifique que copia_texto_1 es igual a texto_1
# Imprima en pantalla según corresponda

if copia_texto_1 == texto_1:
    print ("Se verifica que son iguales")
elif copia_texto_1 != texto_1:
    print ("Las palabras son diferentes")


# Verifique que copia_texto_1 es distinta a texto_2
# Imprima en pantalla según corresponda

if copia_texto_1 != texto_2:
    print(copia_texto_1, "es una palabra distinta a", texto_2)