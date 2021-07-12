class Name():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printval(self):
        print('name is',self.name)
        print('age is',self.age)
    def __str__(self):
        return self.name
x=open('file1', 'r')
for i in x:
    data=i.rstrip("\n").split(",")
    name=data[0]
    age=data[1]
    obj1=Name(name,age)
    obj1.printval()
    print(obj1)





