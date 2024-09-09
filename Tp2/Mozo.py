# a. El atributo pizzas se inicializa como una lista vacía.

# b. El comando tomarPizzas agrega los objetos de la clase Pizza referenciados por 
# el parámetro formal pizzas. El mozo puede tomar hasta un máximo de 2 pizzas.

# c. servirPizzas limpia la lista pizzas, haciendo entrega de los pedidos a los clientes.

# d. obtenerEstadoLibre debe retornar True si es que la lista referenciada por el 
# atributo pizzas tiene una longitud de entre 0 y 1. Así mismo, debe retornar False 
# si su tamaño es igual a 2.
class Mozo:

    def __init__(self, nombre):
        self.nombre = nombre
        self.pizzas = []
        
    def establecerNombre(self, nombre):
        self.nombre = nombre
    
    # Punto b 
    def tomarPizzas(self, pizzas):
        if len(self.pizzas) < 2:
            self.pizzas.extend(pizzas[:2])        
        else:
            raise ValueError('El mozo puede tomar hasta 2 pizzas')

    # Punto c 
    def servirPizzas(self):
        self.pizzas.clear()
    
    def obtenerNombre(self):
        return self.nombre
    
    def obtenerPizzas(self):
        return self.pizzas

    # Punto d
    def obtenerEstadoLibre(self):
        return 0 <= len(self.pizzas) <= 1