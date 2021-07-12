x=int(input(" enter the number of rows "))
k=x
for i in range(x):
    print(" "*k,end="")
    k-=1
    for j in range(x):
        print("*",end=" ")
    print()