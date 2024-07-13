#=============== Find Vovels ================

my_str=input("enter your Name : ")
def vovel(n):
    my_vovel=['a','e','i','o','u','A','E','I','O','U']
    if n in my_vovel:
        return True
print(list(filter(vovel,my_str)))

#================= Find Consonant ============

my_str=input("enter your Name : ")
def vovel(n):
    my_vovel=['a','e','i','o','u','A','E','I','O','U']
    if n not in my_vovel:
        return True
print(list(filter(vovel,my_str)))