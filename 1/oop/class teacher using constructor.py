class Teacher():
    teacher_dep='eletrical'
    school='nehru college'
    def __init__(self,name,sub,teacher_id):
        self.name=name
        self.sub=sub
        self.teacher_id=teacher_id
    def printval(self):
        print(self.name,self.sub,self.teacher_id,Teacher.teacher_dep,Teacher.school)


obj1=Teacher('lijo','basic maths',65458)
obj1.printval()

print()
obj2=Teacher('benson','cgl',58754)
obj2.printval()

print()
tec=Teacher('lissy','malayalam',678544)
tec.printval()