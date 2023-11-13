l=[]
a=int(input("enter the no. of elements: "))
for i in range(a):
    l.append(int(input("enter the no.")))
print(l)
l2=[]
for b in l:
    if b>0:
        l2.append(b**2)
    else:
        l2.append(0)
print("the new list is: ",l2)