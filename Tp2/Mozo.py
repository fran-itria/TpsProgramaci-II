class Mozo:

    def __init__(self, nombre):
        self.nombre = nombre
        self.pizzas = []        # El atributo pizzas se inicializa como una lista vacía
        
    def establecerNombre(self, nombre):
        self.nombre = nombre
        
# El comando tomarPizzas agrega los objetos de la clase Pizza referenciados por 
# el parámetro formal pizzas. El mozo puede tomar hasta un máximo de 2 pizzas
    def tomarPizzas(self, pizzas):
        if len(self.pizzas) < 2:
            self.pizzas.extend(pizzas[:2])        
        else:
            raise ValueError('El mozo puede tomar hasta 2 pizzas')
    
# servirPizzas limpia la lista pizzas, haciendo entrega de los pedidos a los clientes
    def servirPizzas(self):
        self.pizzas.clear()
    
    def obtenerNombre(self):
        return self.nombre
    
    def obtenerPizzas(self):
        return self.pizzas
    
# obtenerEstadoLibre retorna True si es que la lista referenciada
# por el atributo pizzas tiene una longitud de entre 0 y 1. 
# Retorna False si su tamaño es igual a 2

    def obtenerEstadoLibre(self):
        return 0 <= len(self.pizzas) <= 1