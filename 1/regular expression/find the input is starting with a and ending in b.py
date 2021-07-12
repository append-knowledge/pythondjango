import re
inp=input('enter ')
a="^a[a-zA-Z0-9\W]*b$"
match=re.fullmatch(a,inp)
if match is not None:
    print('valid')
else:
    print('invalid')