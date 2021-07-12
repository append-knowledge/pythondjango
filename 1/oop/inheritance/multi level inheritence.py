class Person:
    def perval(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)
class Child(Person):                    #in multi inheritance class child act as both parent class and derived class
    def chval(self,id,roll_no):         #for class child --class person  is parent class
        self.id=id
        self.roll_no=roll_no
        print(self.id,self.roll_no)
class Student(Child):                           #in student class it is the derived class and both child class and person class is parent class
    def stval(self,mark,school):
        self.mark=mark
        self.school=school
        print(self.mark,self.school)


obj1=Child()
obj1.perval('lijo jose',26)
obj1.chval(678544,45)

print()

obj2=Student()
obj2.perval('lissy',53)
obj2.chval(65874,45)
obj2.stval(600,'smmhss')