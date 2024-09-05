# Importar la clase MaestroPizzero desde el archivo maestro_pizzero.py
from maestro_pizzero import MaestroPizzero

# Crear una instancia de MaestroPizzero
maestro = MaestroPizzero("Don Pipo")

# Establecer nombre (opcional, ya se establece en el constructor)
maestro.establecerNombre("Don Pipo")

# Ver el nombre del maestro pizzero
print("Nombre del maestro pizzero:", maestro.obtenerNombre())  # Output: Don Pipo

# Tomar varios pedidos de pizzas
maestro.tomarPedido("Margarita")
maestro.tomarPedido("Pepperoni")
maestro.tomarPedido("Cuatro Quesos")

# Verificar las pizzas por cocinar
print("Pizzas por cocinar:", [pizza.variedad for pizza in maestro.obtenerPizzasPorCocinar()])

# Cocinar las pizzas
maestro.cocinar()

# Verificar las pizzas por cocinar (debería estar vacía)
print("Pizzas por cocinar después de cocinar:", [pizza.variedad for pizza in maestro.obtenerPizzasPorCocinar()])

# Verificar las pizzas por entregar (debería contener las cocinadas)
print("Pizzas por entregar:", [pizza.variedad for pizza in maestro.obtenerPizzasPorEntregar()])

# Entregar hasta 2 pizzas
pizzas_entregadas = maestro.entregar()
print("Pizzas entregadas:", [pizza.variedad for pizza in pizzas_entregadas])

# Verificar las pizzas restantes por entregar
print("Pizzas restantes por entregar:", [pizza.variedad for pizza in maestro.obtenerPizzasPorEntregar()])

# Intentar entregar más pizzas (solo una debería quedar)
pizzas_entregadas = maestro.entregar()
print("Pizzas entregadas:", [pizza.variedad for pizza in pizzas_entregadas])

# Verificar que ya no quedan pizzas por entregar
print("Pizzas por entregar después de entregar todo:", maestro.obtenerPizzasPorEntregar())

