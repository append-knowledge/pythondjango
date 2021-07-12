num1=int(input('enter '))
num2=int(input('enter '))
try:
    print(num1/num2)
    print('hii')
except Exception as e:
    print('exception is',e)
finally:
    print('done')
