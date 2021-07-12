a=int(input("ENTER THE FIRST VALUE "))
b=int(input("ENTER THE SECOND VALUE "))
#using temporary value
# c=a
# a=b
# b=c
# print(a)
# print(b)

#easy way
# (a,b)=(b,a)
# print("FIRST VALUE AFTER SWAPING IS",a)
# print("SECOND VALUE AFTER SWAPING IS",b)

#equation
a=a+b
b=a-b
a=a-b
print("FIRST VALUE AFTER SWAPING IS",a)
print('SECOND VALUE AFTER SWAPING IS',b)
