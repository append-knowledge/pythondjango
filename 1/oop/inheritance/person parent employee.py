class Person:
    def perval(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)
class Parent:
    def parval(self,adrs,occupation):
        self.adrs=adrs
        self.occupation=occupation
        print(self.adrs,self.occupation)
class Employee(Person,Parent):
    def emval(self,id,salary):
        self.id=id
        self.salary=salary
        print(self.id,self.salary)
        print()
        print('occupation of ',self.name,'is',self.occupation)
        print('salary of',self.name,'is',self.salary)
obj1=Employee()
obj1.perval('LIJO JOSE',26)
print()
obj1.parval('OLAKKENGIL HOUSE','PYTHON ENGINEER')
print()
obj1.emval(678544,45000)
