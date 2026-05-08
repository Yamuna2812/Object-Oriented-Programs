class Product:
    def __init__(self, price):
        self.price = price

    def display(self):
        print(self.price)

p = Product(250)
p.display()
