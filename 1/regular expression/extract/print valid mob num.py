import re
x=open('mob1', 'r')
y='[+][9][1]\d{10}'
for i in x:
    i=i.strip('\n')
    match=re.fullmatch(y,i)
    if match is not None:
        print(i)
    else:
        pass