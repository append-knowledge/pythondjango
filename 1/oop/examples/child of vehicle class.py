class Vehicle():
    def vprint(self,model,yr,price):
        self.model=model
        self.yr=yr
        self.price=price
        print(self.model,self.yr,self.price)
class Child(Vehicle):
    def vchild(self,showroom):
        self.showroom=showroom
        print(self.showroom)
        print('price of vehicle in',self.showroom,'is',self.price)
obj1=Child()
obj1.vprint('benz',2020,2000000)
obj1.vchild('pkd')