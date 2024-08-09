# ====================== Protected Accesspacifier =========================

class P1:
    _name="Rahul"
    def display(self):
        print(P1._name)
class P2(P1):                            # Protected ->( _ )
    name=P1._name
    def show(self):
        print("NAME=",P2.name)
obj=P2()
obj.show()
print(obj._name)

# ========================== Private Acces Spacifier =======================

# class P1:                         # Ye Child Class me Access Nhi Krta Hai.
#     _name="Rahul"
#     def display(self):
#         print(P1._name)
# class P2(P1):                     # Private -> ( __ )
#     name=P1._name
#     def show(self):
#         print("NAME=",P2.name)
# obj=P2()
# obj.show()
# print(obj._name)

# ===============================

class P1:
    __name="Rahul"
    def display(self):
        print(P1.__name)
obj=P1()
obj.display()



# =========================== Method Overloding ==========================

class P1:
    def add(*n):
        sum=0
        for i in n:
            sum=sum+i
        return sum
obj=P1
result=obj.add(10,20)
print(result)
obj.add(10,20,30,40,50,60)

# ================= Second Example ===============

class A:
    def add(x=0,y=0):
        return x+y
    def add(x=0,y=0,z=0):
        return x+y+z
obj=A                            # 
x=obj.add(4,5)
print(x)

# =========================== Method Overriding ==========================
# ================= Super() =================

class Parent:
    name="Parent Class"
    def property(self):
        return "I have lot of propertys"
class Child(Parent):
    name="Child Class"
    def property(self):
        return "less propertys"
    def display(self):
        print("Name=",Child.name)
        print("Propertys=",self.property())
        print("========== Using Super Method ==============")
        print("Name=",super().name)
        print("Propertys=",super().property())

obj=Child()
obj.display()

# =============== Example 2 ====================
class A:
    def display(self):
        print("Display A Class")
class B(A):
    def display(self):
        print("Display B Class")
    def show(self):
        super().display()
obj=B()
obj.display()
obj.show()