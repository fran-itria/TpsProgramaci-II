from MaestroPizzero import MaestroPizzero
from Mozo import Mozo
# from Pizza import Pizza

class TesterPizzeria:
    def __init__(self):
        self.maestro_pizzero = MaestroPizzero("Hugo")
        self.mozo1 = Mozo("Juan")
        self.mozo2 = Mozo("Ignacio")


if __name__ == "__main__":
    testerPizzeria = TesterPizzeria()
    testerPizzeria.maestro_pizzero.obtenerNombre()
    testerPizzeria.maestro_pizzero.tomarPedido("Hawaiana")
    testerPizzeria.maestro_pizzero.tomarPedido("Fugazzeta")
    testerPizzeria.maestro_pizzero.tomarPedido("Pepperoni")
    testerPizzeria.maestro_pizzero.tomarPedido("Cuatro quesos")
    testerPizzeria.maestro_pizzero.cocinar()
    print()
    primera_tanda = testerPizzeria.maestro_pizzero.entregar()
    testerPizzeria.mozo1.tomarPizzas(primera_tanda)
    testerPizzeria.mozo1.servirPizzas()
    print()

    segunda_tanda = testerPizzeria.maestro_pizzero.entregar()
    testerPizzeria.mozo2.tomarPizzas(segunda_tanda)
    testerPizzeria.mozo2.servirPizzas()

