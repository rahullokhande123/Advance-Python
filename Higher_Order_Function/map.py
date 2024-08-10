# HIGHER ORDER FUNCTION:-

# FIND POWER OF ANY COLLECTION
# my_list=[1,2,3,4,5]
# def squar(n):
#     return n**2
# new_list=map(squar,my_list)
# print(list(new_list))
# =========Multiple===========
# my_list=(1,2,3,4,5,6,7,8,9,10)
# def cal(n):
#     return n*2
# new_list=map(cal,my_list)
# print(list(new_list))

# ==========  ===========

# my_add=(1,2,3,4,5,6,7,8,9,10)
# def add(n):
#     return n+10-n+2
# add_store=map(add,my_add)
# print(list(add_store))


# ============================================

# # Addition of two list on the bases of indexing.
# my_list1=[1,2,3,4,5]
# my_list2=[5,4,3,2,1]
# def add(x,y):
#     return x+y
# new_list=tuple(map(add,my_list1,my_list2))
# print(new_list)

# ======================

my_list1=(1,2,3,4,5)
my_list2=(5,4,3,2,1)
def multi(x,y):
    return x*y
store=map(multi,my_list1,my_list2)
print(list(store))
# # SECONDE WAY THIS:-
# # WAP TO FINDE ANY COLLECTION
# def add(x,y):
#     return x+y
# new_list=tuple(map(add,[1,2,3,4,5],[5,4,3,2,1]))
# print(new_list)


