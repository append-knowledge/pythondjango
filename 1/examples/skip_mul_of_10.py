x=int(input("enter the range "))
for i in range(x+1):
    if (i%10==0):
        continue
    else:
        print(i)