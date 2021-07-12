class Employee():
    def setval(self,name,designation,age,salary):
        self.name=name
        self.designation=designation
        self.age=age
        self.salary=salary
    def printval(self):
        print('name= ',self.name)
        print('designation =',self.designation)
        print('age = ',self.age)
        print('salary = ',self.salary)

obj1=Employee()
obj1.setval('lijo','engineer',26,30000)
obj1.printval()
print()
obj1.setval('lija','engineer',25,40000)
obj1.printval()
print()
obj1.setval('naveen','Bank',30,30000)
obj1.printval()