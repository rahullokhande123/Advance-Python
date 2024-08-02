# ================ Instainse Method =====================

class Student:
    city="Bhopal"
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def display(self):
        print("Hello ")
    def show(self):
        print(Student.city)
        print("Name=",self.name)
        print("Roll=",self.roll)
        self.display()
obj=Student("Rahul",101)
obj.show()
obj.display()


