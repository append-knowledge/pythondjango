def fact(x):
    if x==1:
        return 1
    else:
        return x*fact(x-1)

x=int(input("enter the number "))
print("the factorial of ",x,"is",fact(x))
fact(3)