class Book:
    def __init__(self, title):
        self.title = title

    def show(self):
        print(self.title)

b = Book("Python")
b.show()