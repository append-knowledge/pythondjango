class Book():
    library_name='ABC'
    def detail(self,name,author,price,publica):
        self.name=name
        self.author=author
        self.price=price
        self.publica=publica
    def print(self):
        print(self.name,self.author,self.price,self.publica,Book.library_name)


obj1=Book()
name=input('enter the name of book ')
author=input('enter the name of author ')
price=int(input('enter the price '))
publica=input('enter the name of publication')
obj1.detail(name,author,price,publica)
obj1.print()
print()
obj2=Book()
obj2.detail('main calf','hittler',600,'cdv')
obj2.print()


#in oops 2 type variable
# 1)  static type......typed inside class.....called by using class.name
# 2)  instant type.....typed in side module....called by using silf.name