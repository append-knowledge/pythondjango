class Student:
    def sval(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
        print(self.name,self.roll_no)
class Child(Student):
    def cval(self,age,adrs):
        self.age=age
        self.adrs=adrs
        print(self.age,self.adrs)
class Parent:
    def parval(self,occu,salary):
        self.occu=occu
        self.salary=salary
        print(self.occu,self.salary)
class Person(Parent,Child):
    def perval(self,id,nick_name):
        self.id=id
        self.nick_name=nick_name
        print(self.id,self.nick_name)




obj1=Person()
obj1.parval('kkk',54)
obj1.perval('5478','ff')
obj1.cval(26,'olakkengil')
obj1.sval('lijo jose',45)