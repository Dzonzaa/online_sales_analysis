class Cart:
    def __init__(self):
        self.cart_items = []  # Lista proizvoda u korpi

    def add_product(self, product):
        self.cart_items.append(product)
        print(f"Proizvod '{product.name}' dodat u korpu.")

    def calculate_total(self):
        total = sum(item.price * item.quantity for item in self.cart_items)
        print(f"Ukupna vrednost korpe: {total} RSD")
        return total

    def display_cart(self):
        print("Sadržaj korpe:")
        for item in self.cart_items:
            item.display_info()
