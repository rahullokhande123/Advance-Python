# Normal ========================
class Student:
    x=10;
    y=20;
    def display():
        print("This is Display")
obj=Student
obj.display()
print(obj.x)


# ======= Constructor =============

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

# ============= Self And Current Class Objects Same Address ===============
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
