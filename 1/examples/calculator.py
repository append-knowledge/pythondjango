def add(num1,num2):
    print(num1+num2)
def sub(num1,num2):
    print(num1-num2)
def mul(num1,num2):
    print(num1*num2)
def div(num1,num2):
    print(num1/num2)

print("SELECT THE OPERATION\n1.add\n2.subtraction\n3.multiplication\n4.division")
n=int(input("enter the number "))
if n<=4:
    num1 = float(input("enter num1 "))
    num2 = float(input("enter num2 "))
    if n == 1:
        add(num1, num2)
    elif n == 2:
        sub(num1, num2)
    elif n == 3:
        mul(num1, num2)
    elif n == 4:
        div(num1, num2)

else:
    print("please check the number you have dialed")


