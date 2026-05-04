class students:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        

    def display_info(self):
        print(f"{self.name}:{self.marks}")  

print("Students marks:")
s1=students("Yamuna",99)
s1.display_info()        
s2=students("Ramya",98)
s2.display_info()
s3=students("Divya",99)
s3.display_info()