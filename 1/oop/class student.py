class Student():
    def stu(self,name,rollnum,mark,school):
        self.name=name
        self.rollnum=rollnum
        self.mark=mark
        self.school=school
        print("name: ",self.name)
        print('rollnum: ',self.rollnum)
        print('mark: ',self.mark)
        print('school: ',self.school)
obj1=Student()
name=input('enter the name ')
rollnum =int(input('enter the rollnum '))
mark = int(input('enter the mark '))
school=input('enter the school name ')
print()
obj1.stu(name,rollnum,mark,school)

print()
name=input('enter the name ')
rollnum =int(input('enter the rollnum '))
mark = int(input('enter the mark '))
school=input('enter the school name ')
print()
obj1.stu(name,rollnum,mark,school)



