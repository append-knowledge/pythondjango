class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)
class Employee(Person):
    def __init__(self,salary,adrs,name,age):
        self.salary=salary
        self.adrs=adrs
        super().__init__(name,age)
        print(self.salary,self.adrs)

obj1=Employee(45000,'olakkengil','lijo jose',26)