x=int(input("enter the rows "))
space=x
for i in range(x):
    print(" "*space,end=" ")
    space-=1
    for j in range(i+1):
        if j<=i:
            print("*",end=" ")
    print()