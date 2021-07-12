# poly morphism
# 1) overloading--------same method name and different number of attributes
# 2) over riding--------same method name and same number of attributes

class Operation():
    def num(self,n1,n2):
        self.n1=n1
        self.n2=n2
        print(self.n1+self.n2)
class Display(Operation):
    def num(self,n3):
        self.n3=n3
        print(self.n3)      #as per the concept of over loading when classes are inherited and name method names
                            # but different attribute numbers the after intialisation the method with same number of
               #attribute works ie concept of over loading but python donot have overloading
obj1=Display()
obj1.num(54)