from MaestroPizzero import MaestroPizzero
from Mozo import Mozo
# from Pizza import Pizza

class TesterPizzeria:
    def main(self):
        self.maestro_pizzero = MaestroPizzero("Hugo")
        self.mozo1 = Mozo("Juan")
        self.mozo2 = Mozo("Ignacio")
        
        self.maestro_pizzero.obtenerNombre()
        self.maestro_pizzero.tomarPedido("Hawaiana")
        self.maestro_pizzero.tomarPedido("Fugazzeta")
        self.maestro_pizzero.tomarPedido("Pepperoni")
        self.maestro_pizzero.tomarPedido("Cuatro quesos")
        self.maestro_pizzero.cocinar()
        print()
        primera_tanda = self.maestro_pizzero.entregar()
        self.mozo1.tomarPizzas(primera_tanda)
        self.mozo1.servirPizzas()
        print()

        segunda_tanda = self.maestro_pizzero.entregar()
        self.mozo2.tomarPizzas(segunda_tanda)
        self.mozo2.servirPizzas()


if __name__ == "__main__":
    testerPizzeria = TesterPizzeria()
    testerPizzeria.main()

