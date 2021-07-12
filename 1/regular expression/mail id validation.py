import re
ip=input('ENTER THE MAIL ID ')
X='[a-z0-9]+[@][a-z]+[.][a-z]+'
match=re.fullmatch(X,ip)
if match is not None:
    print('Valid')
else:
    print('Invalid')