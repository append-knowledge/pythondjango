

def prime(1,50):
sum=0
for i in range(1,50):
    for j in range(2,i):
        if i%j==0:
           break
    else:
        print(i)
        sum=sum+i
return ('sum =',sum)
