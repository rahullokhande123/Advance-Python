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

