# 1) ============ Instance V. Declaration through Constructor ==============
class Student:
    def __init__(self,name,age):
        self.n1=name
        self.n2=age
    def display(self):
        print("Name =",self.n1)
        print("Age =",self.n2)
obj=Student("Rahul",24)
obj.display()
obj1=Student("Arun",24)
obj1.display()

# ============= Instance V. Declaration Out Side The Class =================

class Student:
    def __init__(self,name,age):
        self.n1=name
        self.n2=age
    def display(self):
        print("Name =",self.n1)
        print("Age =",self.n2)
obj=Student("Rahul",24)
obj.display()
# obj1=Student("Arun",24)
# obj1.display()
print(obj.n1)
print(obj.n2)



