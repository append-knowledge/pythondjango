class Student():
    def deta(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
        print(self.name,self.age,self.place)
    def __str__(self):
       return self.name+str(self.age)
oop=Student()
oop.deta('lijo jose',26,'pzb')
print(oop)