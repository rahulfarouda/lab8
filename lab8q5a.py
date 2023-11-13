l=[]
s=0
a=int(input("enter the no. of elements: "))
for i in range(a):
    l.append(str(input("enter the string: ")))
print(l)
b=str(input("enter the string to be searched: "))
for j in l:
    if b==j:
        s=s+1
print(f"the string is repeated {s} times")