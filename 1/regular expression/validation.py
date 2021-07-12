import re
x=input('enter the string ')                #first two number and 2 letters
y='\d{2}\w{2}'
matcher=re.fullmatch(y,x)
if matcher is not None:
    print('Valid')
else:
    print('Invalid')