from modules import add,x,y
print("x:",x,"y:",y)
# x=20
# y=20
p=add(x,y)
print(p)

# from modules import sub,x,y
# print("x:",x,"y:",y)
# # x=20
# # y=20
# p=sub(x,y)
# print(p)

# =================
from modules import sub as s,x,y  # -> Aliyas Long Name Ko Sort Krne ke liye,
                                       #  Usi ka nick name hota h, 
                                       # ab hm pahle vala name use nhi kr sakte. 
                                       # nick name hi use krenge 
print("x:",x,"y:",y)
# x=20
# y=20
p=s(x,y)
print(p)