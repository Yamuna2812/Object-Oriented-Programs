class Cat:
    def sound(self):
        print("Meow")

class Dog:
    def sound(self):
        print("Bark")

for i in [Cat(), Dog()]:
    i.sound()
