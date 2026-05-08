class Patient:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name)

p = Patient("Anu")
p.show()
