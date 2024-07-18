f=open('new.txt','x')
f=open('new1.txt','w')
f=open('new2.txt','a')
f=open('new4.txt','x')
# print(f.read())
print(f.readable())
print(f.writable())
print(f.closed)
f.close()
print(f.closed)
print(f.writable())
# ===================================================




