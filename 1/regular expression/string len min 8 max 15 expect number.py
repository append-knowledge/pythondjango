import re
ipt=input('enter ')
x='[\D]{8,15}'
match=re.fullmatch(x,ipt)
if match is None:
    print('Invalid')
else:
    print('valid')