import re
ipt=input('enter ')
x='(^[A-Z][0-9a-z\W]+)'
match=re.fullmatch(x,ipt)
if match is None:
    print('invalid')
else:
    print('valid')