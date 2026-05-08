class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        print(3.14 * self.r * self.r)

c = Circle(7)
c.area()
