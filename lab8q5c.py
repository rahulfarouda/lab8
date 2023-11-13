l=[]
a=int(input("enter the no. of elements: "))
for i in range(a):
    l.append(int(input("enter the no.")))
print(l)
l2=[]
for b in l:
    if b>=10 and b<=20:
        l2.append(b**2)
    else:
        l2.append(b)
print("the new list is: ",l2)