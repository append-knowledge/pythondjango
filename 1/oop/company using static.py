class Company():
    com_name='luminar ltd'          #static variable will be inside calss
    def deta(self,name,designation,experience):
        self.name=name
        self.designation=designation            #instant variable denoted by self. and will be inside module
        self.experience=experience
    def print(self):
        print('name is ',self.name)
        print('designation is ',self.designation)
        print('experience is ',self.experience)
        print('company name is ',Company.com_name)
obj1=Company()
obj1.deta('lijo','engineer',15)
obj1.print()
print()
obj2=Company()
obj1.deta('cgl','testing',10)
obj1.print()