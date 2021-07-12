x=int(input("enter the number of rows "))
s=x
for i in range(x):
    for e in range(s):
        print(end=" ")
    s-=1
    for j in range(i+1):
        if j<=i+1:
            print("*",end=" ")
    print()