class Number:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return self.x + other.x

n1 = Number(5)
n2 = Number(3)
print(n1 + n2)
