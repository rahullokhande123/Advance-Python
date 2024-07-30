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

# 2) ================ Instance V. Declaration through Object ==============
class Student:
    
    def display(self):
        print("Name =",self.n1)
        print("Age =",self.n2)
obj=Student()
obj.n1="Rahul"
obj.n2=24
obj.display()

# 3) =========== Instance V. Declaration through Instance Method ===========
#============ Instance Method Me Instance Variable Ko Decliare Krna ==========

class Student:
    
    def display(self,name,age):
         self.n1=name
         self.n2=age
    def show(self):
         print("Name =",self.n1)
         print("Age =",self.n2)
obj=Student()
obj.display("Neeraj",37)
obj.show()
print(obj.n1,obj.n2)

