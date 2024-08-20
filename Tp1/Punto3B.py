# Escribir un programa que resuelva la secuencia de Fibonacci a pedido del
# usuario. Deberá codificar una función fibonacci(numero), cuyo parámetro
# numero debe ser ingresado por el usuario y su tipo, al igual que en el ejercicio
# anterior, validado. La función debe encargarse de calcular la secuencia para
# dicho número.


def fibonacci(numero):
    if numero == 0:
        return 0
    elif numero == 1:
        return 1
    else:
        return fibonacci(numero - 1) + fibonacci(numero - 2)


numero = int(input("Ingrese un número: "))
resultado = fibonacci(numero)
print(f"El número Fibonacci para {numero} es: {resultado}")
