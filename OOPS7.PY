class student:
    def __init__(self,name,id,marks):
        self.name=name
        self.id=id
        self.marks=marks

    def display_info(self):
        print(f"Student Name : {self.name}\n Student id no: {self.id}\n Student marks:{self.marks}")    



s=student("Yamuna",102,99)
s.display_info()