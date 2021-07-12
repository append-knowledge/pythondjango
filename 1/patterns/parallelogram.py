x=int(input("enter the number of rows "))
k=1
for i in range(x):
    print(" "*k,end="")
    k+=1
    for j in range(x):
        print("*",end=" ")
    print()