from product import Product
from product_manager import ProductManager

# Kreiramo ProductManager instancu
manager = ProductManager()

# Dodajemo nekoliko proizvoda
product1 = Product("Laptop", 80000, 5)
product2 = Product("Miš", 1500, 20)
product3 = Product("Monitor", 25000, 8)

manager.add_product(product1)
manager.add_product(product2)
manager.add_product(product3)

# Prikaz svih proizvoda
manager.display_all_products()

# Prikaz ukupne vrednosti
manager.calculate_total_value()
