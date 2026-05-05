class student:
    def __init__(self,name,roll_number,Marks,grade):
        self.name=name
        self.roll_number=roll_number
        self.Marks=Marks
        self.grade=grade

         

    def display_result(self):
        print(f"Name: {self.name}\n Roll no:{self.roll_number}\n Marks:{self.Marks} \n Grade:{self.grade}")        
            
s=student("Yamuna",101,99,"A")
s.display_result()

