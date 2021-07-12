x=int(input("enter the number of rows "))
space=1
for i in range(x,0,-1):
    print(" "*space,end="")
    space+=1
    for j in range(x):
        if j<i:
            print("*",end=" ")
    print()
