# A continuación, se presenta el código de un programa que, ante la edad ingresada por el usuario,
# este presenta el equivalente en días, meses y años. Se solicita al alumno que lo refactorice de
# manera tal que:
# a. Se elimine la sentencia if / else de la función anio_bisiesto.
# b. Las múltiples sentencias if la función dia_mes utilicen la cláusula in en lugar de
# varias cláusulas or.
# c. Se agregue una sentencia que valide que la edad ingresada por el usuario es
# numérica.
# d. Se agregue una función que encapsule el cálculo del equivalente de la edad en
# días y que tome como parámetros las variables hora_local, anio_comienzo y
# anio_fin.
# e. Todas las funciones sean transportadas a un archivo auxiliar de funciones
# llamado funciones.py, y este sea importado desde el programa principal.

import time
from calendar import isleap
from funciones import anio_bisiesto, calcular_dias_mes, calcular_equivalente_en_dias, isleap

# ingreso de datos del usuario
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
while not edad.isnumeric():
    print("Por favor, ingrese un valor numerico")
    edad = input("Ingrese su edad: ")
# seteo inicial de variables
hora_local = time.localtime(time.time())
anios = int(edad)
anio_comienzo = int(hora_local.tm_year) - anios
anio_fin = anio_comienzo + anios
meses = anios * 12 + hora_local.tm_mon
dias = 0
# calcular los dias
for a in range(anio_comienzo, anio_fin):
    if anio_bisiesto(a):
        dias = dias + 366
    else:
        dias = dias + 365
# agregar los días transcurridos en este año
for m in range(1, hora_local.tm_mon):
    dias = dias + calcular_dias_mes(m, anio_bisiesto(hora_local.tm_year))
# agregar los días transcurridos en este mes
dias = dias + hora_local.tm_mday
# imprimir la edad del usuario
print("La edad de %s es %d años o " % (nombre, anios), end="")
print("%d meses o %d días" % (meses, dias))