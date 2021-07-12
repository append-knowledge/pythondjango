class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def pprint(self):
        print('name is',self.name)
        print('age is ',self.age)
class Child(Person):
    def __init__(self,school,mark,name,age):
        self.school=school
        self.mark=mark
        super(). __init__ (name,age)
    def cprint(self):
        print('school name is',self.school)
        print('mark is',self.mark)

obj1=Child('smm',55,'lijo',26)
obj1.cprint()
obj1.pprint()