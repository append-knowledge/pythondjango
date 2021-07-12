import re
x=open('F1 REGI', 'r')
z=open('F2 REGI', 'w')
for i in x:
    i=i.strip('\n')
    y='[K][L]\d{2}[A-Z]{2}[0-9]{4}'
    match=re.fullmatch(y,i)
    if match is not None:
        z.write(i)
        z.write('\n')

