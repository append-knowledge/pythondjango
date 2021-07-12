# num1=int(input('enter the num '))
# num2=int(input('enter the num '))
# div=num1/num2
# print(div)

# #if the input is given 5 and 0 error occurs
# #this is known as unexpected error
# #to solve this 3 steops are used
# try........exeptional code
# except......solving code
# finally.....any thing

num1=int(input('enter the num '))
num2=int(input('enter the num '))
try:
    print('hello')
    print(num1/num2)
except Exception as e:
    print("error occured due to ",e)
finally:
    print("finally")

#try and finally block always work except block only when error occurs