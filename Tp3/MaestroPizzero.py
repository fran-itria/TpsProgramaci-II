from Pizza import Pizza
from Orden import Orden

class MaestroPizzero:
    def __init__(self, nom):
        self.nombre = nom
        self.ordenes = [] 

    def establecerNombre(self, nom):
        self.nombre = nom

    def tomarPedido(self, orden):
        if not isinstance(orden, Orden):
            raise ValueError("El pedido debe ser un objeto de la clase Orden")
        if orden.obtenerEstadoOrden() == Orden.ESTADO_INICIAL:
            self.ordenes.append(orden)
        else:
            raise ValueError("La orden no está en el estado inicial")

    def cocinar(self):
        for orden in self.ordenes:
            if orden.obtenerEstadoOrden() == Orden.ESTADO_INICIAL:
                orden.establecerEstadoOrden(Orden.ESTADO_PARA_ENTREGAR)
                for pizza in orden.obtenerPizzas():
                    pizza.establecerEstado(Pizza.ESTADO_COCINADA)
                print(f"Orden {orden.obtenerNroOrden()} cocinada y lista para entregar")

    def entregar(self, orden):
        if orden.obtenerEstadoOrden() != Orden.ESTADO_PARA_ENTREGAR:
            raise ValueError("La orden no está lista para ser entregada")

        pizzas_a_entregar = []
        for pizza in orden.obtenerPizzas():
                if pizza.obtenerEstado() == Pizza.ESTADO_COCINADA:
                    pizza.establecerEstado(Pizza.ESTADO_ENTREGADA)
                    pizzas_a_entregar.append(pizza)
                if len(pizzas_a_entregar) == 2:
                    break
        
        if all(pizza.obtenerEstado() == Pizza.ESTADO_ENTREGADA for pizza in orden.obtenerPizzas()):
            orden.establecerEstadoOrden(Orden.ESTADO_ENTREGADA)

        return pizzas_a_entregar

    def obtenerNombre(self):
        return self.nombre

    def obtenerOrdenes(self):
        return self.ordenes
