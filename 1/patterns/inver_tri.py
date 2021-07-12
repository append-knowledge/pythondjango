x=int(input("enter the number of rows "))
for i in range(x):
    for j in range(x,0,-1):
        if j>i:
            print("*",end="")
    print()