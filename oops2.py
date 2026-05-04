class dog:
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed

    def bark(self):
        print(f"{self.name} barking.")
        print(f"The breed of the dog is {self.breed}")


dog1=dog("naayi","bulldog")           


dog1.bark()