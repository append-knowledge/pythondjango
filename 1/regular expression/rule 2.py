import re
# x='[^at]'
# matcher=re.finditer(x,'aboutthe')
# for i in matcher:
#     print(i.start())
#     print(i.group())


y='[^he]'
matcher=re.finditer(y,'hello')
for i in matcher:
    print(i.start())
    print(i.group())