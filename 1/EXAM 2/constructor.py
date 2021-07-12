class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def pval(self):
        print(self.name,self.age)
class Employee():
    def emdeta(self,adrs):
        self.adrs=adrs
        print(self.adrs)
class Employer(Employee):
    def emp(self,salary):
        self.salary=salary
        print(self.salary)

obj1=Person('LIJO JOSE',26)
obj1.pval()
obj2=Employer()
obj2.emp(600000000)
obj2.emdeta('asdfrgfujd')

