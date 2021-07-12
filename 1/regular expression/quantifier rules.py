import re

#rule 1          to find group
# x='a+'
# input='aaa abc aaa cga'
# matcher=re.finditer(x,input)
# for i in matcher:
#     print(i.start())
#     print(i.group())


#rule 2       to count including zero value of a
# x='a*'
# input='aaa abc aaaa cga'
# matcher=re.finditer(x,input)
# for i in matcher:
#     print(i.start())
#     print(i.group())


#rule 3
# x='a?'          #to count a as each including zero element of a
# input='aaa abc aaaa cga'
# matcher=re.finditer(x,input)
# for i in matcher:
#     print(i.start())
#     print(i.group())
#

# rule 4
# x='a{2}'         #number of a position
# input='aaa abc aaaa cga'
# matcher=re.finditer(x,input)
# for i in matcher:
#     print(i.start())
#     print(i.group())


#rule 5
# x='a{2,3}'    #minimum 2a and maximum 3a
# input='aaa aa abc aaaaa cga'
# matcher=re.finditer(x,input)
# for i in matcher:
#     print(i.start())
#     print(i.group())



#rule 6
# x='^a'       #to check string starting with a
# input='aaa abc aaaa cga'
# matcher=re.finditer(x,input)
# for i in matcher:
#     print(i.start())
#     print(i.group())


#rule7
# x='a$'                  #to check if last name is a
# input='aaa abca aaaaa cga'
# matcher=re.finditer(x,input)
# for i in matcher:
#     print(i.start())
#     print(i.group())