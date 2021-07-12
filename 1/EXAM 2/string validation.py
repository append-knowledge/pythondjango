import re
x='^[A-Z][a-zA-Z0-9]{3,8}[A-Z]$'
input=input('enter the word ')
match=re.fullmatch(x,input)
if match is None:
    print('INVALID')
else:
    print('VALID')