# Dadas dos listas, lista1 y lista2, escribir un método listas_diferencia(lista1, lista2)
# que tome ambas como parámetros e imprima dos listas, cada una con:
# i. Los elementos en común, en orden inverso.
# ii. Los elementos no comunes, en orden alfabético.
# El programa debería arrojar el siguiente resultado:
# listas(['b', 'a', 'c'], ['e', 'b', 'd', 'c'])
# ['c', 'b']
# ['a', 'e', 'd']

def listas_diferencia(lista1,lista2):
    
    #encuentra los elementos en común en cada lista los almacena en lista vacía 
    elementos_en_comun = []
    for  xx in lista1:
        if xx in lista2 and xx not in elementos_en_comun:
            elementos_en_comun.append(xx)
    #ordena los elementos encontrados de manera ascendente 
    elementos_en_comun.sort()
    #una vez ordenados de manera ascendente ordena los elementos de manera inversa 
    elementos_en_comun.reverse()
    
    #encuentra los elementos diferentes 
    elementos_diferentes =[]
    
    for xx in lista1:
        if xx not in lista2 and xx not in elementos_diferentes:
            elementos_diferentes.append(xx)
            
    for xx in lista2:
        if xx not in lista1 and xx not in elementos_diferentes:
            elementos_diferentes.append(xx)
    
    elementos_diferentes.sort()
    

    print(f"Listas {lista1} {lista2}")
    print (f"Elementos que comparten Lista 1 y Lista 2 en orden inverso : {elementos_en_comun}")
    print (f"Elementos que difieren a Lista 1 y Lista 2 en orden alfabético: {elementos_diferentes}")

lista1 = ['a','b','d','f','h','z','h','k','y','o','v','s','n','w','q','2','4','1']
    
lista2 = ['j','l','o','p','t','g','d','v','z','c','a','b','u','e','r','w','3','6','4','6','8','1']

listas_diferencia(lista1,lista2)