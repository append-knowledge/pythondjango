x=[1,2,3,5,45,6,5,87,565,47,2,-15]
x.sort()
print(x)
element=int(input("enter the digit "))
flag=0
low=0
upper=len(x)-1
while low<=upper:
    mid=upper+low//2
    if element<x[mid]:
        upper=mid-1
    elif element>x[mid]:
        low=mid+1
    elif element==x[mid]:
        flag=1
        break
if flag==1:
    print("element found")
else:
    print("element not found")




