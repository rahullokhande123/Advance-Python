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

# ============= Instance V. Declaration-Access Out Side The Class =================

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

# 4) =========== Accesess Instance Variable ===========
              # a )==== Within The Class(through self) ====
          # b )==== Out Side of the class(through obj) ====



# ====================== Static/Class Variable =====================

class Student:
    school='LBHSS'     # Static Decleared Outside Of Method
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll           # Static Decleared Inside Of Construct
        Student.center_code=101
    def display(self):
        Student.gread='10th'     # Static Decleared Inside Of Method
        print("Name",self.name)
        print("Roll",self.roll)
        print("School",Student.school)
        print("Center",Student.center_code)
        print("Gread",Student.gread)
obj=Student('Rahul',1222)
obj.display()
print("School",Student.school)     # Baher Es Tarah Se Access Kr Sakte H


# ==== Static Class Ko Outside Of Class Decleare Krna Or Access Krna =====

class Student:
    school='LBHSS'
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        Student.center_code=101
    def display(self):
        Student.gread='10th'
        print("Name",self.name)
        print("Roll",self.roll)
        print("School",Student.school)
        print("Center",Student.center_code)
        print("Gread",Student.gread)
        print("City",Student.city)
obj=Student('Rahul',1222)

print("School",Student.school)
Student.city="Bhopal"
obj.display()


# ===================== Local Variables ======================

class Student:
    def display(self,name,age):
        x=10
        print("Name =",name)
        print("Age =",age)
        print("Value Of X=",x)
obj=Student();
obj.display("Rahul",24)
# print(x)    
           # Local Variable Ko Hm Scope Ke Baher Access Nhi Kr Sakte