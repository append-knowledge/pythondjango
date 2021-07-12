# constructor is used to intialise instant variable
# constructor automatically invoke when creating object
# denoted by   __init__

class Person():
    com_name="luminar ltd"
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
    def printval(self):
        print(self.name,self.age,self.address,Person.com_name)

obj1=Person('Lijo jose',26,'olakkengil house')
obj1.printval()

obj2=Person('Benson',26,'ahhhh')
obj2.printval()