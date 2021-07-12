x=int(input("enter the number you want to check "))
if x>1:
    for i in range(2,x):
        if x%i==0:
            print("the number is not prime")
            break
        else:
            print("entered number is prime")
else:
    print("check the number you have dialed")