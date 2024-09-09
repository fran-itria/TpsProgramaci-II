# Clase Pizza que representa una pizza de una variedad específica
class Pizza:
    def __init__(self, variedad):
        self.variedad = variedad


# Clase MaestroPizzero que gestiona la preparación y entrega de pizzas
class MaestroPizzero:
    def __init__(self, nom):
        self.nombre = nom
        self.pizzasPorCocinar = []  # Lista que almacenará las pizzas por cocinar
        self.pizzasPorEntregar = (
            []
        )  # Lista que almacenará las pizzas listas para entregar

    # Método para establecer o cambiar el nombre del maestro pizzero
    def establecerNombre(self, nom):
        self.nombre = nom

    # i. El comando tomarPedido debe crear un nuevo objeto de la clase Pizza,
    # de la variedad indicada en el parámetro formal var. Una vez inicializado
    # dicho objeto, debe este agregarse a la lista referenciada por el atributo
    # pizzasPorCocinar.
    def tomarPedido(self, var):
        if not var:  # Validamos que el nombre de la variedad no esté vacío
            raise ValueError("La variedad no puede estar vacía")
        nueva_pizza = Pizza(var)  # Creamos una nueva pizza con la variedad indicada
        self.pizzasPorCocinar.append(
            nueva_pizza
        )  # Agregamos la pizza a la lista de pizzas por cocinar

    # ii. El comando cocinar debe tomar todos los objetos de la clase Pizza de la
    # lista pizzasPorCocinar y depositarlos en una segunda lista,
    # pizzasPorEntregar. Si no hay pizzas por ser cocinadas, el comando no
    # tiene efecto sobre el estado interno del objeto.
    def cocinar(self):
        if self.pizzasPorCocinar:  # Verificamos si hay pizzas para cocinar
            self.pizzasPorEntregar.extend(
                self.pizzasPorCocinar
            )  # Movemos todas las pizzas a la lista de por entregar
            self.pizzasPorCocinar.clear()  # Limpiamos la lista de pizzas por cocinar

    # iii. El comando entregar retorna hasta un máximo de 2 objetos de la clase
    # Pizza de la lista pizzasPorEntregar, removiéndolos de ella. Si no hay
    # pizzas para ser entregadas, se debe retornar una lista vacía.
    def entregar(self):
        pizzas_entregadas = self.pizzasPorEntregar[
            :2
        ]  # Seleccionamos hasta 2 pizzas de la lista
        self.pizzasPorEntregar = self.pizzasPorEntregar[
            2:
        ]  # Removemos las pizzas entregadas de la lista
        return pizzas_entregadas  # Retornamos las pizzas entregadas

    # Consultas adicionales
    def obtenerNombre(self):
        return self.nombre

    def obtenerPizzasPorCocinar(self):
        return self.pizzasPorCocinar

    def obtenerPizzasPorEntregar(self):
        return self.pizzasPorEntregar
