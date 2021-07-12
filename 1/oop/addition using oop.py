class Add():
    def sum(self,num1,num2):
        self.num1=num1
        self.num2=num2
        # self.sum=sum
    def printval(self):
        print("sum is",self.num1+self.num2)

obj1=Add()
num1=int(input('enter the number '))
num2=int(input('enter the number '))
obj1.sum(num1,num2)
obj1.printval()
print()
num1=int(input('enter the number '))
num2=int(input('enter the number '))
obj1.sum(num1,num2)
obj1.printval()
print()
num1=int(input('enter the number '))
num2=int(input('enter the number '))
obj1.sum(num1,num2)
obj1.printval()