class Teacher():
    def deta(self,name,age):
        self.name=name
        self.age=age
        print('teacher deta',self.name,self.age)
class Student(Teacher):
    def deta(self,name,age):
        self.name = name
        self.age = age
        print('student deta',self.name,self.age)

obj1=Student()
obj1.deta('Lijo jose',26)

