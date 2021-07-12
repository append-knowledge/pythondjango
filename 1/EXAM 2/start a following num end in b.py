import re
x='[a]\d+[b]'
input=input('enter ')
match=re.fullmatch(x,input)
if match is not None:
    print('VALID')
else:
    print('INVALID')