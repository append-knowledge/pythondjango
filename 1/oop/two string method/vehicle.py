
                                #double string method
class Vehicle():
    def __init__(self,name,model,year,price):
        self.name=name
        self.model=model
        self.year=year
        self.price=price
        print(self.name,self.model,self.year,self.price)

    def __str__(self):          #if double string is not used it will print the location of reference
        return self.model + self.name + str(self.year)                #int type cannot be printed by using double string method

obj1=Vehicle('Benz','z class',2020,2000000)
print(obj1)

obj2=Vehicle('KTM','DUKE',2021,190000)
print(obj2)