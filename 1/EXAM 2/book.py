class Book():
    Library_name='PZB'
    book_name='A LONG WALK TO FREEDOM'
    author='MANDELA'
    pages='600'
    def bdeta(self,publication,clr):
        self.publication=publication
        self.clr=clr
        print(Book.Library_name,Book.book_name,Book.author,Book.pages,self.publication,self.clr)

obj1=Book()
obj1.bdeta('abc','white')