class Animal():
    def __init__(self,name,clr,price):
        self.name=name
        self.clr=clr
        self.price=price
    def ani(self):
        print('name of animal is ',self.name)
        print('clr is',self.clr)
        print('price is ',self.price)
class Dog(Animal):
    def dprint(self,breed):
        self.breed=breed
        print('Breed name of dog ',self.name,'is',self.breed)
obj1=Dog('honey','black',7500)
obj1.dprint('Beegle')
obj1.ani()