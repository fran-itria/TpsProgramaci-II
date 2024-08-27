# Escribir una función suma(numero) que resuelva la siguiente suma, asumiendo
# que numero = 10:
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
# En el programa que invoque dicha función:
# i. El usuario debe poder ingresar el valor del parámetro numero.
# ii. Debe validarse que el dato ingresado por el usuario corresponda a
# un dígito, y no a otro tipo de dato como un carácter.
# iii. El cálculo debe realizarse utilizando algún tipo de bucle (ej: for,
# while).
# BONUS: Luego, codificar una función equivalente que utilice recursividad.

# pide al usuario que ingrese un numero y verifica que el dato ingresado sea un número
def numero_ingresado ():
    pedir_numero = input ("Ingrese un número positivo: ")
    while not pedir_numero.isdigit():
        print ("El número ingresado no corresponde a un número positivo, por favor intente nuevamente.")
        pedir_numero = input ("Ingrese un número positivo: ")
    return int(pedir_numero)

def suma_iterativa(numero):
    contador = 0
    for xx in range (1, numero +1):
        contador += xx
    return contador

def suma_recursiva(numero):
    if numero == 1:
        return 1
    else:
        return numero + suma_recursiva(numero -1)
    
numero = numero_ingresado()
resultado_iterativo= suma_iterativa(numero)
resultado_recursivo = suma_recursiva(numero)
print (f"La suma de los números del 1 al {numero} usando iteración es: {resultado_iterativo}\n")
print(f"El resultado de la suma de los números de 1 a {numero} usando recursividad es: {resultado_recursivo}\n")