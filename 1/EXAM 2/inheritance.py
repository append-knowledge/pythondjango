class Men():
    def mdeta(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)
class Boy(Men):
    def Bdeta(self,school,cls):
        self.school=school
        self.cls=cls
        print(self.school,self.cls)
class Person(Boy):
    def pdeta(self,job,adrs):
        self.job=job
        self.adrs=adrs
        print(self.job,self.adrs)
oop=Person()
oop.mdeta('lijo jose',26)
oop.Bdeta('smm',8)
oop.pdeta('engineer','ssdjkddhd')
