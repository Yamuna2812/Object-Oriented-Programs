class mobile:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price

    def display_info(self):
        print(f"I am using mobile brand is {self.brand},and it's price is {self.price}")


m1=mobile("Vivo",22000)
m1.display_info()    
m2=mobile("oppo",34999)
m2.display_info()        