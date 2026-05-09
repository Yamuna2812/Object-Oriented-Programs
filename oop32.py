class Animal:
    def sound(self):
        print("Animal")

class Dog(Animal):
    def sound(self):
        print("Bark")

obj = Dog()
obj.sound()
