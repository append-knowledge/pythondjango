class Mark():
    def deta(self,name,yr,course,mark):
        self.name=name
        self.yr=yr
        self.course=course
        self.mark=mark
        print(self.name,self.yr,self.course,self.mark)
x=open('mark', 'r')
maxmark=0
for i in x:
    i=i.rstrip('\n').split(',')
    if int(i[3])>=maxmark:
        maxmark=i[3]
        name=i[0]
        yr=i[1]
        course=i[2]
        maxmark=int(i[3])
        obj1=Mark()
        obj1.deta(name,yr,course,maxmark)
