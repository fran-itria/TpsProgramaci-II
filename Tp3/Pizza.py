from PizzaVariedad import PizzaVariedad

class Pizza:
    ESTADO_POR_COCINAR = 1
    ESTADO_COCINADA = 2
    ESTADO_ENTREGADA = 3


    def __init__(self, var):
        if not isinstance(var, PizzaVariedad):
            raise ValueError("La variedad debe ser un objeto de tipo PizzaVariedad")
        self.variedad = var
        self.estado = Pizza.ESTADO_POR_COCINAR 


    def establecerVariedad(self, var):
        if not isinstance(var, PizzaVariedad):
            raise ValueError("La variedad debe ser un objeto de tipo PizzaVariedad")
        self.variedad = var

    def establecerEstado(self, est):
        if est not in [Pizza.ESTADO_POR_COCINAR, Pizza.ESTADO_COCINADA, Pizza.ESTADO_ENTREGADA]:
            raise ValueError("Estado no válido")
        if self.estado == Pizza.ESTADO_POR_COCINAR and est == Pizza.ESTADO_COCINADA:
            self.estado = est
        elif self.estado == Pizza.ESTADO_COCINADA and est == Pizza.ESTADO_ENTREGADA:
            self.estado = est
        else:
            raise ValueError("Transición de estado no permitida")


    def obtenerVariedad(self):
        return self.variedad

    def obtenerEstado(self):
        return self.estado
