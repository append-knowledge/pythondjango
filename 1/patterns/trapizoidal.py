x=int(input("enter the number of rows "))
k=x
y=5
for i in range(x):
    print(" "*k,end="")
    k-=1
    for j in range(y):
        print("*",end=" ")
    y+=1
    print()