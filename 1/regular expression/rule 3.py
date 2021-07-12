import re
# x='[a-z]'
# matcher=re.finditer(x,'LIJO jose')
# for i in matcher:
#     print(i.start())
#     print(i.group())

# y='[A-Z]'
# matcher=re.finditer(y,'LIJO jose')
# for i in matcher:
#     print(i.start())
#     print(i.group())


#
# z='[a-zA-z]'
# matcher=re.finditer(z,'LIJO jose')
# for i in matcher:
#     print(i.start())
#     print(i.group())



a='[0-9]'
matcher=re.finditer(a,'00LIJOJOSE95')
for i in matcher:
    print('position is ',i.start())
    print('group is ',i.group())


