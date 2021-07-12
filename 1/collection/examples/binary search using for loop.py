x=[55,68,75,97,52,35,4568,235,452,454,100,-55,-4,-25]
x.sort()
print(x)
element=int(input("enter the digit "))
low=0
upper=len(x)-1
flag=0
for i in range(x[low],x[upper]):
    mid=upper+low//2
    if element < x[mid]:
        upper=mid-1
    elif element > x[mid]:
        low=mid+1
    elif element==x[mid]:
        flag=1

if flag==1:
    print("element found")
else:
    print("Element not found")


