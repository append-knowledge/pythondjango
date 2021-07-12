import re
x='^[A-Z][a-z]+'
input=input('enter the string ')
match =re.finditer(x,input)
for i in match:
    print(i.group())
