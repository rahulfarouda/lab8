l=[]
a=int(input("enter the no. of elements: "))
for i in range(a):
    l.append(int(input("enter the no.")))
print("list is: ",l)
l2=[]
for j in range(a):
    s=min(l)
    l2.append(s)
    l.remove(s)
print(l2)