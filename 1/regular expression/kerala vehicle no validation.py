import re
input=input('ENTER THE REGISTERATION NUMBER ')
X='[K][L]\d{2}[A-Z]{2}\d{4}'
match=re.fullmatch(X,input)
if match is None:
    print('Invalid')
else:
    print('Valid')