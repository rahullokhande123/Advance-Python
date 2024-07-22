# f=open('new.txt','x')
# f=open('new1.txt','w')
# f=open('new2.txt','a')
# f=open('new4.txt','x')
# # print(f.read())
# print(f.readable())
# print(f.writable())
# print(f.closed)
# f.close()
# print(f.closed)
# print(f.writable())
# ===================================================

# f=open('n2.txt','x')
# print(f.name)
# print(f.mode)
# print(f.encoding)
# print(f.readable())
# print(f.writable())
# print(f.closed)
# f.close()
# print(f.closed)
# ===================================================

# f=open('n5.txt','x+')
# print(f.name)
# print(f.mode)
# print(f.encoding)
# print(f.readable())
# print(f.writable())
# print(f.closed)
# f.close()
# print(f.closed)
# ===================================================

# f=open('n6.txt','w')
# f.write("Hello I am Rahul Lokhade\nI am Fullstack Developer\n")
# data=('This is C++ Timing 10:30 to 11:30')
# f.writelines(data)
# f.close()
# ===================================================

# f=open('even-odd.txt','w')
# # f.write("Hello I am Rahul Lokhade\nI am Fullstack Developer\n")
# data=('x=10 \n if x%2==0: \n print("Even No.")')
# f.writelines(data)
# f.close()

# =================================================

f=open('n6.txt','rb')
print(f.tell())
print(f.read(6))
print(f.tell())
# print(f.read(5))

