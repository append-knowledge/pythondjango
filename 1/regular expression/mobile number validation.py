import re
ipt=input('ENTER THE MOBILE NUMBER ')
x='[0-9]{10}'
match=re.fullmatch(x,ipt)
if match is None:
    print('INVALID ')
else:
    print('VALID')