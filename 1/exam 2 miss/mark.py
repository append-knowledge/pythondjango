class Student():
    def __init__(self,name,rollno,course,mark):
        self.name=name
        self.rollno=rollno
        self.course=course
        self.mark=mark
    def printval(self):
        print(self.name)
        print(self.rollno)
        print(self.course)
        print(self.mark)
lst=[]
f=open('mark', 'r')
for i in f:
    i=i.rstrip('\n').split(',')
    name=i[0]
    rollno=i[1]
    course=i[2]
    mark=i[3]
    obj1=Student(name,rollno,course,mark)
    obj1.printval()
    lst.append(obj1)
    #print(lst)
mark=[]
for j in lst:
    mark.append(j.mark)
print(mark)
for j in lst:
    if (j.mark==max(mark)):
        print(j.name,j.rollno,j.course,j.mark)