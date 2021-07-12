class Person:
    def perval(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)
class Parent(Person):
    def parval(self,occu,adrs):
        self.occu=occu
        self.adrs=adrs
        print(self.occu,self.adrs)
class Employee(Parent):
    def emval(self,id,salary):
        self.id=id
        self.salary=salary
        print(self.id,self.salary)

obj1=Parent()
obj1.perval('LIJO JOSE',26)
obj1.parval('engineer','olakkengil')

print()

obj2=Employee()
obj2.perval('lissy',53)
obj2.parval('teacher','pulikottil')
obj2.emval(678544,45000)