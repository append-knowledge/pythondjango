x=int(input("enter the number of rows "))
y=int(input("enter the number of coloumn "))
for i in range(x):
    print("*",end=" ")
    for j in range(y-1):
        print("*",end=" ")
    print()