num1=int(input("enter the first number "))
num2=int(input("enter the second number "))
num3=int(input("enter the third number "))
# if num1>num2:
#     if num1>num3:
#         print(num1,"is the greatest")
#     else:
#         print(num3,"is the greatest")
# elif num2>num3:
#     print(num2,'is the greatest')
# elif num3>num2:
#     print(num3,"is gretest")
# else:
#     print("entered numbers are equal")


#logic operators
if (num1>num2)and(num1>num3):
    print(num1,"is greater")
elif (num2>num1)and(num2>num3):
    print(num2,"is greater")
elif(num1==num2)and(num1==num3):
    print("entered numbers are equal")
else:
    print(num3,"is greater")