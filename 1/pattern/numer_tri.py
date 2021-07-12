def tri(n):
    for i in range(n):
        k = 1
        for j in range(0,i+1):
            print(k,end=" ")
            k+=1
        print()

tri(5)