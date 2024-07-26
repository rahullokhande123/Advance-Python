
# Normal Function =====================
def gen():
    i=1
    my_list=[]
    while i<=10:
        my_list.append(i)
        i=i+1
    return my_list
var1=gen()
print(var1)

#==================================== 
def gen():
    i=1
    my_list=[]
    while i<=10:
        my_list.append(i)
        i=i+1
    yield my_list
var1=gen()
# next(var1)
print(next(var1))

# ===================================

def gen():
    i=1
    my_list=[]
    while i<=10:
        my_list.append(i)
        i=i+1
    yield my_list
var1=gen()
# next(var1)
# print(next(var1))
for i in var1:
    print(i)

# ================== Generator Function =================

def gen_no(x,y):
    while x<=y:
        yield x
        x=x+1
var2=gen_no(1,10)
print("Hello")
print(next(var2))
print("Hello2")
print(next(var2))
print("Hello3")
for i in var2:
    i=i+10
    print(i)