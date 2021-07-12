import re
# x='[xyz]'
# matcher=re.finditer(x,'xerozmachineyeld')
# for match in matcher:
#     print('starting of match is',match.start())
#     print('match group is ',match.group())

y='[li]'
matcher=re.finditer(y,'lijojolilissylija')
for match in matcher:
    print('match starts at ',match.start())
    print('match group is ',match.group())
