from MaestroPizzero import MaestroPizzero
from Mozo import Mozo
from Orden import Orden
from PizzaVariedad import PizzaVariedad
from Pizza import Pizza

def prints(pizza1, pizza2, pizza3, pizza4, orden, numOrden):
    print('')
    print(f'Estado de la orden {numOrden}: ')
    if orden.obtenerEstadoOrden() == 1:
        print('Iniciando la orden')
    elif orden.obtenerEstadoOrden() == 2:
        print('Para entregar')
    elif orden.obtenerEstadoOrden() == 3:
        print('Entregada')
    print(f'Estado de la pizza 1: ')
    if pizza1.obtenerEstado() == 1:
        print('Cocinando...')
    elif pizza1.obtenerEstado() == 2:
        print('Cocinada, lista para entregar')
    elif pizza1.obtenerEstado() == 3:
        print('Entregada')
    print(f'Estado de la pizza 2: ')
    if pizza2.obtenerEstado() == 1:
        print('Cocinando...')
    elif pizza2.obtenerEstado() == 2:
        print('Cocinada, lista para entregar')
    elif pizza2.obtenerEstado() == 3:
        print('Entregada')
    print(f'Estado de la pizza 3: ')
    if pizza3.obtenerEstado() == 1:
        print('Cocinando...')
    elif pizza3.obtenerEstado() == 2:
        print('Cocinada, lista para entregar')
    elif pizza3.obtenerEstado() == 3:
        print('Entregada')
    if pizza4:
        print(f'Estado de la pizza 4: ')
        if pizza4.obtenerEstado() == 1:
            print('Cocinando...')
        elif pizza4.obtenerEstado() == 2:
            print('Cocinada, lista para entregar')
        elif pizza4.obtenerEstado() == 3:
            print('Entregada')


class TesterPizzeria:
    def main(self):
        MaestroPizzero1 = MaestroPizzero("MaestroPizzero1")
        Mozo1 = Mozo("Franco")
        Mozo2 = Mozo("Juan")
        
        # ORDEN 1
        orden1 = Orden(1)
        pizza1 = Pizza(PizzaVariedad("Panceta y verdeo", 200))
        pizza2 = Pizza(PizzaVariedad("Palmitos", 300))
        pizza3 = Pizza(PizzaVariedad("Rucula", 400))
        prints(pizza1, pizza2, pizza3, None, orden1, 1)
        orden1.establecerPizzas([pizza1, pizza2, pizza3])
        MaestroPizzero1.tomarPedido(orden1)
        print('')
        
        # Orden 2
        orden2 = Orden(2)
        orden2pizza1 = Pizza(PizzaVariedad("Fugazzeta", 1000))
        orden2pizza2 = Pizza(PizzaVariedad("Calabresa", 500))
        orden2pizza3 = Pizza(PizzaVariedad("Especial", 800))
        orden2pizza4 = Pizza(PizzaVariedad("Comun", 100))
        prints(orden2pizza1, orden2pizza2, orden2pizza3, orden2pizza4, orden2, 2)
        orden2.establecerPizzas([orden2pizza1, orden2pizza2, orden2pizza3, orden2pizza4])
        MaestroPizzero1.tomarPedido(orden2)
        print('')
        
        # COMANDOS MAESTROPIZZERO ORDEN 1
        MaestroPizzero1.cocinar()
        prints(pizza1, pizza2, pizza3, None, orden1, 1)
        print('')
        Mozo2.tomarPizzas(MaestroPizzero1.entregar(orden1))
        Mozo2.servirPizzas()
        prints(pizza1, pizza2, pizza3, None, orden1, 1)
        Mozo1.tomarPizzas(MaestroPizzero1.entregar(orden1))
        print('')
        Mozo1.servirPizzas()
        prints(pizza1, pizza2, pizza3, None, orden1, 1)
        print('')
        totalOrden1 = orden1.calcularTotal()
        print(f'Costo total de la orden 1: {totalOrden1}')
        
        print('')
        print('--------------------------------------------------')
        
        # COMANDOS MAESTROPIZZERO ORDEN 2
        prints(orden2pizza1, orden2pizza2, orden2pizza3, orden2pizza4, orden2, 2)
        Mozo2.tomarPizzas(MaestroPizzero1.entregar(orden2))
        print('')
        Mozo2.servirPizzas()
        prints(orden2pizza1, orden2pizza2, orden2pizza3, orden2pizza4, orden2, 2)
        Mozo1.tomarPizzas(MaestroPizzero1.entregar(orden2))
        print('')
        Mozo1.servirPizzas()
        prints(orden2pizza1, orden2pizza2, orden2pizza3, orden2pizza4, orden2, 2)
        totalOrden2 = orden2.calcularTotal()
        
        print('')
        print(f'Costo total de la orden 2: {totalOrden2}')
        print('')
        print(f'Costo total de las dos ordenes: {totalOrden1 + totalOrden2}')
        print('')
        

if __name__ == "__main__":
    testerPizzeria = TesterPizzeria()
    testerPizzeria.main()

