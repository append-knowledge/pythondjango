import re
count=0
x=re.finditer('li','lijojolilissylijajose')
for i in x:
    print('matching starts at ',i.start())      #to know the starting position
    count+=1
print('searching group is ',i.group())          #to know the group we are searching
print('count is',count)