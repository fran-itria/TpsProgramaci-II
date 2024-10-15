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
        print("El mozo", self.nombre, "entregó las órdenes: ", [pizza.obtenerVariedad().obtenerNombre() for pizza in self.pizzas])
        self.pizzas.clear()
    
    def obtenerNombre(self):
        return self.nombre
    
    def obtenerPizzas(self):
        return self.pizzas

    # Punto d
    def obtenerEstadoLibre(self):
        return 0 <= len(self.pizzas) <= 1