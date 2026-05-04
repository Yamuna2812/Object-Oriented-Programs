class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def greet(self):
        print(f"Hi my name is {self.name}! I am {self.age}yeara old") 



person1 = person ("YAMUNA", 18)
person2=person("Banchi",30)

person1.greet()  
person2.greet()    