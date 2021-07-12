k=1
for i in range(0,5):
    for j in range(i+1):
        if j<=i:
            print(k,end=" ")
    print()
k+=1
for a in range(5,0,-1):
    for b in range(0,5):
        if b<a:
            print(k,end=' ')
    print()
k+=1
for c in range(0,5):
    for d in range(c+1):
        if d<=c:
            print(k,end=" ")
    print()
k+=1
for e in range(5,0,-1):
    for f in range(0,5):
        if f<e:
            print(k,end=' ')
    print()