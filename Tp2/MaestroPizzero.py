# 1. El comando tomarPedido debe crear un nuevo objeto de la clase Pizza,
# de la variedad indicada en el parámetro formal var. Una vez inicializado
# dicho objeto, debe este agregarse a la lista referenciada por el atributo
# pizzasPorCocinar.

# 2. El comando cocinar debe tomar todos los objetos de la clase Pizza de la
# lista pizzasPorCocinar y depositarlos en una segunda lista,
# pizzasPorEntregar. Si no hay pizzas por ser cocinadas, el comando no
# tiene efecto sobre el estado interno del objeto.

# 3. El comando entregar retorna hasta un máximo de 2 objetos de la clase
# Pizza de la lista pizzasPorEntregar, removiéndolos de ella. Si no hay
# pizzas para ser entregadas, se debe retornar una lista vacía.
from Pizza import Pizza
class MaestroPizzero:
    def __init__(self, nom):
        self.nombre = nom
        self.pizzasPorCocinar = []
        self.pizzasPorEntregar = []
        
    def establecerNombre(self, nom):
        self.nombre = nom

    # Punto 1
    def tomarPedido(self, var):
        if not var: 
            raise ValueError("La variedad no puede estar vacía")
        nueva_pizza = Pizza(var)
        self.pizzasPorCocinar.append(nueva_pizza)  

    # Punto 2
    def cocinar(self):
        if self.pizzasPorCocinar:
            self.pizzasPorEntregar.extend(self.pizzasPorCocinar)
            self.pizzasPorCocinar.clear()

    # Punto 3
    def entregar(self):
        pizzas_entregadas = self.pizzasPorEntregar[:2] 
        self.pizzasPorEntregar = self.pizzasPorEntregar[2:]
        return pizzas_entregadas

    # Consultas adicionales
    def obtenerNombre(self):
        return self.nombre

    def obtenerPizzasPorCocinar(self):
        return self.pizzasPorCocinar

    def obtenerPizzasPorEntregar(self):
        return self.pizzasPorEntregar