# Escribir una función de nombre palabra_no_tiene_letras(palabra,
# letras_prohibidas), la cual retorne True si es que los caracteres que componen
# una palabra no se encuentran en una lista de caracteres prohibidos.
def palabra_no_tiene_letras(palabra, letras_prohibidas):
    for letra in palabra:
        if letra in letras_prohibidas:
            return False
    return True

palabra = input("Introduce una palabra: ")
letras_prohibidas = input("Introduce las letras prohibidas, separadas por comas: ").split(',')

resultado = palabra_no_tiene_letras(palabra, letras_prohibidas)

if resultado:
    print("La palabra no contiene ninguna de las letras prohibidas.")
else:
    print("La palabra contiene al menos una de las letras prohibidas.")
