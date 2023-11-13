p=1
sum=0
l=[]
a=int(input("enter the no. of elements: "))
for i in range(a):
    l.append(int(input("enter the no.")))
print(l)
max=l[0]
#sum
for k in l:
    sum=sum + k
print("sum: ",sum)
#product
for j in l:
    p=p*j
print("product is: ",p)
#greatest
for d in l:
    if max<d:
        max=d
print("the greatest of all: ",max)