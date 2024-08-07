# ===================== Single Inheritance =======================

class P:
    city="Bhopal"
    def display(self):
        print("This is from Display")
class C(P):
    def show(self):
        print("Show Section")
        print("Parent City=",P.city)
obj=C()
obj.show()
print(obj.city,obj.display())

# ===================== Multilevel Inheritance =======================

class P:
    city="Bhopal"
    def display(self):
        print("This is from Display")
class C(P):
    def show(self):
        print("Show Section")
        print("Parent City=",P.city)
class C1(C):
    city1=P.city
    def show1(self):
        self.display()
        self.show()
obj=C1()
print(obj.city1)
obj.show1()
obj.show()
obj.display()
print(obj.city)

# ===================== Multiple Inheritance =======================

class P:
    city="Bhopal"
    def display(self):
        print("This is from Display P")
class C:      
        
    def display(self):
        print("This is from Display C")
class C1(P,C):
    city1=P.city
    def show1(self):
        self.display()
        
obj=C1()
print(obj.city1)
obj.display()
print(obj.city)
obj.show1()