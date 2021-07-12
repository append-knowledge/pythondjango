class Students():
    def __init__(self,name,yr,course,mark):
        self.name=name
        self.yr=yr
        self.course=course
        self.mark=mark
    def printval(self):
        print('name is ',self.name)
        print('yr is ',self.yr)
        print('course is ',self.course)
        print('mark is ',self.mark)

x=open('f2', 'r')
for i in x:
    data=i.rstrip("\n").split(',')
    name=data[0]
    yr=data[1]
    course=data[2]
    mark=data[3]
    obj1=Students(name,yr,course,mark)
    obj1.printval()
    print()