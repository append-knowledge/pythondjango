#class inheritanted ,same module name ,different number of attribute

class Person():
    def pval(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)
class Parent(Person):
    def pval(self,adrs):
        self.adrs=adrs
        print(self.adrs)

obj1=Parent()
obj1.pval('olakkengil')