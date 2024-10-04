class PizzaVariedad:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    # Comandos
    def establecerNombre(self, nombre):
        self.nombre = nombre
    def establecerPrecio(self, precio):
        self.precio = precio
        
    # Consultas
    def obtenerNombre(self):
        return self.nombre
    def obtenerPrecio(self):
        return self.precio