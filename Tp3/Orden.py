class Orden:
    # Atributos de clase
    ESTADO_INICIAL = 1
    ESTADO_PARA_ENTREGAR = 2
    ESTADO_ENTREGADA = 3
    
    # Atributos de instancia
    def __init__(self, nro, pizzas):
        self.nroOrden = nro
        self.pizzas = pizzas
        self.estadoOrden = Orden.ESTADO_INICIAL
        
    # Comandos
    def establecerNroOrden(self, nro):
        self.nroOrden = nro
    def establecerPizzas(self, pizzas):
        self.pizzas = pizzas
    def establecerEstadoOrden(self, est):
        self.estadoOrden = est
        
    # Consultas
    def obtenerNroOrden(self):
        return self.nroOrden
    def obtenerPizzas(self):
        return self.pizzas
    def obtenerEstadoOrden(self):
        return self.estadoOrden
    def calcularTotal(self):
        total = 0
        for pizza in self.pizzas:
            total += pizza.obtenerPrecio()
        return total