from product import Product
from product_manager import ProductManager
from cart import Cart  # Importuj klasu Cart

# Kreiraj ProductManager instancu
manager = ProductManager()

# Dodaj proizvode
product1 = Product("Laptop", 80000, 5)
product2 = Product("Miš", 1500, 20)
product3 = Product("Monitor", 25000, 8)

manager.add_product(product1)
manager.add_product(product2)
manager.add_product(product3)

# Kreiraj instancu klase Cart
cart = Cart()

# Dodaj proizvode u korpu
cart.add_product(product1)
cart.add_product(product2)
cart.add_product(product3)

# Ispis sadržaja korpe
cart.display_cart()

# Računaj ukupnu vrednost korpe
cart.calculate_total()
