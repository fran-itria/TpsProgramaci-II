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
    for elemento in lista1:
        if (elemento in lista2) and (elemento not in elementos_en_comun):
            elementos_en_comun.append(elemento)
    # ordena alfabeticamente los elementos en común
    elementos_en_comun.sort()
    # ordena los elementos de manera inversa 
    elementos_en_comun.reverse()
    
    #encuentra los elementos diferentes 
    elementos_diferentes =[]
    for elemento in lista1:
        if elemento not in elementos_en_comun:
            elementos_diferentes.append(elemento)
            
    for elemento in lista2:
        if elemento not in elementos_en_comun:
            elementos_diferentes.append(elemento)
    
    elementos_diferentes.sort()
    

    print(f"Listas {lista1} {lista2}")
    print (f"Elementos que comparten en orden inverso : {elementos_en_comun}")
    print (f"Elementos que difieren en orden alfabético: {elementos_diferentes}")

lista1 = ['a','b','d','f','h','z','h','k','y','o','v','s','n','w','q','2','4','1']
    
lista2 = ['j','l','o','p','t','g','d','v','z','c','a','b','u','e','r','w','3','6','4','6','8','1']

listas_diferencia(lista1,lista2)