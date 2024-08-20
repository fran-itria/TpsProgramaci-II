# Escriba un procedimiento procesar_palabras(entrada) que acepte una
# secuencia de palabras separadas por coma, las ordene y las imprima.
# Suponiendo que la entrada provista al programa es la siguiente:
# te,felicito,que,bien,actuas
# La salida esperada es:
# actuas,bien,felicito,que,te
def procesar_palabras(entrada):
    if(entrada == ''):
        print('No se ingresaron palabras')
        return
    elif(not ',' in entrada):
        print("Se ingreso una sola palabra: " + entrada)
        return
    palabras = entrada.split(',')
    palabras.sort()
    print(','.join(palabras))
    return palabras

procesar_palabras('te,felicito,que,bien,actuas')
procesar_palabras('hola, como, andas, ?')
procesar_palabras('')
procesar_palabras('hola')