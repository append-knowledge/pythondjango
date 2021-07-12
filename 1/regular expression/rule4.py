#for special symbol
import re
x='[^a-zA-Z0-9]'
matcher=re.finditer(x,'LijoJose95@')
for i in matcher:
    print(i.start())
    print(i.group())