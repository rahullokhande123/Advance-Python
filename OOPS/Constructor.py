# Normal ========================
class Student:
    x=10;
    y=20;
    def display(self,x,y):
        print("This is Display")
        print(x)
        print(y)
        print(obj.y)
obj=Student()
obj.display(30,40)
print(obj.x)


# ======================= Constructor =============

class Student:
    x=10;
    y=20;
    def __init__(self):
        print("This is Construnctor")
    @staticmethod
    def display():
        print("This is Display")
obj=Student()

print(obj.x)
obj.display()    # () lagana must be recurged

# =================== Self And Current Class Objects Same Address ===============
class Student:
    x=10;
    y=20;
    def __init__(self):
        print("This is Construnctor")
        print(id(self))
    @staticmethod
    def display():
        print("This is Display")
obj=Student()

print(obj.x)
print(id(obj))
obj.display()
obj2=Student()
print(id(obj2))

# ======================== Multipale Constructor =================

class Student:
    x=10;
    y=20;
    def __init__(self,x):
        print("This is Construnctor")
        print(id(self))
    def __init__(self,x,y):
        print("This is Construnctor")
        print(id(self))
    def __init__(self,x,y,z):
        print("This is Construnctor")
        print(id(self))
obj=Student(10,20,30)

# We can create multipale Constructor But we can'nt call all.
# By default Evary Time Call Last Constructor In Multiple.
