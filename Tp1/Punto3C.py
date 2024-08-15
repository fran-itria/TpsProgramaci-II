# Tal como sucede con la lógica proposicional, en Python muchas veces las
# expresiones booleanas pueden ser simplificadas manteniendo el valor de
# verdad de la expresión. Así, por ejemplo, (a and b) or (b and a) es equivalente
# a a and b. A continuación, intente simplificar las siguientes expresiones y
# escriba un procedimiento procesar_sentencias(a, b, c) que permita evaluar el
# valor de verdad de las expresiones ya simplificadas:
# i. (a or b) or (b and c)
# ii. b and c or False
# iii. a and b or c or (b and a)
# iv. a == True or b == False