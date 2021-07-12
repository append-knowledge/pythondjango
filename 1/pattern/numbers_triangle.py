x=int(input("enter the row "))
k=1
for i in range(x):
    for j in range(0,i+1):
        print(k,end=" ")
        k+=1
    print()