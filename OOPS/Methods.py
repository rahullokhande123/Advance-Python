# ======================= Instainse Method =====================

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

# self ko bhi hm medify kr sakte h pr krte nhi kyo ki python ne self hi refer kiya h
# Instance Methode Ko Bhi jab kisi method me call krte hai to self ki helf se hi hota h
# Or Method Ko Class Ke Baher Call krne ke liye obj.ka use krke 

# ======================== Class Method ==========================

class Book:
    price=1000
    def datails(self,author_name,author_city):
        print("Name=",author_name)
        print("City=",author_city)
        print("price=",Book.price)
    @classmethod
    def update_price(cls,updated_price):
        cls.price=updated_price
obj=Book()
obj.datails("Neeraj","BHopal")
obj.update_price(2000) 
obj.datails("Rahul","Bhopal")

# Class Method Ka Use Hm Class Variable Ko Modifiy/ Update Krne Ke Liye Krte H
# cls ko modify bhi kr sakte h pr krte nhi h kyoki python ne cls hi refer kiya h

# ============================= Static Method ===============================

class Student:
    city="Bhopal"
    def display(self):
        print("Hello")
    @staticmethod
    def show():
        print("Thanks Lot")
obj=Student()
obj.display()
obj.show()   # Yeisi Method Jiska Class Methods Or Variable Se Koi Mtlb Nhi Ho
          #Esme Hm Class Methods Ya Variables Ko Access Nhi Kr Sakte H
