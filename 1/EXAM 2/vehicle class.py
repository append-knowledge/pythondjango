class Vehicle():
    def vdeta(self,model,reg_no,clr):
        self.model=model
        self.reg_no=reg_no
        self.clr=clr
        print(self.model,self.reg_no,self.clr)
class Car(Vehicle):
    def cardeta(self,price):
        self.price=price
        print(self.price)

obj1=Car()
obj1.vdeta('CD110','KL09AF8055','RED')
obj1.cardeta(100000)


