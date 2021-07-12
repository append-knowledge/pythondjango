class Person:
    def pdeta(self,name,age,adrs):
        self.name=name
        self.age=age
        self.adrs=adrs
        print(self.name,self.age,self.adrs)
class Student(Person):              #this calling as inheritant now only one object is needed for two classes
    def sdeta(self,id,department,mark):
        self.id=id
        self.department=department
        self.mark=mark
        print(self.id,self.department,self.mark)

        print('mark of',self.name,'is',self.mark)       #we can merge the values of two classes using inheritence

obj1=Student()
obj1.pdeta('lijo',26,'olakkengil')
obj1.sdeta(654789,'electrical',654)

