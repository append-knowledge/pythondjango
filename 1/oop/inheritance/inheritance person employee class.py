        #single inheritance
class Person:   #parent class/super class/base class
    def pdetail(self,name,age,adrs):
        self.name=name
        self.age=age
        self.adrs=adrs
        print(self.name,self.age,self.adrs)
class employee(Person):     #child class/derived class
    def emdetail(self,id,department,salary):
        self.id=id
        self.department=department
        self.salary=salary
        print(self.id,self.department,self.salary)

        print()
        print('salary and age of',self.name,'is',self.salary,'and',self.age)
        print(self.name,'is working in',self.department)

obj1=employee()
obj1.pdetail('lijo jose',26,'olakkengil house')
print()

obj1.emdetail(678544,'electrical',45000)
