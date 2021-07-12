def add(num1,num2):
    print(num1+num2)
def sub(num1,num2):
    print(num1-num2)
def mul(num1,num2):
    print(num1*num2)
def div(num1,num2):
    print(num1/num2)
def expo(num1,num2):
    print(num1**num2)
print("calculator")
x=print('1)ADDITION\n2)SUBTRACTION\n3)MULTIPLICATION\n4)DIVISION\n5)EXPONENT')
print()
y=int(input('enter the operetion '))
num1=float(input("enter the first number "))
num2=float(input('enter the second number '))
if y >= 6:
    print('check the number you have dialed')
elif y==1:
        add(num1,num2)
elif y==2:
    sub(num1,num2)
elif y==3:
    mul(num1,num2)
elif y==4:
    div(num1,num2)
elif y==5:
    expo(num1,num2)
else:
    print("check the number you have dialed")