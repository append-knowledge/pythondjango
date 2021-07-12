x=int(input(" enter the limit "))
lst=[]
lst2=[]
for i in range(x):
    i=float(input("enter the digit "))
    lst.append(i)
for j in range(x):
    min=lst[0]
    for e in lst:
        if e<min:
            min=e
    lst2.append(min)
    lst.remove(min)

print(lst2)