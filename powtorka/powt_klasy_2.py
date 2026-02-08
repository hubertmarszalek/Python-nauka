class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price



class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        if isinstance(product, Product):
            self.products.append(product)

    def showProducts(self):
        for product in self.products:
            print(product.name, product.price)

milk = Product("Mleko", 4.5)
bread = Product("Chleb", 3)

cart = ShoppingCart()
cart.add_product(milk)
cart.add_product(bread)

cart.showProducts()

