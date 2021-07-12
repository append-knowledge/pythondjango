#same method and attribute number
class Person():
    def pval(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)
class Child(Person):
    def pval(self,id,adrs):         #latest methods override the other methods it is overriding
        self.id=id
        self.adrs=adrs
        print(self.id,self.adrs)

obj1=Child()
obj1.pval(5648,'olakkengil')