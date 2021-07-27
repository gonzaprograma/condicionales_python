# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de práctica numérica

# Comparadores
# Ingrese dos números cualesquiera y realice las sigueintes
# comparaciones entre ellos
numero_1 = int(input('Ingrese el primer número:\n')) #32

numero_2 = int(input('Ingrese el segundo número:\n')) #-7

# Compare cual de los dos números es mayor
# Imprima en pantalla según corresponda

if numero_1 > numero_2:
    print("El número", numero_1," es mayor que el número", numero_2)
else:
    print("El número",numero_2," es mayor que el número", numero_1)

# Verifique si el numero_1 positivo, negativo o cero
# Imprima el resultado en cada caso

if numero_1 > 0:
    print("El numero", numero_1, "es positivo")
elif numero_1 < 0:
    print("El numero", numero_1, "es negativo")
else:
    print("El nuemro", numero_1, "es igual a 0")


# Verifique si el numero_1 es mayor a 0 y menor a 100
# Imprima en pantalla si se cumple o no la condición

if numero_1 > 0 and numero_1 < 100:
    print ("El nuemro", numero_1, "es mayor a 0 y menor que 100")
elif numero_1 == 0:
    print("El nuemro", numero_1, "es igual a 0")
elif numero_1 == 100:
    print("El nuemro", numero_1, "es igual a 100")
else:
    print("El nuemro", numero_1, "no se encuentra entre el 0 y el 100")

# Verifique si el numero_1 es menor a 10 o el numero_2
# es mayor a -2
# Imprima en pantalla si se cumple o no la condición

if numero_1 < 10 or numero_2 > -2:
    print("El numero {} es menor a 10 o el numero {} es mayor a -2".format(numero_1, numero_2))
else:
    print("El numero {} NO es menor a 10 o el numero {} NO es mayor a -2".format(numero_1, numero_2))