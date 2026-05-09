class Teacher:
    def teach(self):
        print("Teaching")

class Student(Teacher):
    pass

s = Student()
s.teach()
