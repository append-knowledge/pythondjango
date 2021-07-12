import re
x='^[a-zA-Z]+\d$'
input=input('enter the string ')
match=re.fullmatch(x,input)
if match is not None:
    print('VALID')
else:
    print('INVALID')