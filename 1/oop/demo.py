# oop.......object oriented programming
#
#
# class.....design or blueprint
# object....realworld entity
# reference.....to perform operations in object


# class Person:
#     def walk(self):
#         print('he is walking')       #function inside class is known as method
#     def reading(self):               #
#         print('he is reading')
#     def running(self):
#         print('!@####')

# obj1=Person()
# obj1.walk()
# obj1.running()
#
# lijo=Person()
# lijo.reading()

#arguments used inside methods is known as arguments

class Person():
    def setval(self,name,age):
        self.name=name
        self.age=age
    def printval(self):
        print('name is ',self.name)
        print('age is ',self.age)

obj1=Person()
obj1.setval('lijo',26)
obj1.printval()






