import re
x=open('phone no', 'r')
z=open('valid', 'w')
valid='[+][9][1]\d{10}'
for i in x:
    i=i.rstrip('\n')
    match=re.fullmatch(valid,i)
    if match is not None:
        z.write(i)
        z.write('\n')
