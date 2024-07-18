# reduce import krne ke 2 tarike h:-
# (1) import functools :- print way: print(functools.reduce(max_digit,my_list))
# (2) from functools import reduce : print(reduce(max_digit,my_list))

# esme hm to argument pass krte h

#============= Max Number ==============
# from functools import reduce
# my_list=[10,20,30,50,40,60,80]
# def high_digit(x,y):
#     if x>y:
#         return x
#     else:
#         return y
# print(reduce(high_digit,my_list))

# #============= Min Number ===============

# my_list=[10,20,30,50,40,60,80]
# def high_digit(x,y):
#     if x<y:
#         return x
#     else:
#         return y
# print(reduce(high_digit,my_list))

# # ============= Sum Of All Numbres ==========

# from functools import reduce
# my_list=[10,20,30,50,40,60,80]
# def high_digit(x,y):
#         return x+y
   
# print(reduce(high_digit,my_list))

# ============= Lambda Function ==============

# n=int(input("enter no."))
# x=lambda n: True if n%2==0 else False
# print(x(n))

# ================================================
# from functools import reduce
# my_list=[20,30,40,50,60]
# def small(x,y):
#     if x<y:
#         return x
#     else:
#         return y
# print(reduce(small,my_list))




