class Person:
    def pval(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)
class Child:
    def cval(self,roll,adrs):
        self.roll=roll
        self.adrs=adrs
        print(self.roll,self.adrs)
class Student(Person,Child):
    def sval(self,mark,cls):
        self.mark=mark
        self.cls=cls
        print(self.mark,self.cls)


obj1=Student()
obj1.pval('Lijo Jose',26)
print()
obj1.cval(678544,'Olakkengil house')
print()
obj1.sval(600,'6A')