lst=[1,2,3,54,88,5,997,225,335,44]
element=int(input("the the search keyword  "))
for i in lst:
    if i==element:
        print(element,"found")
        break
else:
    print(element,"not found")