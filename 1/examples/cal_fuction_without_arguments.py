def add():
    num1=float(input("enter the first number "))
    num2=float(input("enter the second number "))
    print(num1+num2)
def sub():
    num1 = float(input("enter the first number "))
    num2 = float(input("enter the second number "))
    print(num1-num2)
def mul():
    num1 = float(input("enter the first number "))
    num2 = float(input("enter the second number "))
    print(num1*num2)
def div():
    num1 = float(input("enter the first number "))
    num2 = float(input("enter the second number "))
    print(num1/num2)
print("SELECT THE OPERATION")
n=int(input("1.ADDITION\n2.SUBTRACTION\n3.MULTIPLICATION\n4.DIVISION\nENTER THE NUMBER "))
if n<=4:
    if n==1:
        add()
    elif n==2:
        sub()
    elif n==3:
        mul()
    elif n==4:
        div()
else:
    print("check the number you have dialed")