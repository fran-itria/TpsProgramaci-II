# Escribir un procedimiento numeros_par_impar(entrada) que, dada una lisa de
# números, eleve cada elemento impar en ella al cuadrado y los mueva a otra lista
# e imprima ambas. La lista de números la ingresa el usuario en forma de números
# separados por coma.
# Suponiendo que el usuario ingresa la siguiente lista:
# 1,2,3,4,5,6,7,8,9
# Entonces, la salida del programa debería ser:
# 2,4,6,8
# 1,9,25,49,81

def numeros_par_impar(entrada):
    lista_numeros = [int(num) for num in entrada.split(',')]
    lista_par = []
    lista_impar = []
    for numero in lista_numeros:
        if numero % 2 != 0:
            lista_impar.append(numero**2)
        else:
            lista_par.append(numero)
            
    print('Numeros impares elevados al cuadrado:', lista_impar)
    print('Numeros pares:', lista_par)
    
def validar_entrada(entrada):
    try:
        lista_numeros = [int(num) for num in entrada.split(',')]
        return True
    except ValueError:
        return False

while True:
    entrada_usuario = input('Ingrese una lista de numeros separados por coma: ')
    if validar_entrada(entrada_usuario):
        numeros_par_impar(entrada_usuario)
        break
    else:
        print('Ingreso incorrecto. Ingrese solo numeros separados por comas')