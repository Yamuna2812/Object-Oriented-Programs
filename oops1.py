class car:
    def __init__(self,brand,model):
        self.brand= brand
        self.model= model
    def display_info(self):
        print(f"car brand:{self.brand},car model:{self.model}")



my_car =car("toyota","Corolla")
my_car.display_info() 
my_car=car("BMW","DXU")           
my_car.display_info()