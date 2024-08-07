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

