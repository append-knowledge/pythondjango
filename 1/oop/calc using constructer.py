class Calc():
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        print('addition result is ',self.num1+self.num2)
    def sub(self):
        print('sub result is  ',self.num1-self.num2)
    def mul(self):
        print('mul result is ',self.num1*self.num2)
    def div(self):
        print('div result is ',self.num1/self.num2)
obj1=Calc(10,15)
obj1.add()

print()

obj2=Calc(50,5)
obj2.div()

print()

num1=int(input('enter the num1 '))
num2=int(input('enter the num2  '))
print('1)addition\n2)subtraction\n3)multiplication\n)4division')
num3=int(input('enter the operation '))
obj3=Calc(num1,num2)
if num3==1:
    obj3.add()
elif num3==2:
    obj3.sub()
elif num3==3:
    obj3.mul()
elif num3==4:
    obj3.div()
else:
    print('check the number you have dialed')