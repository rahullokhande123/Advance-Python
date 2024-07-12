# HIGHER ORDER FUNCTION:-

# FIND POWER OF ANY COLLECTION
my_list=[1,2,3,4,5]
def squar(n):
    return n**2
new_list=tuple(map(squar,my_list))
print(new_list)


# ============================================

# Addition of two list on the bases of indexing.
my_list1=[1,2,3,4,5]
my_list2=[5,4,3,2,1]
def add(x,y):
    return x+y
new_list=tuple(map(add,my_list1,my_list2))
print(new_list)

# SECONDE WAY THIS:-
# WAP TO FINDE ANY COLLECTION
def add(x,y):
    return x+y
new_list=tuple(map(add,[1,2,3,4,5],[5,4,3,2,1]))
print(new_list)


